# jev-skill-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Gate Claude Code's skill manifest with TypeSafe Jev: score installed skills for relevance to the current work and write `skillOverrides` so only the useful ones reach context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ShivamPansuriya/jev-skill-gate) |
| Maintainer | [ShivamPansuriya](https://github.com/ShivamPansuriya). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI (`jev-skill-gate`) with zero runtime dependencies, version **0.2.0**. |
| Requirements | Node.js ≥ 18; Claude Code; `TYPESAFE_API_KEY` (or Vercel AI Gateway key per upstream transport). Local scorer/eval paths need no key. |
| License | [MIT](https://github.com/ShivamPansuriya/jev-skill-gate/blob/1ab4c9a7cd117e1c7e129021303416bb7c2f5328/LICENSE). |

## When to use

Use it when a large Claude Code skill library burns tokens before you type, and you want Jev (or the bundled local scorer) to hide irrelevant skills via overrides. Prefer [SkillRanker](skillranker.md) when you want ranked suggestions for the next step rather than muting the manifest. Prefer [Skillbox](skillbox.md) for hosting a shared skill library with optional recommendations.

## How it works

[`src/jev.mjs`](https://github.com/ShivamPansuriya/jev-skill-gate/blob/1ab4c9a7cd117e1c7e129021303416bb7c2f5328/src/jev.mjs) batches noul (TypeSafe `/v1/systemone`) or boolean (Vercel AI Gateway) questions—one shared state, many skills in parallel—then code writes Claude Code `skillOverrides`. Committed evals under `eval/` compare Jev and local scorers on labeled cases.

## Get started

```sh
git clone https://github.com/ShivamPansuriya/jev-skill-gate.git
cd jev-skill-gate
git checkout 1ab4c9a7cd117e1c7e129021303416bb7c2f5328
npm test                 # offline unit tests
node eval/run-eval.mjs --local --fresh   # free local scorer eval
# Live Jev arm needs TYPESAFE_API_KEY / credits — not run for this listing
```

Installing into Claude Code follows upstream `install.sh` / README. Live scoring sends skill descriptions and prompt state to the chosen provider.

## Examples and demos

- Offline `npm test` and `node eval/run-eval.mjs --local --fresh`.
- Committed reports: `eval/RESULTS.md`, `eval/COMPARISON.md`, `eval/JEV-PARTIAL.md`.

## Limits and data handling

Skill names/descriptions and prompt/project state leave the host when using TypeSafe or the Gateway. Hiding the wrong skill is worse than no gate—review overrides. Upstream AUC/token-saving figures are author-reported; only offline local eval was exercised here as documented above.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 1ab4c9a](https://github.com/ShivamPansuriya/jev-skill-gate/tree/1ab4c9a7cd117e1c7e129021303416bb7c2f5328): **0.2.0**, MIT. AI-assisted source review of README, `src/jev.mjs`, package metadata, license, and eval layout. Offline `npm test` / local eval may be re-run by maintainers; this listing did not call live TypeSafe.

Related: [SkillRanker](skillranker.md), [Skillbox](skillbox.md), [Hermes Jev Skills](hermes-jev-skills.md).
