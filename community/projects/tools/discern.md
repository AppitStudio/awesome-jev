# Discern

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Uncertainty-aware semantic control flow for [Effect](https://effect.website): type-safe patterns, policies, and routable procedures over Effect `Decision` / `DecisionModel`, including TypeSafe’s Jev provider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doeixd/discern) |
| Maintainer | [doeixd](https://github.com/doeixd) / Patrick Glenn. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript library published as npm **`@doeixd/discern` 0.4.0** (MIT); peer Effect / `@effect/ai-typesafe`. |
| Requirements | Node.js with ESM; Effect **4.0.0-rc.117** line and `@effect/ai-typesafe` for the TypeSafe Jev `DecisionModel`. Live calls need a TypeSafe API key via the Effect TypeSafe client layer. |
| License | [MIT](https://github.com/doeixd/discern/blob/41d7cde74362650d81b1014b4386314d49bc1c9b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm run check` inspected. Live TypeSafe calls were not run. |

## When to use

Use it when an Effect service should branch on semantic evidence (classify / probability / ordered rating) the way `Match` branches on exact facts, and you want policies and procedures that treat *maybe* as a first-class path. Prefer a thinner SDK client when you only need raw Noul/Choice/Score HTTP calls without Effect’s `DecisionModel` stack.

## How it works

Discern builds typed observations with Effect’s `Decision` vocabulary (`classify`, probability, ordered rating), then matches them with policies and optional procedure registries. With [`TypeSafeDecisionModel`](https://github.com/doeixd/discern/blob/41d7cde74362650d81b1014b4386314d49bc1c9b/src/model.ts) from `@effect/ai-typesafe`, those decisions can be answered by TypeSafe Jev (`jev-latest` in upstream examples). Application code still owns thresholds, routing, and side effects; Discern owns the typed match/procedure layer over the model’s answers.

## Get started

```sh
git clone https://github.com/doeixd/discern.git
cd discern
git checkout 41d7cde74362650d81b1014b4386314d49bc1c9b
npm ci --ignore-scripts
npm run check
```

Install for an Effect app with `npm install @doeixd/discern` and wire `TypeSafeClient` / `TypeSafeDecisionModel` as shown in the upstream README. Live inference sends structured state to TypeSafe and may incur charges.

## Examples and demos

- README stack example: change → classify impact → policy → procedures.
- [`examples/`](https://github.com/doeixd/discern/tree/41d7cde74362650d81b1014b4386314d49bc1c9b/examples) walkthrough and comparison scripts.
- Explainer assets under `docs/assets/` (optional; not required for offline checks).

## Limits and data handling

When the TypeSafe provider layer is active, decision inputs leave the host toward TypeSafe. Provider-neutral `DecisionModel` implementations can avoid that path. Effect v4 release-candidate peers may move; pin versions. Upstream GIF/video demos were not independently reproduced.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 41d7cde](https://github.com/doeixd/discern/tree/41d7cde74362650d81b1014b4386314d49bc1c9b): **0.4.0**, MIT. AI-assisted source review of README, `src/`, LICENSE, and package metadata. On the review host: **`npm run check`** (typecheck + type tests + **48** node:test cases) passed. No live TypeSafe calls.

Related: [decision-first](decision-first.md), [jev-toolkit](jev-toolkit.md), [patdown](patdown.md).
