# Crosstalk

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Visualize which options a typed-decision router confuses (all 197 Twilio Voice API operations on one ring), rewrite their wording, and check the fix on a sealed test set; live mode targets a `/v1/systemone` server such as TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Chaddacus/crosstalk-lab) |
| Maintainer | [Chaddacus](https://github.com/Chaddacus). Independently curated. |
| Format | Web app + scripts |
| Requirements | Node.js; TypeSafe key for live mode (mock mode needs none). |
| License | [MIT](https://github.com/Chaddacus/crosstalk-lab/blob/0eb44311edde114da713ed160fd9e9d91c616013/LICENSE) |
| Jev evidence | [`server/live.ts`](https://github.com/Chaddacus/crosstalk-lab/blob/0eb44311edde114da713ed160fd9e9d91c616013/server/live.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Tune option wording for an agent router that picks among many similar API operations.
- Mismatch: all README numbers and clips are from a lexical mock, not Jev.

## How it works

The dev set streams probability leakage between options; you edit option text and re-run against the sealed test split, either with the BM25 mock or a live System One backend. (Summarized from the upstream [README](https://github.com/Chaddacus/crosstalk-lab/blob/0eb44311edde114da713ed160fd9e9d91c616013/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install dependencies and run the dev server per the README; add a key for live mode.

## Limits and data handling

Option text and probes go to TypeSafe in live mode. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 0eb44311edde](https://github.com/Chaddacus/crosstalk-lab/tree/0eb44311edde114da713ed160fd9e9d91c616013). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
