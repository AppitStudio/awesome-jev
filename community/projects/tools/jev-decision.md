# Jev Decision

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable, budgeted Jev client for coding-agent harnesses (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, any MCP or shell client) with a shared daily budget ledger, explicit `unavailable` results and harness recipes; advice, never authority.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Coding-Dev-Tools/jev-decision) |
| Maintainer | [Coding-Dev-Tools](https://github.com/Coding-Dev-Tools). Independently curated. |
| Format | Python library, CLI (`jev`) and MCP server (`jev-mcp`); TypeScript client |
| Requirements | Python 3.10+ for MCP (3.9+ core); TypeSafe API key and a daily budget set via `jev setup`. |
| License | [MIT](https://github.com/Coding-Dev-Tools/jev-decision/blob/bb6528b9c3cc9cc634f7c577125c57fb291e8bfe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_decision/client.py`](https://github.com/Coding-Dev-Tools/jev-decision/blob/bb6528b9c3cc9cc634f7c577125c57fb291e8bfe/jev_decision/client.py) at the pinned commit. |

## When to use

- Give several coding agents one budgeted way to ask Jev narrow yes/no, choice or rubric questions.
- Keep Jev advisory: permission rules and executed tests stay in charge.
- Mismatch: the README installs a v0.3 development branch under review, not a published release.

## How it works

The client posts typed questions to `api.typesafe.ai`, charges each call against a shared Python budget ledger, and returns an explicit `unavailable` result on missing key, exhausted budget, timeout or provider error so harnesses fall back instead of guessing. Integration evidence: [`jev_decision/client.py`](https://github.com/Coding-Dev-Tools/jev-decision/blob/bb6528b9c3cc9cc634f7c577125c57fb291e8bfe/jev_decision/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install "jev-decision[mcp,setup] @ git+https://github.com/Coding-Dev-Tools/jev-decision@codex/jev-harness-integration"
jev setup
jev doctor --live   # one small budgeted request
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Harness recipes: `docs/` and `SKILL.md` in the repository.

## Limits and data handling

Questions and state go to TypeSafe on your key, bounded by the configured daily budget.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit bb6528b9c3cc](https://github.com/Coding-Dev-Tools/jev-decision/tree/bb6528b9c3cc9cc634f7c577125c57fb291e8bfe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
