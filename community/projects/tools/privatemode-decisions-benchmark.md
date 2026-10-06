# Privatemode Decisions benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Edgeless Systems' benchmark comparing its Privatemode Decisions library (GLM-5.3-Flash in an attested enclave) with TypeSafe Jev and local Laya on speed, accuracy, calibration and cost across 29 labelled public datasets, plus JevBench comparisons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/edgelesssys/privatemode-decisions-benchmark) |
| Maintainer | [edgelesssys](https://github.com/edgelesssys). Independently curated. |
| Format | Benchmark harness, datasets and published results |
| Requirements | Python venv; a TypeSafe key for the Jev arm, Privatemode access for its arm, local Laya for the third; budget flag in EUR. |
| License | [MIT](https://github.com/edgelesssys/privatemode-decisions-benchmark/blob/c9afbd606028cbeda3c91513688ebaf47562e19d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Compare hosted Jev with an alternative decision backend on your own budget and datasets.
- Reuse the methodology (frozen option sets, replicates, calibration metrics) for your own evaluation.
- Mismatch: vendor-run comparison of its own product — treat headline results as vendor claims.

## How it works

`bench.curate` freezes each dataset's option set; `bench.suite` forecasts cost, refuses to exceed `--budget-eur`, then runs each arm on the same examples and writes JSONL; `bench.aggregate` recomputes tables. See [`METHODOLOGY.md`](https://github.com/edgelesssys/privatemode-decisions-benchmark/blob/c9afbd606028cbeda3c91513688ebaf47562e19d/METHODOLOGY.md).

## Get started

Dry-run the suite to see the cost forecast before any live call:

```sh
git clone https://github.com/edgelesssys/privatemode-decisions-benchmark.git
cd privatemode-decisions-benchmark
.venv/bin/python -m bench.suite --dry-run -n 1000 --replicates 2 --arms all
```

Live runs call TypeSafe and Privatemode and are billed to your accounts; use the budget cap.

## Examples and demos

- `results/` tables and per-dataset reports (upstream).

## Limits and data handling

Published by the vendor of one compared system; results not reproduced. Dataset text is sent to each provider during live runs. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit c9afbd606028](https://github.com/edgelesssys/privatemode-decisions-benchmark/tree/c9afbd606028cbeda3c91513688ebaf47562e19d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
