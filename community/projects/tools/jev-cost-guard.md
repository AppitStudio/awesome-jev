# jev-cost-guard (portable plugin and MCP server that lets Jev rank files, screen fetched content and verdict tool output to cut agent tokens)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin of skills plus a `jev` MCP server for Hermes, Claude Code and Codex that attacks two token leaks: the fixed prompt re-sent each call and bloated tool output. The MCP tools `jev_find` (rank files before reading), `jev_screen` (admit or quarantine fetched content) and `jev_summarize` (one short Noul verdict) judge text on demand; Jev never replaces the bytes, it only decides what to read or keep. Works through TypeSafe directly or the free OpenCode Zen `jev-1.13-free` relay.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ronail/jev-cost-guard) |
| Maintainer | [ronail](https://github.com/ronail). Independently curated. |
| Format | Portable agent plugin (Markdown skills and a Python MCP server) |
| Requirements | Python 3 and a harness that accepts portable plugins (Hermes, Claude Code, Codex); a TypeSafe key, or the OpenCode Zen relay key for the free route. |
| License | [MIT](https://github.com/ronail/jev-cost-guard/blob/9c6dc9a6a3788cdfa7cf6895d0f486801ff7c698/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mcp/jev/server.py`](https://github.com/ronail/jev-cost-guard/blob/9c6dc9a6a3788cdfa7cf6895d0f486801ff7c698/mcp/jev/server.py) at the pinned commit. |

## When to use

- Trim an agent's context spend by letting a cheap typed model screen and rank tool output instead of reading everything.
- Mismatch: savings depend on your workload, and the free relay's availability is outside the project's control.

## How it works

`mcp/jev/server.py` sends noul questions to `https://api.typesafe.ai/v1/systemone` when `TYPESAFE_API_KEY` is set, otherwise to the OpenCode Zen relay `https://opencode.ai/zen/v1/systemone` with `jev-1.13-free`, and exposes `jev_health`, `jev_summarize`, `jev_find` and `jev_screen` with call budgets. Integration evidence: [`mcp/jev/server.py`](https://github.com/ronail/jev-cost-guard/blob/9c6dc9a6a3788cdfa7cf6895d0f486801ff7c698/mcp/jev/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
hermes -p dev plugins install ronail/jev-cost-guard
hermes -p dev plugins enable jev-cost-guard
hermes -p dev mcp list
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the skills table and harness adapters: [github.com/ronail/jev-cost-guard#readme](https://github.com/ronail/jev-cost-guard#readme)
- Harness adapter notes: [github.com/ronail/jev-cost-guard/blob/9c6dc9a6a3788cdfa7cf6895d0f486801ff7c698/docs/harness-adapters.md](https://github.com/ronail/jev-cost-guard/blob/9c6dc9a6a3788cdfa7cf6895d0f486801ff7c698/docs/harness-adapters.md)

## Limits and data handling

Text you ask Jev to judge (candidate file contents, fetched pages, tool output) goes to the chosen provider; a hosted relay may be rate-limited or retired. The README's token-savings framing was not reproduced. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 9c6dc9a6a378](https://github.com/ronail/jev-cost-guard/tree/9c6dc9a6a3788cdfa7cf6895d0f486801ff7c698). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
