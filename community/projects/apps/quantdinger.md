# QuantDinger

[All projects](../README.md) · [Web apps](README.md#web-apps)

Open-source AI trading OS (research → Python strategies → backtest → paper/live execution → monitoring) with an optional TypeSafe Jev pre-trade decision gate on live entry orders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/OpenByteInc/QuantDinger) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://www.quantdinger.com) — also [hosted app](https://ai.quantdinger.com). |
| Pricing and access | Apache-2.0 self-host via Docker Compose has no app purchase fee. Hosted SaaS at `ai.quantdinger.com` may have separate account/billing terms (hosted pricing not verified here). Live Jev filtering needs a TypeSafe key (`JEV_API_KEY` and related settings). Exchange, LLM, and infrastructure costs are separate. Checked **2026-09-20**. |
| Jev evidence | [`backend_api_python/app/services/ai_decision_filter.py`](https://github.com/OpenByteInc/QuantDinger/blob/12c04eb2cdb8a9d08dc84502f5261ec3f1c56bf7/backend_api_python/app/services/ai_decision_filter.py) posts typed Choice questions to TypeSafe System One (`JEV_BASE_URL` default `https://api.typesafe.ai/v1` + `/systemone`, model `jev-latest`) for pre-trade entry checks; code-owned policy maps answers to allow/block with fail-open on provider failure. |
| Disclosure | Independently curated listing; not an upstream submission or endorsement. AI-assisted source review of README and the decision-filter module. Live trading, hosted signup, and live TypeSafe calls were not run. Brand/commercial licensing for QuantDinger identity is separate from the Apache-2.0 backend license per upstream. Inclusion is not investment advice. |
| Maintainer | [Open Byte Inc / OpenByteInc](https://github.com/OpenByteInc). Contributor affiliation/commercial relationships were not supplied. |
| Format | Self-hosted Docker Compose stack (Python 3.12 API/workers, web UI) plus optional multi-tenant SaaS path documented upstream. |
| Platform and availability | Source-built local/production Docker; hosted product at [ai.quantdinger.com](https://ai.quantdinger.com). Release stage: actively maintained public repo (11k+ stars at review). |
| Jev's role | Optional **AI Decision Filter** on regular live strategy / Quick Trade *entry* orders: six Choice checks (evidence quality, signal alignment, regime, account risk, execution quality, final pass/reject). Exits and emergency actions bypass AI. Grid/DCA/martingale runtimes excluded in this version. Without Jev, upstream may fall back to a configured LLM or fail-open allow with audit log. |
| Requirements | Docker Compose v2 for self-host; `JEV_API_KEY` (and optional `JEV_MODEL` / timeout / confidence) in System Settings → AI / LLM for the Jev path; exchange credentials for real trading. |
| License | [Apache-2.0](https://github.com/OpenByteInc/QuantDinger/blob/12c04eb2cdb8a9d08dc84502f5261ec3f1c56bf7/LICENSE) for backend source; upstream notes brand/commercial terms separately. |

## When to use

Use it when you want a full self-hosted trading research and execution stack and an inspectable typed pre-trade gate. Prefer [Jev Trader](../tools/jev-trader.md) for a small Bun experiment studying direction choices, or [SmartMoney-Cub](../tools/smartmoney-cub.md) for a read-only journal/review harness without order routing.

## How it works

When the filter is enabled, entry intents gather market/strategy/portfolio/budget state and call TypeSafe System One with the fixed `JEV_QUESTIONS` map. Application code interprets Choice outcomes and confidence (`JEV_MIN_CONFIDENCE` default 0.65), records an auditable timeline, and either allows the entry or blocks it. Provider failure fails open so AI outages cannot trap open positions; exits bypass the filter.

## Get started

```sh
git clone https://github.com/OpenByteInc/QuantDinger.git
cd QuantDinger
git checkout 12c04eb2cdb8a9d08dc84502f5261ec3f1c56bf7
# follow upstream Docker Compose quick start in README
# configure JEV_API_KEY in System Settings → AI / LLM for the decision filter
```

Do not run live trading from this listing's review host. Enabling the filter sends order and portfolio evidence to TypeSafe when Jev is configured.

## Examples and demos

- README section **JEV-powered pre-trade decisions** (flow diagram and settings).
- [docs/agent](https://github.com/OpenByteInc/QuantDinger/tree/12c04eb2cdb8a9d08dc84502f5261ec3f1c56bf7/docs/agent) for Agent Gateway / MCP notes.
- Upstream website/video links (vendor demos; not re-run here).

## Limits and data handling

Pre-trade evidence leaves your deployment for TypeSafe when Jev is enabled. Fail-open behavior prioritizes position management over blocking on outages—confirm that matches your risk posture. This catalog does not validate strategy profitability, exchange integrations, or hosted billing. Trading involves financial risk.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 12c04eb](https://github.com/OpenByteInc/QuantDinger/tree/12c04eb2cdb8a9d08dc84502f5261ec3f1c56bf7): Apache-2.0. AI-assisted review of README Jev section and `ai_decision_filter.py`. Docker bring-up, live exchanges, hosted SaaS, and live TypeSafe calls were not exercised.

Related: [Jev Trader](../tools/jev-trader.md), [SmartMoney-Cub](../tools/smartmoney-cub.md).
