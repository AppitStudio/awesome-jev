# Jev Investment Forecast

[All projects](../README.md) · [Web apps](README.md#web-apps)

A Chrome extension that inspects any displayed web page and uses TypeSafe Jev to forecast investment potential across 27 category judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/serejkaaa512/jev-investment-forecast) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [serejkaaa512/jev-investment-forecast](https://github.com/serejkaaa512/jev-investment-forecast) — the MIT-licensed source repository and project homepage. |
| Pricing and access | Free source build with no app purchase fee; requires a TypeSafe Jev API key for inference. Access terms checked on 2026-01-05. |
| Jev evidence | [`background.js`](https://github.com/serejkaaa512/jev-investment-forecast/blob/main/background.js) — 27 noul detection categories (50% threshold for positive-value, 25% for risk) plus 2 choice questions (investment amount and duration), sent to `https://api.typesafe.ai/v1/systemone` using model `jev-latest`. |
| Disclosure | Copyright holder: `serejkaaa512`. Built from source under MIT license. This review inspected source files only; live Jev calls were not executed. |

## What it does

The extension opens a popup on any page and prompts the user to paste a TypeSafe Jev API key. Once provided, it collects the page's text content, sends 29 typed questions to the Jev API (27 noul categories + 2 choice questions), and displays a percentage card summarising detection results. Results render as a card on top of the page (z-index 10003) and errors self-dismiss in a toast without breaking the page.

## Categories and thresholds

- **Positive-value categories** (15): novelty, scalability, monetizable, authority, feasible, ethical, well-designed, clear, etc. — each flagged when Jev confidence ≥ 50%.
- **Risk categories** (12): fraud, advertising, spam, clickbait, etc. — each flagged when Jev confidence ≥ 25%.
- **Choice questions**: `investment_amount` ($1k / $10k / $100k / $1m) and `investment_duration` (1m / 1y / 3y / 10y).

## Setup

1. Clone or install the Chrome extension from the repository.
2. Open the popup and paste a valid TypeSafe Jev API token into the password-input field.
3. Click "Inspect this page" to trigger a Jev request on the current page's text.
4. View the percentage card with detection results.

## Limitations

- Requires a TypeSafe Jev API key; usage may incur charges depending on the provider.
- Results depend on page text quality; short or non-text pages produce limited input.
- No live Jev execution was performed during review; all claims are based on source inspection.
- The extension does not parse or act on Jev responses beyond rendering the percentage card.