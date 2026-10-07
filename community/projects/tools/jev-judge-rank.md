# jev-judge-rank

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Three standard-library Python scripts (and an agent skill) that use TypeSafe Jev to rank a list on several written criteria, merge near-duplicates under one representative, and recall the corpus entries that help with a one-sentence situation; every request and response is logged locally, with a recorded example run and its costs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tsetse012/jev-judge-rank) |
| Maintainer | [tsetse012](https://github.com/tsetse012). Independently curated. |
| Format | Python scripts (`jev_rank.py`, `jev_dedupe.py`, `jev_recall.py`) and `SKILL.md` |
| Requirements | Python 3.9+ (standard library only) and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/tsetse012/jev-judge-rank/blob/5072e556b40c8995358675cec18c72dde251d102/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Prioritise idea lists, backlogs or notes on several axes at once.
- Collapse near-duplicate entries before review.
- Mismatch: ranking quality depends on how you word the axes.

## How it works

[`scripts/jev_rank.py`](https://github.com/tsetse012/jev-judge-rank/blob/5072e556b40c8995358675cec18c72dde251d102/scripts/jev_rank.py) asks Score questions per axis and sorts by a weighted combined score; [`jev_dedupe.py`](https://github.com/tsetse012/jev-judge-rank/blob/5072e556b40c8995358675cec18c72dde251d102/scripts/jev_dedupe.py) groups near-duplicates; [`jev_recall.py`](https://github.com/tsetse012/jev-judge-rank/blob/5072e556b40c8995358675cec18c72dde251d102/scripts/jev_recall.py) returns relevant entries. Recorded outputs are in [`examples/ideas/out/`](https://github.com/tsetse012/jev-judge-rank/tree/5072e556b40c8995358675cec18c72dde251d102/examples/ideas/out).

## Get started

Run the ranking example (README):

```sh
git clone https://github.com/tsetse012/jev-judge-rank && cd jev-judge-rank
export TYPESAFE_API_KEY=...
python3 scripts/jev_rank.py --items examples/ideas/items.json --config examples/ideas/axes.json \
  --out out/rank --check feasibility:has_demo
```

Upstream's example (40 items, 80 requests) reports about $0.002 of Jev; billed to your TypeSafe key.

## Examples and demos

- [Example report](https://github.com/tsetse012/jev-judge-rank/blob/5072e556b40c8995358675cec18c72dde251d102/examples/ideas/out/rank/report.txt).
- [Agent skill](https://github.com/tsetse012/jev-judge-rank/blob/5072e556b40c8995358675cec18c72dde251d102/SKILL.md).

## Limits and data handling

Item text goes to TypeSafe; requests and responses are logged to `raw_jev.jsonl` locally. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 5072e556b40c](https://github.com/tsetse012/jev-judge-rank/tree/5072e556b40c8995358675cec18c72dde251d102). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
