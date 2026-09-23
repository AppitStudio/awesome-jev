# jev-guard (CMaintz)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Framework-agnostic TypeScript guardrail that vets proposed agent tool calls with TypeSafe Jev (score/noul dimensions → allow/block/hold), plus LangChain and Vercel AI SDK adapters. Distinct from [jev-guard](jev-guard.md) (leepokai multi-agent hooks) and [JevGuard](jevguard.md) (CLAUDE.md/AGENTS.md rule enforcement).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CMaintz/jev-guard) |
| Maintainer | [CMaintz](https://github.com/CMaintz) (Christoffer Maintz). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript library **`jev-guard` 0.1.0** (ESM): `guard` / `enforce` / `wrapTool` + `jev-guard/langchain` and `jev-guard/vercel` subpaths; policy presets. |
| Requirements | Node compatible with the package build; TypeSafe (or compatible) Jev API key via `TypeSafeProvider`. |
| License | [MIT](https://github.com/CMaintz/jev-guard/blob/62138129abd8b603fc2e405e715d1805289e1aab/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `src/guard.ts`, adapters, policy). Offline Foundry gate and live Jev were **not** run on the review host. Upstream accuracy/latency figures are author-reported. |

## When to use

Use it when you want a **portable** allow/block/hold policy around tool `execute` (or LangChain `wrapToolCall`) with confidence-gated escalation. Prefer [leepokai/jev-guard](jev-guard.md) for ready multi-agent PreToolUse hooks; prefer [agent-chaperone](agent-chaperone.md) for MCP proxy + hooks firewalling. Upstream is explicit: not a security boundary alone—keep sandboxing and least privilege.

## How it works

[`guard()`](https://github.com/CMaintz/jev-guard/blob/62138129abd8b603fc2e405e715d1805289e1aab/src/guard.ts) builds state/questions from the proposed tool call, asks the provider once, and [`decide`](https://github.com/CMaintz/jev-guard/blob/62138129abd8b603fc2e405e715d1805289e1aab/src/core/decide.ts) maps typed answers through your policy (`escalateBelow`, `perTool` shortcuts). Adapters throw `GuardBlockedError` before execution; presets (`shellPolicy`, `sqlPolicy`, …) seed common dangerous classes. Audit sink is recommended because Jev returns no natural-language rationale.

## Get started

```sh
git clone https://github.com/CMaintz/jev-guard.git
cd jev-guard
git checkout 62138129abd8b603fc2e405e715d1805289e1aab
npm ci
npm run build
# Live (charges): configure JEV_API_KEY / TypeSafeProvider per README examples
```

## Examples and demos

- README snippets for LangChain middleware and Vercel `guardVercelTool`.
- Upstream `examples/smoke.mjs` and Foundry `mise run gate` (not run here).

## Limits and data handling

Tool names/arguments and task context go to TypeSafe when not short-circuited. Fail-safe holds on low confidence. Probabilistic model—prompt injection can slip through. This listing did not call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 6213812](https://github.com/CMaintz/jev-guard/tree/62138129abd8b603fc2e405e715d1805289e1aab) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, `src/guard.ts` and adapters. No live TypeSafe spend.

Related: [jev-guard](jev-guard.md), [JevGuard](jevguard.md), [agent-chaperone](agent-chaperone.md).
