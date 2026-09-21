# Jev demos

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local Node demo suite with six side-by-side TypeSafe Jev workflows (router, ticket triage, inbox at scale, slop filter, title scorer, cost calculator). Claude and Kimi are interchangeable LLMs for the text side; Jev makes the typed decisions. Runs in clearly badged **simulated** mode without API keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mayank953/Jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/mayank953/Jev#jev-demos) |
| Pricing and access | [Clone and `npm start`](https://github.com/mayank953/Jev#quickstart). No app purchase fee. Optional `TYPESAFE_API_KEY`, `ANTHROPIC_API_KEY`, `MOONSHOT_API_KEY`. Default process spend cap `DEMO_BUDGET_USD` ($0.50) for paid LLM calls; Jev usage is separate. Reviewed 2026-09-21. |
| Jev evidence | [`src/jev.ts`](https://github.com/mayank953/Jev/blob/ff0c79122e6eee64e8e0dfc428120de4fdcfce37/src/jev.ts) uses `@typesafe-ai/sdk` against TypeSafe System One for the demo judgments. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Community project, not affiliated with TypeSafe, Anthropic, or Moonshot. Listing is not an endorsement. Source and `npm run typecheck` inspected; browser UI and live provider calls were not exercised on the review host. |
| Maintainer | [mayank953](https://github.com/mayank953) (Mayank Aggarwal). Independently curated. |
| Format | Local web app **jev-demos 0.1.0** (Node ≥ 22.6; TypeScript via Node native strip-types; no separate build step). |
| Platform and availability | localhost:3000 after `npm start`. No hosted production URL claimed in this listing. |
| Jev's role | Supplies typed routing, triage, feed-label, and title-scoring judgments. Claude/Kimi write prose or provide comparison baselines. App code owns UI, budgets, and simulated fallbacks. |
| Requirements | Node 22.6+; optional TypeSafe / Anthropic / Moonshot keys. |
| License | [MIT](https://github.com/mayank953/Jev/blob/ff0c79122e6eee64e8e0dfc428120de4fdcfce37/LICENSE). |

## When to use

Use it to explore several Jev + LLM patterns in one UI, including head-to-head cost/latency races and simulated mode for demos without keys. Prefer production tools (for example [toolgate](../tools/toolgate.md) or [daf-jev](../tools/daf-jev.md)) when you need a library rather than a teaching app.

## How it works

Each tab builds state and typed questions, calls Jev (or a simulated stub), and may call Claude/Kimi for text. Missing keys or budget exhaustion switch that lane to badged simulated output without inventing baseline “wins.” Configured list prices live in `src/config.ts` (author-maintained; re-check before quoting).

## Get started

```sh
git clone https://github.com/mayank953/Jev.git
cd Jev
git checkout ff0c79122e6eee64e8e0dfc428120de4fdcfce37
npm ci --ignore-scripts
npm run typecheck
cp .env.example .env   # optional keys
npm start
# Open http://localhost:3000
# Live demos send state/text to TypeSafe and optional LLM providers and can incur charges.
```

## Examples and demos

- Six in-app tabs documented in the upstream README.
- Screenshot under `docs/screenshot.png`.
- Review host: **`npm run typecheck`** passed. Server UI and live calls not run.

## Limits and data handling

With keys set, demo state and sample content go to TypeSafe and/or Anthropic/Moonshot. Session LLM spend is capped by `DEMO_BUDGET_USD`; Jev is not blocked by that cap per upstream. Router benchmarks measure speed/cost, not answer quality. This listing did not validate upstream marketing latency or price figures.

## Review and maintenance

Reviewed on **2026-09-21** at [commit ff0c791](https://github.com/mayank953/Jev/tree/ff0c79122e6eee64e8e0dfc428120de4fdcfce37): **0.1.0**, MIT. AI-assisted source review of README, `src/jev.ts`, `src/config.ts`, and LICENSE. Offline: `npm run typecheck` OK. No live TypeSafe/LLM calls.

Related: [Watermelon](watermelon.md), [JevSlop](jevslop.md), [daf-jev](../tools/daf-jev.md).
