# Jev Focus Guard

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome Manifest V3 extension that asks TypeSafe Jev whether page elements are ads or distractions, then hides them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tx-smitht/jev-focus-guard) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/tx-smitht/jev-focus-guard#readme) |
| Pricing and access | Load unpacked from MIT source; no app purchase fee. Bring a TypeSafe API key; judgments can incur charges. Checked **2026-09-26**. |
| Jev evidence | [`background.js`](https://github.com/tx-smitht/jev-focus-guard/blob/449f01e322da6e767bfd550fd90b29a2bb020172/background.js) posts Choice disposition questions with compact candidate metadata (hostname, tokens, geometry—not page text) to TypeSafe System One. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live install/provider paths not run on the review host. Distinct from Focus and TypeSafe Fun AdBlocker. |
| Maintainer | [tx-smitht](https://github.com/tx-smitht). Independently curated. |
| Format | JavaScript Manifest V3 Chrome extension. |
| Platform and availability | Source-built Chromium extension (Developer mode → Load unpacked). No store listing verified. |
| Jev's role | Classifies each candidate as remove_ad / remove_distraction / keep (Choice); content script applies hide. |
| Requirements | Chromium browser; TypeSafe API key. |
| License | [MIT](https://github.com/tx-smitht/jev-focus-guard/blob/449f01e322da6e767bfd550fd90b29a2bb020172/LICENSE). |

## When to use

Explore Jev-driven **DOM triage** for ads/distractions without sending page body text. Do not treat it as a network ad blocker. Distinct from [Focus](focus.md) and [TypeSafe Fun AdBlocker](typesafe-adblock.md).

## How it works

[`content.js`](https://github.com/tx-smitht/jev-focus-guard/blob/449f01e322da6e767bfd550fd90b29a2bb020172/content.js) finds candidates; the service worker calls Jev; matching elements are hidden. Per-page caps and 429 pause are documented upstream.

## Get started

```sh
git clone https://github.com/tx-smitht/jev-focus-guard.git
cd jev-focus-guard
git checkout 449f01e322da6e767bfd550fd90b29a2bb020172
# Chrome → Extensions → Developer mode → Load unpacked → this folder
# Paste TypeSafe API key in extension options
```

## Examples and demos

- Upstream README documents state payload shape, undo/allow-site, and privacy notes.
- No separate hosted demo.

## Limits and data handling

Candidate metadata goes to TypeSafe. Page text/cookies/full URLs excluded per upstream. Elements may flash before hide. AI decisions can be wrong—use undo/allow-site.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 449f01e](https://github.com/tx-smitht/jev-focus-guard/tree/449f01e322da6e767bfd550fd90b29a2bb020172). AI-assisted source inspection; live paths not executed.
