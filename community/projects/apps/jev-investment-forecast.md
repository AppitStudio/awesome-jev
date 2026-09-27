# Jev Investment Forecast

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that inspects the current page and uses TypeSafe Jev to forecast investment potential across 27 category judgments plus amount/duration choices.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/serejkaaa512/jev-investment-forecast) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/serejkaaa512/jev-investment-forecast#readme) |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-27**. Live inspection needs a TypeSafe Jev API key; usage separate. Optional Chrome Web Store listing linked from the catalog README. |
| Jev evidence | [`background.js`](https://github.com/serejkaaa512/jev-investment-forecast/blob/1bf8b1f9d408c1e4b9654e5545611fb9218aee14/background.js) posts typed questions to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` (27 noul categories + 2 choice questions). Pin the reviewed commit below for the live blob. |
| Disclosure | Copyright holder: `serejkaaa512`. Community submission (PR #638). AI-assisted maintainer review of the listing; source inspected; live Jev calls were not executed. Listing is not an endorsement. |
| Maintainer | [serejkaaa512](https://github.com/serejkaaa512). Upstream author submission. |
| Format | Chrome Manifest V3 extension. |
| Platform and availability | Chromium extension (load unpacked or Chrome Web Store). Early public release. |
| Jev's role | Scores page text across positive-value and risk categories and chooses investment amount/duration labels; the extension only renders results. |
| Requirements | Chromium browser; TypeSafe Jev API key in the popup. |
| License | [MIT](https://github.com/serejkaaa512/jev-investment-forecast/blob/1bf8b1f9d408c1e4b9654e5545611fb9218aee14/LICENSE). |

## When to use

Use when you want a quick, BYOK page-level investment-signal readout driven by typed Jev questions. Prefer dedicated research tools for financial advice; this listing is a demo workflow, not investment advice.

## How it works

The popup stores a TypeSafe key, collects page text, and sends 29 typed questions (27 noul detection categories with 50%/25% thresholds plus `investment_amount` and `investment_duration` choices) to System One. Results render as an overlay card; errors self-dismiss without breaking the page.

## Get started

```sh
git clone https://github.com/serejkaaa512/jev-investment-forecast.git
cd jev-investment-forecast
git checkout 1bf8b1f9d408c1e4b9654e5545611fb9218aee14
# Load the folder as an unpacked Chrome extension; paste a TypeSafe key in the popup
```

Pin revision `1bf8b1f9d408c1e4b9654e5545611fb9218aee14` when reproducing this review (full SHA in Review).

## Examples and demos

No separate offline demo. Upstream README documents the inspect-page flow. Live Jev calls were not run on the review host.

## Limits and data handling

Page text is sent to TypeSafe's hosted API. Results depend on page text quality. Not financial advice. Live calls not executed during review.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 1bf8b1f9d408c1e4b9654e5545611fb9218aee14](https://github.com/serejkaaa512/jev-investment-forecast/tree/1bf8b1f9d408c1e4b9654e5545611fb9218aee14). AI-assisted inspection of README, LICENSE, and community PR #638; Chrome install and live TypeSafe calls not run.
