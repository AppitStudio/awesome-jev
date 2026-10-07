# Brave Jev MCP

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Fork of the Brave Search MCP Server whose `brave_llm_context` results are screened by TypeSafe Jev against the purpose of the search, removing pages and passages that match keywords without answering the question before they reach the AI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/romantcig/brave-jev-mcp) |
| Product homepage | [www.npmjs.com](https://www.npmjs.com/package/@romantcig/brave-jev-mcp) |
| Maintainer | [romantcig](https://github.com/romantcig). Independently curated. |
| Format | MCP server via `npx` (npm `@romantcig/brave-jev-mcp`, 0.1.2 at review) |
| Requirements | Node.js; a Brave Search API key (credit card required; upstream notes monthly free credits); `TYPESAFE_API_KEY` for filtering. |
| License | [MIT](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a coding or research agent web context with fewer off-topic snippets.
- Inspect which passages Jev filtered and why, with near-threshold compensation documented upstream.
- Mismatch: only `brave_llm_context` is filtered; without a Jev key it falls back to local cleanup only.

## How it works

Search results first pass local cleanup rules ([`src/filter/`](https://github.com/romantcig/brave-jev-mcp/tree/7ba1036bef34d0555741bc3655b380204c21136e/src/filter)), then [`src/filter/jev/client.ts`](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/src/filter/jev/client.ts) sends passages with the search intent to Jev using questions from [`questions.ts`](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/src/filter/jev/questions.ts); [`threshold.ts`](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/src/filter/jev/threshold.ts) and [`verdict.ts`](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/src/filter/jev/verdict.ts) decide what is kept. Mechanisms and filtering rules are documented in [`MECHANISMS.md`](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/MECHANISMS.md) and [`FILTERING.md`](https://github.com/romantcig/brave-jev-mcp/blob/7ba1036bef34d0555741bc3655b380204c21136e/FILTERING.md).

## Get started

Add to your MCP client (keys from the environment):

```sh
export BRAVE_API_KEY=...
export TYPESAFE_API_KEY=...
# MCP client config:
# { "mcpServers": { "brave-jev": { "command": "npx", "args": ["-y", "@romantcig/brave-jev-mcp"] } } }
```

Brave searches and Jev screening are billed to your own keys.

## Examples and demos

- README *Usage* example (comparing SQLite and PostgreSQL for a single-machine app) and *Default search budgets*.
- Replay fixtures for Jev decisions: [`fixtures/`](https://github.com/romantcig/brave-jev-mcp/tree/7ba1036bef34d0555741bc3655b380204c21136e/fixtures).

## Limits and data handling

Search queries and extracted page passages go to Brave and TypeSafe. Only `brave_llm_context` is filtered. Community fork, not affiliated with Brave. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 7ba1036bef34](https://github.com/romantcig/brave-jev-mcp/tree/7ba1036bef34d0555741bc3655b380204c21136e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
