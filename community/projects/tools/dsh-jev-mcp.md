# dsh-jev-mcp (Jev decision tools for DeepSeek Harness: dependency-free client and stdio MCP server)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Dependency-free JavaScript client and stdio MCP server that give DeepSeek Harness (or any MCP client) four Jev decision tools: `jev_check`, `jev_route`, `jev_score` and `jev_evaluate`, with credential redaction and probability thresholds. Demos cover realistic coding-agent judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bojansandhaus/dsh-jev-mcp) |
| Maintainer | [bojansandhaus](https://github.com/bojansandhaus). Independently curated. |
| Format | Node.js library + stdio MCP server |
| Requirements | Node.js; a TypeSafe key. |
| License | [MIT](https://github.com/bojansandhaus/dsh-jev-mcp/blob/a151343dfb9c142f7dad3f4b6d9d099e071f01ca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.mjs`](https://github.com/bojansandhaus/dsh-jev-mcp/blob/a151343dfb9c142f7dad3f4b6d9d099e071f01ca/lib/jev.mjs) at the pinned commit. |

## When to use

- Let a coding agent ask Jev for yes/no, routing and score judgments over MCP.
- Mismatch: thin wrapper; judgment quality depends on how you phrase questions.

## How it works

`lib/jev.mjs` calls `api.typesafe.ai` with typed questions and applies thresholds; `server/jev-mcp.mjs` exposes the same four operations as MCP tools, and `examples/demo.mjs` runs four sample judgments. Integration evidence: [`lib/jev.mjs`](https://github.com/bojansandhaus/dsh-jev-mcp/blob/a151343dfb9c142f7dad3f4b6d9d099e071f01ca/lib/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bojansandhaus/dsh-jev-mcp && cd dsh-jev-mcp
TYPESAFE_API_KEY=... node examples/demo.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bojansandhaus/dsh-jev-mcp#readme](https://github.com/bojansandhaus/dsh-jev-mcp#readme)

## Limits and data handling

Agent state passed to the tools is sent to TypeSafe after credential redaction. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit a151343dfb9c](https://github.com/bojansandhaus/dsh-jev-mcp/tree/a151343dfb9c142f7dad3f4b6d9d099e071f01ca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
