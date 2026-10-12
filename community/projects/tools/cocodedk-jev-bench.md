# Jev Bench (cocodedk)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Configurable classifier workbench for repeatable latency and accuracy experiments on TypeSafe Jev (Banking77 accuracy, OpenRouter comparisons) with a published results site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cocodedk/jev-bench) |
| Maintainer | [cocodedk](https://github.com/cocodedk). Independently curated. |
| Format | Python CLI |
| Requirements | Python; TypeSafe/OpenRouter keys per README. |
| License | [Apache-2.0](https://github.com/cocodedk/jev-bench/blob/348737dd1bcecef5843b70f580e02a76e423a44b/LICENSE) |
| Jev evidence | [`jev_bench/cli.py`](https://github.com/cocodedk/jev-bench/blob/348737dd1bcecef5843b70f580e02a76e423a44b/jev_bench/cli.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Re-run Jev classification and latency comparisons on your own config.
- Mismatch: results are the author's runs; not an official benchmark.

## How it works

Config-driven runs call Jev and comparison models, record latency and accuracy, and publish results under `results/`. (Summarized from the upstream [README](https://github.com/cocodedk/jev-bench/blob/348737dd1bcecef5843b70f580e02a76e423a44b/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `git clone https://github.com/cocodedk/jev-bench.git` and follow the README.

## Limits and data handling

Benchmark inputs go to the configured providers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 348737dd1bce](https://github.com/cocodedk/jev-bench/tree/348737dd1bcecef5843b70f580e02a76e423a44b). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
