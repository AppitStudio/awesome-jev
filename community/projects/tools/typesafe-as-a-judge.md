# TypeSafe-as-a-Judge

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Codex and Claude Code MCP plugin that gives coding agents a bounded TypeSafe Jev judgment layer (route, rank, extract, verify, judge, escalation gate) while the agent keeps orchestration, permissions, and side effects.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/E-FL/typesafe-as-a-judge) |
| Maintainer | [E-FL](https://github.com/E-FL) / Arik Aizikovich. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js **≥ 20** MCP server (`server/*.mjs`) + bundled skills; package version **0.1.0** (private npm package layout). |
| Requirements | `TYPESAFE_API_KEY` for live System One calls to `https://api.typesafe.ai/v1/systemone`. Codex/Claude Code plugin install per upstream README. |
| License | [Apache-2.0](https://github.com/E-FL/typesafe-as-a-judge/blob/d7a70549fcc539aabbe8645dd0e2ba44e0deffd0/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation with TypeSafe AI, OpenAI, or Anthropic. Listing is not an endorsement. Offline: `npm test` → **9 passed**. No live TypeSafe calls. Distinct from [jev-mcp](jev-mcp.md), [Jev MCP (Freepik)](freepik-jev-mcp.md), and [TypeSafe MCP](typesafe-mcp.md). |

## When to use

Use it when Codex or Claude Code should ask Jev for narrow route/rank/verify signals under an explicit proceed/review policy. Prefer [jev-mcp](jev-mcp.md) or [TypeSafe MCP](typesafe-mcp.md) for general-purpose MCP tool packs outside those two hosts.

## How it works

[`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/d7a70549fcc539aabbe8645dd0e2ba44e0deffd0/server/judge.mjs) posts to `https://api.typesafe.ai/v1/systemone`. Tools (`typesafe_route`, `typesafe_rank`, `typesafe_extract`, `typesafe_verify`, `typesafe_judge`, session/usage helpers, `typesafe_escalation_gate`) are documented as read-only: they do not edit files or invoke other models. Bundled skills tell the agent when to call which tool and to escalate on low confidence. Upstream states it is an unofficial community integration.

## Get started

```sh
git clone https://github.com/E-FL/typesafe-as-a-judge.git
cd typesafe-as-a-judge
git checkout d7a70549fcc539aabbe8645dd0e2ba44e0deffd0
npm test
# Follow upstream README / scripts/setup.sh to register the Codex or Claude plugin
```

Live MCP tool calls need `TYPESAFE_API_KEY` and can incur charges. Tests refuse live calls without a key.

## Examples and demos

- README tool table and autonomous use-case map.
- Offline tests in `tests/*.test.mjs` (executed for this listing).

## Limits and data handling

Tool arguments (state, candidates, claims) leave the host for TypeSafe on live calls. Recommendations are not permissions for consequential actions. Upstream “substitute model” savings are labeled theoretical in the usage summary.

## Review and maintenance

Reviewed on **2026-09-21** at [commit d7a7054](https://github.com/E-FL/typesafe-as-a-judge/tree/d7a70549fcc539aabbe8645dd0e2ba44e0deffd0): **0.1.0**, Apache-2.0. AI-assisted source review of README, `server/judge.mjs`, skills, and offline `npm test`. No live provider calls.

Related: [jev-mcp](jev-mcp.md), [TypeSafe MCP](typesafe-mcp.md), [askjev](askjev.md).
