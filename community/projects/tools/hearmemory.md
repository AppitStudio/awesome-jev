# HearMemory

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shared project memory for multi-agent coding (Claude Code, Codex, Cursor): TypeSafe Jev judges claims against recorded evidence (tests, diffs, commits) before the next agent trusts them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ssd1051/hearmemory) |
| Maintainer | [ssd1051](https://github.com/ssd1051). Independently curated. |
| Format | Python package (`hearmemory` / `hmem`) + MCP/hooks for supported hosts. |
| Requirements | Python 3.11+; optional `typesafe-sdk` via `hearmemory[jev]`; host integrations per README. |
| License | [MIT](https://github.com/ssd1051/hearmemory/blob/e5eaabe05d8b5a9c77f830f14fdf77951931d666/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live host/Jev paths not run on the review host. |

## When to use

Use when **parallel or sequential coding agents** need a project-scoped brief of what is supported vs disputed, with optional pre-commit checks.

## How it works

Agents write commands/results/claims into `.hearmemory`; a worker asks Jev narrow questions (same object? same event? evidence support?). New sessions receive a checked brief; git hooks can flag risky commits.

## Get started

```sh
python3 -m venv .venv
.venv/bin/pip install "hearmemory[jev] @ git+https://github.com/ssd1051/hearmemory@e5eaabe05d8b5a9c77f830f14fdf77951931d666"
.venv/bin/hearmemory init --hosts claude,codex,git
# export TYPESAFE_API_KEY=...  # optional; rules-only without it
```

## Examples and demos

- Overview diagram and host table in the README.

## Limits and data handling

Memory stays under the project directory. With Jev enabled, claim/evidence text goes to TypeSafe. Without a key, deterministic rules apply.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit e5eaabe](https://github.com/ssd1051/hearmemory/tree/e5eaabe05d8b5a9c77f830f14fdf77951931d666). AI-assisted README and LICENSE inspection; live multi-agent runs not executed.
