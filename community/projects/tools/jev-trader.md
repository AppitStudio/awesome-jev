# Jev Trader

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev Trader is a trading experiment for studying how Jev direction judgments connect to market data, order execution, and a streaming dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jarrodwatts/jev-trader) |
| Maintainer | [Jarrod Watts](https://github.com/jarrodwatts). |
| Format | Bun/TypeScript trading reference with a Next.js dashboard. |
| Jev's role | Optional buy/sell classification over MON-USDC order-book and trade data. Default `MODEL=mock` uses a local heuristic. |
| Requirements | Bun; Monad RPC connectivity; `TYPESAFE_AI_API_KEY` for Jev; a wallet and funds only for live order execution. |
| License | [MIT](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/LICENSE). |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use this as an inspectable integration experiment for market-data ingestion, model decisions, asynchronous transaction receipts, and SSE visualization.

Its simulation is useful for understanding plumbing. It does not establish profitability, predictive accuracy, or readiness to trade funds.

## How it works

[`src/model.ts`](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/src/model.ts) uses the Vercel AI SDK's `experimental_evaluate` and `@ai-sdk/typesafe-ai`. Jev receives order-book depth, recent prices, trade flow, horizon, and allowed sides. A Choice question selects buy or sell; `JEV_MODEL_ID` defaults to `jev-latest`.

[`src/trader.ts`](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/src/trader.ts) permits one processing loop at a time, tracks positions, and applies position/margin restrictions. It may reverse the model's chosen side when only the opposite side is allowed. The returned probabilities remain attached even when that policy changes the action.

[`src/market.ts`](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/src/market.ts) posts a limit order and cancels known resting orders in one update. Transaction submission, confirmation, and fills are distinct events. In dry-run mode, observed market prints drive simulated fills.

The [TypeSafe API reference](https://docs.typesafe.ai/api) describes the underlying provider; direct API compatibility and the SDK path were not executed in this review.

## Get started

The following path starts the heuristic model with simulated execution. **It still contacts live Monad RPC services.** It makes no Jev request with `MODEL=mock` and explicitly disables real trading:

```sh
git clone https://github.com/jarrodwatts/jev-trader.git
cd jev-trader
git checkout b587759e459ea049590102e54a0b07800864cdc3
cp .env.example .env
bun install
DRY_RUN=true MODEL=mock bun run start
```

Inspect the [example configuration](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/.env.example), leaving `PRIVATE_KEY` empty. The backend serves a snapshot at `http://localhost:3000/`, recent events at `/history`, and an SSE stream at `/events`. Stop the process to stop polling.

To evaluate Jev, privately configure `TYPESAFE_AI_API_KEY` and select `MODEL=jev` while retaining `DRY_RUN=true`. This is a continuous paid-provider path, not a bounded one-call demo; stop it when your planned test is complete.

The optional [web dashboard](https://github.com/jarrodwatts/jev-trader/tree/b587759e459ea049590102e54a0b07800864cdc3/web) has separate Bun dependencies. Run its backend on port 3001 and set `NEXT_PUBLIC_API_URL=http://localhost:3001` when launching the web app on port 3000. Otherwise the frontend defaults to an upstream hosted backend.

No install or run command above was executed for this catalog review.

## Examples and demos

- [README event examples](https://github.com/jarrodwatts/jev-trader#endpoints) show decisions, quotes, confirmations, and simulated versus actual fills. These are upstream examples, not review measurements.
- [Dashboard source and setup](https://github.com/jarrodwatts/jev-trader/tree/b587759e459ea049590102e54a0b07800864cdc3/web) provide an SSE display of the experiment.
- [Calldata check](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/scripts/dry-encode.ts) signs with a random wallet and checks encoded orders without broadcasting. Despite the README's “offline” wording, it reads market parameters and the order book over RPC.

The README links a deployed backend described as dry-run/mock. Its availability and running model were not independently checked.

## Limits and data handling

- Jev mode sends market state to TypeSafe. RPC providers receive market queries; live mode broadcasts signed transactions. The dashboard API exposes wallet address, decisions, fills, and history without authentication in the inspected server.
- Live mode can automatically deposit funds into Kuru margin and grant a large token allowance during startup. Merely supplying `PRIVATE_KEY` enables that path unless `DRY_RUN=true` remains set.
- The decision question describes crossing the spread with an immediate-or-cancel order, while execution now uses post-only limit orders. This policy mismatch matters when interpreting decisions.
- The model has only buy/sell choices and no uncertainty-based abstention. Missing probability maps become a one-hot fallback; the raw provider response is not retained in dashboard events.
- A busy loop marks subsequent blocks as late/hold. That does not cancel a slow model request or guarantee the eventual order is based on fresh state.
- Errors are logged and the loop continues; existing resting orders are not comprehensively canceled by that catch block. Some background failures are ignored.
- Simulated fills, local accounting, and hard-coded inference-cost estimates are not realized trading returns or verified current pricing. Inference, RPC access, transactions, and losses can all carry costs.

## Review and maintenance

Reviewed **2026-09-19**, commit [`b587759e459ea049590102e54a0b07800864cdc3`](https://github.com/jarrodwatts/jev-trader/tree/b587759e459ea049590102e54a0b07800864cdc3).

Inspected README, MIT license, package manifests, example configuration, model questions, startup, execution restrictions, margin setup, API server, dashboard instructions, and the calldata-check script. Recorded the exact revision with `git rev-parse HEAD`.

Source inspection only: no dependencies installed, scripts executed, provider calls made, wallet accessed, or orders signed/submitted. No conventional test suite was identified; diagnostic scripts are not evidence of passing tests. No financial or performance claims were validated.

Related: [offline decision examples](../../../examples/README.md) for simpler synthetic workflows.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Guard LangChain agent tool calls with Jev and human approval](../../knowledge-base/articles/building-a-jev-agent-harness.md) — Mentioned in the source article. Study how code limits sit between a Jev judgment and an irreversible action.
- [Jev decision audits: validate the business case](../../knowledge-base/articles/jev-decision-audit.md) — Mentioned in the source article. Account for the cost of a wrong action.
<!-- knowledge:backlinks:end -->
