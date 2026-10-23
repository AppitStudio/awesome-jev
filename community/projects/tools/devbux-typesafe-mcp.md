# typesafe-mcp by devbux (Jev as MCP tools via npx)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Stdio MCP server published to npm that exposes Jev's choice, score, noul and box questions as typed tools, including image inputs, so any MCP client can ask Jev for calibrated decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/devbux/typesafe-mcp) |
| Maintainer | [devbux](https://github.com/devbux). Independently curated. |
| Format | MCP server (npm: @devbux/typesafe-mcp) |
| Requirements | Node.js 18+ or Bun; a TypeSafe API key. |
| License | [MIT](https://github.com/devbux/typesafe-mcp/blob/8516e685b732ee6eb3dce60a9d30f5e406c03ede/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/devbux/typesafe-mcp/blob/8516e685b732ee6eb3dce60a9d30f5e406c03ede/src/jev/client.ts) at the pinned commit. |

## When to use

- Give an MCP-capable agent a cheap typed decision step.
- Ask Jev about images from an agent.
- Mismatch: one of several Jev MCP servers in this catalog; pick by runtime and features.

## How it works

`src/jev/client.ts` posts to `/v1/systemone` on `https://api.typesafe.ai` (configurable with `TYPESAFE_BASE_URL`; model `jev-latest` unless `TYPESAFE_JEV_MODEL` is set). Integration evidence: [`src/jev/client.ts`](https://github.com/devbux/typesafe-mcp/blob/8516e685b732ee6eb3dce60a9d30f5e406c03ede/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx -y @devbux/typesafe-mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Client config example: [github.com/devbux/typesafe-mcp/blob/main/examples/mcp-config.json](https://github.com/devbux/typesafe-mcp/blob/main/examples/mcp-config.json)

## Limits and data handling

Tool inputs, including images, are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 8516e685b732](https://github.com/devbux/typesafe-mcp/tree/8516e685b732ee6eb3dce60a9d30f5e406c03ede). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
