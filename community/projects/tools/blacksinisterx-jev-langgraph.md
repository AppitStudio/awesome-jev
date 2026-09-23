# JevLangGraph (blacksinisterx)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

LangGraph agent where TypeSafe Jev—not an LLM—chooses continue/search/use_tool/retry/finish/escalate at every branch (distinct from wudilyy999/jev-langgraph).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blacksinisterx/jev-langgraph) |
| Maintainer | [blacksinisterx](https://github.com/blacksinisterx). Independently curated. Not an endorsement. |
| Format | FastAPI + Vite/React demo (`jev-langgraph`). |
| Requirements | Python backend + Node frontend; `.env` for live TypeSafe (mock-first by default). |
| License | **No LICENSE** in the reviewed tree. Treat as source-available, not Open source. Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review. Source inspected (README, `backend/app/providers/typesafe.py`). Live agent/Jev **not** run. No SPDX license file. |

## When to use

Use it to study a LangGraph loop whose control plane is typed Jev Choice over a closed action set. Prefer production LangGraph apps when you need LLM planning at forks.

## How it works

`decide` calls Jev via providers (`typesafe.py` / `jev_agent.py`); tool/search/retry nodes execute; escalate ends to a human. Mock providers keep default runs zero-cost.

## Get started

```sh
git clone https://github.com/blacksinisterx/jev-langgraph.git
cd jev-langgraph
git checkout abd073e7a0ed2a13eb773ef8abd5c41d87136868
# follow README: docker-compose or backend venv + frontend npm; mock by default
```

## Examples and demos

- README control-flow diagram and mock-first note.
- `docker-compose.yml` for local stack.

## Limits and data handling

Query/tool transcripts go to TypeSafe when live. No LICENSE file. Distinct from other `jev-langgraph` owners already considered in discovery.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit abd073e](https://github.com/blacksinisterx/jev-langgraph/tree/abd073e7a0ed2a13eb773ef8abd5c41d87136868). AI-assisted source review. No live TypeSafe spend.

Related: [Intent-Router](intent-router.md), [jev-guard](jev-guard.md), [DecideKit](decidekit.md).
