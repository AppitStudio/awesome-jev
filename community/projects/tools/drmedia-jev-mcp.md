# jev-mcp (drmedia)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

General-purpose MCP server for System One decision models: MCP clients ask typed yes/no, choice and score questions about structured state and get calibrated probabilities from TypeSafe Jev, OpenRouter (Jev, Cloudflare Clef) or a local server, with batching, retries, image input notes, stdio/HTTP transports and Docker. Distinct from the separately listed jev-mcp.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/drmedia/jev-mcp) |
| Maintainer | [drmedia](https://github.com/drmedia). Independently curated. |
| Format | Node MCP server (stdio or streamable HTTP), Docker image build |
| Requirements | Node.js 20.12+ and a TypeSafe or OpenRouter API key (or a local decision server). |
| License | [MIT](https://github.com/drmedia/jev-mcp/blob/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let Claude Code or another MCP client call Jev for classification and gating.
- Switch providers per request when several are configured (`JEV_PROVIDERS`).
- Mismatch: build from source; see also the other [jev-mcp](jev-mcp.md) listing (different project).

## How it works

[`src/core/jev-core.ts`](https://github.com/drmedia/jev-mcp/blob/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d/src/core/jev-core.ts) validates questions and dispatches to providers such as [`typesafe-provider.ts`](https://github.com/drmedia/jev-mcp/blob/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d/src/providers/typesafe/typesafe-provider.ts) and the OpenRouter provider; tools `jev.evaluate`, `jev.evaluate_batch`, `jev.choice`, `jev.score` and `jev.noul` are documented in the README. API contracts are recorded in [`docs/typesafe-api-notes.md`](https://github.com/drmedia/jev-mcp/blob/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d/docs/typesafe-api-notes.md).

## Get started

Build and register with Claude Code (README *Setup* and *Use with Claude Code*):

```sh
git clone https://github.com/drmedia/jev-mcp && cd jev-mcp
npm install && cp .env.example .env   # set TYPESAFE_API_KEY
npm run build
claude mcp add jev -- node /absolute/path/to/jev-mcp/dist/transport/stdio.js
```

Each tool call sends Jev requests billed by TypeSafe or OpenRouter.

## Examples and demos

- [Usage guide](https://github.com/drmedia/jev-mcp/blob/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d/docs/usage.md) and [client setup](https://github.com/drmedia/jev-mcp/blob/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d/docs/clients.md).
- README *Tools* section.

## Limits and data handling

State and questions the client sends go to the configured provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 2897e8fe34fc](https://github.com/drmedia/jev-mcp/tree/2897e8fe34fc93906b3863a442edf8ccd1d0ef3d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
