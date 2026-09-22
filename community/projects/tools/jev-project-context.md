# jev-project-context

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evidence-first long-term experiment memory skill for AI coding agents: structured lab-notebook operations with optional TypeSafe Jev semantic triage on audits and context loading.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/poiuyjie/jev_project_context) |
| Maintainer | [poiuyjie](https://github.com/poiuyjie). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill (**Project Context V2**) + stdlib Python scripts under `scripts/` (zero runtime deps). |
| Requirements | Skills-compatible agent; optional `TYPESAFE_API_KEY` for Jev doctor/context layers (degrades without a key). |
| License | [MIT](https://github.com/poiuyjie/jev_project_context/blob/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Scripts compiled and structural `doctor.py` exercised; live TypeSafe not run on the review host. |

## When to use

Use it when an agent needs **resumable research memory** with provenance gates (frame/plan/record/synthesize) and optional Jev-backed audits. Prefer plain notes when you do not need the V2 schema. Jev layers are optional triage—not a substitute for human review of claims.

## How it works

Local `doctor.py` checks structure. Optional `jev_doctor.py` / `jev_context.py` batch typed questions through `scripts/jev_client.py` to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and degrade with notes when no key is set. The main agent remains the judge; Jev only flags support/provenance questions.

## Get started

```sh
git clone https://github.com/poiuyjie/jev_project_context.git
cd jev_project_context
git checkout 52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359
python3 -m py_compile scripts/*.py
python3 scripts/doctor.py .
# Optional live: export TYPESAFE_API_KEY=... then python3 scripts/jev_doctor.py <project-root>
```

Live Jev audits send memory excerpts to TypeSafe and may incur charges. This listing did not call TypeSafe.

## Examples and demos

- Offline on the review host: `python3 -m py_compile scripts/*.py` clean; `python3 scripts/doctor.py .` reported expected missing V2 files on the skill repo itself (0 critical).
- Upstream SKILL.md operations table and mermaid audit flow.

## Limits and data handling

Without a key, semantic Jev triage is skipped. Memory text leaves the host only when Jev scripts run live. Treat Jev findings as triage signals with confidence gates, not ground truth.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 52b06f6](https://github.com/poiuyjie/jev_project_context/tree/52b06f6fc4ebe2ac91d504ffa90bd3eeb9245359): MIT. AI-assisted source review of README, LICENSE, `scripts/jev_client.py`, `scripts/jev_doctor.py`. Offline compile + structural doctor only. No live TypeSafe on the review host.

Related: [jevmory](jevmory.md), [decision-first](decision-first.md), [pi-jev-context](pi-jev-context.md).
