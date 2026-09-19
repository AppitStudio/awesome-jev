#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Try an Awesome Jev fixture offline, or make one explicitly requested live attempt."""

import argparse
import getpass
import importlib
import json
import os
from pathlib import Path
import sys
import warnings


RECIPES = ("support-routing", "quality-rubric", "span-selection", "rag-triage")


def load_runtime(repo):
    examples = repo / "examples"
    for filename in ("jev_examples/client.py", "jev_examples/recipes.py"):
        if not (examples / filename).is_file():
            raise ValueError("Choose an Awesome Jev checkout with --repo, or run from its root.")
    sys.path.insert(0, str(examples))
    return (
        importlib.import_module("jev_examples.client"),
        importlib.import_module("jev_examples.recipes"),
    )


def private_key():
    key = os.environ.get("TYPESAFE_API_KEY")
    if key:
        return key
    if not sys.stdin.isatty():
        raise ValueError(
            "Live setup needs TYPESAFE_API_KEY in the private process environment, "
            "or run this command in an interactive terminal for a hidden key prompt. "
            "Do not paste the key into chat."
        )
    try:
        with warnings.catch_warnings():
            # getpass normally warns then falls back to echo; refuse that fallback.
            warnings.simplefilter("error", getpass.GetPassWarning)
            key = getpass.getpass("TypeSafe API key (hidden; not saved): ")
    except (getpass.GetPassWarning, EOFError, OSError) as error:
        raise ValueError("A hidden key prompt is unavailable; configure the private process environment.") from error
    if not key:
        raise ValueError("No key entered. Use offline mode or configure TYPESAFE_API_KEY privately.")
    return key


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recipe", choices=RECIPES)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Awesome Jev checkout (default: current directory)")
    parser.add_argument("--live", action="store_true", help="Send the fixture to TypeSafe; may incur charges; one attempt")
    parser.add_argument("--show-request", action="store_true", help="Print the request without reading a key or calling the API")
    parser.add_argument("--model", help="Deliberate model override for a live request or preview")
    args = parser.parse_args(argv)
    if args.model and not (args.live or args.show_request):
        parser.error("--model requires --live or --show-request; offline fixtures keep their authored model.")

    try:
        repo = args.repo.expanduser().resolve()
        client, recipes = load_runtime(repo)
    except (ImportError, OSError, ValueError) as error:
        print(f"Setup stopped: {error}", file=sys.stderr)
        return 1

    try:
        directory = repo / "examples" / args.recipe
        data = json.loads((directory / "input.json").read_text(encoding="utf-8"))
        request = recipes.build_request(args.recipe, data, model=args.model or client.MODEL)
        if args.show_request:
            print(json.dumps(request, indent=2, allow_nan=False))
            return 0
        if args.live:
            response = client.evaluate(request, private_key(), max_attempts=1)
        else:
            response = json.loads((directory / "mock-response.json").read_text(encoding="utf-8"))
        answers = client.validate_response(request, response)
        print(json.dumps({
            "mode": "live" if args.live else "mock (synthetic; not a model evaluation)",
            "recipe": args.recipe,
            "http_attempt_budget": 1 if args.live else 0,
            "requested_model": request["model"],
            "returned_model": response["model"],
            "usage": response["usage"],
            "decision": recipes.decide(args.recipe, request, answers),
        }, indent=2, allow_nan=False))
        return 0
    except (client.JevError, OSError, ValueError, KeyError) as error:
        print(f"Example stopped: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Example cancelled.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
