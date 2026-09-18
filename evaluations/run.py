# SPDX-License-Identifier: MIT
"""Bounded support-routing evaluation. Defaults to a synthetic, offline baseline."""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import statistics
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))
from jev_examples.client import ENDPOINT, MAX_RESPONSE_BYTES, MODEL, JevError, NoRedirects, validate_response  # noqa: E402


def load_router():
    spec = importlib.util.spec_from_file_location("support_router", ROOT / "projects/support-router/support_router.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fingerprint(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def reject_nonfinite(_value):
    raise ValueError("Nonfinite JSON number")


def read_jsonl(path):
    rows = []
    with Path(path).open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line, parse_constant=reject_nonfinite)
            except (ValueError, UnicodeError):
                raise ValueError(f"Invalid JSON on line {line_number}") from None
            if not isinstance(row, dict):
                raise ValueError(f"Line {line_number} must be a JSON object")
            rows.append(row)
    return rows


def load_dataset(path, departments, split):
    rows = read_jsonl(path)
    seen = set()
    required_strings = ("id", "split", "slice", "message", "expected_department", "expected_urgency")
    for line_number, row in enumerate(rows, 1):
        if any(not isinstance(row.get(key), str) or not row[key].strip() for key in required_strings):
            raise ValueError(f"Dataset record {line_number} needs nonempty string fields: {', '.join(required_strings)}")
        if row["id"] in seen:
            raise ValueError(f"Duplicate dataset ID at record {line_number}")
        seen.add(row["id"])
        if row["split"] not in ("development", "holdout"):
            raise ValueError(f"Dataset record {line_number} has an invalid split")
        if row["expected_department"] not in departments:
            raise ValueError(f"Dataset record {line_number} has an unknown expected department")
        if row["expected_urgency"] not in ("ordinary", "high"):
            raise ValueError(f"Dataset record {line_number} has an invalid expected urgency")
        if "require_review" in row and not isinstance(row["require_review"], bool):
            raise ValueError(f"Dataset record {line_number} require_review must be boolean")
    selected = [row for row in rows if split == "all" or row["split"] == split]
    if not selected:
        raise ValueError("No cases match the selected split")
    return selected


def ticket_only(case):
    """The request constructor never receives labels, split, or slice metadata."""
    return {"id": case["id"], "message": case["message"]}


def mock_response(request):
    """Deliberately uninformative fixture; never read the expected labels."""
    choices = list(request["questions"]["department"]["criteria"])
    return {
        "model": "synthetic-uniform-baseline",
        "answers": {
            "department": {
                "type": "choice", "choice": "other", "confidence": 0.0,
                "probabilities": {key: 1 / len(choices) for key in choices},
            },
            "explicit_urgency": {"type": "noul", "noul": 0.5},
        },
        "usage": {"input_tokens": 0, "output_tokens": 0},
    }


class ServiceError(Exception):
    """Redacted HTTP/transport errors; messages never include credentials or bodies."""


