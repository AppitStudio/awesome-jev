# TypeSafe Fun AdBlocker

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

An experimental Chrome extension that asks Jev whether heuristically selected page elements are ads, then removes or highlights matches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/realZachi/typesafe-adblock) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/realZachi/typesafe-adblock#typesafe-fun-adblocker-) |
| Pricing and access | [Load unpacked from source](https://github.com/realZachi/typesafe-adblock#install); no app purchase fee. Bring a TypeSafe API key; each batch can incur provider charges. Reviewed 2026-09-19. |
| Jev evidence | [Request construction and noul parsing](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/src/typesafe.js) post one `/v1/systemone` batch (`jev-latest`) with a noul question per candidate. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. Source inspected; Chrome installation and live browsing were not tested. Upstream harness accuracy claims were not independently reproduced. |
| Maintainer | [realZachi](https://github.com/realZachi) (also maintains [pg-jev](../tools/pg-jev.md)). |
| Format | JavaScript Manifest V3 Chrome extension, version 0.1.0 |
| Platform and availability | Source-built Chromium extension (Developer mode → Load unpacked). No store listing verified. Explicitly framed as a fun demo, not a production ad blocker. |
| Jev's role | Judges whether each compact candidate description is a paid/sponsored placement; heuristics find candidates and code removes or outlines matches. |
| Requirements | Chromium browser; TypeSafe account and API key. |
| License | [MIT](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/LICENSE) |

## When to use

Explore it to see a tiny closed-set DOM judgment loop: local candidate finding, one Jev probability per element, then deterministic removal. Do **not** use it as a substitute for uBlock Origin or similar blockers. It costs tokens per page, will miss ads, can remove non-ads, and does not stop tracking, malware, or most video-ad networks.

## How it works

1. The [content script](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/src/content.js) finds ad-shaped candidates (iframes/`ins`, ad-like class/id tokens, labels such as Sponsored/Anzeige, ad-network hosts) and builds compact JSON descriptions.
2. The service worker calls [judgeCandidates](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/src/typesafe.js) → `POST https://api.typesafe.ai/v1/systemone` with model `jev-latest`, one noul question per candidate (default batch cap 30).
3. Elements with probability at or above the popup threshold (default 0.70) are highlighted and/or removed. A MutationObserver and scroll handler catch lazy loads; batches debounce ~600 ms.

Keys live in `chrome.storage.sync` and are sent only to `api.typesafe.ai`. There is no project backend.

## Get started

```sh
git clone https://github.com/realZachi/typesafe-adblock.git
cd typesafe-adblock
git checkout 7e067d243d87b7fe4d511653c0ddcd77b9beee18
```

In Chrome: `chrome://extensions` → Developer mode → **Load unpacked** → select the repo folder. Open the popup, paste a TypeSafe API key, and use **Test**. Browsing eligible pages sends candidate descriptions to TypeSafe and can incur charges. Prefer highlight-only mode while evaluating false positives.

## Examples and demos

- [Offline harness](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/test/harness.html) and [fixture page](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/test/fixture.html): local static server plus optional relay; without a key the harness falls back to a heuristic.
- Author-reported live checks in the README (2026-09-17) were **not** re-run for this listing.

## Limits and data handling

Each batch sends hostname, title, and compact candidate fields (bounded text, hosts, shape hints)—not the full page HTML. Cross-origin iframe interiors are invisible; whole iframes may still be removed. Heuristics miss unlabeled ads. Sites that detect missing ad slots may break. Default remove mode is destructive to the live DOM (highlight-only is available). Provider retries cover some 429/5xx responses; permanent auth errors surface to the user.

## Review and maintenance

Reviewed **2026-09-19** at [`7e067d2`](https://github.com/realZachi/typesafe-adblock/tree/7e067d243d87b7fe4d511653c0ddcd77b9beee18). Inspected README, MIT license, manifest permissions, TypeSafe client, content/background/popup scripts, and test harness files. Offline Node smoke confirmed `buildRequest`/`parseResponse` shape. No Chrome installation, live provider request, or accuracy evaluation was performed.

Related: [Unclutter](unclutter.md) classifies broader page clutter into reusable local hide rules rather than focusing on ad removal.
