# Jev Flow

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standalone Node.js studio for typed Jev workflows: Studio, Compendium, Battle Arena, labs, and local examples (distinct from aviletek/jev-flow-harness).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/daltonrpj/jev-flow) |
| Maintainer | [daltonrpj](https://github.com/daltonrpj). Independently curated. Not an endorsement. |
| Format | Node.js application (`jev-flow`) with static multilingual guides. |
| Requirements | Node.js; `npm ci` / `npm start`; optional `TYPESAFE_API_KEY` for live judgments. |
| License | [MIT](https://github.com/daltonrpj/jev-flow/blob/684702711c5a35d3f26cf7a2fffe1fc37d84b389/LICENSE). TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live Studio/Jev **not** run. Distinct from [jev-flow-harness](https://github.com/aviletek/jev-flow-harness). |

## When to use

Use it to author and battle-test typed Jev workflow graphs locally with a studio UI. Prefer harness/CI packages when you only need headless gates.

## How it works

Code-owned decisions combine with typed Jev judgments across Studio, generated Compendium, Battle Arena, and labs. Static docs are prepared for GitHub Pages.

## Get started

```sh
git clone https://github.com/daltonrpj/jev-flow.git
cd jev-flow
git checkout 684702711c5a35d3f26cf7a2fffe1fc37d84b389
npm ci
npm start
```

## Examples and demos

- README multilingual static guide links.
- Local examples and tests under the repo (not executed on the review host).

## Limits and data handling

Workflow prompts/state go to TypeSafe when live keys are set. Quality of arena results was not measured here.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 6847027](https://github.com/daltonrpj/jev-flow/tree/684702711c5a35d3f26cf7a2fffe1fc37d84b389) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [DecideKit](decidekit.md), [daf-jev](daf-jev.md).
