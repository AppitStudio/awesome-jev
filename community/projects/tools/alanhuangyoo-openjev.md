# OpenJev (alanhuangyoo)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

OpenJev (`wev-ai` / `openjev-ai` on PyPI): open, local System One decision models OpenJev-1.7B/4B/8B on Hugging Face that answer the `POST /v1/systemone` request shape for general decisions and browser-agent steps; independent, distinct from other projects named OpenJev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alanhuangyoo/OpenJev) |
| Maintainer | [alanhuangyoo](https://github.com/alanhuangyoo). Independently curated. |
| Format | Python package + HTTP server (`wev serve`) + training recipes |
| Requirements | Python; GPU recommended (OpenJev-4B v0.2 needs transformers 5); no API key. |
| License | [Apache-2.0](https://github.com/alanhuangyoo/OpenJev/blob/e23a44ac3c5289d5a91802d9b7fd8961850ea960/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run triage, routing or policy checks locally with a Jev-compatible endpoint.
- Use a local decider for browser-agent steps and compare against hosted models.
- Mismatch: not TypeSafe Jev; 8B and 1.7B are still v0.1.

## How it works

`wev.load("alanhuangya/OpenJev-4B")` loads a fine-tuned backbone; `predict(state, questions)` returns calibrated probabilities per option in one forward pass, and `wev serve` exposes `/v1/systemone` ([`wev/api.py`](https://github.com/alanhuangyoo/OpenJev/blob/e23a44ac3c5289d5a91802d9b7fd8961850ea960/wev/api.py)). The repo includes data and training scripts.

## Get started

Install and serve a model locally:

```sh
pip install "wev-ai[serve]"
wev serve --model alanhuangya/OpenJev-4B --port 8009
curl -s localhost:8009/v1/systemone -H 'content-type: application/json' -d '{"state": "...", "questions": {...}}'
```

No hosted calls; local compute only.

## Examples and demos

- README results tables (wev-bench, live-website tasks) — upstream-reported.
- Hugging Face [model collection](https://huggingface.co/collections/alanhuangya/wev-6ab4eb5d872c9ae9fd68faa6) and project Space.

## Limits and data handling

Benchmarks and calibration figures are maintainer-reported; not reproduced. Independent of TypeSafe; not a validated substitute. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit e23a44ac3c52](https://github.com/alanhuangyoo/OpenJev/tree/e23a44ac3c5289d5a91802d9b7fd8961850ea960). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
