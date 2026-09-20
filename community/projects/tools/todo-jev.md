# todo-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI experiment that classifies a user request and recommends a three-tier handling path (local rule, Jev/structured skill, or foundation model) with skill profiles and basic environment preflight.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maker-KK/todo-jev) |
| Maintainer | [maker-KK](https://github.com/maker-KK). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **todo-jev 0.1.0** — Typer CLI (`todo-jev` / `python -m app.cli`), skill profiles under `data/`, and offline heuristic fallback. |
| Requirements | Python ≥ 3.10; optional `TYPESAFE_API_KEY` for live Jev (offline keyword fallback works without a key). Depends on `typesafe-sdk`. |
| License | [MIT](https://github.com/maker-KK/todo-jev/blob/08c8a1e744c311e9f88721b414e636d7eb7c156c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live Jev and full eval scripts were not run. Execution handlers are stubs—upstream states connecting your own runners is required to perform tasks. |

## When to use

Use it to explore request→tier routing with bundled skill application/exclusion criteria and local environment checks. Prefer [jev-router](jev-router.md) / [Jev Model Router](jev-model-router.md) when the goal is coding-CLI model selection. Prefer [SkillRanker](skillranker.md) or [jev-skill-gate](jev-skill-gate.md) when ranking or muting an installed skill inventory inside a coding agent rather than choosing a routing tier.

## How it works

[`app/classifier.py`](https://github.com/maker-KK/todo-jev/blob/08c8a1e744c311e9f88721b414e636d7eb7c156c/app/classifier.py) posts Choice questions to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` when `TYPESAFE_API_KEY` is set; otherwise a keyword heuristic returns a tier. Skill profiles supply apply/exclude conditions; preflight checks report environment evidence that can influence recommendations. The CLI prints a routing recommendation; example handlers do not execute the real task.

## Get started

```sh
git clone https://github.com/maker-KK/todo-jev.git
cd todo-jev
git checkout 08c8a1e744c311e9f88721b414e636d7eb7c156c
python -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
# offline (no key):
python -m app.cli route "15 + 27 계산해줘"
```

Live classification sends the prompt and profile criteria to TypeSafe and can incur charges. This listing did not run the live eval script or call live Jev.

## Examples and demos

- README offline routing table (Tier 1/2/3 examples).
- `tests/test_router.py` offline classifier tests — not executed on the review host.
- Optional `scripts/run_eval_comparison.py` (live; not run).

## Limits and data handling

Prompts and skill-profile text leave the host when a key is set. Routing recommendations are advisory; task execution is out of scope of the shipped handlers. Upstream accuracy/cost claims from eval JSON were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 08c8a1e](https://github.com/maker-KK/todo-jev/tree/08c8a1e744c311e9f88721b414e636d7eb7c156c): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `app/classifier.py`, `pyproject.toml`, and tests layout. No live TypeSafe calls.

Related: [jev-router](jev-router.md), [SkillRanker](skillranker.md), [jev-skill-gate](jev-skill-gate.md).
