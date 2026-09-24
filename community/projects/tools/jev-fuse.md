# jev-fuse

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Governed reverse proxy between callers (Claude Code, MCP, SDKs) and TypeSafe Jev or local Laya: turn probabilities into ALLOW/ASK/DENY-style actions with AST guards, singleflight, and WAL audit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0xshikhar/jev-fuse) |
| Maintainer | [0xshikhar](https://github.com/0xshikhar). Independently curated. |
| Format | Python package/proxy (`jev-fuse` on PyPI). |
| Requirements | Python 3.12+; upstream TypeSafe Jev or local Laya; MCP/agent callers as configured. |
| License | [Apache-2.0](https://github.com/0xshikhar/jev-fuse/blob/27ca7c014a539d7228583d846b68d13c4e9c13a2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live proxy not run. Note: default branch is `master`. |

## When to use

Use when raw decision probabilities need a **policy and audit plane** before agents act. Prefer [agent-chaperone](agent-chaperone.md) for MCP tool-call firewalls without a System One proxy.

## How it works

Callers POST System One traffic through Fuse; AST guard, dedupe, and DuckDB WAL audit translate model outputs into deterministic actions (per README).

## Get started

```sh
git clone https://github.com/0xshikhar/jev-fuse.git
cd jev-fuse
git checkout 27ca7c014a539d7228583d846b68d13c4e9c13a2
# pip install / run per README (PyPI jev-fuse)
```

## Examples and demos

- README architecture diagram and capability list.

## Limits and data handling

Decision payloads and related command context may be logged locally and forwarded to the configured decision engine.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 27ca7c0](https://github.com/0xshikhar/jev-fuse/tree/27ca7c014a539d7228583d846b68d13c4e9c13a2). AI-assisted README inspection; live governance path not run.

Related: [agent-chaperone](agent-chaperone.md).
