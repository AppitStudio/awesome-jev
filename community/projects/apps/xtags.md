# Xtags

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension (and optional userscript) that labels each X timeline post with intent and risk signals. Jev answers four typed questions per post; the UI shows an intent tag and thresholded warnings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/manifoldor/xtags) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/manifoldor/xtags#xtags) |
| Pricing and access | [Load unpacked from source](https://github.com/manifoldor/xtags#安装) or import the Tampermonkey userscript; no app purchase fee. Bring a TypeSafe API key. Reviewed 2026-09-20. |
| Jev evidence | [`extension/background.js`](https://github.com/manifoldor/xtags/blob/f1a75251d89071036e818aca95cbb42470b0c57f/extension/background.js) posts to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with choice/noul questions for intent, rage-bait, synthetic, and undisclosed-ad judgments. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. Independent of X Corp. Source inspected; Chrome installation and live timeline labeling were not tested. Labels are probabilistic judgments, not facts. |
| Maintainer | [manifoldor](https://github.com/manifoldor) / author noted as yishan on the extension manifest. Independently curated. |
| Format | Manifest V3 Chrome extension **0.1.0** plus optional userscript. |
| Platform and availability | Chromium Developer mode → Load unpacked (`extension/`). Userscript alternative under `userscript/`. No store listing verified. |
| Jev's role | Classifies each visible post's text into intent (choice) and three noul signals; thresholds and colors are application policy. |
| Requirements | Chromium browser; TypeSafe account and API key. Do not enable extension and userscript together. |
| License | [MIT](https://github.com/manifoldor/xtags/blob/f1a75251d89071036e818aca95cbb42470b0c57f/LICENSE). |

## When to use

Use it for personal, local browsing assistance when you want calibrated intent/risk tags on posts you already see in the browser. Prefer official X tools or manual reading when automation or third-party labeling would violate your jurisdiction or X's terms. Do not treat tags as factual statements about people or events.

## How it works

1. The content script reads rendered post text on `x.com` / `twitter.com` and asks the service worker to judge it.
2. The service worker (required for CORS) calls TypeSafe System One with four questions defined in [`background.js`](https://github.com/manifoldor/xtags/blob/f1a75251d89071036e818aca95cbb42470b0c57f/extension/background.js).
3. Intent always renders; rage-bait / synthetic / undisclosed-ad tags appear only above configured thresholds. Keys live in `chrome.storage.local`.

Host permission is limited to `https://api.typesafe.ai/*` plus the timeline content-script matches.

## Get started

```sh
git clone https://github.com/manifoldor/xtags.git
cd xtags
git checkout f1a75251d89071036e818aca95cbb42470b0c57f
```

In Chrome: `chrome://extensions` → Developer mode → **Load unpacked** → select `extension/`. Open the popup and paste a TypeSafe API key. Live browsing sends post text to TypeSafe and can incur charges.

## Examples and demos

- README documents the four questions and color severity ladder (Chinese UI copy).
- No automated test suite was found in the reviewed revision; behavior was not exercised live.

## Limits and data handling

Post text leaves the browser for TypeSafe. The project is not affiliated with X Corp; upstream README stresses personal local use and compliance responsibility. Classification errors are expected. Pausing the extension changes the toolbar icon state via storage listeners.

## Review and maintenance

Reviewed on **2026-09-20** at [commit f1a7525](https://github.com/manifoldor/xtags/tree/f1a75251d89071036e818aca95cbb42470b0c57f): MIT, extension 0.1.0. AI-assisted source review of `extension/background.js`, `content.js`, `manifest.json`, README, and license. No Chrome load and no live TypeSafe calls.

Related: [Vibe Check for X](vibecheck.md), [TypeSafe Fun AdBlocker](typesafe-adblock.md).
