# jev-batch (BramVR, formerly jev-cli) (dependency-free Python CLI and agent skill for classifying many records with Jev, then scoring and counting the results offline)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-file Python 3.9+ standard-library CLI (renamed from jev-cli): write a question document, classify one JSON record or a JSONL batch, cache responses, then `summarize` label counts and `eval` saved results against hand labels (confusion matrix and calibration buckets) offline; ships example question sets and a `SKILL.md` so coding agents can run classify-many loops.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BramVR/jev-batch) |
| Maintainer | [Bram Van Rompuy](https://github.com/BramVR) (BramVR). Independently curated. |
| Format | Single-file Python CLI plus agent skill (installed command `jev-batch`) |
| Requirements | Python 3.9+. By default it calls OpenCode's free `jev-1.13-free` endpoint with no key; for TypeSafe pass `--base-url https://api.typesafe.ai/v1 --model jev-1.14.0` and set `TYPESAFE_API_KEY` (or a macOS Keychain item under service `typesafe`). |
| License | [MIT](https://github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The project says it is unofficial and not affiliated with TypeSafe. |
| Jev evidence | [`jev.py`](https://github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/jev.py) at the pinned commit. |

## When to use

- Label a JSONL file, let a coding agent classify many records from the shell, or check Jev's answers against your own hand labels before relying on a threshold.
- Mismatch: confidential data with the default endpoint; records go to OpenCode's free service unless you point it at TypeSafe.

## How it works

`jev.py` defaults to `https://opencode.ai/zen/v1` with model `jev-1.13-free` and appends `/systemone`; it reads a TypeSafe key only when the origin is exactly `https://api.typesafe.ai`, and other origins get no Authorization header. `--dry-run` validates questions and records and estimates cost without sending anything; `--cache DIR` reuses successful responses after an interrupted batch. Integration evidence: [`jev.py`](https://github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/jev.py).

## Get started

Run it from a checkout (no install needed), or install the `jev-batch` command with `uvx --from git+…`; a PyPI release was not found when checked (2026-11-26).

```sh
git clone https://github.com/BramVR/jev-batch && cd jev-batch
printf '%s\n' '{"id":"t1","state":"Charged twice"}' | python3 jev.py classify --questions questions.json
# TypeSafe instead of the free default:
TYPESAFE_API_KEY=... python3 jev.py batch --base-url https://api.typesafe.ai/v1 --model jev-1.14.0 --questions examples/failure-patterns.json < records.jsonl > results.jsonl
python3 jev.py summarize --question failure_pattern --questions examples/failure-patterns.json < results.jsonl
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/README.md](https://github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/README.md)
- Agent skill: [github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/SKILL.md](https://github.com/BramVR/jev-batch/blob/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8/SKILL.md)

## Limits and data handling

The default sends record text to OpenCode's free endpoint (a third party, not TypeSafe); switch the base URL for TypeSafe. Free OpenCode and Jev 1.13 reject Box questions and image assets. The old `BramVR/jev-cli` URL redirects to this repository.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia); refreshed **2026-11-26** at [commit 1d3ee1ea6c71](https://github.com/BramVR/jev-batch/tree/1d3ee1ea6c71c8ddaa03c09990dec63302b8f8a8) after the repository was renamed from jev-cli to jev-batch and gained an MIT licence. Inspected the upstream README, LICENSE and `jev.py`; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
