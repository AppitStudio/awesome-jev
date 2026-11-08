# OpenRouter MCP Multimodal (MCP server with a `decide` tool for TypeSafe Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MCP server with 21 tools across 300+ OpenRouter models (text, vision, audio, video); its `decide` tool sends structured decisions to OpenRouter's decisions API with TypeSafe Jev as the default System One model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stabgan/openrouter-mcp-multimodal) |
| Maintainer | [stabgan](https://github.com/stabgan). Independently curated. |
| Format | MCP server (TypeScript, npm/PyPI, Apache-2.0) |
| Requirements | Node.js or Python, an MCP client, and an OpenRouter key. |
| License | [Apache-2.0](https://github.com/stabgan/openrouter-mcp-multimodal/blob/dbc5ceb84cee8bc75a9a8e81ad43aeb2fb816a6e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/tool-handlers/decide.ts`](https://github.com/stabgan/openrouter-mcp-multimodal/blob/dbc5ceb84cee8bc75a9a8e81ad43aeb2fb816a6e/src/tool-handlers/decide.ts) at the pinned commit. |

## When to use

- Give an agent a typed decision tool next to multimodal tools.
- Compare Jev with other System One models through one MCP server.
- Mismatch: Jev is one tool among many.

## How it works

`src/tool-handlers/decide.ts` posts to `/api/alpha/decisions`; `src/tool-definitions.ts` defaults the decision model to `typesafe/jev-1.13` with noul/choice/score questions. Integration evidence: [`src/tool-handlers/decide.ts`](https://github.com/stabgan/openrouter-mcp-multimodal/blob/dbc5ceb84cee8bc75a9a8e81ad43aeb2fb816a6e/src/tool-handlers/decide.ts).

## Get started

Install the npm package, add it to your MCP client config with your OpenRouter key, and call `decide`.

```sh
git clone https://github.com/stabgan/openrouter-mcp-multimodal.git && cd openrouter-mcp-multimodal
export OPENROUTER_API_KEY=...
npx @stabgan/openrouter-mcp-multimodal
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/stabgan/openrouter-mcp-multimodal/blob/dbc5ceb84cee8bc75a9a8e81ad43aeb2fb816a6e/README.md](https://github.com/stabgan/openrouter-mcp-multimodal/blob/dbc5ceb84cee8bc75a9a8e81ad43aeb2fb816a6e/README.md)

## Limits and data handling

Decision state is sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit dbc5ceb84cee](https://github.com/stabgan/openrouter-mcp-multimodal/tree/dbc5ceb84cee8bc75a9a8e81ad43aeb2fb816a6e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
