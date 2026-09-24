# ask-jev (Aether-254)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MCP server and Codex/Claude plugin wrapping TypeSafe Jev System One: `jev_evaluate`, `jev_batch_evaluate`, and `jev_ping` with Choice/Score/Noul primitives.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Aether-254/ask-jev) |
| Maintainer | [Aether-254](https://github.com/Aether-254). Independently curated. |
| Format | TypeScript MCP (`mcp/dist/index.js`) + Codex/Claude plugin packaging. |
| Requirements | Node.js 20+; `TYPESAFE_API_KEY` (or `JEV_API_KEY`); defaults to `https://api.typesafe.ai/v1` / `jev-latest`. |
| License | [MIT](https://github.com/Aether-254/ask-jev/blob/3435f3f68682bdfcdd9a262ba89652609ffee4d0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live MCP clients and TypeSafe calls not run. Distinct from [ask-jev-skill](ask-jev-skill.md) and [askjev](askjev.md). |

## When to use

Use when Codex/Claude should call **typed Jev evaluate/batch tools** over stdio MCP with a committed dist bundle. Prefer [ask-jev-skill](ask-jev-skill.md) for a Hermes-only skill path.

## How it works

The stdio MCP server posts System One requests with retries/timeouts configurable via env; `jev_ping` checks endpoint/credentials/latency (per README). Project-local `.mcp.json` points at the committed bundle.

## Get started

```sh
git clone https://github.com/Aether-254/ask-jev.git
cd ask-jev
git checkout 3435f3f68682bdfcdd9a262ba89652609ffee4d0
export TYPESAFE_API_KEY="<your-key>"
# Point your MCP client at mcp/dist/index.js (see .mcp.json)
```

## Examples and demos

- README env table and `npm test` / `npm run test:smoke` in `mcp/`.
- Optional `JEV_LIVE=1` live integration test (not run here).

## Limits and data handling

States and criteria you supply reach TypeSafe. Protocol traffic stays on stdout; diagnostics on stderr.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 3435f3f](https://github.com/Aether-254/ask-jev/tree/3435f3f68682bdfcdd9a262ba89652609ffee4d0). AI-assisted README and LICENSE inspection; CI badge noted; live ping not run.

Related: [askjev](askjev.md), [ask-jev-skill](ask-jev-skill.md).
