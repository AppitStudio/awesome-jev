# prompt2jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill plus dependency-free CLI that turn natural language, an LLM prompt, or the code that runs one into a TypeSafe Jev decision: typed `state` + Choice/Score/Noul questions, validation against the API contract, and a runnable script.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sumleo/prompt2jev) |
| Maintainer | [sumleo](https://github.com/sumleo). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill (`skills/prompt2jev/SKILL.md`) + stdlib Python CLI (`skills/prompt2jev/scripts/prompt2jev.py`); works with Claude Code, Codex, Cursor, and similar skill hosts. |
| Requirements | Python **3.10+** for validate/codegen (no third-party packages). Generated SDK scripts need `typesafe-sdk` or `@typesafe-ai/sdk`; live calls need `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/sumleo/prompt2jev/blob/f3b6bc763b742b9f489bf0fa0c9514e334996283/LICENSE). TypeSafe/OpenRouter usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline: `python3 -m pytest tests/ -q` → **85 passed, 56 subtests passed**. No live TypeSafe calls. Distinct from [ask-jev-skill](ask-jev-skill.md) (Hermes tiebreaker) and [decision-first](decision-first.md) (adopt/decline logging). |

## When to use

Use it when you are migrating a classifier/router/grader prompt (or the code around it) onto Jev and want a verified request JSON plus a runnable decide script. Prefer [ask-jev-skill](ask-jev-skill.md) when the agent only needs an ad-hoc typed tiebreak, not a conversion package.

## How it works

The skill teaches an agent to split judgments into atomic questions, move computable rules into code, and drop prose-generation instructions. The CLI validates `{"model","state","questions"}` against the System One contract and can emit Python, JavaScript, stdlib Python, or `curl`. Archetype requests cover routing, guardrails, rubrics, extraction, and claim checks. Live generation/answers call TypeSafe (or OpenRouter→Jev) and send state text.

## Get started

```sh
git clone https://github.com/sumleo/prompt2jev.git
cd prompt2jev
git checkout f3b6bc763b742b9f489bf0fa0c9514e334996283
python3 -m pytest tests/ -q
# Install the skill into your agent host per upstream README, then:
python3 skills/prompt2jev/scripts/prompt2jev.py validate path/to/request.json --strict
```

Live `code`/`decide` paths that hit the API need a key and can incur charges. Validation and tests do not.

## Examples and demos

- Walkthrough video `assets/prompt2jev-walkthrough.mp4` and `examples/triage/`.
- Offline unit tests under `tests/` (executed for this listing).

## Limits and data handling

Converted `state` and question text leave the host on live calls. Do not put secrets in prompts or state. Upstream timing/cost anecdotes were not independently measured.

## Review and maintenance

Reviewed on **2026-09-21** at [commit f3b6bc7](https://github.com/sumleo/prompt2jev/tree/f3b6bc763b742b9f489bf0fa0c9514e334996283): MIT. AI-assisted source review of README, `SKILL.md`, CLI script, and offline pytest. No live provider calls.

Related: [ask-jev-skill](ask-jev-skill.md), [decision-first](decision-first.md), [daf-jev](daf-jev.md).
