# pi-jev-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Minimal Pareto-oriented OpenRouter model router for the [pi](https://github.com/badlogic/pi-mono) coding agent: TypeSafe Jev classifies each task; local policy selects a role/model tier (shadow mode by default). Distinct from [jev-router](jev-router.md) (Claude Code/Codex proxies) and other pi gate/sentinel extensions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/philippdubach/pi-jev-router) |
| Maintainer | [philippdubach](https://github.com/philippdubach). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension **pi-jev-router 0.1.0** (`extensions/router.ts`; `@typesafe-ai/sdk`). |
| Requirements | Node.js with `--experimental-strip-types` for tests; Pi coding agent and peer packages. Classifier uses `OPENROUTER_API_KEY` or `~/.pi/agent/auth.json`. |
| License | [MIT](https://github.com/philippdubach/pi-jev-router/blob/00c45605230a571b4583a2396a8604386cf78ac3/LICENSE). OpenRouter and model usage have separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline unit tests inspected; live OpenRouter/Jev routing and eval benchmarks were not run. |

## When to use

Use it when you want **per-task model/role switching inside pi** (planning / code / writing profiles, optional budget) with Jev classification and deterministic selection. Prefer [pi-jev](pi-jev.md) for pre-tool gates and output judges; prefer [jev-router](jev-router.md) for Claude Code/Codex proxy routing.

## How it works

[`src/classifier.ts`](https://github.com/philippdubach/pi-jev-router/blob/00c45605230a571b4583a2396a8604386cf78ac3/src/classifier.ts) builds Choice/Score questions and calls TypeSafe via OpenRouter’s System One endpoint (`TypeSafeClient`, `maxRetries: 0`). [`src/selector.ts`](https://github.com/philippdubach/pi-jev-router/blob/00c45605230a571b4583a2396a8604386cf78ac3/src/selector.ts) applies local policy with no model calls. [`extensions/router.ts`](https://github.com/philippdubach/pi-jev-router/blob/00c45605230a571b4583a2396a8604386cf78ac3/extensions/router.ts) registers pi hooks and `/router` commands (`shadow` default, `auto`, profiles, budget).

## Get started

```sh
git clone https://github.com/philippdubach/pi-jev-router.git
cd pi-jev-router
git checkout 00c45605230a571b4583a2396a8604386cf78ac3
npm ci --ignore-scripts
npm test
# Link as a Pi extension per upstream README; set OPENROUTER_API_KEY or reuse Pi auth.
```

Live routing sends task context to OpenRouter/Jev and can incur charges; this listing ran offline tests only. Upstream cost/pass percentages were not independently measured.

## Examples and demos

- Offline `npm test` — selector, role-routing, and worktree tests **passed** on the review host.
- Upstream `eval/` benchmark runner (`npm run bench`) — not executed here.

## Limits and data handling

Task envelopes leave the host on live classification. Shadow mode recommends without switching until `/router auto`. Worktree workers merge only when `verifierCommand` exits 0. Not a general multi-CLI gateway.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 00c4560](https://github.com/philippdubach/pi-jev-router/tree/00c45605230a571b4583a2396a8604386cf78ac3): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `package.json`, `src/classifier.ts`, `src/selector.ts`, and `extensions/router.ts`. Ran `npm ci --ignore-scripts` and `npm test` (all pass). No live OpenRouter calls.

Related: [pi-jev](pi-jev.md), [pi-jev-sentinel](pi-jev-sentinel.md), [jev-router](jev-router.md), [Distill](distill.md).
