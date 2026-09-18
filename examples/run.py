#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run with mock fixtures unless --live is explicitly supplied."""

import argparse
import json
import os
import sys
from pathlib import Path

from jev_examples.client import JevError, MODEL, evaluate, validate_response
from jev_examples.recipes import RECIPES, build_request, decide


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recipe", choices=RECIPES)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--mock", action="store_true", help="Use synthetic local responses (default)")
    mode.add_argument("--live", action="store_true", help="Call TypeSafe; requires TYPESAFE_API_KEY and may incur charges")
    parser.add_argument("--show-request", action="store_true", help="Print the request and exit without contacting the API")
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent / args.recipe
    try:
        data = json.loads((directory / "input.json").read_text(encoding="utf-8"))
        model = os.environ.get("JEV_MODEL", MODEL) if args.live else MODEL
        request = build_request(args.recipe, data, model=model)
        if args.show_request:
            print(json.dumps(request, indent=2))
            return 0
        if args.live:
            response = evaluate(request, os.environ.get("TYPESAFE_API_KEY"))
        else:
            response = json.loads((directory / "mock-response.json").read_text(encoding="utf-8"))
        answers = validate_response(request, response)
        result = {
            "mode": "live" if args.live else "mock (synthetic; not a model evaluation)",
            "recipe": args.recipe,
            "model": response["model"],
            "usage": response["usage"],
            "decision": decide(args.recipe, request, answers),
        }
        print(json.dumps(result, indent=2))
        return 0
    except (JevError, ValueError, KeyError, OSError) as error:
        print(f"Example stopped: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
