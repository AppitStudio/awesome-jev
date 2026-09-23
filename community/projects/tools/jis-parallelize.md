# JIS · PARALLELIZE (lovstudio/jis)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-organising agent swarm: rules do zero-token coordination; TypeSafe Jev judges verify/adopt/dispute when rules cannot; LLMs solve tasks and escalate on low confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lovstudio/jis) |
| Maintainer | [lovstudio](https://github.com/lovstudio). EvoTavern SECTION 9 entry. Independently curated. Not an endorsement. |
| Format | Node swarm harness + web dashboard (`pnpm dev`). |
| Requirements | Node/pnpm; `OPENROUTER_API_KEY` (Jev + LLM via OpenRouter per README). |
| License | [Apache-2.0](https://github.com/lovstudio/jis/blob/d0c693e372075fb3d36f05b52dbf7c52f59bdd2b/LICENSE). Provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, PROTOCOL.md). Live swarm/Jev **not** run. Benchmark tables are upstream-reported, not re-measured. |

## When to use

Use it when studying or demoing multi-agent coordination where Jev handles non-rule judgments (verify/adopt/dispute) with calibration guards and precedent libraries. Prefer simpler single-agent routers for production coding assistants.

## How it works

Cells claim tasks under permission handles; probation/random/low-trust reviews are rules. Remaining judgments call Jev; low confidence escalates to an LLM whose verdicts become precedents only after outcomes confirm them. Modes include swarm-jev, swarm-rules, swarm-solo, and vote baselines. Optional EvoMap gene publish.

## Get started

```sh
git clone https://github.com/lovstudio/jis.git
cd jis && git checkout d0c693e372075fb3d36f05b52dbf7c52f59bdd2b
pnpm install && cp .env.example .env   # OPENROUTER_API_KEY
pnpm dev   # API :8787 + dashboard :5173
```

## Examples and demos

- README ablation tables and EvoMap gene link (upstream).
- PROTOCOL.md message catalog.

## Limits and data handling

Task text and judgments go to OpenRouter/Jev providers. Secrets stay server-side per README. Accuracy/cost numbers are author benchmarks on synthetic tasks—not catalog claims.

## Review and maintenance

Reviewed **2026-09-23** at [commit d0c693e](https://github.com/lovstudio/jis/tree/d0c693e372075fb3d36f05b52dbf7c52f59bdd2b) (Apache-2.0). AI-assisted source review. No live TypeSafe/OpenRouter spend.

Related: [Intent-Router](intent-router.md), [open-jev-bridge](open-jev-bridge.md).
