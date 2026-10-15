# Jev 1.14 comparison benchmark (etsabary)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

1,136 deterministic text decisions across 25 families run on eleven services (Jev 1.14 and 1.13, Luna Decisions, Luna, Mercury, Gemini Flash-Lite, Qwen, Granite and others) with matched diagnostics, latency percentiles and versioned results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/etsabary/jev-1.14-comparison-benchmark) |
| Maintainer | [etsabary](https://github.com/etsabary). Independently curated. |
| Format | Python benchmark scripts, data, figures and report |
| Requirements | Python; an OpenRouter key to rerun model calls. |
| License | [MIT](https://github.com/etsabary/jev-1.14-comparison-benchmark/blob/d35fecc5bbb3bedaa54f015d8b64b399147a2c14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run_benchmark.py`](https://github.com/etsabary/jev-1.14-comparison-benchmark/blob/d35fecc5bbb3bedaa54f015d8b64b399147a2c14/run_benchmark.py) at the pinned commit. |

## When to use

- Compare Jev 1.14 with Jev 1.13 and general LLMs on single-answer decisions before upgrading.
- Reuse the question bank and analysis scripts for your own model comparison.
- Mismatch: author's question bank and a single collection day (15 Oct 2026) via OpenRouter; not reproduced here.

## How it works

Every model gets the same instructions, facts, question and five options in the same order; `run_benchmark.py` collects first attempts through OpenRouter, and analysis scripts separate wrong valid answers from errors and report median/p95 latency. Integration evidence: [`run_benchmark.py`](https://github.com/etsabary/jev-1.14-comparison-benchmark/blob/d35fecc5bbb3bedaa54f015d8b64b399147a2c14/run_benchmark.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/etsabary/jev-1.14-comparison-benchmark.git && cd jev-1.14-comparison-benchmark
python validate.py
python analyze.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Family tables: `FUNCTIONS.md`.
- Companion image benchmark: [github.com/etsabary/visual-decision-benchmark](https://github.com/etsabary/visual-decision-benchmark)

## Limits and data handling

Benchmark questions are synthetic and go to OpenRouter on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit d35fecc5bbb3](https://github.com/etsabary/jev-1.14-comparison-benchmark/tree/d35fecc5bbb3bedaa54f015d8b64b399147a2c14). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
