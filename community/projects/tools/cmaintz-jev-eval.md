# jev-eval (calibrate Jev confidence thresholds on your labeled data)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI that runs your labeled rows through Jev once, then reports per-question accuracy, calibration (ECE and reliability tables) and risk-coverage, and recommends the confidence cut-points to gate on, written to a thresholds file the author's other Jev tools can load.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CMaintz/jev-eval) |
| Maintainer | [CMaintz](https://github.com/CMaintz). Independently curated. |
| Format | Python CLI (stdlib only) |
| Requirements | Python 3.10+; a TypeSafe API key for the `run` step only. |
| License | [MIT](https://github.com/CMaintz/jev-eval/blob/d8fb0182d49a22e5ff71b108eb332416737511a9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_eval/provider.py`](https://github.com/CMaintz/jev-eval/blob/d8fb0182d49a22e5ff71b108eb332416737511a9/src/jev_eval/provider.py) at the pinned commit. |

## When to use

- Pick a confidence threshold for a Jev-gated workflow from measured accuracy instead of a guess.
- Compare two model pins or two question wordings on the same rows.
- Mismatch: needs labeled data from your own domain; it does not label data for you.

## How it works

`src/jev_eval/provider.py` posts one batched request per labeled row to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default, pinnable) and caches answers locally; `report`, `thresholds`, `compare`, `calibrate` and `check` then work offline on that cache. Integration evidence: [`src/jev_eval/provider.py`](https://github.com/CMaintz/jev-eval/blob/d8fb0182d49a22e5ff71b108eb332416737511a9/src/jev_eval/provider.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/CMaintz/jev-eval
cd jev-eval && pip install .
jev-eval run --data labeled.jsonl --config jev-eval.json --cache run.jsonl
jev-eval thresholds --cache run.jsonl --target-accuracy 0.95
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Command reference and input formats in the README: [github.com/CMaintz/jev-eval#readme](https://github.com/CMaintz/jev-eval#readme)

## Limits and data handling

The `state` of every labeled row is sent to TypeSafe during `run`; the `meta` field stays local. Install line is inferred from the package's `pyproject.toml` (no PyPI release verified).

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit d8fb0182d49a](https://github.com/CMaintz/jev-eval/tree/d8fb0182d49a22e5ff71b108eb332416737511a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
