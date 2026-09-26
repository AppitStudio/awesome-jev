# jev-frontier-bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible benchmark of TypeSafe Jev 1.13 against frontier LLMs on 200 typed decisions with accuracy, calibration, human-agreement, latency, and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/manjunathshiva/jev-frontier-bench) |
| Maintainer | [manjunathshiva](https://github.com/manjunathshiva). Independently curated. |
| Format | Python benchmark + results figures. |
| Requirements | Python; OPENROUTER_API_KEY for live reruns. Offline results ship in-repo. |
| License | [MIT](https://github.com/manjunathshiva/jev-frontier-bench/blob/a532783efffbd57ad31781d2d9d5bb55c988bc16/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Upstream metrics not independently reproduced. |

## When to use

Use to **inspect or rerun** a published Jev-vs-frontier comparison on shared public datasets.

## How it works

[`jev_client.py`](https://github.com/manjunathshiva/jev-frontier-bench/blob/a532783efffbd57ad31781d2d9d5bb55c988bc16/jev_client.py) calls OpenRouter Decisions for Jev; LLMs return JSON-schema probabilities. Charts under `results/`.

## Get started

```sh
git clone https://github.com/manjunathshiva/jev-frontier-bench.git
cd jev-frontier-bench
git checkout a532783efffbd57ad31781d2d9d5bb55c988bc16
pip install -r requirements.txt
# echo OPENROUTER_API_KEY=... > .env   # live rerun only
```

## Examples and demos

- Medium write-up linked from README; figures in `results/`.

## Limits and data handling

Live prompts go to OpenRouter. Metrics are as of the pinned run described in the README.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit a532783](https://github.com/manjunathshiva/jev-frontier-bench/tree/a532783efffbd57ad31781d2d9d5bb55c988bc16). AI-assisted README and LICENSE inspection of client and results tree; install/live paths not executed.
