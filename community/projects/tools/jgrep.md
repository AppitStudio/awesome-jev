# jgrep

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Filters text, structured records, functions, and diff hunks against plain-English descriptions using Jev Noul judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/keltokhy/jgrep) |
| Maintainer | [keltokhy](https://github.com/keltokhy) (Khaled Eltokhy); submitted from the maintainer's account with Codex assistance. |
| Format | Python library and CLI; `jev-grep` 0.2.1. |
| Requirements | Python 3.10+; live inference requires a configured TypeSafe or OpenRouter key and incurs provider charges. |
| Access | MIT-licensed source; bring your own provider key. No hosted service is included. |
| License | [MIT](https://github.com/keltokhy/jgrep/blob/fdceb6bdf79165a133667b8e57f3b7244545f0a2/LICENSE). |
| Disclosure | Maintainer self-submission, prepared and source-reviewed by Codex; no independent human review or directory endorsement is claimed. |

## When to use

Use it to filter logs or structured records by a natural-language description, or retrieve complete Python functions and unified diff hunks for review. A configurable probability threshold decides which source units are printed.

## How it works

Jev receives the input unit and one or more Noul questions derived from the description. Python parses records or code units, validates returned probabilities, applies the threshold, and preserves source text. Functions and diff hunks are treated as complete units rather than individual lines.

Inspected implementation:

- [src/jgrep/core.py](https://github.com/keltokhy/jgrep/blob/fdceb6bdf79165a133667b8e57f3b7244545f0a2/src/jgrep/core.py#L204)
- [src/jgrep/cli.py](https://github.com/keltokhy/jgrep/blob/fdceb6bdf79165a133667b8e57f3b7244545f0a2/src/jgrep/cli.py#L30)
- [src/jgrep/code_inputs.py](https://github.com/keltokhy/jgrep/blob/fdceb6bdf79165a133667b8e57f3b7244545f0a2/src/jgrep/code_inputs.py#L1)

Default model identifiers at the reviewed revision: `jev-latest` on TypeSafe; `~typesafe/jev-latest` on OpenRouter; aliases can change.

## Get started

Install [uv](https://docs.astral.sh/uv/) and use the upstream instructions for other package managers.

```sh
uv tool install jev-grep
# Offline estimate on synthetic text; no credentials or provider calls.
printf '%s\n' 'Checkout failed again.' | jgrep "a payment failed" --estimate --json
```

For live use, configure `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` privately, following the [upstream README](https://github.com/keltokhy/jgrep/blob/fdceb6bdf79165a133667b8e57f3b7244545f0a2/README.md). Input text is sent to the chosen provider and calls may be billed.

After configuring a provider key, omit `--estimate` to make billable Jev calls and print matching text. `jgrep --jsonl --field message "a payment failed" events.jsonl` filters complete records by a selected field. Install `jev-grep[code]` for optional Go parsing; Python functions and unified diffs work with the base package.

The example commands above were checked against source and documentation. The submission review ran only the tests listed below; it did not run a live provider workflow or independently test the published package installation.

## Examples and demos

- [Upstream usage examples](https://github.com/keltokhy/jgrep/blob/fdceb6bdf79165a133667b8e57f3b7244545f0a2/README.md) document the CLI and Python paths.
- [Tests](https://github.com/keltokhy/jgrep/tree/fdceb6bdf79165a133667b8e57f3b7244545f0a2/tests) provide runnable fixture-based checks.
- No separate hosted demo was verified for this submission.

## Limits and data handling

Judged text and any requested surrounding context are sent to TypeSafe, OpenRouter, or a configured gateway. Answers are cached locally. Ordinary inputs may be truncated at the configured character limit, with a warning; oversized function/diff units fail instead. Model scores are retrieval evidence, not proof that a code change is correct or safe. Provider errors can produce partial output with a nonzero exit status.

## Review and maintenance

Reviewed on **2026-09-20** at [commit fdceb6b](https://github.com/keltokhy/jgrep/tree/fdceb6bdf79165a133667b8e57f3b7244545f0a2). Codex inspected the public README, license, package manifest, Jev call sites, and relevant tests.

Ran `uv run --group dev pytest -q tests/test_core.py tests/test_code_inputs.py`: **47 passed, 5 skipped in 1.15s**. These offline fixture checks verify software behavior; they do not measure Jev accuracy, latency, or calibration. No live inference was performed for this listing.
