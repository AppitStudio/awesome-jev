# Decision models vs small LLMs (Jev, Kev, Laya and Mammoth-1 against cheap LLMs on agent decisions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rerunnable comparison of decision models (Jev 1.14, Kev-4B, Laya, Mammoth-1) with small LLMs on six decisions an agent makes between generative steps: routing, classification, a guardrail, an ordered score and a mixed workflow, scored on accuracy, calibration, format failures, latency and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pournasserian/decision-models-vs-small-llms) |
| Maintainer | [pournasserian](https://github.com/pournasserian). Independently curated. |
| Format | Python benchmark harness with raw results and reports |
| Requirements | Python; OpenRouter and Vercel AI Gateway keys to rerun. |
| License | [MIT](https://github.com/pournasserian/decision-models-vs-small-llms/blob/28a026a22c0dd5cc35d93bd9c80c48f255a88a37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bench/config.py`](https://github.com/pournasserian/decision-models-vs-small-llms/blob/28a026a22c0dd5cc35d93bd9c80c48f255a88a37/bench/config.py) at the pinned commit. |

## When to use

- Decide whether a decision model or a small LLM fits an agent step.
- Reuse the harness and raw request/response logs for your own comparison.
- Mismatch: Jev is reached through OpenRouter's Decisions API, not TypeSafe directly.

## How it works

`bench/config.py` defines each model; Jev is `typesafe/jev-1.14` through OpenRouter's Decisions API. Every model gets the same System One-shaped question; LLMs answer under a strict JSON schema. Spending is logged in `ledger.csv`. Integration evidence: [`bench/config.py`](https://github.com/pournasserian/decision-models-vs-small-llms/blob/28a026a22c0dd5cc35d93bd9c80c48f255a88a37/bench/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/pournasserian/decision-models-vs-small-llms
# see README for running bench/ against each dataset
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Reports: [github.com/pournasserian/decision-models-vs-small-llms/tree/master/reports](https://github.com/pournasserian/decision-models-vs-small-llms/tree/master/reports)
- Article: [pournasserian.com/writing](https://pournasserian.com/writing)

## Limits and data handling

Benchmark data goes to the gateways. Results are the author's own and were not reproduced.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 28a026a22c0d](https://github.com/pournasserian/decision-models-vs-small-llms/tree/28a026a22c0dd5cc35d93bd9c80c48f255a88a37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
