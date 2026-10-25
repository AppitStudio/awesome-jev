# Decisium (plain-English Gherkin UI tests run in Playwright, with Jev picking the page actions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic UI testing: plain-English Gherkin steps run in a real Playwright browser, Jev picks among the actions the page actually offers and answers whether each step is done, and code decides pass or fail; record and replay cassettes make CI runs deterministic with no model calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andletenkov/decisium) |
| Maintainer | [andletenkov](https://github.com/andletenkov). Independently curated. |
| Format | npm package and cucumber-js steps (TypeScript) |
| Requirements | Node.js and Playwright Chromium; a TypeSafe API key for live runs (replays need none). |
| License | [MIT](https://github.com/andletenkov/decisium/blob/b5d92542897d43128d3b8347d8393a93ebec24fb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/andletenkov/decisium/blob/b5d92542897d43128d3b8347d8393a93ebec24fb/src/jev.ts) at the pinned commit. |

## When to use

- Write UI tests without selectors and keep them stable when markup changes.
- Record a run once with Jev, then replay it in CI with zero model calls.
- Mismatch: live runs call TypeSafe's hosted Jev under its own terms.

## How it works

`src/jev.ts` uses `@typesafe-ai/sdk` (`jev-1.14.0`) to send the step and the page's available actions as Choice questions and Noul questions for completion; cassettes store the answers for replay. Integration evidence: [`src/jev.ts`](https://github.com/andletenkov/decisium/blob/b5d92542897d43128d3b8347d8393a93ebec24fb/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install --save-dev decisium
npx playwright install chromium
export TYPESAFE_API_KEY=...
npx decisium doctor my.feature
npx decisium run my.feature
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs site: [andletenkov.github.io/decisium/](https://andletenkov.github.io/decisium/)
- README: [github.com/andletenkov/decisium#readme](https://github.com/andletenkov/decisium#readme)

## Limits and data handling

During live runs, step text and page UI content go to TypeSafe. Replays with `--record none` make no network calls to Jev.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit b5d92542897d](https://github.com/andletenkov/decisium/tree/b5d92542897d43128d3b8347d8393a93ebec24fb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
