# jev-skill-scout

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Audit CLI (and Claude Code function-hook mod) that finds turns where a skill should have loaded and did not, judged by TypeSafe Jev—then optionally attaches a one-line live suggestion without changing the skill roster.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/karanb192/jev-skill-scout) |
| Maintainer | [karanb192](https://github.com/karanb192) (Karan Bansal). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`jev-skill-scout` 0.1.0** (bin `jev-skill-scout`); audit CLI + Claude Code mod under `hooks/`. |
| Requirements | Node.js ≥ 20. Live audit/mod need `TYPESAFE_API_KEY`. Audit reads local Claude Code transcripts and `SKILL.md` trees; writes only under the chosen output directory. |
| License | [MIT](https://github.com/karanb192/jev-skill-scout/blob/a10b1a1fe71bc9d6572ba4c2c79dcadc17d01fb0/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `npm test`: **8 passed**. No live TypeSafe calls here. Distinct from [jev-skill-gate](jev-skill-gate.md) (manifest `skillOverrides` gate vs miss audit + live suggest). |

## When to use

Use it to measure skill-miss rates on your own Claude Code history, or to nudge the model with a suggested skill name before each prompt. Prefer [jev-skill-gate](jev-skill-gate.md) when you want to drop irrelevant skills from context via overrides rather than audit misses.

## How it works

[`lib/scout.js`](https://github.com/karanb192/jev-skill-scout/blob/a10b1a1fe71bc9d6572ba4c2c79dcadc17d01fb0/lib/scout.js) posts Choice + Noul gate questions to `https://api.typesafe.ai/v1/systemone` (skill-suggestion cookbook pattern: rank roster, gate the turn, verify the winner). The audit replays transcript prompts; the mod runs the same judgment live. Caller-supplied `fetch` keeps audit and mod aligned.

## Get started

```sh
export TYPESAFE_API_KEY=your_key   # live audit only
npx jev-skill-scout audit --dry-run
# From source at the reviewed commit:
git clone https://github.com/karanb192/jev-skill-scout.git
cd jev-skill-scout
git checkout a10b1a1fe71bc9d6572ba4c2c79dcadc17d01fb0
npm test
```

Live audit/mod calls send prompt excerpts and skill descriptions to TypeSafe and can incur charges. `--dry-run` estimates without spending.

## Examples and demos

- README includes an author-run audit table (vendor/author-reported; not re-run here).
- Offline unit tests in `tests/lib.test.mjs` (mocked fetch).

## Limits and data handling

Transcript paths and skill text are read locally; judged excerpts leave the host on live runs. Jev is a second opinion—upstream reports precision limits on hand labels. This listing did not run a live audit against real transcripts or install the mod.

## Review and maintenance

Reviewed on **2026-09-21** at [commit a10b1a1](https://github.com/karanb192/jev-skill-scout/tree/a10b1a1fe71bc9d6572ba4c2c79dcadc17d01fb0) (`jev-skill-scout` 0.1.0, MIT). AI-assisted source review of README, LICENSE, `lib/scout.js`, package metadata. Offline `npm test`: 8 passed. No live provider calls.

Related: [jev-skill-gate](jev-skill-gate.md), [Hermes Jev Skills](hermes-jev-skills.md), [ask-jev-skill](ask-jev-skill.md).
