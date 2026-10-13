# Noa

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension for browser automation in your own logged-in Chrome: Claude Code plans each task and TypeSafe Jev picks what to click and type step by step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m0dE/noa) |
| Tags | `Open source` · `Pricing unverified` · `BYOK` |
| Product homepage | [www.noa.bot](https://www.noa.bot) |
| Pricing and access | Free MIT source with your own Claude plan/key and Jev key; voice and Noa-hosted Jev need a Noa account plan ([pricing](https://www.noa.bot/pricing), not verified here). |
| Jev evidence | [`packages/core/src/jev.ts`](https://github.com/m0dE/noa/blob/e0db8b67bfa5b155928a6c85000f4f5105ef0435/packages/core/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [m0dE](https://github.com/m0dE). Independently curated. |
| Format | Chrome extension + helper (TypeScript) |
| Platform and availability | Chrome extension + local helper |
| Jev's role | Jev carries out single steps (which element to click, what to type) so runs don't wait on a full Claude turn per click; Claude plans and handles the rest. |
| Requirements | Chrome; Claude Code or Claude API key; TypeSafe key (or Noa account credit). |
| License | [MIT](https://github.com/m0dE/noa/blob/e0db8b67bfa5b155928a6c85000f4f5105ef0435/LICENSE) |

## When to use

- Work through a to-do list or scheduled social posts in your own browser session.
- Mismatch: Acts in your logged-in browser; paid features for voice/hosted Jev.

## How it works

Claude Code plans the task; for each step the page state goes to Jev to choose the action and target; scheduled and voice runs are supported. (Summarized from the upstream [README](https://github.com/m0dE/noa/blob/e0db8b67bfa5b155928a6c85000f4f5105ef0435/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the extension and helper per the README, connect Claude Code, and add your Jev key.

## Limits and data handling

Page content goes to TypeSafe (or Noa's hosted Jev) and to Anthropic. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit e0db8b67bfa5](https://github.com/m0dE/noa/tree/e0db8b67bfa5b155928a6c85000f4f5105ef0435). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
