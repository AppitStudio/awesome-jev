# jev-mcp (Afloat16)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial conservative MCP server for TypeSafe AI Jev (stdio) so agents can ask typed System One questions

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Afloat16/jev-mcp) |
| Maintainer | [Afloat16](https://github.com/Afloat16). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Unofficial Node MCP server (stdio). |
| Requirements | Node.js 20+; TypeSafe API key. |
| License | [MIT](https://github.com/Afloat16/jev-mcp/blob/4362f2f69252af4749cc7a4e922e931388e2c51c/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [pyck-ai/jev-mcp](pyck-ai-jev-mcp.md), [legostin/jev-mcp](legostin-jev-mcp.md), and [keysersoft/jev-mcp-server](keysersoft-jev-mcp-server.md). |

## When to use

Use when an MCP client needs a cautious, unofficial Jev bridge. Prefer other listed `jev-mcp` owners if you already standardized on them.

## How it works

Exposes Jev evaluate/tools over MCP stdio. Distinct from pyck-ai/jev-mcp, legostin/jev-mcp, and keysersoft/jev-mcp-server. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/Afloat16/jev-mcp.git
cd jev-mcp
git checkout 4362f2f69252af4749cc7a4e922e931388e2c51c
```

Pin revision `4362f2f69252af4749cc7a4e922e931388e2c51c` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 4362f2f](https://github.com/Afloat16/jev-mcp/tree/4362f2f69252af4749cc7a4e922e931388e2c51c). AI-assisted README and LICENSE inspection; install/live paths not executed.
