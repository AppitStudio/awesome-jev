# Jev decision-model benchmarks (vilinski)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible decision-model benchmark: a hand-labelled own set (60 tasks x3) and a 1,100-item public sample, run against Jev and other System One routes, with raw results, pricing snapshots and generators for a published report and interactive model explorer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vilinski/jev-benchmarks) |
| Maintainer | [vilinski](https://github.com/vilinski). Independently curated. |
| Format | Python scripts (standard library) + saved results and HTML report |
| Requirements | Python 3.14; the `jev` Rust CLI 0.4.1+ and provider credentials only for live runs. |
| License | [MIT OR Apache-2.0](https://github.com/vilinski/jev-benchmarks/blob/4d3bb21d5f5bff4062a61010c6206eeca8b0f185/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevcall.py`](https://github.com/vilinski/jev-benchmarks/blob/4d3bb21d5f5bff4062a61010c6206eeca8b0f185/jevcall.py) at the pinned commit. |

## When to use

- Compare Jev with other decision models on accuracy, latency and price using checked-in raw data.
- Rebuild the report offline from saved results, or resume runs on your own credentials.
- Mismatch: results are the author's; live runs cost money; the public sample's component datasets carry their own licenses.

## How it works

`jevcall.py` sends each System One request body through `jev run` (from vilinski/jev) and records timing, answers and usage; `run_variants.py` resumes per-route checkpoints, and `report.py` builds `report.html`, `data.json` and `statistics.csv` from `results/`. Integration evidence: [`jevcall.py`](https://github.com/vilinski/jev-benchmarks/blob/4d3bb21d5f5bff4062a61010c6206eeca8b0f185/jevcall.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/vilinski/jev-benchmarks.git && cd jev-benchmarks
python3 report.py   # offline, from saved results
# live: cargo install --git https://github.com/vilinski/jev --locked && jev login -p <provider>
python3 run_variants.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Published report: [ai.vilinski.dev/jev-benchmark/](https://ai.vilinski.dev/jev-benchmark/)
- Model explorer: [ai.vilinski.dev/decision-models/](https://ai.vilinski.dev/decision-models/)

## Limits and data handling

Rebuilding the report needs no network; live runs send benchmark items to the chosen provider using credentials held by the `jev` CLI.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 4d3bb21d5f5b](https://github.com/vilinski/jev-benchmarks/tree/4d3bb21d5f5bff4062a61010c6206eeca8b0f185). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
