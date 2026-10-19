# Jev MCP (tmbmartell)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Portuguese-language MCP server that exposes Jev (TypeSafe System One) to agents such as Hermes, Claude Code, and Cursor as a typed judgment tool for noul, choice, and score questions, routed via OpenRouter or TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tmbmartell/jev-mcp) |
| Maintainer | [tmbmartell](https://github.com/tmbmartell). Independently curated. |
| Format | Python MCP server |
| Requirements | Python 3.10+, the `mcp` package, and an OpenRouter or TypeSafe key. |
| License | [MIT](https://github.com/tmbmartell/jev-mcp/blob/98d1455da8c82c840b95d6a7d6dc9fa4f0af60a1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cli.py`](https://github.com/tmbmartell/jev-mcp/blob/98d1455da8c82c840b95d6a7d6dc9fa4f0af60a1/cli.py) at the pinned commit. |

## When to use

- Give an agent calibrated yes/no, choice, or score answers as a tool.
- Mismatch: docs are in Portuguese; one of several Jev MCP servers.

## How it works

The server forwards typed questions to Jev and returns probabilities and confidence; `cli.py` documents a `route` option for OpenRouter (default) or TypeSafe. Integration evidence: [`cli.py`](https://github.com/tmbmartell/jev-mcp/blob/98d1455da8c82c840b95d6a7d6dc9fa4f0af60a1/cli.py).

## Get started

From the upstream INSTALL.md: clone, install `mcp`, set your key, and register the server with your MCP client.

```sh
git clone https://github.com/tmbmartell/jev-mcp.git
# see INSTALL.md to register with Hermes, Claude Code, or Cursor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- INSTALL.md

## Limits and data handling

State and questions go to OpenRouter or TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 98d1455da8c8](https://github.com/tmbmartell/jev-mcp/tree/98d1455da8c82c840b95d6a7d6dc9fa4f0af60a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
