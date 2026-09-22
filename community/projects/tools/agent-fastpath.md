# agent-fastpath

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP decision layer for coding agents: deterministic rules first, then TypeSafe Jev for typed ship gates, risk checks, file triage (files stay out of agent context), and a gated headless browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abhishekswe/agent-fastpath) |
| Maintainer | [abhishekswe](https://github.com/abhishekswe). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript monorepo publishing npm CLI **`agent-fastpath` 0.2.0** (MCP server + presets). |
| Requirements | Node.js ≥ 20.12; `TYPESAFE_API_KEY` for semantic Jev questions. Deterministic presets work without a key. |
| License | [MIT](https://github.com/abhishekswe/agent-fastpath/blob/bdabe148469e4f6c3c00b066964dd811418a0667/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline node:test suite inspected; live TypeSafe and public-web browser runs not executed on the review host. |

## When to use

Use it when a coding agent (Claude Code, Codex, Cursor, and other MCP clients) needs **calibrated accept/review/escalate** answers for ship readiness, command risk, ambiguity, file relevance, or page claims without dumping whole files into the model context. Prefer [askjev](askjev.md) or [jev-mcp](jev-mcp.md) for raw typed questions without the preset/rules/browser stack. Prefer [agent-chaperone](agent-chaperone.md) when the primary need is a tool-call firewall rather than triage and ship gates.

## How it works

Clear-cut cases are decided by local deterministic rules. Remaining questions go to [`TypeSafeJudgmentProvider`](https://github.com/abhishekswe/agent-fastpath/blob/bdabe148469e4f6c3c00b066964dd811418a0667/packages/provider-typesafe/src/client.ts), which posts to `https://api.typesafe.ai/v1/systemone` when `TYPESAFE_API_KEY` is set. MCP tools such as `fastpath_evaluate`, triage, and browser verification wrap presets (`ship_gate`, `risk`, `ambiguity`, and others) and return structured outcomes. A mock provider supports offline tests.

## Get started

```sh
git clone https://github.com/abhishekswe/agent-fastpath.git
cd agent-fastpath
git checkout bdabe148469e4f6c3c00b066964dd811418a0667
npm ci --ignore-scripts
npm test
# Live MCP: export TYPESAFE_API_KEY=... ; npx agent-fastpath start
```

Live TypeSafe calls and browser verification send content to TypeSafe (and optionally the public web) and may incur charges. This listing did not call live APIs.

## Examples and demos

- Offline on the review host: `npm test` → **52 passed** (unit, integration, and e2e with mock TypeSafe provider).
- Upstream docs cover client setup for Claude Code, Codex, Cursor, and other MCP hosts; a separate `npm run test:live` path requires a real key and was not run.

## Limits and data handling

Without `TYPESAFE_API_KEY`, semantic questions escalate rather than invent answers. Browser tooling includes SSRF protections and gates irreversible actions; it is not a full sandbox. Benchmark token-savings figures in upstream docs were not independently re-measured here.

## Review and maintenance

Reviewed on **2026-09-22** at [commit bdabe14](https://github.com/abhishekswe/agent-fastpath/tree/bdabe148469e4f6c3c00b066964dd811418a0667): **0.2.0**, MIT. AI-assisted source review of README, LICENSE, `packages/provider-typesafe/`, MCP server wiring. Offline `npm test` 52 passed. No live TypeSafe or network browser runs on the review host.

Related: [agent-chaperone](agent-chaperone.md), [askjev](askjev.md), [jev-mcp](jev-mcp.md), [TypeSafe MCP](typesafe-mcp.md).
