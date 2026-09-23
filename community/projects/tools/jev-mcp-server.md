# jev-mcp-server

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python MCP server for TypeSafe Jev: exposes the three official question types (choice, score, noul) plus compare, verify, batch classify, and a one-command client installer. Distinct from [jev-mcp](jev-mcp.md) (ten purpose-built judgment tools) and [TypeSafe MCP](typesafe-mcp.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wangkuangkuang/jev-mcp-server) |
| Maintainer | [wangkuangkuang](https://github.com/wangkuangkuang). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | PyPI **jev-mcp-server 0.2.3** (stdio MCP + `install` subcommand for Claude Code / Pi / Cursor / OpenCode / Codex). |
| Requirements | Python 3.10+ (via `uvx` / `pip`). Live tools need `TYPESAFE_API_KEY` (or the `setup` tool to store a key locally). |
| License | [MIT](https://github.com/wangkuangkuang/jev-mcp-server/blob/97e185e9a2196be27b5a68065458f4ae4cdc6395/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, tool table). Package install and live Jev were **not** executed on the review host. Upstream latency/cost claims were not re-measured. |

## When to use

Use it when an MCP client should ask raw Choice/Score/Noul (plus compare/verify/classify) against TypeSafe Jev with a short installer path. Prefer [jev-mcp](jev-mcp.md) when you want named verify/screen/find/gate workflows instead of the official question primitives.

## How it works

The server maps MCP tools onto TypeSafe System One question types and returns typed answers with probabilities. `uvx jev-mcp-server install <client>` writes client config; `setup` can verify and store a key with restrictive file permissions.

## Get started

```sh
# Needs a TypeSafe API key: https://console.typesafe.ai/settings/keys
uvx jev-mcp-server install claude-code   # or: pi | cursor | opencode | codex
# Restart the client, then ask for a typed probability split
```

Pin for review: [commit 97e185e](https://github.com/wangkuangkuang/jev-mcp-server/tree/97e185e9a2196be27b5a68065458f4ae4cdc6395) (`jev-mcp-server` **0.2.3**).

## Examples and demos

- README tool table (choice / score / noul / compare / verify / classify / setup).
- Manual stdio JSON config examples for clients without the installer.

## Limits and data handling

Live calls send question state to TypeSafe. No local model. This listing did not install the package or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 97e185e](https://github.com/wangkuangkuang/jev-mcp-server/tree/97e185e9a2196be27b5a68065458f4ae4cdc6395) (MIT). AI-assisted review of README and LICENSE. No live TypeSafe spend.

Related: [jev-mcp](jev-mcp.md), [jev-cli (tumf)](tumf-jev-cli.md), [TypeSafe MCP](typesafe-mcp.md), [askjev](askjev.md).
