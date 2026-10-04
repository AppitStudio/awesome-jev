# jev-mcp-router (ini8labs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP gateway where TypeSafe Jev answers yes/no per server and tool, so the agent LLM only sees the tools a request needs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ini8labs/jev-mcp-router) |
| Maintainer | [ini8labs](https://github.com/ini8labs). Independently curated. |
| Format | MCP gateway + CLI + benchmark harness |
| Requirements | Python with `uv`; `TYPESAFE_API_KEY`; LLM credentials for `run --compare` and the benchmark. |
| License | [MIT](https://github.com/ini8labs/jev-mcp-router/blob/168bbce8112c5543243edd3fbd2ada2b71cace16/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Large MCP catalogs where tool schemas dominate the context window.
- Measure Jev routing accuracy against your own query set (`eval`).
- Mismatch: small tool sets gain little from routing.

## How it works

For each request, Jev answers a yes/no question per server and tool; the gateway forwards only the approved tools to the agent. Upstream reports 95% needed-tool recall vs 99% for full-catalog Claude Sonnet 5 at lower cost; maintainer results, not reproduced here.

## Get started

Clone, sync, and inspect routing decisions:

```sh
git clone https://github.com/ini8labs/jev-mcp-router.git
cd jev-mcp-router
uv sync
uv run python -m jevmcp route "why is checkout slow?"   # Jev yes/no only
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream benchmark (`bench/run.py report` re-scores saved results without API spend).

## Limits and data handling

Routing sends request text and tool descriptions to TypeSafe. A missed tool means the agent cannot call it; keep a fallback.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 168bbce8112c](https://github.com/ini8labs/jev-mcp-router/tree/168bbce8112c5543243edd3fbd2ada2b71cace16). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
