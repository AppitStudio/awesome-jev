# Jev MCP Server (keysersoft)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

AnythingMCP connector exposing TypeSafe Jev yes/no, classification, and scoring tools to Claude, ChatGPT, and other MCP hosts (hosted or self-hosted).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/keysersoft/jev-mcp-server) |
| Maintainer | [keysersoft](https://github.com/keysersoft). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | AnythingMCP connector / MCP server definition. |
| Requirements | AnythingMCP (hosted or self-host); `TYPESAFE_API_KEY`. |
| License | [AGPL-3.0](https://github.com/keysersoft/jev-mcp-server/blob/762e7e5e15a8582dbb0a64cc79458e7b57395f99/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from wangkuangkuang/jev-mcp-server and pyck-ai/jev-mcp. AGPL-3.0 (AnythingMCP stack). |

## When to use

Use when you want Jev as remote MCP tools through AnythingMCP. Prefer wangkuangkuang/jev-mcp-server for a standalone MIT PyPI MCP package.

## How it works

Adapter installs on AnythingMCP, stores the TypeSafe key encrypted, and exposes MCP tools that call `https://api.typesafe.ai`. Community submission issue #641. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/keysersoft/jev-mcp-server.git
cd jev-mcp-server
git checkout 762e7e5e15a8582dbb0a64cc79458e7b57395f99
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `762e7e5e15a8582dbb0a64cc79458e7b57395f99` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream). Distinct from wangkuangkuang/jev-mcp-server and pyck-ai/jev-mcp. AGPL-3.0 (AnythingMCP stack). Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 762e7e5e15a8](https://github.com/keysersoft/jev-mcp-server/tree/762e7e5e15a8582dbb0a64cc79458e7b57395f99). AI-assisted README and LICENSE inspection; install/live paths not executed.
