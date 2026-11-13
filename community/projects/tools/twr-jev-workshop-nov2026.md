# Building with Jev and System One models (two-hour hands-on workshop with Playwright test-triage demos)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Workshop repository with a step-by-step guide and runnable demos on the DemoQA Book Store: race the same question across models for time, tokens and cost, probe where Jev breaks (numbers, double negatives, no option fits), route failing Playwright tests with Jev before a strong model, flag pages for review, and compare a hybrid Jev + LLM agent with an LLM-only one.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/raptatinha/twr-jev-nov2026) |
| Maintainer | [raptatinha](https://github.com/raptatinha). Independently curated. |
| Format | Workshop demos and guide (TypeScript with Playwright; no license file) |
| Requirements | Node.js, Playwright Chromium, a TypeSafe key and at least one LLM key; Docker only for the optional observability level. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/models/jev.ts`](https://github.com/raptatinha/twr-jev-nov2026/blob/82e92d52143fb768e2672f69f2e6e11634afacf5/src/models/jev.ts) at the pinned commit. |

## When to use

- Teach or learn when a System One model beats an LLM in a test-automation workflow.
- Mismatch: a reusable library; it is workshop material.

## How it works

`src/models/jev.ts` posts `{model, state, questions}` straight to `https://api.typesafe.ai/v1/systemone` (overridable with `JEV_ENDPOINT`) so participants can see the whole request; `src/meter.ts` and `src/prices.ts` track time, tokens and cost per model. Integration evidence: [`src/models/jev.ts`](https://github.com/raptatinha/twr-jev-nov2026/blob/82e92d52143fb768e2672f69f2e6e11634afacf5/src/models/jev.ts).

## Get started

Install, add the Playwright browser, copy the env file and run the first demo.

```sh
npm install
npx playwright install chromium
cp .env.example .env   # Jev + at least one LLM key
npm run race
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/raptatinha/twr-jev-nov2026/blob/82e92d52143fb768e2672f69f2e6e11634afacf5/README.md](https://github.com/raptatinha/twr-jev-nov2026/blob/82e92d52143fb768e2672f69f2e6e11634afacf5/README.md)
- Guide: [github.com/raptatinha/twr-jev-nov2026/blob/82e92d52143fb768e2672f69f2e6e11634afacf5/guide/guide.md](https://github.com/raptatinha/twr-jev-nov2026/blob/82e92d52143fb768e2672f69f2e6e11634afacf5/guide/guide.md)

## Limits and data handling

Test failures, page content and prompts go to TypeSafe and the LLM providers you configure on your keys.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 82e92d52143f](https://github.com/raptatinha/twr-jev-nov2026/tree/82e92d52143fb768e2672f69f2e6e11634afacf5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
