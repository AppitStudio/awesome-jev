#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Synthetic UI fixture; --live changes only the decision provider (one HTTP attempt)."""

import argparse
import json
import os
from pathlib import Path
import sys

DIRECTORY = Path(__file__).resolve().parent
sys.path.insert(0, str(DIRECTORY.parent))

from jev_examples.client import JevError, evaluate  # noqa: E402
from jev_examples.computer_use import apply_to_fixture, build_request, prepare, verify_fixture  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="One TypeSafe attempt; may incur charges")
    parser.add_argument("--show-request", action="store_true", help="Print payload without contacting TypeSafe")
    args = parser.parse_args(argv)
    case = json.loads((DIRECTORY / "input.json").read_text())
    request = build_request(case)
    if args.show_request:
        print(json.dumps(request, indent=2))
        return 0
    try:
        response = evaluate(request, os.environ.get("TYPESAFE_API_KEY"), max_attempts=1) if args.live else json.loads(
            (DIRECTORY / "mock-response.json").read_text()
        )
        proposal = prepare(request, response)
        result = proposal
        if proposal["status"] == "ready":
            after = apply_to_fixture(proposal, case["snapshot"], case["values"],
                                     allowed_surface="https://invoice.example.invalid/fixture",
                                     allowed_fields={"e1", "e2"})
            result = verify_fixture(case, after, proposal)
        print(json.dumps({
            "mode": "live judgments, simulated UI" if args.live else "synthetic judgments and simulated UI",
            "raw_response": response, "proposal": proposal, "result": result,
        }, indent=2))
        return 0 if result["status"] == "simulated_verified" else 2
    except (JevError, ValueError, KeyError, OSError) as error:
        print(f"Example stopped: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
