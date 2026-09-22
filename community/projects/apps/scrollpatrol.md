# ScrollPatrol

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that mutes feed posts by meaning: TypeSafe Jev scores each post against your mute rules and hides matches on LinkedIn, Reddit, Hacker News, and selected short-video surfaces.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ennsharma/scrollpatrol) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/ennsharma/scrollpatrol#readme) — load-unpacked Manifest V3 extension; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Bring a TypeSafe API key. Optional deeper visual sampling may use additional providers per upstream docs. TypeSafe usage can incur charges; upstream documents a daily budget setting. |
| Jev evidence | Inspected [`src/background.ts`](https://github.com/ennsharma/scrollpatrol/blob/eed8caeb3d946210415012691020b69daec21ab0/src/background.ts) and [`src/core.ts`](https://github.com/ennsharma/scrollpatrol/blob/eed8caeb3d946210415012691020b69daec21ab0/src/core.ts): posts Noul questions per mute rule to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`; content scripts collapse matched posts. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source inspected; Chrome install and live TypeSafe calls not run on the review host. |
| Maintainer | [ennsharma](https://github.com/ennsharma). Independently curated. |
| Format | Manifest V3 TypeScript extension **0.1.0** (`scrollpatrol`); build via `npm run build`. |
| Platform and availability | Chromium load-unpacked from built `dist/`. Not verified on extension stores in this review. |
| Jev's role | Answers whether each post matches each mute rule (Noul). Extension code owns site adapters, thresholds, budgets, UI, optional transcript/visual enrichment, and collapsing/restoring posts. |
| Requirements | Chromium; TypeSafe API key in extension storage; Node for building from source. |
| License | [MIT](https://github.com/ennsharma/scrollpatrol/blob/eed8caeb3d946210415012691020b69daec21ab0/LICENSE). |

## When to use

Use it when you want **semantic mute rules on social feeds** rather than keyword filters. Prefer [Focus](focus.md) for domain-level distraction blocking, or [Tab Bouncer](tab-bouncer.md) for one-shot tab triage. Do not treat mute matches as content-moderation ground truth.

## How it works

Content scripts extract post text/metadata per site. The background worker batches Noul questions to System One; posts above the configured probability threshold are hidden (short videos can be covered/paused). Settings and a daily spend budget live in extension storage.

## Get started

```sh
git clone https://github.com/ennsharma/scrollpatrol.git
cd scrollpatrol
git checkout eed8caeb3d946210415012691020b69daec21ab0
npm ci --ignore-scripts
npm run build
npm test
# Load the unpacked dist/ folder in chrome://extensions
```

Live judgments send post text (and optional enrichment) to TypeSafe and may incur charges. This listing did not load the extension in a browser or call TypeSafe.

## Examples and demos

- Offline on the review host: `npm run build` then `npm test` → **40 passed**.
- Upstream README site matrix (LinkedIn, Reddit, HN, Shorts/Reels/TikTok beta).

## Limits and data handling

Feed text and optional transcript/frame summaries leave the host on live judgments. Upstream notes incomplete subtitle/frame coverage for short video. Failures should leave posts visible (inspect upstream for exact fail-open behavior).

## Review and maintenance

Reviewed on **2026-09-22** at [commit eed8cae](https://github.com/ennsharma/scrollpatrol/tree/eed8caeb3d946210415012691020b69daec21ab0): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/core.ts`, `src/background.ts`. Offline vitest 40 passed after build. No Chrome install or live TypeSafe on the review host.

Related: [Focus](focus.md), [Tab Bouncer](tab-bouncer.md), [HookMeter](hookmeter.md).
