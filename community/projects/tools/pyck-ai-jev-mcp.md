# jev-mcp (pyck-ai)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev via OpenRouter as a suite of fail-closed MCP tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pyck-ai/jev-mcp) |
| Maintainer | [pyck-ai](https://github.com/pyck-ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go MCP server with plugin-style tools. |
| Requirements | Go toolchain or released binary; OpenRouter credentials (opencode login reused when available). |
| License | [MIT](https://github.com/pyck-ai/jev-mcp/blob/74cfb4c385f2896c7f79b868d3e3d1d6e60a4de9/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when an MCP host should call structured Jev tools. Prefer direct SDKs for non-MCP apps.

## How it works

Each tool batches System One primitives with documented thresholds; fail-closed conventions avoid fabricated verdicts. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/pyck-ai/jev-mcp.git
cd jev-mcp
git checkout 74cfb4c385f2896c7f79b868d3e3d1d6e60a4de9
# build/install per upstream README; configure OpenRouter
```

Pin revision `74cfb4c385f2896c7f79b868d3e3d1d6e60a4de9` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

OpenRouter path (not direct TypeSafe). Distinct from other jev-mcp packages. Live MCP tools not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 74cfb4c](https://github.com/pyck-ai/jev-mcp/tree/74cfb4c385f2896c7f79b868d3e3d1d6e60a4de9). AI-assisted README and LICENSE inspection; install/live paths not executed.
