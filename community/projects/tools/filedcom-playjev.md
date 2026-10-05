# PlayJev (filed)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

"Stagehand, but with Jev": natural-language Playwright automation where TypeSafe Jev selects real browser nodes (`check`, `choose`, `rate`, `act`) and deterministic code performs actions; distinct from the listed OmniJev/PlayJev game player.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/filedcom/playjev) |
| Maintainer | [filedcom](https://github.com/filedcom). Independently curated. |
| Format | Node library wrapping a Playwright page (Chromium/CDP) |
| Requirements | Node.js 20+, Playwright with Chromium, and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/filedcom/playjev/blob/1aa875817c030b7287fa748b561cbc2000cd5ad0/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Write resilient e2e steps in plain language without generated selectors or JavaScript.
- Verify page state with a typed Jev `check()` in CI smoke tests.
- Mismatch: stable pages with known selectors are faster with plain Playwright.

## How it works

PlayJev captures accessibility and frame nodes into sparse numbered YAML (no raw HTML, no internal selectors) and asks Jev Score/Choice/Noul questions; Jev picks a node and operation from a fixed vocabulary, and Playwright executes fills/clicks with caller-supplied values ([README](https://github.com/filedcom/playjev/blob/1aa875817c030b7287fa748b561cbc2000cd5ad0/README.md)).

## Get started

Install with Playwright and run a step (live Jev calls):

```sh
npm install @filed/playjev playwright
npx playwright install chromium
export TYPESAFE_API_KEY=...
# const page = playjev(await browser.newPage());
# await page.act("Open the documentation link");
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README reports a 4/4 WebVoyager golden smoke run (maintainer-reported integration gate).

## Limits and data handling

Experimental, API evolving; Chromium/CDP only. Page structure (not caller values) is sent to TypeSafe and billed.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 1aa875817c03](https://github.com/filedcom/playjev/tree/1aa875817c030b7287fa748b561cbc2000cd5ad0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
