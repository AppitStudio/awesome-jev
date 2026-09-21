# Jev MCP (Freepik)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dependency-light Go MCP server that exposes typed Jev / System One decisions (`decide`, `classify`, `verify`, `rerank`, `list_models`) via OpenRouter or TypeSafe. Distinct from the npm [`jev-mcp`](jev-mcp.md) package.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/freepik-company/jev-mcp) |
| Maintainer | [freepik-company](https://github.com/freepik-company). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Go module / binary **`jev-mcp` v0.3.0**; multi-arch release archives and `ghcr.io/freepik-company/jev-mcp` images. |
| Requirements | Go 1.26+ to build from source, or a released binary/container; `OPENROUTER_API_KEY` (default) or `TYPESAFE_API_KEY` with `JEV_PROVIDER=typesafe`. |
| License | [Apache-2.0](https://github.com/freepik-company/jev-mcp/blob/c1c5704d6bfc3bcac4674c639918dcfc8229cfcc/LICENSE). Provider usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `go test ./...`: **72 passed** across packages. Live MCP client registration and paid inference were not run. |

## When to use

Use it when an MCP client should call a small Go binary/container for typed classify/verify/rerank/decide tools with validated answers and no credential leakage into tool args. Prefer [jev-mcp](jev-mcp.md) (`@jkudish/jev-mcp`) for the ten purpose-built TypeScript judgment tools, or [TypeSafe MCP](typesafe-mcp.md) for a thin general-purpose `evaluate` tool. Do not treat tool outputs as automated merge/ship approval.

## How it works

The stdio MCP server reads credentials only from its environment, enforces HTTPS, refuses redirects, and bounds request/response size and time. Tool handlers build System One questions, call OpenRouter Decisions or TypeSafe, validate answers against the asked questions, and return typed results plus the unchanged provider response (including `usage.cost` when present). One paid inference call per tool invocation; no automatic retry of paid calls.

## Get started

```sh
# binary from Releases, or:
go install github.com/freepik-company/jev-mcp/cmd/jev-mcp@c1c5704d6bfc3bcac4674c639918dcfc8229cfcc
# reviewed tree:
git clone https://github.com/freepik-company/jev-mcp.git
cd jev-mcp
git checkout c1c5704d6bfc3bcac4674c639918dcfc8229cfcc
go test ./...
```

Register with an MCP client (credential in the server environment only):

```sh
claude mcp add jev -e OPENROUTER_API_KEY="$OPENROUTER_API_KEY" -- jev-mcp
```

Live tool calls send supplied state/items/claims/candidates to the configured provider and incur charges. This listing did not register an MCP client.

## Examples and demos

- README tool table: `decide`, `classify`, `verify`, `rerank`, `list_models`.
- [GitHub Releases](https://github.com/freepik-company/jev-mcp/releases) (`v0.3.0` at review time) and GHCR images.
- Upstream CI workflow badge.

## Limits and data handling

All tool inputs leave the host for the provider. Answers that are inconsistent with the asked questions fail the call rather than being silently repaired. Early software; quality claims were not independently benchmarked here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit c1c5704](https://github.com/freepik-company/jev-mcp/tree/c1c5704d6bfc3bcac4674c639918dcfc8229cfcc) / release **v0.3.0**, Apache-2.0. AI-assisted source review of README, license, and packages. Offline `go test ./...` → **72 passed**. Live OpenRouter/TypeSafe MCP sessions were not run.

Related: [jev-mcp](jev-mcp.md), [TypeSafe MCP](typesafe-mcp.md), [askjev](askjev.md).
