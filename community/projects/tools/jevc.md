# jevc

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Compile natural-language agent rules (and JSON Schema) into **TypeSafe Jev programs**: narrow typed questions plus a code-owned reducer/verdict you can diff and unit-test—aimed at hooks, tool gates, and policy-as-code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doronp/jevc) |
| Maintainer | [doronp](https://github.com/doronp). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI/library **jevc 0.1.0** (npm bin `jevc`; `@typesafe-ai/sdk`). |
| Requirements | Node.js **≥ 20** (tests prefer ≥ 22). Offline `jevc check` replays recorded fixtures; live check needs a TypeSafe key. |
| License | [Apache-2.0](https://github.com/doronp/jevc/blob/e9c2d0b9759a29fa83df01cbb090087d22b998aa/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected; live TypeSafe `jevc check --live` was not run. |

## When to use

Use it when markdown rules keep being “suggestions” and you want **reviewable, testable gates** (for example Claude Code PreToolUse) expressed as Jev questions + ordinary code. Prefer [jev-guard](jev-guard.md) for a ready-made risk-scoring hook pack; prefer [daf-jev](daf-jev.md) for a Python question/gate toolkit without the compile/scan workflow.

## How it works

`jevc scan` heuristically finds decidable rules in `CLAUDE.md` / `AGENTS.md` / skill files. Compilation separates decisions (System One), generation (still needs an LLM), and procedure (belongs in code). Runtime uses `@typesafe-ai/sdk` against TypeSafe System One (`jev-1.13.0` documented upstream). `jevc check` validates fixtures offline without network.

## Get started

```sh
git clone https://github.com/doronp/jevc.git
cd jevc
git checkout e9c2d0b9759a29fa83df01cbb090087d22b998aa
npm ci --ignore-scripts
npm run build
npm test
npx jevc check    # offline fixture replay
# npx jevc scan . / compile --lift — see upstream README
```

Live evaluation sends rule state to TypeSafe and can incur charges; this listing ran offline build/tests only.

## Examples and demos

- Offline `npm test` — **1010 passed** (19 files) on the review host.
- Upstream examples, Claude Code gate samples, and `jevc check` fixture corpus.

## Limits and data handling

Scan classification is a text heuristic, not a guarantee every rule is decidable. Compilations with no decisions are valid. Live runs send decision state to TypeSafe. Upstream latency/cost claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit e9c2d0b](https://github.com/doronp/jevc/tree/e9c2d0b9759a29fa83df01cbb090087d22b998aa): **0.1.0**, Apache-2.0. AI-assisted source review of README, LICENSE, `package.json`, and gate/examples layout. Ran `npm ci --ignore-scripts`, `npm run build`, and `npm test` (1010 pass). No live TypeSafe calls.

Related: [jev-guard](jev-guard.md), [daf-jev](daf-jev.md), [toolgate](toolgate.md), [SemDecide](semdecide.md).
