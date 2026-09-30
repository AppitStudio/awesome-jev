# calfram-bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

External calibration audit of TypeSafe Jev (`jev-1.13.0`) on 25 public benchmarks using CalFram, with paper source under `paper/`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lorenzofamiglini/calfram-bench) |
| Maintainer | [lorenzofamiglini](https://github.com/lorenzofamiglini). Independently curated. |
| Format | Python measurement harness + LaTeX paper; MIT. |
| Requirements | Python env per upstream; `TYPESAFE_API_KEY` for live Jev caches; CalFram dependency. |
| License | [MIT](https://github.com/lorenzofamiglini/calfram-bench/blob/1e2bb193b4b4a0c9fb0ff726d49a78952268158c/LICENSE). Live Jev calls incur TypeSafe charges. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Paper/metrics are author research—not re-run here. Live TypeSafe paths not run on the review host. |

## When to use

Use when studying Jev probability calibration on public tasks. Prefer vendor workflow evals ([WorkflowEvals](workflowevals.md)) for action-agreement benchmarks.

## How it works

Asks semantic/MCQ as Choice and binary as Noul; scores ECE/ECI and related CalFram metrics from cached answers; optional local recalibration study. Design documented in `docs/DESIGN.md`.

## Get started

```sh
git clone https://github.com/lorenzofamiglini/calfram-bench.git
cd calfram-bench
git checkout 1e2bb193b4b4a0c9fb0ff726d49a78952268158c
# follow upstream docs/DESIGN.md and README for env + runs
```

## Examples and demos

- Paper source: `paper/main.tex`.
- Methodology: `docs/DESIGN.md`.

## Limits and data handling

Live runs send benchmark items to TypeSafe. Catalog checks did not execute measurements.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 1e2bb19](https://github.com/lorenzofamiglini/calfram-bench/tree/1e2bb193b4b4a0c9fb0ff726d49a78952268158c). AI-assisted README and license inspection; live evals not executed.
