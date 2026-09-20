# jev-mcp

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

npm MCP server that exposes ten purpose-built TypeSafe Jev judgment tools (verify, screen, find, rerank, classify, decide, compare, extract, review, gate) instead of a single raw evaluate call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jkudish/jev-mcp) |
| Maintainer | [Joey Kudish / jkudish](https://github.com/jkudish). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **@jkudish/jev-mcp 0.5.0** (Node.js ≥ 20 MCP server via `npx -y @jkudish/jev-mcp`). |
| Requirements | Node.js 20+; a TypeSafe key (`TYPESAFE_API_KEY`) or configured OpenRouter / Cloudflare / Vercel AI Gateway provider via `JEV_PROVIDER`. |
| License | [MIT](https://github.com/jkudish/jev-mcp/blob/67dd9fa5a6e895909f1b2d80bf45534c29cff25a/LICENSE). |

## When to use

Use it when an agent should call named judgment tools (claim verification, content screening, candidate find/rerank, batch classify, bounded decide, compare, extract, diff review, ship gate) rather than inventing System One question shapes each time. Prefer [TypeSafe MCP](typesafe-mcp.md) for a thin general-purpose `evaluate` tool that returns raw provider answers. Prefer [Jev Sift](jev-sift.md) / [Jev Review](jev-review.md) when you want those narrower single-purpose servers.

## How it works

[`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/67dd9fa5a6e895909f1b2d80bf45534c29cff25a/src/provider.ts) talks to TypeSafe via `@typesafe-ai/sdk` `systemOne` by default (also OpenRouter Decisions, Cloudflare Workers AI, or Vercel AI Gateway). Tool handlers in the package build typed questions and return probabilities/confidence for the agent. Default model selection follows provider conventions (`jev-latest` on TypeSafe when configured).

## Get started

```sh
# register with your MCP client, e.g. Claude Code:
claude mcp add jev -- npx -y @jkudish/jev-mcp
# ensure TYPESAFE_API_KEY is in the server environment (do not paste keys into chat)
# or inspect the reviewed tree:
git clone https://github.com/jkudish/jev-mcp.git
cd jev-mcp
git checkout 67dd9fa5a6e895909f1b2d80bf45534c29cff25a
npm test   # offline unit/mock tests when dependencies are installed
```

Live tool calls send supplied evidence to the chosen provider and incur charges. This listing did not register an MCP client or call TypeSafe.

## Examples and demos

- README tool catalog and agent install paste.
- Offline tests under [`test/`](https://github.com/jkudish/jev-mcp/tree/67dd9fa5a6e895909f1b2d80bf45534c29cff25a/test) (`unit`, `mock`, optional `e2e`).
- Upstream CI workflow badge.

## Limits and data handling

All tool inputs (claims, page text, candidates, diffs, completion claims) leave the machine for the configured provider. The server does not own your merge/ship policy—callers must interpret probabilities and confidence. Early software; treat quality claims as unbenchmarked here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 67dd9fa](https://github.com/jkudish/jev-mcp/tree/67dd9fa5a6e895909f1b2d80bf45534c29cff25a): **0.5.0**, MIT. AI-assisted source review of README, `src/provider.ts`, `package.json`, and license. Offline `npm test` / live MCP or TypeSafe calls were not run on the review host.

Related: [TypeSafe MCP](typesafe-mcp.md), [Jev Sift](jev-sift.md), [Jev Review](jev-review.md).
