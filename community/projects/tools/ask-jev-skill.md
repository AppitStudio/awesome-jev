# ask-jev-skill

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes skill that calls TypeSafe Jev (`jev-latest`) as a typed Choice / Score / Noul tiebreaker when an agent still has plausible paths.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shantanugoel/ask-jev-skill) |
| Maintainer | [shantanugoel](https://github.com/shantanugoel). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Hermes skill (`SKILL.md` + stdlib Python `scripts/askjev.py`), version **0.1.0**. |
| Requirements | Python 3; Hermes (`HERMES_HOME`); `TYPESAFE_API_KEY` in `$HERMES_HOME/.env`. Disable with `ASKJEV_DISABLED=1`. |
| License | [MIT](https://github.com/shantanugoel/ask-jev-skill/blob/72313d3c88f8dbff40a11ffe69656ff9843ea78e/LICENSE). |

## When to use

Use it when Hermes (or another agent hosting the skill) needs a calibrated tiebreak rather than a coin-flip among remaining options. Prefer [Hermes Jev Skills](hermes-jev-skills.md) when you want a broader pack (routing, memory, compaction, skill pick). Prefer [SkillRanker](skillranker.md) for ranking a large skill inventory from live session context.

## How it works

[`scripts/askjev.py`](https://github.com/shantanugoel/ask-jev-skill/blob/72313d3c88f8dbff40a11ffe69656ff9843ea78e/scripts/askjev.py) posts to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` (override via `TYPESAFE_DEFAULT_MODEL` / `--model`). The skill document states when to call Jev, confidence gates, and pitfalls; application code owns acting or escalating on the returned probabilities.

## Get started

```sh
git clone https://github.com/shantanugoel/ask-jev-skill.git
cd ask-jev-skill
git checkout 72313d3c88f8dbff40a11ffe69656ff9843ea78e
mkdir -p "${HERMES_HOME:-$HOME/.hermes}/skills/autonomous-ai-agents/askjev"
cp -R SKILL.md scripts "${HERMES_HOME:-$HOME/.hermes}/skills/autonomous-ai-agents/askjev/"
# Put TYPESAFE_API_KEY in $HERMES_HOME/.env
python3 scripts/askjev.py choice --state '...' --question 'Which path?' \
  --option a='...' --option b='...'
```

Live calls need a TypeSafe key and incur charges. This listing did not run Hermes or live Jev.

## Examples and demos

- Upstream `SKILL.md` usage contract and `scripts/askjev.py` CLI (`choice` / score / noul).
- Optional `scripts/eval.py` live reliability suite (needs API key; not run here).

## Limits and data handling

Decision `state` and question text leave the host for TypeSafe. Do not put secrets in state. Upstream confidence/cost anecdotes were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 72313d3](https://github.com/shantanugoel/ask-jev-skill/tree/72313d3c88f8dbff40a11ffe69656ff9843ea78e): **0.1.0**, MIT. AI-assisted source review of README, `SKILL.md`, `scripts/askjev.py`, and license. No live TypeSafe or Hermes sessions were run.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [SkillRanker](skillranker.md), [Advocaat](advocaat.md).
