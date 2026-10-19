# Docket (pg-jev Phase 0 benchmark)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Design and reproducible Phase 0 benchmark for durable, versioned, calibrated AI decisions in Postgres: measures jev-1.13 through pg-jev on 2,000 real complaint narratives for calibration, determinism and context effects.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ElyasEbrahim/docket) |
| Maintainer | [ElyasEbrahim](https://github.com/ElyasEbrahim). Independently curated. |
| Format | Docker harness (Postgres + pg-jev) + design docs |
| Requirements | Docker; a TypeSafe key for real Jev runs (default backend is simulated). |
| License | [Apache-2.0](https://github.com/ElyasEbrahim/docket/blob/87992628a732f28c9cadb30328330c43404b32a1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/jevbench/runner.py`](https://github.com/ElyasEbrahim/docket/blob/87992628a732f28c9cadb30328330c43404b32a1/harness/jevbench/runner.py) at the pinned commit. |

## When to use

- See how stable and calibrated Jev labels are inside SQL before relying on them.
- Reproduce the measurements on your own data.
- Mismatch: the Docket product itself is not built yet; this is research and design.

## How it works

The harness loads CFPB complaints into Postgres 16 with pg-jev and runs experiments through `jev_eval()` in `harness/jevbench/runner.py`, against a mock, a simulated backend or the real Jev API. Real runs print the estimated spend and refuse anything over $1. Integration evidence: [`harness/jevbench/runner.py`](https://github.com/ElyasEbrahim/docket/blob/87992628a732f28c9cadb30328330c43404b32a1/harness/jevbench/runner.py).

## Get started

From the upstream README: `make up`, load the sample, run the benchmark on the simulated backend, then optionally on real Jev.

```sh
make up && make fetch load && make bench
make bench BACKEND=jev ARGS=--yes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/phase0/FINDINGS-jev-1.13.md
- REPORT.md

## Limits and data handling

Real runs send complaint text to TypeSafe. Findings cover one model version and dataset.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 87992628a732](https://github.com/ElyasEbrahim/docket/tree/87992628a732f28c9cadb30328330c43404b32a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
