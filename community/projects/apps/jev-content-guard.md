# Jev Content Guard

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

A Manifest V3 Chrome extension that filters fraud, advertising, AI slop, spam, clickbait, "info-gypsy" schemes, and toxicity from web pages using TypeSafe Jev AI content analysis.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/serejkaaa512/jev-content-guard-ext) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project README](https://github.com/serejkaaa512/jev-content-guard-ext) |
| Pricing and access | No app purchase fee; TypeSafe inference costs are separate. No hosted product; source build only. |
| Jev evidence | [background.js](https://github.com/serejkaaa512/jev-content-guard-ext/blob/main/background.js) proxies analysis requests to the TypeSafe API (`https://api.typesafe.ai/v1/systemone`) with model `jev-latest`. Seven typed `noul` questions per text block. |
| Disclosure | Open source (MIT license). No affiliate relationship. Implementation inspected on Linux review host. |
| Maintainer | [serejkaaa512](https://github.com/serejkaaa512) — self-submission, no commercial relationship. |
| Format | Application (browser extension) |
| Platform and availability | Chrome (Chromium Manifest V3); version 1.3. Source-build link: clone the MIT source. |
| Jev's role | Classifies DOM text snippets into 7 categories (fraud, advertising, AI-generated, spam, clickbait, infobusiness, toxicity) with probability scores. Lower threshold flags elements; upper limit triggers hard-mode blur overlay, otherwise soft-mode badge. |
| Requirements | Chrome extension APIs, `chrome.storage.local`, TypeSafe API key (`JEV_API_KEY`). No external JS dependencies beyond Chrome APIs. |
| License | [MIT](https://github.com/serejkaaa512/jev-content-guard-ext/blob/main/LICENSE) |

## When to use

- **Web page scanning**: As you browse any site, the extension automatically analyzes page text (including dynamically added content via `MutationObserver`) and renders badges or blur overlays on flagged elements.
- **Configurable thresholding**: Users can set per-category lower thresholds and upper limits to control badge placement vs. hard-mode blur. Default thresholds: fraud 50%, advertising 20%, AI-generated 25%, spam 25%, clickbait 20%, infobusiness 25%, toxicity 25%.
- **Privacy-friendly**: API key and settings are stored in `chrome.storage.local` — no persistent data leaves the user's machine.

## How it works

The extension runs three Chrome scripts:

1. **Background worker** (`background.js`): Proxies `analyzeContent` requests to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`, sending seven typed `noul` questions per text block.
2. **Content script** (`content.js`): Scans DOM elements (60–4000 chars), debounces requests, queues up to 3 concurrent analysis calls, and renders badges/blur overlays based on Jev response scores.
3. **Settings popup** (`popup.js`): Lets users configure their API key and per-category thresholds/upper limits.

Jev returns calibrated probabilities per category. Text below the lower threshold gets no badge; text between lower and upper threshold gets a dismissible badge; text above the upper limit triggers a blur overlay (hard mode).

## Get started

1. Clone the [MIT source](https://github.com/serejkaaa512/jev-content-guard-ext) (Node.js / npm).
2. Obtain a TypeSafe API key (`JEV_API_KEY`).
3. Build the Chrome extension from source and load it into Chrome.
4. Set your API key via the popup UI (stored in `chrome.storage.local`).
5. Configure thresholds via the popup if desired (defaults are safe for general browsing).
6. Browse any page — the extension scans text automatically.

Expected result: flagged elements display badges or blur overlays. Source build only; no hosted product.

## Examples and demos

No separate hosted demo exists. The extension must be loaded as a Chrome MV3 extension. Source inspected: `background.js`, `content.js`, `popup.js`, `manifest.json` reviewed on the Linux review host. Live Chrome extension loading and analysis not run on the review host.

## Limits and data handling

- Text blocks must be 60–4000 characters to be analyzed.
- Maximum 3 concurrent Jev API requests queued at once.
- 400ms debounce delay to avoid flooding the API.
- Text goes only to TypeSafe Jev; no other system receives page content.
- All state (API key, thresholds) stays in `chrome.storage.local`.
- Provider inference charges apply per analysis call.
- Jev judgments are probabilistic scores, not fact-checks.

## Review and maintenance

Reviewed: 2026-09-22. Upstream commit: version 1.3 of `jev-content-guard-ext`. Source files (`background.js`, `content.js`, `popup.js`, `manifest.json`) inspected on Linux review host. Chrome extension install and live page analysis were not tested.

Related: See other [browser extensions powered by Jev](README.md#browser-extensions).
