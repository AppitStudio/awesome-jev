# jevskillz

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skills + zero-dependency `jev` CLI: calibrated multi-phrasing TypeSafe Jev checks for claims, tests, acceptance, triage, and ranking over pasted evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/calelamb/jevskillz) |
| Maintainer | [calelamb](https://github.com/calelamb). Independently curated. Not an endorsement. |
| Format | CLI `bin/jev.mjs` + Claude Code skills under `skills/`. |
| Requirements | Node ≥ 18; `TYPESAFE_API_KEY`; Claude Code for skills path. |
| License | [MIT](https://github.com/calelamb/jevskillz/blob/9205774dda8207a970d01118f67298be97cfff68/LICENSE). TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live calibrate/Jev **not** run. |

## When to use

Use it when Claude Code should run evidence-backed gates (“does this claim hold?”, “is the test behavioral?”) with mean confidence intervals across phrasings. Prefer [clear-head](clear-head.md) for Stop-hook claim-vs-tool evidence specifically.

## How it works

Eight CLI modes (`claims`, `tests`, `ac`, `resolve`, `score`, `rerank`, `choice`, …) send several independently phrased noul/choice/score questions and report `mean [95% interval]`. Skills tell the agent when to invoke each mode. `npm test` is offline; `npm run calibrate` hits the live API.

## Get started

```sh
git clone https://github.com/calelamb/jevskillz.git ~/jevskillz
cd ~/jevskillz && git checkout 9205774dda8207a970d01118f67298be97cfff68
export TYPESAFE_API_KEY=...
./install.sh
npm test   # offline
```

## Examples and demos

- `bin/examples/` good/bad fixtures per mode.
- README sample `jev claims` output.

## Limits and data handling

Evidence JSON you paste goes to TypeSafe. Exit codes encode pass/fail/error. Calibration is live and may spend.

## Review and maintenance

Reviewed **2026-09-23** at [commit 9205774](https://github.com/calelamb/jevskillz/tree/9205774dda8207a970d01118f67298be97cfff68) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [clear-head](clear-head.md), [Hermes Jev Skills](hermes-jev-skills.md), [Intent-Router](intent-router.md).
