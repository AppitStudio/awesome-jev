# Brier

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local calibrated choice/score/noul decisions in TypeSafe Jev API form, trained for Portuguese, on Apple Silicon MLX.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mangaba-ai/brier) |
| Maintainer | [Mangaba-ai](https://github.com/Mangaba-ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python MLX local decision model + Jev-format HTTP API. |
| Requirements | Apple Silicon / MLX per upstream; offline after weights load. |
| License | [Apache-2.0](https://github.com/Mangaba-ai/brier/blob/e951b857969fda17e8284ad0b72a1fd62c0c2d68/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent of TypeSafe AI; Jev-format local model. |

## When to use

Use for local PT-oriented System One–style decisions on Mac. Prefer TypeSafe hosted Jev for the product API.

## How it works

Serves POST /v1/systemone-style typed questions from a Qwen3-1.7B + LoRA head optimized for Brier-style calibration. Independent reproduction, not TypeSafe weights. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/Mangaba-ai/brier.git
cd brier
git checkout e951b857969fda17e8284ad0b72a1fd62c0c2d68
# follow upstream README (PT) for MLX install and serve
```

Pin revision `e951b857969fda17e8284ad0b72a1fd62c0c2d68` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Author comparison vs Jev is upstream-reported. Live MLX serve not run on the review host. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit e951b85](https://github.com/Mangaba-ai/brier/tree/e951b857969fda17e8284ad0b72a1fd62c0c2d68). AI-assisted README and LICENSE inspection; install/live paths not executed.
