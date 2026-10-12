# snap-vs-jev-swe

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible benchmark of fast decision models (SubQ Snap, TypeSafe Jev and three open models) on software-engineering tasks: SWE-bench Verified file localization, long context and option-order sensitivity.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kprzybys/snap-vs-jev-swe) |
| Maintainer | [kprzybys](https://github.com/kprzybys). Independently curated. |
| Format | Python benchmark |
| Requirements | Python; provider keys for the models you rerun. |
| License | [MIT](https://github.com/kprzybys/snap-vs-jev-swe/blob/b754c446986aacb14ea5857c75ad2db2c739f6e7/LICENSE) |
| Jev evidence | [`src/snapbench`](https://github.com/kprzybys/snap-vs-jev-swe/tree/b754c446986aacb14ea5857c75ad2db2c739f6e7/src/snapbench) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Compare Jev against other fast decision models on code-localization style decisions.
- Mismatch: author reports some differences as not statistically significant.

## How it works

Benchmarks in `src/snapbench/benchmarks/` issue typed choice questions to each model and log per-item results under `results/`. (Summarized from the upstream [README](https://github.com/kprzybys/snap-vs-jev-swe/blob/b754c446986aacb14ea5857c75ad2db2c739f6e7/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): clone and install per the README, then run the benchmark scripts.

## Limits and data handling

Issue text and file lists go to each provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit b754c446986a](https://github.com/kprzybys/snap-vs-jev-swe/tree/b754c446986aacb14ea5857c75ad2db2c739f6e7). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
