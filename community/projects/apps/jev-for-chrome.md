# Jev for Chrome

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that drives the tab you already have open with TypeSafe Jev. Community Manifest V3 port of [Jev Ultrafast](../tools/jev-ultrafast.md): same observation format and action questions, running in your profile instead of a Python CDP harness.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chy4pro/jev-for-chrome) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/chy4pro/jev-for-chrome#jev-for-chrome) |
| Pricing and access | [Load unpacked from source / releases](https://github.com/chy4pro/jev-for-chrome); no app purchase fee. Bring a TypeSafe (or OpenRouter / Cloudflare) key for Jev, plus a separate OpenAI-compatible text-helper key for `TYPE_TEXT`. Reviewed 2026-09-20. |
| Jev evidence | [`src/shared/providers/typesafe.ts`](https://github.com/chy4pro/jev-for-chrome/blob/a509b327798b1e81d6b21b02e3ac2d8d48d44b83/src/shared/providers/typesafe.ts) posts `{model, state, questions}` to TypeSafe System One (default `jev-latest`) for operation + element choice and goal/stuck noul checks. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Community project, not affiliated with TypeSafe or Browser Use. Listing is not an endorsement. Source and offline vitest inspected; Chrome installation and live tab driving were not tested on the review host. Upstream e2e accuracy tables were not independently reproduced. |
| Maintainer | [chy4pro](https://github.com/chy4pro). Independently curated. |
| Format | TypeScript/React Manifest V3 Chrome extension **1.4.4**. |
| Platform and availability | Chromium Developer mode → Load unpacked after `npm run build`, or use release artifacts. Runs in your real Chrome profile/sessions. |
| Jev's role | Selects the next DOM operation and target element; separate small chat model fills typed strings. Application code observes the DOM, validates answers, and executes clicks/types. |
| Requirements | Chromium; TypeSafe or alternate Jev provider key; OpenAI-compatible text helper for typing. |
| License | [MIT](https://github.com/chy4pro/jev-for-chrome/blob/a509b327798b1e81d6b21b02e3ac2d8d48d44b83/LICENSE). |

## When to use

Use it when you want Jev-driven browser steps inside the tab and cookies you already use, including sites that block datacenter automation. Prefer [Jev Ultrafast](../tools/jev-ultrafast.md) for a Python/Browser Harness workflow, or [pi-Jev-browser](../tools/pi-jev-browser.md) inside Pi. Do not grant the extension goals that purchase, delete, or send irreversible actions without watching Step mode.

## How it works

1. The content script indexes interactive elements (role, name, value, href, section) and visible text (capped).
2. The background worker asks Jev for an operation (`CLICK`, `TYPE_TEXT`, `SELECT`, scroll/wait/done/blocked, …) and element; independent goal/stuck noul questions can veto premature DONE/BLOCKED.
3. For `TYPE_TEXT`, a helper LLM produces the exact string; the content script executes only if the page fingerprint is still fresh.

Provider modules under `src/shared/providers/` support TypeSafe, OpenRouter, and Cloudflare Workers AI paths.

## Get started

```sh
git clone https://github.com/chy4pro/jev-for-chrome.git
cd jev-for-chrome
git checkout a509b327798b1e81d6b21b02e3ac2d8d48d44b83
npm ci
npm run build
```

Load the build output as an unpacked extension, set keys in the options/popup, then run a goal. Live runs send page observations to your Jev provider and text-helper and can incur charges.

## Examples and demos

- Upstream README demo GIF/webm and e2e suite notes under `docs/`.
- Offline **`npm test`** (vitest) on the review host: **73 passed** across 6 files. Live extension e2e was not run here.

## Limits and data handling

Page text and element metadata leave the browser for the configured providers. Headless Chromium e2e differs from a normal profile (Cloudflare, rate limits). Strict answer validation stops the run rather than repairing inconsistent distributions. Repeated clicks on the same control can end as BLOCKED.

## Review and maintenance

Reviewed on **2026-09-20** at [commit a509b32](https://github.com/chy4pro/jev-for-chrome/tree/a509b327798b1e81d6b21b02e3ac2d8d48d44b83): **1.4.4**, MIT. AI-assisted source review of TypeSafe provider, README comparison table, and license. **`npm test`**: **73 passed**. No Chrome load and no live provider calls on the review host.

Related: [Jev Ultrafast](../tools/jev-ultrafast.md), [pi-Jev-browser](../tools/pi-jev-browser.md), [TypeSafe Fun AdBlocker](typesafe-adblock.md).
