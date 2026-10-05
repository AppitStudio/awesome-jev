# Cygnet recipe

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent recipe that answers Jev-format typed decisions (`choice`, `noul`, `score`) with frozen Gemma-4-12B-it on unmodified vLLM via a one-token option-letter readout and a `/v1/systemone` shim; not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blockbrain-ai/cygnet-recipe) |
| Maintainer | [blockbrain-ai](https://github.com/blockbrain-ai). Independently curated. |
| Format | Reproducible recipe: serving shim, application server, and benchmark commands |
| Requirements | A GPU able to serve Gemma-4-12B-it with vLLM 0.30.0 (pinned image digest in the README); no TypeSafe key for self-hosting. |
| License | [MIT (shim and docs); Gemma weights Apache-2.0](https://github.com/blockbrain-ai/cygnet-recipe/blob/10b4099a61e7dca6a82032b54c74dc0a8c496d4b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Point an existing Jev client at a self-hosted decision endpoint built on open weights.
- Study how a one-token readout turns a generative model into a calibrated option scorer.
- Mismatch: no GPU, or you need vendor support: use hosted Jev.

## How it works

The shim presents options as letters, reads the model's probability for each letter at one answer position, and applies a calibration step; `shim/decision_server.py` serves the same readout on `POST /v1/systemone` and `GET /v1/models` with application features. Upstream reports a JevBench v1.5.4 overall #1 measured by the benchmark's evaluators; that is a maintainer-cited result, not reproduced here.

## Get started

Serve Gemma with vLLM as documented, then start the application server:

```sh
pip install vllm==0.30.0
# start vLLM with google/gemma-4-12B-it per the README, then:
python3 shim/decision_server.py
curl -s http://127.0.0.1:8009/v1/systemone -H 'Content-Type: application/json' -d '{...}'
```

Self-hosted inference has no TypeSafe charge; GPU costs are yours.

## Examples and demos

- README benchmark commands against JevBench public items and `shim/test_decision_server.py` (runs without a GPU against a stand-in).

## Limits and data handling

Gemma weights are subject to Google's Gemma Prohibited Use Policy (see upstream NOTICE.md). Benchmark rankings are cited from upstream. Independent of TypeSafe.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 10b4099a61e7](https://github.com/blockbrain-ai/cygnet-recipe/tree/10b4099a61e7dca6a82032b54c74dc0a8c496d4b). Inspected the README (method, disclosures, licence section) and LICENSE; no model was served on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
