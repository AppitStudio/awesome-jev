# pi-jev-thinking

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension: before each prompt TypeSafe Jev scores difficulty on four rungs (low → xhigh) and whether it is a short continuation, then sets Pi's thinking level; decisions are logged for tuning.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lancejohnson/pi-jev-thinking) |
| Maintainer | [lancejohnson](https://github.com/lancejohnson). Independently curated. |
| Format | Pi extension |
| Requirements | Pi; TypeSafe key. |
| License | [MIT](https://github.com/lancejohnson/pi-jev-thinking/blob/062c10e474f570a4c3ff22f6ee5fb0a3490896ab/LICENSE) |
| Jev evidence | [`src/decide.ts`](https://github.com/lancejohnson/pi-jev-thinking/blob/062c10e474f570a4c3ff22f6ee5fb0a3490896ab/src/decide.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Match thinking effort to prompt difficulty automatically in Pi.
- Mismatch: Pi only; see other thinking routers for omp.

## How it works

Prompt plus tail of the last reply (redacted) go to Jev; the score maps to a thinking level and decisions append to a local JSONL file. (Summarized from the upstream [README](https://github.com/lancejohnson/pi-jev-thinking/blob/062c10e474f570a4c3ff22f6ee5fb0a3490896ab/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the extension per the README and set your key.

## Limits and data handling

Redacted prompt text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 062c10e474f5](https://github.com/lancejohnson/pi-jev-thinking/tree/062c10e474f570a4c3ff22f6ee5fb0a3490896ab). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
