# Jeeves (PostHog)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

PostHog’s open 9B Jev-like decision model with chain-of-thought before noul/choice/score answers and a Jev-compatible API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PostHog/jeeves) |
| Maintainer | [PostHog](https://github.com/PostHog). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python research model + training/serving code (Hugging Face weights). |
| Requirements | CUDA (Hopper for FP8 kernel per upstream); follow README for serving. Not the TypeSafe hosted API. |
| License | [MIT](https://github.com/PostHog/jeeves/blob/f04ec5567301450dcaae0210dd54deeb4f647f87/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent of TypeSafe AI; Jev-compatible open model, not hosted Jev. |

## When to use

Use when self-hosting a Jev-style decision API with optional reasoning. Prefer TypeSafe docs/API for the hosted Jev product.

## How it works

Trains a Qwen3.5-9B LoRA pointer-head classifier with optional thinking; serves yes/no, choice, and score through a Jev-compatible API. Independent open-weight alternative—not TypeSafe Jev weights or the hosted TypeSafe service. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/PostHog/jeeves.git
cd jeeves
git checkout f04ec5567301450dcaae0210dd54deeb4f647f87
# follow upstream README for weights (huggingface.co/PostHog/jeeves) and serving
```

Pin revision `f04ec5567301450dcaae0210dd54deeb4f647f87` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Not affiliated with TypeSafe. Benchmark numbers are author-reported. Live GPU serving not run on the review host. Disclose to readers: Jev-compatible / Jev-like, not TypeSafe-hosted Jev.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit f04ec55](https://github.com/PostHog/jeeves/tree/f04ec5567301450dcaae0210dd54deeb4f647f87). AI-assisted README and LICENSE inspection; install/live paths not executed.
