# Decision Layer Benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

What an AI agent's decision layer (routing, prompt-injection, PII, permission, next step) costs on OpenAI, Anthropic, Google and TypeSafe Jev 1.13, with code and a PDF report to rerun it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GOhaike/decision-layer-benchmark) |
| Maintainer | [GOhaike](https://github.com/GOhaike). Independently curated. |
| Format | Python benchmark + PDF report |
| Requirements | Python; provider keys to rerun. |
| License | [MIT](https://github.com/GOhaike/decision-layer-benchmark/blob/62a6a269bace25415cf68dd10f1abd107f4856cf/LICENSE) |
| Jev evidence | [`benchmark/jev_cost_model.py`](https://github.com/GOhaike/decision-layer-benchmark/blob/62a6a269bace25415cf68dd10f1abd107f4856cf/benchmark/jev_cost_model.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Estimate the monthly cost of moving agent decisions onto Jev.
- Mismatch: cost model with author assumptions; prices change.

## How it works

Cost models and a billing probe price five decision questions per request across providers; the report summarizes results. (Summarized from the upstream [README](https://github.com/GOhaike/decision-layer-benchmark/blob/62a6a269bace25415cf68dd10f1abd107f4856cf/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): clone and run the scripts in `benchmark/` per the README.

## Limits and data handling

Probe requests go to providers when rerun live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 62a6a269bace](https://github.com/GOhaike/decision-layer-benchmark/tree/62a6a269bace25415cf68dd10f1abd107f4856cf). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
