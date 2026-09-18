#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Route JSONL tickets with a local replay by default; --live opts into API calls."""

import argparse
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import sys

from support_router import (
    JevError, MODEL, PROJECT, QUESTION_VERSION, build_request, decide,
    load_config, validate_response, validate_ticket,
)
from jev_examples.client import evaluate


def json_line(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False) + "\n"


def reject_nonfinite(_value):
    raise ValueError("Nonfinite JSON number")


def fingerprint(request):
    serialized = json.dumps(request, sort_keys=True, ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def read_jsonl(path):
    rows = []
    with Path(path).open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line, parse_constant=reject_nonfinite)
            except ValueError as error:
                raise JevError(f"Invalid JSON on line {line_number}") from error
            if not isinstance(row, dict):
                raise JevError(f"Line {line_number} must contain a JSON object")
            rows.append(row)
    if not rows:
        raise JevError("JSONL input must contain at least one record")
    return rows


def load_tickets(path):
    tickets = [validate_ticket(row) for row in read_jsonl(path)]
    ids = [ticket["id"] for ticket in tickets]
    if len(ids) != len(set(ids)):
        raise JevError("Ticket IDs must be unique within a batch")
    return tickets


def load_replay(path, requests):
    """Bind each response to its full request, preventing stale fixture reuse."""
    replay = {}
    for row in read_jsonl(path):
        ticket_id = row.get("ticket_id")
        if not isinstance(ticket_id, str) or ticket_id in replay:
            raise JevError("Replay records require unique string ticket_id values")
        replay[ticket_id] = row
    for ticket_id, request in requests.items():
        row = replay.get(ticket_id)
        if row is None or row.get("request") != request:
            raise JevError("Replay does not match the ticket text, model, or current questions; make a new live capture")
        validate_response(request, row.get("response"))
    return replay


def failed_decision(reason):
    return {
        "department": None, "route": "human_review", "urgency": "review",
        "needs_review": True, "review_reasons": [reason],
        "department_confidence": None, "urgency_noul": None,
    }


def positive_integer(value):
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("Value must be greater than zero")
    return parsed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--demo", action="store_true", help="Use synthetic fixtures (default)")
    mode.add_argument("--live", action="store_true", help="Send tickets to TypeSafe; requires TYPESAFE_API_KEY and may incur charges")
    mode.add_argument("--replay", type=Path, help="Replay a prior decisions.jsonl capture without API calls")
    parser.add_argument("--input", type=Path, help="JSONL tickets with id and message; default: bundled synthetic tickets")
    parser.add_argument("--config", type=Path, help="Complete department and review-policy JSON configuration")
    parser.add_argument("--model", default=MODEL, help=f"Requested model; default: {MODEL}")
    parser.add_argument("--limit", type=positive_integer, help="Process only the first N validated input tickets")
    parser.add_argument("--max-tickets", type=positive_integer, default=50, help="Live call budget; reject larger selected batches before calling (default: 50)")
    parser.add_argument("--dry-run", action="store_true", help="Print exact requests and exit without API calls or output files")
    parser.add_argument("--output-dir", type=Path, help="Create a NEW directory with decisions, review queue, and summary")
    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
        tickets = load_tickets(args.input or PROJECT / "demo" / "tickets.jsonl")
        if args.limit:
            tickets = tickets[:args.limit]
        requests = {ticket["id"]: build_request(ticket, config, args.model) for ticket in tickets}
        if args.dry_run:
            for ticket_id, request in requests.items():
                sys.stdout.write(json_line({"ticket_id": ticket_id, "request": request}))
            return 0

        mode_name = "live" if args.live else "replay" if args.replay else "demo_synthetic"
        if args.output_dir and args.output_dir.resolve().is_relative_to(PROJECT.parents[1]):
            raise JevError("Output must use a private directory outside the public repository")
        replay = None
        if args.live:
            if len(tickets) > args.max_tickets:
                raise JevError("Selected live batch exceeds --max-tickets; choose an explicit --limit or increase the budget")
            if not os.environ.get("TYPESAFE_API_KEY", "").strip():
                raise JevError("Live mode requires TYPESAFE_API_KEY in the environment")
        else:
            replay = load_replay(args.replay or PROJECT / "demo" / "responses.jsonl", requests)

        quality_evidence = args.live or (
            bool(args.replay) and all(replay[ticket_id].get("quality_evidence") is True for ticket_id in requests)
        )

        # All configuration, input, and replay validation happens before output or API use.
        with ExitStack() as files:
            decisions_file = review_file = None
            if args.output_dir:
                args.output_dir.mkdir(parents=True, exist_ok=False)
                decisions_file = files.enter_context((args.output_dir / "decisions.jsonl").open("x", encoding="utf-8"))
                review_file = files.enter_context((args.output_dir / "review-queue.jsonl").open("x", encoding="utf-8"))
            summary = {
                "mode": mode_name, "question_version": QUESTION_VERSION,
                "quality_evidence": quality_evidence,
                "requested_model": args.model, "config": config, "total": len(tickets),
                "processed": 0, "automatic": 0, "human_review": 0, "errors": 0,
                "not_processed": 0, "usage": {"input_tokens": 0, "output_tokens": 0},
                "response_models": [],
            }
            stopped = False
            response_models = set()
            for ticket in tickets:
                request = requests[ticket["id"]]
                record = {
                    "ticket_id": ticket["id"], "ticket": ticket, "mode": mode_name,
                    "question_version": QUESTION_VERSION, "config": config,
                    "quality_evidence": args.live or (
                        bool(args.replay) and replay[ticket["id"]].get("quality_evidence") is True
                    ),
                    "request_sha256": fingerprint(request), "request": request,
                    "response": None,
                }
                if args.replay:
                    source = replay[ticket["id"]]
                    record["source_mode"] = source.get("source_mode", source.get("mode", "unknown"))
                    record["source_provenance"] = source.get("source_provenance", source.get("provenance"))
                elif not args.live:
                    record["provenance"] = "synthetic authored fixture; not an API response"
                if stopped:
                    record.update(status="not_processed", decision=failed_decision("batch_stopped_after_error"))
                    summary["not_processed"] += 1
                else:
                    try:
                        response = (
                            evaluate(request, os.environ.get("TYPESAFE_API_KEY"), max_attempts=1)
                            if args.live else replay[ticket["id"]]["response"]
                        )
                        answers = validate_response(request, response)
                        decision = decide(request, answers, config)
                        record.update(status="processed", response=response, decision=decision)
                        summary["processed"] += 1
                        response_models.add(response["model"])
                        for key in summary["usage"]:
                            summary["usage"][key] += response["usage"][key]
                    except JevError as error:
                        record.update(status="error", error=str(error), decision=failed_decision("service_or_contract_error"))
                        summary["errors"] += 1
                        stopped = True
                line = json_line(record)
                sys.stdout.write(line)
                sys.stdout.flush()
                if decisions_file:
                    decisions_file.write(line)
                    decisions_file.flush()
                if record["decision"]["needs_review"]:
                    summary["human_review"] += 1
                    if review_file:
                        review_file.write(line)
                        review_file.flush()
                else:
                    summary["automatic"] += 1
            summary["response_models"] = sorted(response_models)
            if args.output_dir:
                with (args.output_dir / "summary.json").open("x", encoding="utf-8") as destination:
                    destination.write(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
            print(json.dumps(summary, ensure_ascii=False), file=sys.stderr)
            return 1 if stopped else 0
    except (JevError, OSError, UnicodeError, ValueError) as error:
        print(f"Support router stopped: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
