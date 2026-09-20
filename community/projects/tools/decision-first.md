# decision-first

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill that spots bounded-judgment steps, tries TypeSafe Jev (Choice / Score / Noul) before regex/LLM heuristics, and documents every attempt in a reusable “decision lab” directory.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/harrymunro/decision-first) |
| Maintainer | [harrymunro](https://github.com/harrymunro). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill pack (`skills/decision-first/` + stdlib Python scripts); Claude plugin metadata included. |
| Requirements | Python 3; an agent that can load skills (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Pi, Hermes, …). Live trials need `TYPESAFE_API_KEY`. Lab defaults to `~/Workspace/decision-lab` (`DECISION_LAB` override). |
| License | [MIT](https://github.com/harrymunro/decision-first/blob/d57ff835dd91d9eb72d2a6e74488a84108d1b556/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `pytest` inspected; live agent installs and live TypeSafe trials were not run. Editable `pip install -e .` failed on setuptools multi-package discovery—tests were run against the tree without packaging. |

## When to use

Use it when you want agents to **notice** classify/tag/triage/route/gate steps and leave a paper trail of Jev trials (adopted or declined). Prefer [ask-jev-skill](ask-jev-skill.md) for a Hermes-focused typed tiebreak CLI; prefer [Hermes Jev Skills](hermes-jev-skills.md) for a broader routing/memory/compaction pack; prefer [SkillRanker](skillranker.md) for ranking a large skill inventory from live context.

## How it works

[`skills/decision-first/SKILL.md`](https://github.com/harrymunro/decision-first/blob/d57ff835dd91d9eb72d2a6e74488a84108d1b556/skills/decision-first/SKILL.md) defines the announce → shape test → design → try → measure → document loop. [`scripts/ask.py`](https://github.com/harrymunro/decision-first/blob/d57ff835dd91d9eb72d2a6e74488a84108d1b556/skills/decision-first/scripts/ask.py) posts to `https://api.typesafe.ai/v1/systemone` (stdlib only; `--dry-run` supported). `compare.py` and `lab.py` handle agreement tables and case directories. Optional Claude `UserPromptSubmit` hook nudges without forcing.

## Get started

```sh
git clone https://github.com/harrymunro/decision-first.git
cd decision-first
git checkout d57ff835dd91d9eb72d2a6e74488a84108d1b556
# Copy skills/decision-first into your agent skills directory (see upstream README).
python3 -m pytest -q
# Dry-run a questions file without contacting TypeSafe:
python3 skills/decision-first/scripts/ask.py --questions path/to/q.json --state-text '...' --dry-run
```

Set `TYPESAFE_API_KEY` before live trials. Live calls send state/items to TypeSafe and can incur charges; this listing ran offline pytest only.

## Examples and demos

- Offline `pytest` — **14 passed** on the review host (`tests/test_skill.py`).
- Upstream `evals/` trigger measurement and case-report issue template.

## Limits and data handling

Trial state and question text leave the host on live asks. Do not put secrets in lab case files that will be re-run. Upstream cost/latency tables were not independently measured. Packaging the repo as an installable wheel may need an explicit setuptools package layout (not required to use the skill files).

## Review and maintenance

Reviewed on **2026-09-20** at [commit d57ff83](https://github.com/harrymunro/decision-first/tree/d57ff835dd91d9eb72d2a6e74488a84108d1b556): MIT. AI-assisted source review of README, LICENSE, `SKILL.md`, `scripts/ask.py`, and tests. Ran `python3 -m pytest -q` (14 pass). No live TypeSafe or multi-agent install runs.

Related: [ask-jev-skill](ask-jev-skill.md), [Hermes Jev Skills](hermes-jev-skills.md), [SkillRanker](skillranker.md).
