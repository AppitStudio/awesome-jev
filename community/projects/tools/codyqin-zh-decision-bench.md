# zh-decision-bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Chinese-language calibration benchmark for Jev-class System One decision models (dataset CC BY 4.0; code Apache-2.0), including Jev and NeoHorse arms

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CodyQin/zh-decision-bench) |
| Maintainer | [CodyQin](https://github.com/CodyQin). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python benchmark + Hugging Face dataset. |
| Requirements | Python; HF dataset `CodyQin/zh-decision-bench`; model/provider keys for eval arms. |
| License | [Apache-2.0](https://github.com/CodyQin/zh-decision-bench/blob/1a4079b1931712f22e164256aa64825fc7e7b32f/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to measure Chinese-task calibration (not only accuracy) for System One models including hosted Jev. Prefer English Decision Index / other benches for non-Chinese suites.

## How it works

Dataset plus eval scripts with temperature refit and robustness tests across five models. Integration evidence: upstream README and HF dataset at the pinned commit.

## Get started

```sh
git clone https://github.com/CodyQin/zh-decision-bench.git
cd zh-decision-bench
git checkout 1a4079b1931712f22e164256aa64825fc7e7b32f
```

Pin revision `1a4079b1931712f22e164256aa64825fc7e7b32f` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 1a4079b](https://github.com/CodyQin/zh-decision-bench/tree/1a4079b1931712f22e164256aa64825fc7e7b32f). AI-assisted README and LICENSE inspection; install/live paths not executed.
