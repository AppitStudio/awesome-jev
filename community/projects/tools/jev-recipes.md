# jev-recipes

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

66 composable TypeScript recipes (npm `jev-recipes`) for TypeSafe Jev decisions—rerank, verify, clarify, route, and related agent/retrieval/conversation judgments—via `@typesafe-ai/sdk`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agencyenterprise/jev-recipes) |
| Maintainer | [Agency Enterprise](https://github.com/agencyenterprise). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript library + CLI (`jev-recipes`); Node.js **≥22.9**; npm package **0.2.0**. |
| Requirements | `TYPESAFE_API_KEY` for live recipe calls; optional `client`/`model`/`signal` overrides. |
| License | [MIT](https://github.com/agencyenterprise/jev-recipes/blob/e63b53e5c6d478c1ec8ef08ab12332ef21fb6505/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline vitest on the review host; live TypeSafe demos not run. |

## When to use

Use it when you want **small, typed Jev decision helpers** (schemas + examples) rather than wiring System One by hand. Prefer [daf-jev](daf-jev.md) for a Python toolkit, or [jev-harness](jev-harness.md) for confidence gates and shadow mode around custom questions.

## How it works

[`src/client.ts`](https://github.com/agencyenterprise/jev-recipes/blob/e63b53e5c6d478c1ec8ef08ab12332ef21fb6505/src/client.ts) wraps `TypeSafeClient.systemOne`. Individual recipes under `recipes/` call `@typesafe-ai/sdk` helpers (`noul`, `choice`, …) with Zod-validated inputs and return structured `ready` / error statuses for application code to act on.

## Get started

```sh
git clone https://github.com/agencyenterprise/jev-recipes.git
cd jev-recipes
git checkout e63b53e5c6d478c1ec8ef08ab12332ef21fb6505
npm ci
npm test
# Live (charges apply): export TYPESAFE_API_KEY=... && npm run demo
```

Or `npm install jev-recipes` and import e.g. `jev-recipes/rerank`. Keep the API key on the server.

## Examples and demos

- Offline on the review host: `npm test` → **1571 passed** (66 files).
- Recipe catalog: [recipes/README.md](https://github.com/agencyenterprise/jev-recipes/blob/e63b53e5c6d478c1ec8ef08ab12332ef21fb6505/recipes/README.md).

## Limits and data handling

Live calls send supplied inputs to TypeSafe and consume quota. Recipes do not execute side effects—your app owns handlers. CLI demos may require a key.

## Review and maintenance

Reviewed on **2026-09-22** at [commit e63b53e](https://github.com/agencyenterprise/jev-recipes/tree/e63b53e5c6d478c1ec8ef08ab12332ef21fb6505): MIT **0.2.0**. AI-assisted source review of README, LICENSE, `src/client.ts`, and package exports. Offline vitest **1571 passed**. No live TypeSafe spend.

Related: [daf-jev](daf-jev.md), [jev-harness](jev-harness.md), [jev-mcp](jev-mcp.md).
