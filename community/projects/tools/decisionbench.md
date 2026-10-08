# DecisionBench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Evaluation harness and dashboard comparing TypeSafe Jev (via OpenRouter) with Claude Sonnet 5 on the same structured decision tasks — 100 real `invoice_processing` cases with five sub-questions each — reporting accuracy vs gold, cost per 1k decisions, p50/p95 latency and a disagreement view; Jev led overall but Claude won duplicate detection (author-reported).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KizitoNaanma/decisionbench) |
| Maintainer | [KizitoNaanma](https://github.com/KizitoNaanma). Independently curated. |
| Format | pnpm project with Postgres (Docker) and a web dashboard |
| Requirements | Node 20+, pnpm, Docker, Python 3, `psql`; `OPENROUTER_API_KEY` (covers Jev) and `ANTHROPIC_API_KEY`. |
| License | [MIT](https://github.com/KizitoNaanma/decisionbench/blob/196e424b942155e5b1c3322638d078130c6be031/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check whether Jev beats a frontier LLM on your style of structured decision before switching.
- Browse per-case disagreements rather than a single accuracy number.
- Mismatch: one task family (invoices); results are task-dependent.

## How it works

[`src/lib/models/jev.ts`](https://github.com/KizitoNaanma/decisionbench/blob/196e424b942155e5b1c3322638d078130c6be031/src/lib/models/jev.ts) calls Jev through OpenRouter; cases come from the `LocalLLaMA/typed-decisions` dataset and extend TypeSafe's published `Luni/laya-jev-benchmark` numbers; runs are stored in Postgres for the dashboard.

## Get started

Install, configure keys and start the database (README *Running it yourself*):

```sh
git clone https://github.com/KizitoNaanma/decisionbench.git && cd decisionbench
pnpm install
cp .env.example .env   # ANTHROPIC_API_KEY, OPENROUTER_API_KEY
pnpm db:up
```

Benchmark runs bill OpenRouter (Jev) and Anthropic.

## Examples and demos

- README *Findings* (82.1% vs 62.2% accuracy; $0.0245 vs $3.2287 per 1k decisions — author-reported).

## Limits and data handling

Benchmark cases are public datasets; results are the author's single run. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 196e424b9421](https://github.com/KizitoNaanma/decisionbench/tree/196e424b942155e5b1c3322638d078130c6be031). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
