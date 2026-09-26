# Jev Model Routing Lab

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript demonstration of typed, confidence-aware model routing: Jev returns tier/complexity/reasoning signals; application code applies escalation policy; Claude or Kimi generates the final reply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/goldytech/jev-model-routing) |
| Maintainer | [goldytech](https://github.com/goldytech). Independently curated. |
| Format | TypeScript demos (six interactive scenarios). |
| Requirements | Node.js; optional API keys for live Jev/Claude/Kimi—simulated fallbacks work without keys. |
| License | [MIT](https://github.com/goldytech/jev-model-routing/blob/1023d25d718be9906f7057b113626f5c92b21cda/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Teaching lab, not a production router. |

## When to use

Use to **learn the routing pattern** (typed Jev → deterministic policy → generative model).

## How it works

[`src/jev.ts`](https://github.com/goldytech/jev-model-routing/blob/1023d25d718be9906f7057b113626f5c92b21cda/src/jev.ts) and [`src/router.ts`](https://github.com/goldytech/jev-model-routing/blob/1023d25d718be9906f7057b113626f5c92b21cda/src/router.ts) ask tier/complexity/reasoning questions; confidence below 0.60 escalates one tier.

## Get started

```sh
git clone https://github.com/goldytech/jev-model-routing.git
cd jev-model-routing
git checkout 1023d25d718be9906f7057b113626f5c92b21cda
# npm install && follow upstream README (simulated mode works without keys)
```

## Examples and demos

- Six demos: routing, support triage, inbox, feed filter, title scoring, cost comparison.

## Limits and data handling

Live prompts go to configured providers. Lab code is illustrative; do not treat demo savings as measured production results.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 1023d25](https://github.com/goldytech/jev-model-routing/tree/1023d25d718be9906f7057b113626f5c92b21cda). AI-assisted README and LICENSE inspection of router modules; install/live paths not executed.
