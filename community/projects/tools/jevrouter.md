# JevRouter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Capability router for agents: models, subagents, skills, MCP tools, CLIs, and plugins share one candidate set; TypeSafe Jev (or OpenRouter Decisions) answers a typed Choice, while JevRouter enforces availability, permissions, risk, confirmation, and receipts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BillionsBobby/JevRouter) |
| Maintainer | [BillionsBobby](https://github.com/BillionsBobby) (direct submission via [issue #71](https://github.com/AppitStudio/awesome-jev/issues/71)). Independently curated; listing is not an endorsement. |
| Format | TypeScript package **jevrouter 0.1.0** with SDK, CLI, optional MCP adapter, and policy/receipts. |
| Requirements | Node.js **≥ 20**; `TYPESAFE_API_KEY` / `JEV_API_KEY` or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/BillionsBobby/JevRouter/blob/7378f1d06b113b86b71de5f839c9058d381874cb/LICENSE). TypeSafe/OpenRouter usage has separate costs. |
| Disclosure | AI-assisted catalog review. Maintainer self-submitted via issue #71. Listing is not an endorsement. Offline node:test suite passed; live agent routing and live Jev calls were **not** run. Distinct from [jev-router](jev-router.md) (Claude/Codex model proxy), [Agent Router](agent-router.md) (Herdr model/effort launcher), [jev-codex-router](jev-codex-router.md), and [jev-layer](jev-layer.md). |

## When to use

Use it when your host should ask Jev which capability handles the next step (or a multi-step plan) while code owns permission gates, confirmation for medium/high/critical actions, and append-only receipts. Prefer [jev-router](jev-router.md) for per-turn Claude/Codex model selection proxies, or [Agent Router](agent-router.md) for quota-aware Herdr launches.

## How it works

[`src/provider.ts`](https://github.com/BillionsBobby/JevRouter/blob/7378f1d06b113b86b71de5f839c9058d381874cb/src/provider.ts) posts typed questions to `https://api.typesafe.ai/v1/systemone` or OpenRouter Decisions. [`src/runtime.ts`](https://github.com/BillionsBobby/JevRouter/blob/7378f1d06b113b86b71de5f839c9058d381874cb/src/runtime.ts) selects the provider from env keys. Router fields live under `router`; filtered candidates are not re-normalized. Decision state and capability descriptions leave the host when Jev is called.

## Get started

```sh
export TYPESAFE_API_KEY=...   # or OPENROUTER_API_KEY
npm i jevrouter
# See upstream Quickstart / cookbook for route vs plan and agent setup
```

Pinned offline tests:

```sh
git clone https://github.com/BillionsBobby/JevRouter.git
cd JevRouter
git checkout 7378f1d06b113b86b71de5f839c9058d381874cb
npm ci --ignore-scripts
npm test
```

Live routing calls Jev and can incur charges; medium/high/critical capabilities require confirmation by design.

## Examples and demos

- Upstream website, architecture diagrams, cookbook, and benchmark notes.
- Offline `npm test` on the review host: **71 passed**. No live TypeSafe/OpenRouter or agent-host session.

## Limits and data handling

Candidate descriptions and routing state go to TypeSafe or OpenRouter. Keys via env or secure prompt—never print them. Upstream latency/benchmark figures are author claims, not revalidated here. Decision-only by default: the host still executes after confirmation.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 7378f1d](https://github.com/BillionsBobby/JevRouter/tree/7378f1d06b113b86b71de5f839c9058d381874cb): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/provider.ts`, `src/runtime.ts`, and tests. **`npm test`: 71 passed**. No live TypeSafe/OpenRouter or agent session. Closes the catalog gap for [issue #71](https://github.com/AppitStudio/awesome-jev/issues/71).

Related: [jev-router](jev-router.md), [Agent Router](agent-router.md), [jev-layer](jev-layer.md), [jev-codex-router](jev-codex-router.md).
