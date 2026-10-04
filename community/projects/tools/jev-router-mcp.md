# jev-router-mcp

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server that routes a question to the best tool via a Jev-compatible `/v1/systemone` decision engine (works with Laya).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/humayunkabir/jev-router-mcp) |
| Maintainer | [humayunkabir](https://github.com/humayunkabir). Independently curated. |
| Format | MCP server / npm package (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/humayunkabir/jev-router-mcp/blob/ffe110ed2ac278eab8ebed9094d848be4a21d544/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when mCP server that routes a question to the best tool via a Jev-compatible `/v1/systemone` decision engine (works with Laya). Prefer related catalog tools when another listing better matches your stack.

## How it works

MCP `route_code` / `route_query` ask a System One server for a tool Choice; agent calls the selected tool. Fail-open advice when unreachable.

## Get started

```sh
git clone https://github.com/humayunkabir/jev-router-mcp.git
cd jev-router-mcp
git checkout ffe110ed2ac278eab8ebed9094d848be4a21d544
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit ffe110ed2ac2](https://github.com/humayunkabir/jev-router-mcp/tree/ffe110ed2ac278eab8ebed9094d848be4a21d544). AI-assisted README and license inspection; install/live paths not executed.
