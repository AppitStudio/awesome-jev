# jev-support-agents

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Teaching/reference FastAPI multi-agent customer-support API where LLM agents write reply text and TypeSafe Jev owns routing plus response evaluation (accept / ask-user / escalate / retry).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RavioliCodes/jev-support-agents) |
| Maintainer | [RavioliCodes](https://github.com/RavioliCodes). Independently curated. |
| Format | Python FastAPI service with evaluation harness. |
| Requirements | Python; Ollama (or configured LLMs); TypeSafe/Jev access for decisions. |
| License | [MIT](https://github.com/RavioliCodes/jev-support-agents/blob/160b77c959a321ec566d11db6d5d9ad9d2bd673d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live ticket runs not executed. |

## When to use

Use to learn a **decision-vs-generation** support loop with inspectable Jev routing. Prefer hosted helpdesk products when you need a production inbox.

## How it works

`SupportOrchestrator` triages with an LLM, asks `JevDecisionService` for a route, then runs specialist LLM(s). Jev evaluates each draft under Python-owned retry limits.

## Get started

```sh
git clone https://github.com/RavioliCodes/jev-support-agents.git
cd jev-support-agents
git checkout 160b77c959a321ec566d11db6d5d9ad9d2bd673d
pip install -r requirements.txt
# configure .env per README; start FastAPI; optional evaluation scripts
```

## Examples and demos

- `evaluation/` 60-ticket benchmark materials.
- `tests/` pytest suite (not re-run here).

## Limits and data handling

Ticket text and drafts go to configured LLM and Jev providers. Benchmark claims are upstream.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 160b77c](https://github.com/RavioliCodes/jev-support-agents/tree/160b77c959a321ec566d11db6d5d9ad9d2bd673d). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [Juardrails](juardrails.md), [agent-chaperone](agent-chaperone.md).