def live_response(request, api_key, open_url=None):
    """Exactly one HTTP attempt, including on 429/529, to enforce the call budget."""
    if not isinstance(api_key, str) or not api_key or any(ord(char) < 33 or ord(char) > 126 for char in api_key):
        raise ValueError("Live mode requires a valid TYPESAFE_API_KEY token")
    if open_url is None:
        open_url = urllib.request.build_opener(NoRedirects()).open
    http_request = urllib.request.Request(
        ENDPOINT, data=json.dumps(request, allow_nan=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with open_url(http_request, timeout=30) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.HTTPError as error:
        status = error.code
        error.close()
        raise ServiceError(f"HTTP {status}; no retry attempted") from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise ServiceError("Network request failed; no retry attempted") from None
    if len(body) > MAX_RESPONSE_BYTES:
        raise ServiceError("Response exceeded the byte limit")
    try:
        return json.loads(body, parse_constant=reject_nonfinite)
    except (ValueError, UnicodeError):
        raise ServiceError("Response was not valid JSON") from None


def rate(numerator, denominator):
    return {"numerator": numerator, "denominator": denominator, "value": numerator / denominator if denominator else None}


def summarize(records):
    """All rates carry their denominator; missing decisions remain in coverage totals."""
    total = len(records)
    successes = [record for record in records if record["error"] is None]
    automatic = [record for record in successes if not record["decision"]["needs_review"]]
    review = [record for record in successes if record["decision"]["needs_review"]]
    urgency_decided = [record for record in successes if record["decision"]["urgency"] != "review"]
    required_review = [record for record in successes if record["expected"]["require_review"]]
    high = [record for record in successes if record["expected"]["urgency"] == "high"]
    ordinary = [record for record in successes if record["expected"]["urgency"] == "ordinary"]
    errors = Counter(record["error"]["category"] for record in records if record["error"])
    confusion = {}
    for record in successes:
        expected, actual = record["expected"]["department"], record["decision"]["department"]
        confusion.setdefault(expected, {})[actual] = confusion.setdefault(expected, {}).get(actual, 0) + 1
    latencies = [record["latency_ms"] for record in records if record["latency_ms"] is not None]
    usage_records = [record for record in records if isinstance(record.get("usage"), dict)]
    incorrect_department = lambda record: record["decision"]["department"] != record["expected"]["department"]
    return {
        "counts": {"total": total, "successful": len(successes), "automatic": len(automatic), "review": len(review),
                   "errors": total - len(successes), "errors_by_category": dict(errors)},
        "department_confusion": confusion,
        "department_accuracy": rate(sum(not incorrect_department(record) for record in successes), len(successes)),
        "automatic_coverage": rate(len(automatic), total),
        "review_rate": rate(len(review), total),
        "unresolved_rate": rate(total - len(successes), total),
        "wrong_automatic_assignments": rate(sum(incorrect_department(record) for record in automatic), len(automatic)),
        "unsafe_automatic_decisions": rate(sum(incorrect_department(record) or record["expected"]["require_review"] for record in automatic), len(automatic)),
        "required_review_missed": rate(sum(not record["decision"]["needs_review"] for record in required_review), len(required_review)),
        "urgency_errors": rate(sum(record["decision"]["urgency"] != record["expected"]["urgency"] for record in urgency_decided), len(urgency_decided)),
        "urgency_review": rate(sum(record["decision"]["urgency"] == "review" for record in successes), len(successes)),
        "high_urgency_downgraded": rate(sum(record["decision"]["urgency"] == "ordinary" for record in high), len(high)),
        "ordinary_urgency_escalated": rate(sum(record["decision"]["urgency"] == "high" for record in ordinary), len(ordinary)),
        "high_urgency_review": rate(sum(record["decision"]["urgency"] == "review" for record in high), len(high)),
        "service_error_rate": rate(errors["service"], total),
        "latency_ms": {"count": len(latencies), "median": statistics.median(latencies) if latencies else None,
                       "maximum": max(latencies) if latencies else None},
        "usage": {"records_with_usage": len(usage_records),
                  **{key: sum(record["usage"].get(key, 0) for record in usage_records) for key in ("input_tokens", "output_tokens")}},
    }


def load_replay(path, cases, requests, config_hash):
    records = read_jsonl(path)
    indexed = {}
    for record in records:
        if not isinstance(record.get("id"), str) or record["id"] in indexed:
            raise ValueError("Replay records need unique string IDs")
        indexed[record["id"]] = record
    for case, request in zip(cases, requests):
        prior = indexed.get(case["id"])
        if prior is None or prior.get("request") != request:
            raise ValueError("Replay requires a saved record with exactly the same request for every case")
        expected = {"department": case["expected_department"], "urgency": case["expected_urgency"], "require_review": case.get("require_review", False)}
        if prior.get("split") != case["split"] or prior.get("expected") != expected:
            raise ValueError("Replay cannot change a case's labels or split")
        if case["split"] == "holdout" and prior.get("config_sha256") != config_hash:
            raise ValueError("Holdout replay requires the original configuration; tune only on development cases")
        if "response" not in prior or "error" not in prior:
            raise ValueError("Replay record must contain response and error fields")
        if prior["response"] is None and prior["error"] is None:
            raise ValueError("Replay record needs a response or a recorded failure")
        if prior["error"] is not None and (
            not isinstance(prior["error"], dict) or
            prior["error"].get("category") not in ("service", "contract", "policy") or
            not isinstance(prior["error"].get("message"), str)
        ):
            raise ValueError("Replay record has an invalid error shape")
    return indexed


def run(args, *, router=None, live_call=None):
    router = router or load_router()
    live_call = live_call or live_response
    config = router.load_config(args.config)
    cases = load_dataset(args.dataset, config["departments"], args.split)
    if args.max_calls < 1 or args.max_calls > 50:
        raise ValueError("--max-calls must be between 1 and 50")
    if len(cases) > args.max_calls:
        raise ValueError("Selected cases exceed --max-calls; choose a smaller dataset/split (no requests were sent)")
    destination = Path(args.output_dir).expanduser().resolve()
    if destination == ROOT or ROOT in destination.parents:
        raise ValueError("Evaluation outputs must be outside the repository")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Output directory must be new or empty; existing evaluation records are never overwritten")
    api_key = os.environ.get("TYPESAFE_API_KEY", "") if args.mode == "live" else None
    if args.mode == "live" and (not api_key or any(ord(char) < 33 or ord(char) > 126 for char in api_key)):
        raise ValueError("Live mode requires a valid TYPESAFE_API_KEY token")
    config_hash = fingerprint(config)
    requests = [router.build_request(ticket_only(case), config, args.model) for case in cases]
    replay = load_replay(args.replay_from, cases, requests, config_hash) if args.mode == "replay" else {}
    destination.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    records = []
    manifest = {
        "schema_version": 1, "started_at": started, "mode": args.mode,
        "quality_evidence": args.mode == "live" or (args.mode == "replay" and all(record.get("quality_evidence", False) for record in replay.values())),
        "dataset_sha256": fingerprint(cases), "config_sha256": config_hash, "config": config,
        "question_sha256": fingerprint(requests[0]["questions"]), "question_version": getattr(router, "QUESTION_VERSION", None),
        "model_requested": args.model, "split": args.split, "selected_cases": len(cases),
        "max_calls": args.max_calls, "http_attempts": 0,
        "note": "No automatic tuning. Holdout results must not select thresholds or questions.",
    }
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    with (destination / "records.jsonl").open("x", encoding="utf-8") as output:
        for case, request in zip(cases, requests):
            record = {
                "schema_version": 1, "id": case["id"], "split": case["split"], "slice": case["slice"],
                "mode": args.mode, "quality_evidence": manifest["quality_evidence"],
                "expected": {"department": case["expected_department"], "urgency": case["expected_urgency"], "require_review": case.get("require_review", False)},
                "request": request, "request_sha256": fingerprint(request), "question_sha256": fingerprint(request["questions"]),
                "config_sha256": config_hash, "policy": config["policy"], "model_requested": request["model"],
                "model_returned": None, "response": None, "decision": None, "usage": None, "latency_ms": None, "error": None,
            }
            begin = time.monotonic()
            try:
                if args.mode == "live":
                    manifest["http_attempts"] += 1
                    record["response"] = live_call(request, api_key)
                elif args.mode == "mock":
                    record["response"] = mock_response(request)
                else:
                    prior = replay[case["id"]]
                    record["response"], record["error"] = prior["response"], prior["error"]
                    record["source_mode"] = prior["mode"]
                    record["source_latency_ms"] = prior.get("latency_ms")
                if record["response"] is not None:
                    response = record["response"]
                    if isinstance(response, dict):
                        record["model_returned"] = response.get("model")
                    answers = validate_response(request, response)
                    record["usage"] = response["usage"]
                    try:
                        record["decision"] = router.decide(request, answers, config)
                    except (ValueError, KeyError, TypeError, JevError):
                        record["error"] = {"category": "policy", "message": "Routing policy rejected the validated answers"}
            except ServiceError as error:
                record["error"] = {"category": "service", "message": str(error)}
            except (JevError, ValueError, KeyError, TypeError):
                record["error"] = {"category": "contract", "message": "Response did not match the requested answer contract"}
            finally:
                if args.mode == "live":
                    record["latency_ms"] = round((time.monotonic() - begin) * 1000, 3)
            records.append(record)
            output.write(json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n")
            output.flush()
    summary = {"schema_version": 1, "mode": args.mode, "quality_evidence": manifest["quality_evidence"],
               "overall": summarize(records), "by_slice": {name: summarize([record for record in records if record["slice"] == name]) for name in sorted({record["slice"] for record in records})}}
    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (destination / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--split", choices=("development", "holdout", "all"), default="development")
    parser.add_argument("--mode", choices=("mock", "live", "replay"), default="mock")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--max-calls", type=int, default=50)
    parser.add_argument("--replay-from", type=Path)
    args = parser.parse_args(argv)
    if (args.mode == "replay") != (args.replay_from is not None):
        parser.error("--replay-from is required only in replay mode")
    return args


def main(argv=None):
    try:
        summary = run(parse_args(argv))
    except (ValueError, OSError, JevError) as error:
        print(f"Evaluation failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(summary["overall"], indent=2))
    return 1 if summary["overall"]["counts"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
