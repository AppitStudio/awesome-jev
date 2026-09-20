# Tab Bouncer

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that rates open tabs for how useful they are for a task you type, then lets you close the ones that do not belong. Distinct from [Jev for Chrome](jev-for-chrome.md), which drives in-tab computer-use actions rather than bulk tab triage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MANISH007700/tab-bouncer) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/MANISH007700/tab-bouncer#tab-bouncer) |
| Pricing and access | [Load unpacked from source](https://github.com/MANISH007700/tab-bouncer#install); no app purchase fee. Bring a TypeSafe API key. Inference usage can incur charges. Reviewed 2026-09-20. |
| Jev evidence | [`judge.js`](https://github.com/MANISH007700/tab-bouncer/blob/7798c758bd32d2f739e2391e2b0d436de42d1a85/judge.js) posts `{model, state, questions}` to `https://api.typesafe.ai/v1/systemone` with `jev-latest`: one noul “keep” and one kind choice per tab, in batches of up to 120. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Community project, not affiliated with TypeSafe. Listing is not an endorsement. Source and offline `node --test` inspected; Chrome installation and live TypeSafe calls were not tested on the review host. Upstream latency/cost anecdotes were not independently reproduced. |
| Maintainer | [MANISH007700](https://github.com/MANISH007700). Independently curated. |
| Format | Manifest V3 Chromium extension **0.1.0** (plain JS; no build step). |
| Platform and availability | Chrome, Edge, Brave, Arc: Developer mode → Load unpacked on the repo folder. Shortcut ⌘⇧B / Ctrl+Shift+B. |
| Jev's role | Judges whether each open tab is useful for the stated task (noul) and assigns a kind (on task / reference / rabbit hole / shopping / social). Extension code applies VIP safe-tab rules, a strictness threshold, closes selected tabs, and can reopen the last batch. |
| Requirements | Chromium; TypeSafe API key in extension options. |
| License | [MIT](https://github.com/MANISH007700/tab-bouncer/blob/7798c758bd32d2f739e2391e2b0d436de42d1a85/LICENSE). |

## When to use

Use it when you want a one-shot triage of many open tabs against a short description of what you are doing, with review before close and a reopen path. Prefer [Jev for Chrome](jev-for-chrome.md) when you need Jev to drive clicks and typing inside a page. Do not treat kind labels or keep scores as audited productivity metrics.

## How it works

1. You type what you are working on (current window or all windows).
2. `judge.js` batches tabs (up to 120 per request) and asks Jev two questions per tab against shared state `{ what_the_user_is_doing_right_now, open_tabs[] }`.
3. `planBounce` keeps pinned, audible, and active tabs regardless of score; other tabs below the strictness slider are proposed for close.
4. You confirm closes; the popup can reopen the last closed batch and copy a summary line.

Host permission is limited to `https://api.typesafe.ai/*`. Titles and URLs leave the browser only when you press **Check my tabs**.

## Get started

```sh
git clone https://github.com/MANISH007700/tab-bouncer.git
cd tab-bouncer
git checkout 7798c758bd32d2f739e2391e2b0d436de42d1a85
```

Load the folder unpacked at `chrome://extensions` (Developer mode), paste a TypeSafe key in Extension options, then open the popup. Live runs send tab titles and URLs to TypeSafe and can incur charges.

## Examples and demos

- Upstream README screenshots under `docs/` show ask, results, keep/close lists, reopen, and settings.
- Offline **`node --test tests/judge.test.mjs`** on the review host: **7 passed**. Covers request shape, batching, mocked fetch pricing, VIP rules, and summary text. No live provider calls.

## Limits and data handling

Tab titles and URLs go to `api.typesafe.ai` with your key; the key stays in extension local storage. Browser pages such as `chrome://` are not closed. Keep-score defaults and kind fallbacks apply when answers are missing. Latency and cost figures in the upstream README and share text are vendor/author claims for live runs; they were not measured on the review host.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 7798c75](https://github.com/MANISH007700/tab-bouncer/tree/7798c758bd32d2f739e2391e2b0d436de42d1a85): **0.1.0**, MIT. AI-assisted source review of `judge.js`, `manifest.json`, README, LICENSE, and tests. **`node --test`**: **7 passed**. No Chrome load and no live TypeSafe calls on the review host.

Related: [Jev for Chrome](jev-for-chrome.md), [TypeSafe Fun AdBlocker](typesafe-adblock.md), [Unclutter](unclutter.md).
