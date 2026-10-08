# QuickE2E

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plain-English end-to-end testing library for web apps: you write a goal and inputs, a small decision model picks each browser step — hosted Jev (`typesafe/jev-1.13` via OpenRouter, the default) or a local Shisa DE-1 engine — Playwright acts, and an explicit check (e.g. one SQL query) verifies the result; specs can be turned into generated Playwright code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dmoka/quicke2e) |
| Maintainer | [dmoka](https://github.com/dmoka). Independently curated. |
| Format | npm library/CLI used with `@playwright/test` (`quicke2e.spec.mjs` specs) |
| Requirements | Node + Playwright Chromium; `OPENROUTER_API_KEY` for the default `jev` engine, or the `local` engine with no key. |
| License | [MIT](https://github.com/dmoka/quicke2e/blob/98f74b6ceb44e8eb68c0bc176e522983639b9521/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Smoke-test critical flows (checkout, signup) described in English rather than selectors.
- Compare a hosted Jev engine with a fully local engine on the same specs.
- Mismatch: goals still need a deterministic final check; unchecked steps can pass weakly (the README flags `WEAK_ASSERTION`).

## How it works

A one-time discover pass maps the app; each step sends the page's interactive elements and the goal to the decision engine, which picks the next action; verification uses the spec's own check. Benchmarks in the README compare wall time and cost against Claude Code + Playwright MCP on the TicketBay demo (author-reported).

## Get started

Install next to Playwright (README *Quick start*):

```sh
npm i -D quicke2e @playwright/test
npx playwright install chromium
export OPENROUTER_API_KEY=...   # default jev engine
```

The `jev` engine bills OpenRouter per step; the `local` engine has no API cost.

## Examples and demos

- npm package: [`quicke2e`](https://www.npmjs.com/package/quicke2e) (0.5.0).
- README *Benchmarks* (hosted Jev 5/5 in 3.74 s at $0.00038 vs Claude Code 25.29 s — author-reported).

## Limits and data handling

Page element text and goal inputs go to OpenRouter with the `jev` engine; README documents secret redaction. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 98f74b6ceb44](https://github.com/dmoka/quicke2e/tree/98f74b6ceb44e8eb68c0bc176e522983639b9521). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
