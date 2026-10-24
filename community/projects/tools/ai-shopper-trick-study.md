# Can You Trick an AI Shopper? (study with a Jev trick shield and router)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Preregistered study of store tricks on AI shopping agents (47,215 decisions across five models); in phase 2 Jev labels every listing line to strip sales pressure and AI-directed text, and routes easy shelves to a small model and hard ones to a large one.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frostyhand/can-you-trick-an-ai-shopper) |
| Maintainer | [frostyhand](https://github.com/frostyhand). Independently curated. |
| Format | Python study code, data and charts |
| Requirements | Python 3; a TypeSafe key only to rerun Jev calls (raw results are included). |
| License | [MIT (code); CC BY 4.0 (data)](https://github.com/frostyhand/can-you-trick-an-ai-shopper/blob/9fde24f529f62da738ed3a291f5365042a68e52b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`study/shield.py`](https://github.com/frostyhand/can-you-trick-an-ai-shopper/blob/9fde24f529f62da738ed3a291f5365042a68e52b/study/shield.py) at the pinned commit. |

## When to use

- Reuse a prompt-injection and dark-pattern shield for shopping agents.
- Study cost-aware routing between a small and a large model.
- Mismatch: research code on fictional products, not a library.

## How it works

`study/shield.py` uses the Python SDK (`typesafe_sdk`) with choice and noul questions to label listing snippets and rate how clear-cut each shelf is. The README reports results; they were not reproduced here. Integration evidence: [`study/shield.py`](https://github.com/frostyhand/can-you-trick-an-ai-shopper/blob/9fde24f529f62da738ed3a291f5365042a68e52b/study/shield.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -q study/tests
.venv/bin/python -m study.analyze
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results and method: [github.com/frostyhand/can-you-trick-an-ai-shopper#readme](https://github.com/frostyhand/can-you-trick-an-ai-shopper#readme)

## Limits and data handling

Reported numbers are the authors' own measurements. Video assets are licensed separately and not in the repo.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 9fde24f529f6](https://github.com/frostyhand/can-you-trick-an-ai-shopper/tree/9fde24f529f62da738ed3a291f5365042a68e52b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
