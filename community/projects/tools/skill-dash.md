# Skill Dash

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local dashboard that uses TypeSafe Jev to judge Claude Code and Codex skills (usefulness, redundancy, clarity, action) with transcript evidence and overlap audit; also the pipeline behind the public whichskills.dev census.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/48Nauts-Operator/skill-dash) |
| Maintainer | [48Nauts-Operator](https://github.com/48Nauts-Operator) / 48Nauts. Independently curated; this entry is not an upstream submission or endorsement. TypeSafe did not commission the whichskills.dev run. |
| Format | Python stdlib + SQLite local server (`server.py`); browser UI on loopback. |
| Requirements | Python 3. Loader/evidence/static pre-scan need no key. Judgments and overlap audit need `TYPESAFE_API_KEY` (or macOS Keychain `xnaut` / `plugin/typesafe/TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/48Nauts-Operator/skill-dash/blob/fc13176636934faa251bf9b8e57674cc134fcf96/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline unittest inspected. Live TypeSafe judgments and whichskills.dev regeneration were not run. Distinct from [SkillRanker](skillranker.md) / [Skillbox](skillbox.md) / [jev-skill-gate](jev-skill-gate.md). |

## When to use

Use it to review your own `~/.claude/skills` tree (or any `SKILL.md` roots) with inspectable Jev distributions and keep/merge/delete decisions stored locally. Prefer [SkillRanker](skillranker.md) for next-step ranking in a live session, or [jev-skill-gate](jev-skill-gate.md) for Claude Code `skillOverrides` gating.

## How it works

[`engine.py`](https://github.com/48Nauts-Operator/skill-dash/blob/fc13176636934faa251bf9b8e57674cc134fcf96/engine.py) posts typed Score/Choice questions to `https://api.typesafe.ai/v1/systemone` (default `jev-1.13.0`). Local code owns skill loading, transcript evidence scans, pairwise overlap, SQLite persistence, and the loopback UI. Nothing on disk is deleted by the app; only judgment payloads leave the machine when you run judges.

## Get started

```sh
git clone https://github.com/48Nauts-Operator/skill-dash.git
cd skill-dash
git checkout fc13176636934faa251bf9b8e57674cc134fcf96
python3 -m unittest discover -s tests -v
# Live dashboard (charges TypeSafe when judging):
# export TYPESAFE_API_KEY=… && python3 server.py --port 3345
```

## Examples and demos

- README describes the local skill tree UI and `--roots` mode for third-party skill repos.
- Public census methodology notes for [whichskills.dev](https://whichskills.dev) in `scripts/build_site.py` (author-reported costs).

## Limits and data handling

Binds to 127.0.0.1. Skill bodies and descriptions are treated as data to judge, not instructions (policy text in `engine.py`). Token/cost figures in upstream docs are author-reported. Live judgment runs send skill state to TypeSafe.

## Review and maintenance

Reviewed on **2026-09-21** at [commit fc13176](https://github.com/48Nauts-Operator/skill-dash/tree/fc13176636934faa251bf9b8e57674cc134fcf96): MIT. AI-assisted source review of `engine.py`, `server.py`, README, and LICENSE. **`python3 -m unittest discover -s tests -v`**: **4 passed**. No live TypeSafe calls.

Related: [SkillRanker](skillranker.md), [Skillbox](skillbox.md), [jev-skill-gate](jev-skill-gate.md).
