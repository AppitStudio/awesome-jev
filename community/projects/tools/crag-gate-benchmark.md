# CRAG Gate Benchmark (Jev vs. GPT-4.1 Mini as the filtering gate in corrective RAG)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Audited benchmark asking whether Jev can replace GPT-4.1 Mini as the product-filtering and routing gate in a corrective RAG workflow on Amazon ESCI: 800 calibration and 2,000 held-out queries with a shared BGE reranker and real OpenRouter calls; it publishes the failed acceptance condition as well as the precision, latency and cost gains.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Tue2day/crag-gate-benchmark) |
| Maintainer | [Tue2day](https://github.com/Tue2day). Independently curated. |
| Format | Python benchmark with results and reports |
| Requirements | Python 3.11–3.12; an OpenRouter key for live runs; a mock configuration runs offline. |
| License | [MIT](https://github.com/Tue2day/crag-gate-benchmark/blob/aa341063f8171eafdf65e4a3846a5221983c67de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`config.example.toml`](https://github.com/Tue2day/crag-gate-benchmark/blob/aa341063f8171eafdf65e4a3846a5221983c67de/config.example.toml) at the pinned commit. |

## When to use

- Decide whether a decision model can stand in for a small LLM as a RAG filter.
- Reuse the calibration and held-out method for your own gate.
- Mismatch: one dataset; numbers are the author's.

## How it works

`config.example.toml` sets `jev_model = "typesafe/jev-1.13"` for the OpenRouter route; Jev answers native Noul and Choice questions over the top five reranked items, and the same deterministic rule turns either model's answers into keep, filter or fallback. Integration evidence: [`config.example.toml`](https://github.com/Tue2day/crag-gate-benchmark/blob/aa341063f8171eafdf65e4a3846a5221983c67de/config.example.toml).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Tue2day/crag-gate-benchmark && cd crag-gate-benchmark
# see docs/REPRODUCIBILITY.md; config.mock.toml runs without API calls
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Experiment report: [github.com/Tue2day/crag-gate-benchmark/blob/main/docs/EXPERIMENT_REPORT.md](https://github.com/Tue2day/crag-gate-benchmark/blob/main/docs/EXPERIMENT_REPORT.md)
- README: [github.com/Tue2day/crag-gate-benchmark#readme](https://github.com/Tue2day/crag-gate-benchmark#readme)

## Limits and data handling

Live runs send queries and product text to OpenRouter and on to TypeSafe; Jev is reached through OpenRouter. All results are the author's, not verified here. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit aa341063f817](https://github.com/Tue2day/crag-gate-benchmark/tree/aa341063f8171eafdf65e4a3846a5221983c67de). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
