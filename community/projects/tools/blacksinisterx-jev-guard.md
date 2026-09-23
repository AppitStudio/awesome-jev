# JevGuard (blacksinisterx)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent tool-execution security layer: hard-rule prefilter, then TypeSafe Jev allow/review/block (distinct from catalog leepokai/CMaintz/klauswg jev-guard).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blacksinisterx/jev-guard) |
| Maintainer | [blacksinisterx](https://github.com/blacksinisterx). Independently curated. Not an endorsement. |
| Format | FastAPI + Vite/React demo (`jev-guard`). |
| Requirements | Python backend + Node frontend; `.env` for live TypeSafe (mock-first by default). |
| License | **No LICENSE** in the reviewed tree. Treat as source-available, not Open source. Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review. Source inspected (README, `backend/app/providers/typesafe.py`). Live guard/Jev **not** run. No SPDX license file. Distinct from [leepokai/jev-guard](jev-guard.md). |

## When to use

Use it to demo a security decision layer between an agent and tools with inspectable Jev Choice/Noul. Prefer mature hook packages (leepokai, opencode-jev-guard) for production coding-agent installs.

## How it works

Hard rules short-circuit obvious allow/deny; ambiguous actions get parallel Jev questions; policy maps to allow/review/block before execution.

## Get started

```sh
git clone https://github.com/blacksinisterx/jev-guard.git
cd jev-guard
git checkout 0a2b4d8b16d32559756c611f70badf488f4b9d6e
# follow README mock-first / docker-compose
```

## Examples and demos

- README mermaid flowchart.
- Provider swap via env (documented upstream).

## Limits and data handling

Proposed action text goes to TypeSafe when live. No LICENSE file. Mock mode is the default cost path.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 0a2b4d8](https://github.com/blacksinisterx/jev-guard/tree/0a2b4d8b16d32559756c611f70badf488f4b9d6e). AI-assisted source review. No live TypeSafe spend.

Related: [jev-guard](jev-guard.md), [opencode-jev-guard](opencode-jev-guard.md), [grok-jev-guard](grok-jev-guard.md).
