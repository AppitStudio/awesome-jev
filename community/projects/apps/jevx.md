# jevx

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome and Firefox extension that finds relevant X (Twitter) posts for your interests and optionally scores unpublished drafts with TypeSafe Jev. BYOK, no backend: local storage holds profile and key; consented post/draft text goes only to TypeSafe. Distinct from [Focus](focus.md) (productivity domain blocking) and [Tab Bouncer](tab-bouncer.md) (open-tab triage).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hawkyre/jevx) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/hawkyre/jevx#jevx) |
| Pricing and access | [Build and load unpacked](https://github.com/hawkyre/jevx#install) (Chrome MV3 / Firefox temporary). No app purchase fee. Bring your own TypeSafe API key. TypeSafe usage can incur charges. Reviewed 2026-09-21. |
| Jev evidence | [`lib/jev.ts`](https://github.com/hawkyre/jevx/blob/50c311181da592983d6ca1a922c6ea6441f56dbe/lib/jev.ts) and [`lib/draft-jev.ts`](https://github.com/hawkyre/jevx/blob/50c311181da592983d6ca1a922c6ea6441f56dbe/lib/draft-jev.ts) `fetch` `https://api.typesafe.ai/v1/systemone` for feed relevance and draft-axis Score/Noul judgments. Host permission includes `https://api.typesafe.ai/*`. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Community project, not affiliated with TypeSafe or X. Listing is not an endorsement. Source and offline vitest inspected; browser install and live TypeSafe/X sessions were not tested on the review host. |
| Maintainer | [hawkyre](https://github.com/hawkyre). Independently curated. |
| Format | TypeScript WXT Manifest V3 extension **0.1.0** (Chrome + Firefox builds). |
| Platform and availability | Chrome/Chromium load unpacked (`.output/chrome-mv3`); Firefox temporary add-on (`.output/firefox-mv3`). Not assumed listed on stores. |
| Jev's role | Scores loaded X posts for relevance/recency (weighted 1–5) and optionally assesses unpublished drafts against editable axes. Extension code owns filtering UI, caches, tab search helpers, and consent gates. |
| Requirements | Chromium or Firefox; Node 24.x to build from source; TypeSafe API key for assessment. |
| License | [MIT](https://github.com/hawkyre/jevx/blob/50c311181da592983d6ca1a922c6ea6441f56dbe/LICENSE). |

## When to use

Use it when you want an on-device filter and draft coach for X timelines using your own TypeSafe key, without giving a third-party backend your feed. Prefer [Focus](focus.md) for blocking distracting *sites*; prefer [Polymorph](polymorph.md) for rule-based post collapse with OpenRouter Decisions.

## How it works

1. You set interests/profile and enable assessment; the key stays in extension-origin IndexedDB.
2. Feed filtering asks Jev for visibility/reason/relevance over eligible post text (replies bypass; empty bodies stay visible unscored).
3. Optional draft scoring waits after typing stops and batches enabled axes; results for stale text are ignored.
4. Concurrent request pool (default 20) and session caches reduce duplicate calls; weight edits can recompute without new judgments.

## Get started

```sh
git clone https://github.com/hawkyre/jevx.git
cd jevx
git checkout 50c311181da592983d6ca1a922c6ea6441f56dbe
npm ci
npx wxt prepare
npm test
npm run build
# Load .output/chrome-mv3 unpacked; enter a TypeSafe key in Settings.
# Live assessments send consented post/draft text to TypeSafe and incur charges.
```

## Examples and demos

- Upstream README screenshots and `/tools/preview.html` synthetic draft preview.
- Review host: after `wxt prepare`, **`npm test`**: **87 passed** across 8 files. Browser load and live calls not run.

## Limits and data handling

With consent, eligible post/author/profile text and draft text go to `api.typesafe.ai`. The key never enters X page scripts. Notifications and DM pages are excluded from filtering. Relevance and draft scores are product judgments, not validated virality predictions. Concurrent-request limits are product settings, not TypeSafe account guarantees.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 50c3111](https://github.com/hawkyre/jevx/tree/50c311181da592983d6ca1a922c6ea6441f56dbe): **0.1.0**, MIT. AI-assisted source review of README, `lib/jev.ts`, `lib/draft-jev.ts`, `wxt.config.ts`, and LICENSE. Offline vitest: **87 passed**. No Chrome/Firefox load and no live TypeSafe calls.

Related: [Focus](focus.md), [Tab Bouncer](tab-bouncer.md), [Polymorph](polymorph.md).
