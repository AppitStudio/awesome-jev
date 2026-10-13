# voice-browser

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS command bar that drives Chromium, Dia, Arc or Chrome from plain English; TypeSafe Jev (or SubQ Snap) picks clicks and targets for fast single actions and goal chains.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ken-code-wq/voice-browser) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/ken-code-wq/voice-browser#readme](https://github.com/ken-code-wq/voice-browser#readme) |
| Pricing and access | Free MIT source; decisions use your TypeSafe or SubQ key. Checked 2026-10-13. |
| Jev evidence | [`src/jev.js`](https://github.com/ken-code-wq/voice-browser/blob/e391d986c0cd2ab6f519472390807a2063013ad9/src/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [ken-code-wq](https://github.com/ken-code-wq). Independently curated. |
| Format | macOS app / CLI (JavaScript) |
| Platform and availability | macOS; Chromium, Dia, Arc, or Chrome |
| Jev's role | Jev (or SubQ Snap) picks intent and UI targets; automation executes clicks, forms, and goals. |
| Requirements | macOS; TypeSafe or SubQ key per README. |
| License | [MIT](https://github.com/ken-code-wq/voice-browser/blob/e391d986c0cd2ab6f519472390807a2063013ad9/LICENSE) |

## When to use

- Drive a real browser by voice or short typed commands without hand-writing selectors.
- Mismatch: Decision path can use SubQ Snap instead of hosted TypeSafe Jev.

## How it works

Commands go through a decision model that selects among candidate actions, then Playwright-style automation runs them. (Summarized from the upstream [README](https://github.com/ken-code-wq/voice-browser/blob/e391d986c0cd2ab6f519472390807a2063013ad9/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install deps, set your decision-model key, and launch the command bar against a supported browser.

## Limits and data handling

Command text and page context may go to TypeSafe or SubQ. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit e391d986c0cd](https://github.com/ken-code-wq/voice-browser/tree/e391d986c0cd2ab6f519472390807a2063013ad9). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
