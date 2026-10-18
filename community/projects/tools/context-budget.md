# context-budget

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context-compaction toolkit that can rank relevance with TypeSafe Jev (`/v1/systemone` on `api.typesafe.ai`) to cut most of what agents send upstream while measuring answer quality on a benchmark.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samiulhuda360/context-budget) |
| Maintainer | [samiulhuda360](https://github.com/samiulhuda360). Independently curated. |
| Format | Python package with Jev relevance strategy |
| Requirements | Python; TYPESAFE_API_KEY for live Jev relevance ranking. |
| License | [MIT](https://github.com/samiulhuda360/context-budget/blob/c73a4e85016d5595bda8ec15e9b283a7b04b0907/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`context_budget/jev.py`](https://github.com/samiulhuda360/context-budget/blob/c73a4e85016d5595bda8ec15e9b283a7b04b0907/context_budget/jev.py) at the pinned commit. |

## When to use

- Shrink agent context with typed Jev relevance scores.
- Want a measurable compaction strategy, not only heuristics.
- Mismatch: early toolkit; quality claims are author-benchmarked.

## How it works

`context_budget/jev.py` POSTs to `https://api.typesafe.ai/v1` + `/systemone` for relevance questions used by `strategies/jev_relevance.py`. Integration evidence: [`context_budget/jev.py`](https://github.com/samiulhuda360/context-budget/blob/c73a4e85016d5595bda8ec15e9b283a7b04b0907/context_budget/jev.py).

## Get started

Clone, set TYPESAFE_API_KEY, and run the Jev relevance strategy / benchmark per README.

```sh
git clone https://github.com/samiulhuda360/context-budget && cd context-budget
# set TYPESAFE_API_KEY; see README for jev relevance strategy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- context_budget/strategies/jev_relevance.py
- docs/screenshots/jev-relevance.png

## Limits and data handling

Author benchmarks (~90% cut) are not independently verified here. Context snippets go to TypeSafe when ranking live.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit c73a4e85016d](https://github.com/samiulhuda360/context-budget/tree/c73a4e85016d5595bda8ec15e9b283a7b04b0907). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
