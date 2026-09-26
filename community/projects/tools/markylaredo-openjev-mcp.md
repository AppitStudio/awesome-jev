# openjev-mcp (markylaredo)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP wrapper for the public OpenJEV API—typed judgments, not prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/markylaredo/openjev-mcp) |
| Maintainer | [markylaredo](https://github.com/markylaredo). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node 20+ stdio MCP server with four tools. |
| Requirements | Node.js 20+; `OPENJEV_API_KEY` from openjev.sh (not TypeSafe console). |
| License | [MIT](https://github.com/markylaredo/openjev-mcp/blob/807317732aedef5d8409e44267e87788bbc8672a/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when an MCP client should call OpenJEV without putting the API key in the model context.

## How it works

Server holds the key and posts to `api.openjev.sh/v1/systemone`; clients get choice/score/noul answers. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/markylaredo/openjev-mcp.git
cd openjev-mcp
git checkout 807317732aedef5d8409e44267e87788bbc8672a
npm install && npm run build
# configure MCP client with OPENJEV_API_KEY
```

Pin revision `807317732aedef5d8409e44267e87788bbc8672a` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Uses OpenJEV, not direct TypeSafe console keys. Live MCP/OpenJEV path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 8073177](https://github.com/markylaredo/openjev-mcp/tree/807317732aedef5d8409e44267e87788bbc8672a). AI-assisted README and LICENSE inspection; install/live paths not executed.
