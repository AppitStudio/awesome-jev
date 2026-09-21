# Focus

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Browser extension that classifies domains as productive or distracting with TypeSafe Jev (via OpenRouter Decisions) and blocks distracting navigations behind a local allow/block list and cache.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bramtechs/Focus) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [Project homepage](https://github.com/bramtechs/Focus#readme) |
| Pricing and access | Load unpacked from GPL-3.0 source (Chrome/Edge/Brave, Firefox temporary, Safari packaging script). No app purchase fee. Bring an OpenRouter API key (`typesafe/jev-1.13` by default). OpenRouter/TypeSafe usage can incur charges. Checked 2026-09-21. |
| Jev evidence | [`background.js`](https://github.com/bramtechs/Focus/blob/412740c5dc0e689df037106ee3d3442d01ac9890/background.js) posts Choice `site_category` (productive/distracting) to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; browser install and live OpenRouter/TypeSafe calls were not run on the review host. |
| Maintainer | [bramtechs](https://github.com/bramtechs). Independently curated. |
| Format | Manifest V3 extension **1.0.0** (plain JS; shared Chrome/Firefox/Safari assets). |
| Platform and availability | Chromium load-unpacked; Firefox temporary add-on; Safari via `scripts/package-safari.sh`. Not listed on extension stores in the reviewed tree. |
| Jev's role | Judges whether the navigated domain is productive or distracting; extension code applies threshold, cache (7 days), allow/block overrides, and redirects to `blocked.html`. Offline heuristic list applies when no key is set. |
| Requirements | Chromium/Firefox/Safari; `OPENROUTER_API_KEY` in extension options for live judgments. |
| License | [GPL-3.0](https://github.com/bramtechs/Focus/blob/412740c5dc0e689df037106ee3d3442d01ac9890/LICENSE). |

## When to use

Use it when you want navigation-time distraction blocking with calibrated Jev probabilities and local overrides. Prefer [Tab Bouncer](tab-bouncer.md) for one-shot triage of already-open tabs against a typed task. Do not treat productive/distracting labels as audited productivity metrics.

## How it works

On top-frame navigation, the service worker checks allow/block lists and a fresh cache, then asks Jev via OpenRouter Decisions whether the domain is `productive` or `distracting`. If `P(distracting)` meets the threshold (default 0.6), the tab redirects to the blocked interstitial showing probability and confidence. Failures and missing keys fall back to a small offline heuristic list.

## Get started

```sh
git clone https://github.com/bramtechs/Focus.git
cd Focus
git checkout 412740c5dc0e689df037106ee3d3442d01ac9890
```

Load the folder unpacked at `chrome://extensions` (Developer mode), open Settings, paste an OpenRouter key, save, and browse. Live runs send domain/URL/title context to OpenRouter (TypeSafe Jev) and can incur charges.

## Examples and demos

- Upstream README documents Chrome, Firefox, and Safari install paths and the Decisions request shape.
- Review host: `node --check background.js` succeeded. No packaged automated test suite was found.

## Limits and data handling

Domain, full URL, page title, and user-goal text go to OpenRouter on live judgments; the key stays in extension storage. Host permission includes `<all_urls>` plus `https://openrouter.ai/*`. Classification is policy + model output, not a guarantee of focus. Confirm OpenRouter account terms and model availability separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 412740c](https://github.com/bramtechs/Focus/tree/412740c5dc0e689df037106ee3d3442d01ac9890): **1.0.0**, GPL-3.0. AI-assisted source review of README, `background.js`, `manifest.json`, and LICENSE. Syntax check only; no Chrome load and no live provider calls.

Related: [Tab Bouncer](tab-bouncer.md), [TypeSafe Fun AdBlocker](typesafe-adblock.md), [Unclutter](unclutter.md).
