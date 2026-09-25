# Agent Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first CLI that filters eligible Cursor / Claude Code / Codex / OpenCode models by quota and policy, then uses TypeSafe System One (Jev) to classify the task and pick a route plus reasoning effort before launching the agent in a Herdr pane. Distinct from [Jev Model Router](jev-model-router.md), [jev-router](jev-router.md), [jev-codex-router](jev-codex-router.md), and [pi-jev-router](pi-jev-router.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nidhi-singh02/agent-router) |
| Maintainer | [nidhi-singh02](https://github.com/nidhi-singh02). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js monorepo CLI **@agent-router/router 0.1.0** (`router` binary); Herdr-integrated launcher. |
| Requirements | Node.js **≥ 20**; TypeSafe API key; at least one logged-in agent CLI (`agent` / `claude` / `codex` / `opencode`); Herdr for live launches (`HERDR_ENV=1`). |
| License | [MIT](https://github.com/nidhi-singh02/agent-router/blob/e1cc3c1bf11b52f845422ef38f9fa190f9fc16fb/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; offline unit tests run in the upstream checkout. Live TypeSafe routing and Herdr launches were not run. Pre-release software. |

## When to use

Use it when you run **several coding-agent subscriptions** and want quota-aware, policy-first selection of agent + model + effort for a task, with TypeSafe ranking only after deterministic eligibility. Prefer [jev-router](jev-router.md) / [jev-codex-router](jev-codex-router.md) for per-turn proxy routing inside one agent; prefer [pi-jev-router](pi-jev-router.md) inside pi.

## How it works

Deterministic rules drop disabled, depleted, or reserved models first. [`packages/router/src/semantic/decision-engine.ts`](https://github.com/nidhi-singh02/agent-router/blob/e1cc3c1bf11b52f845422ef38f9fa190f9fc16fb/packages/router/src/semantic/decision-engine.ts) then calls `systemOne` via [`typesafe-client.ts`](https://github.com/nidhi-singh02/agent-router/blob/e1cc3c1bf11b52f845422ef38f9fa190f9fc16fb/packages/router/src/semantic/typesafe-client.ts) (`@typesafe-ai/sdk`) to classify task family/phase/scores and Choice-rank an opaque candidate id, then select a supported reasoning effort. Local code rejects recognizable secrets in TypeSafe state before the call. Live `router run` without `--dry-run` starts the chosen agent only from a Herdr pane.

## Get started

```sh
git clone https://github.com/nidhi-singh02/agent-router.git
cd agent-router
git checkout e1cc3c1bf11b52f845422ef38f9fa190f9fc16fb
npm install
npm run build
npm test -- --run
# Optional dry-run after local config + TYPESAFE_API_KEY (billable):
# npm link -w @agent-router/router
# router run "summarize the approved plan" --dry-run
```

Follow the [upstream README](https://github.com/nidhi-singh02/agent-router/blob/e1cc3c1bf11b52f845422ef38f9fa190f9fc16fb/README.md) for `MODEL_ROUTER_HOME`, account config, and Herdr. Live routing sends task text to TypeSafe; this listing did not call TypeSafe or launch Herdr.

## Examples and demos

- Upstream [YouTube demo](https://youtu.be/7w8eRWnUUA8).
- Offline `npm test -- --run` on the review host (see Review).
- `router run … --dry-run` documents the selected opaque route without launching.

## Limits and data handling

Task text leaves the host on every live TypeSafe call; there is no non-TypeSafe routing fallback. Quota snapshots and session history stay local unless an integration is configured. Sticky same-phase reuse can skip re-ranking. Pre-release: review upstream security/privacy notes before shared accounts.

## Review and maintenance

Reviewed on **2026-09-20** at [commit e1cc3c1](https://github.com/nidhi-singh02/agent-router/tree/e1cc3c1bf11b52f845422ef38f9fa190f9fc16fb): **@agent-router/router 0.1.0**, MIT. AI-assisted source review of README, LICENSE, `packages/router/src/semantic/typesafe-client.ts`, `decision-engine.ts`, `task-classifier.ts`, and `effort-selector.ts`. Ran `npm install`, `npm run build`, and `npm test -- --run` in the upstream checkout: **42** test files, **270** tests passed. Live TypeSafe/Herdr paths not executed.

Related: [jev-router](jev-router.md), [Jev Model Router](jev-model-router.md), [jev-codex-router](jev-codex-router.md), [pi-jev-router](pi-jev-router.md), [Distill](distill.md).

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Guard LangChain agent tool calls with Jev and human approval](../../knowledge-base/articles/building-a-jev-agent-harness.md) — Independently suggested by JevList; not an endorsement by Sydney Runkle. Explore model selection after the tool gate works.
<!-- knowledge:backlinks:end -->
