# jev-title-abstract-screening (systematic-review title/abstract screening with TypeSafe Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reference labels, saved predictions, prompts and runners for title-and-abstract screening in systematic reviews, including an API runner that calls TypeSafe System One (`jev-1.13.0`) for live Jev judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/matsuikentaro1/jev-title-abstract-screening) |
| Maintainer | [matsuikentaro1](https://github.com/matsuikentaro1). Independently curated. |
| Format | Research datasets + Node runners (MIT) |
| Requirements | Node for the runners; a TypeSafe API key for live screening calls. |
| License | [MIT](https://github.com/matsuikentaro1/jev-title-abstract-screening/blob/d911eafc5299aa3ca41a6aacf0167931c81fcbbc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`api_runners/1_run_jev.mjs`](https://github.com/matsuikentaro1/jev-title-abstract-screening/blob/d911eafc5299aa3ca41a6aacf0167931c81fcbbc/api_runners/1_run_jev.mjs) at the pinned commit. |

## When to use

- Reproduce or extend the study's Jev screening protocol.
- Reanalyze saved outputs without new API calls.
- Mismatch: research artifact; not a full review management product.

## How it works

`api_runners/1_run_jev.mjs` POSTs to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0` using `TYPESAFE_API_KEY`. Integration evidence: [`api_runners/1_run_jev.mjs`](https://github.com/matsuikentaro1/jev-title-abstract-screening/blob/d911eafc5299aa3ca41a6aacf0167931c81fcbbc/api_runners/1_run_jev.mjs).

## Get started

Clone, set TYPESAFE_API_KEY for live runs, or use saved outputs for offline reanalysis per README.

```sh
git clone https://github.com/matsuikentaro1/jev-title-abstract-screening.git && cd jev-title-abstract-screening
export TYPESAFE_API_KEY=...
node api_runners/1_run_jev.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/matsuikentaro1/jev-title-abstract-screening/blob/d911eafc5299aa3ca41a6aacf0167931c81fcbbc/README.md](https://github.com/matsuikentaro1/jev-title-abstract-screening/blob/d911eafc5299aa3ca41a6aacf0167931c81fcbbc/README.md)

## Limits and data handling

Title/abstract text is sent to TypeSafe on your key during live runs.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit d911eafc5299](https://github.com/matsuikentaro1/jev-title-abstract-screening/tree/d911eafc5299aa3ca41a6aacf0167931c81fcbbc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
