# JCR

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev Capability Resolver: one agent tool that searches a nested capability tree with TypeSafe Jev and returns deterministic command documentation (stdio MCP, Claude/Codex harnesses, and a 50-scenario benchmark suite). Does not execute target-service commands.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NiazMorshed2007/jcr) |
| Maintainer | [NiazMorshed2007](https://github.com/NiazMorshed2007). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript resolver + MCP + comparison harnesses **1.0.0** (private root package; run from checkout). |
| Requirements | Node.js 22+; `TYPESAFE_API_KEY` for resolve/agent JCR modes; optional `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` for compound decomposition and harnesses. |
| License | [MIT](https://github.com/NiazMorshed2007/jcr/blob/138b3832eabaf899dbb8366520a676682bbdf2e5/LICENSE). TypeSafe and other provider usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; offline `npm test` and capability audit run. Live resolve/agent runs with API keys were not executed. |

## When to use

Use it when an agent would otherwise load several skill files to find a few deterministic commands and you want Jev-backed lookup that keeps search out of the main context. Prefer [SkillRanker](skillranker.md) or [jev-skill-gate](jev-skill-gate.md) when the goal is ranking or gating `SKILL.md` trees rather than a capability catalog. Same author as cataloged [Jev Review](jev-review.md); this is a distinct product.

## How it works

The resolver walks a nested capability tree and uses [`src/jcr/jev.ts`](https://github.com/NiazMorshed2007/jcr/blob/138b3832eabaf899dbb8366520a676682bbdf2e5/src/jcr/jev.ts) (`@typesafe-ai/sdk` `systemOne`) to select operations and return attached documentation. Compound requests may call an OpenAI decomposer. Included Claude and Codex harnesses compare skills mode vs JCR mode; benchmarks report context/cost/tool metrics. JCR returns documentation only.

## Get started

```sh
git clone https://github.com/NiazMorshed2007/jcr.git
cd jcr
git checkout 138b3832eabaf899dbb8366520a676682bbdf2e5
npm ci
npm test
npm run capabilities:audit
# Live resolve (charges): copy .env.example → .env, then
# npm run jcr:resolve -- --agent-output "Create a Stripe customer"
```

This listing did not set API keys or run live resolve/agent comparisons.

## Examples and demos

- Product write-up/demo: [jcr.niazmorshed.dev](https://jcr.niazmorshed.dev).
- Offline capability audit and unit tests on the review host (see Review).
- Upstream `compare` / harness scripts require provider keys (not run here).

## Limits and data handling

Agent prompts and capability context leave the host on live TypeSafe/OpenAI/Anthropic calls. The checkout is the supported run path (package not published to npm). Catalog shape and skill mappings can change; re-run `capabilities:audit` after updates.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 138b383](https://github.com/NiazMorshed2007/jcr/tree/138b3832eabaf899dbb8366520a676682bbdf2e5): **1.0.0**, MIT. AI-assisted source review of README, LICENSE, and `src/jcr/jev.ts`. Ran `npm ci`, `npm test` (**50 passed**), and `npm run capabilities:audit` (**passed**; 960 nodes / 11,360 items reported). Live Jev resolve not executed.

Related: [Jev Review](jev-review.md), [SkillRanker](skillranker.md), [jev-skill-gate](jev-skill-gate.md), [jev-layer](jev-layer.md).
