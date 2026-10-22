# system-one-decision-bench (Jev vs chat LLMs, with confidence cascades)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open, reproducible benchmark from Dwayo AI comparing Jev with a chat model on banking77 routing and a guardrail set for accuracy, calibration, latency and cost, plus a confidence cascade that escalates only uncertain calls, with negative results reported.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dwayo-ai/system-one-decision-bench) |
| Maintainer | [dwayo-ai](https://github.com/dwayo-ai). Independently curated. |
| Format | Python benchmark harness |
| Requirements | Python 3.11+; a TypeSafe API key and a chat-provider key for baselines (mock backends need none). |
| License | [Apache-2.0](https://github.com/dwayo-ai/system-one-decision-bench/blob/6f7ddd309a918bfac6b2b716990c3fda4c2a6224/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_bench/deciders/jev_http.py`](https://github.com/dwayo-ai/system-one-decision-bench/blob/6f7ddd309a918bfac6b2b716990c3fda4c2a6224/src/jev_bench/deciders/jev_http.py) at the pinned commit. |

## When to use

- Decide which of your LLM calls could be decision-model calls.
- Reproduce a dated Jev snapshot against your own chat baseline.
- Mismatch: results are a snapshot on the run date, not a lasting property of the model.

## How it works

`src/jev_bench/deciders/jev_http.py` calls Jev (`jev-1.13.0`, set in `config/models.yaml`) over HTTP for each benchmark item; the cascade sends low-confidence items to the chat model. Integration evidence: [`src/jev_bench/deciders/jev_http.py`](https://github.com/dwayo-ai/system-one-decision-bench/blob/6f7ddd309a918bfac6b2b716990c3fda4c2a6224/src/jev_bench/deciders/jev_http.py).

## Get started

From the upstream README (not run on the review host):

```sh
make setup
cp .env.example .env
make test lint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/dwayo-ai/system-one-decision-bench/blob/main/results/REPORT.md](https://github.com/dwayo-ai/system-one-decision-bench/blob/main/results/REPORT.md)
- Write-up: [dwayo.ai/blog/jev-system-one-decision-model-benchmark/](https://dwayo.ai/blog/jev-system-one-decision-model-benchmark/)

## Limits and data handling

Benchmark items are sent to TypeSafe and the chat provider during real runs.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 6f7ddd309a91](https://github.com/dwayo-ai/system-one-decision-bench/tree/6f7ddd309a918bfac6b2b716990c3fda4c2a6224). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
