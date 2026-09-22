# DecideKit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Provider-neutral runtime for typed, confidence-aware decisions: define policies in YAML or TypeScript, evaluate with Jev through OpenRouter or TypeSafe, and branch on explicit fallbacks when confidence is low.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sameerkhan24/decidekit) |
| Maintainer | [sameerkhan24](https://github.com/sameerkhan24). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript package **`decidekit` 0.1.0** (CLI + library) with a matching Python package under `python/`. |
| Requirements | Node.js ≥ 20 (or Python 3 for the Python package); `OPENROUTER_API_KEY` or `TYPESAFE_API_KEY` for live runs. Offline fixture provider needs no key. |
| License | [MIT](https://github.com/sameerkhan24/decidekit/blob/26300c5c555b0b93c2f1bab069ecb2484be22261/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline vitest/pytest and fixture CLI inspected; live OpenRouter/TypeSafe calls not run on the review host. |

## When to use

Use it when you want **policy-as-code** for routing, scoring, gating, or classification with calibrated probabilities and named fallbacks. Prefer [SemDecide](semdecide.md) for Unix exit-code predicates, or [daf-jev](daf-jev.md) for a Python-first question toolkit. DecideKit is not an agent framework and does not generate prose.

## How it works

Policies declare typed questions over application state. `OpenRouterProvider` targets OpenRouter’s Decisions API (default model `typesafe/jev-1.13`); `TypeSafeProvider` calls `https://api.typesafe.ai/v1/systemone`. A `fixture` provider replays recorded answers for offline tests. Application code owns branching on value, confidence, and fallbacks.

## Get started

```sh
git clone https://github.com/sameerkhan24/decidekit.git
cd decidekit
git checkout 26300c5c555b0b93c2f1bab069ecb2484be22261
npm ci
npm test
npm run build
node dist/cli.js run examples/pull-request.yml \
  --all \
  --state @examples/pull-request-state.json \
  --provider fixture \
  --fixture examples/pull-request-fixture.json
```

Live OpenRouter/TypeSafe runs send policy state to the provider and may incur charges. This listing did not call live APIs.

## Examples and demos

- Offline on the review host: `npm test` → **9 passed**; Python `pytest` → **4 passed**; fixture CLI run succeeded.
- Upstream `examples/` includes pull-request, support-routing, agent-action, and webhook policies with matching fixtures.

## Limits and data handling

Live evaluation sends decision state to OpenRouter or TypeSafe. Cost estimates in traces use configured token prices and are not billing statements. Provider APIs (especially OpenRouter Decisions) may change while marked alpha.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 26300c5](https://github.com/sameerkhan24/decidekit/tree/26300c5c555b0b93c2f1bab069ecb2484be22261): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/providers/`, examples. Offline vitest 9 passed, Python pytest 4 passed, fixture CLI OK. No live provider calls on the review host.

Related: [SemDecide](semdecide.md), [daf-jev](daf-jev.md), [wellposed](wellposed.md).
