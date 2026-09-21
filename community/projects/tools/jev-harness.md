# jev-harness

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript decision harness around TypeSafe Jev: map typed answers to actions with a policy, confidence gate, optional shadow mode, reusable recipes, and an offline eval CLI (`jev-eval`). Not affiliated with TypeSafe. Distinct from [super-jev](super-jev.md) (evidence→action journals), [jev-layer](jev-layer.md) (capability routing with receipts), and [Responsible AI Harness](responsible-ai-harness.md) (safety assessment).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AntonioCoppe/jev-harness) |
| Maintainer | [AntonioCoppe](https://github.com/AntonioCoppe). Independently curated; this entry is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | npm package **jev-harness 0.1.0** (library + `jev-eval` CLI; Node.js ≥ 20). |
| Requirements | Node 20+; `npm install jev-harness`. Live runs need `TYPESAFE_API_KEY`. Depends on `@typesafe-ai/sdk`. |
| License | [MIT](https://github.com/AntonioCoppe/jev-harness/blob/2934d12e18157881440362d747d31b688a1c6ed6/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; `npm run build` passed. Upstream marketing timing claims were not re-measured. No live TypeSafe calls. |

## When to use

Use it when you already know the Jev questions and need production-shaped policy, confidence thresholds, shadow logging, and fixture evals around the answers. Prefer [daf-jev](daf-jev.md) for a broader Python toolkit; prefer [super-jev](super-jev.md) when you want permitted-tool execution journals.

## How it works

[`DecisionHarness`](https://github.com/AntonioCoppe/jev-harness/blob/2934d12e18157881440362d747d31b688a1c6ed6/src/harness.ts) uses `@typesafe-ai/sdk` `TypeSafeClient` to ask Choice/Score/Noul questions, then applies your `policy.decide` plus `minConfidence` / `onLowConfidence`. Recipes under `recipes/` package common patterns. The eval CLI replays fixtures and asserts on the resulting **action**, not free text.

## Get started

```sh
npm install jev-harness
export TYPESAFE_API_KEY=tsk_...
```

```sh
git clone https://github.com/AntonioCoppe/jev-harness.git
cd jev-harness
git checkout 2934d12e18157881440362d747d31b688a1c6ed6
npm ci --ignore-scripts
npm run build
# Live examples (charges): npm run example:alert
```

## Examples and demos

- README alert-gate example (disposition Choice + severity Score + needs_human Noul → notify/queue/suppress).
- `examples/alert-gate.ts`, `examples/model-router.ts`.
- Review host: **`npm run build`** succeeded (TypeScript compile). No separate unit-test script in package.json; live examples not run.

## Limits and data handling

State and question text go to TypeSafe when the harness runs live. Shadow mode logs intended actions without applying them only if you wire it that way—your integrator still owns side effects. Upstream wall-clock comparisons versus Claude CLI are author-reported; this listing did not reproduce them.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 2934d12](https://github.com/AntonioCoppe/jev-harness/tree/2934d12e18157881440362d747d31b688a1c6ed6): **0.1.0**, MIT. AI-assisted source review of README, `src/harness.ts`, `src/policy.ts`, `package.json`, and LICENSE. Offline: `npm run build` OK. No live TypeSafe calls.

Related: [super-jev](super-jev.md), [jev-layer](jev-layer.md), [daf-jev](daf-jev.md), [Responsible AI Harness](responsible-ai-harness.md).
