# Jev-LCT

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open System One decision engine (Looped Calibration Transformer): looped prefill on small Qwen backbones, endogenous trajectory confidence, and Jev-compatible Choice/Noul/Score serving—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gitchw/LCT) |
| Maintainer | [gitchw](https://github.com/gitchw). Independently curated. |
| Format | Python training/inference code, FastAPI/SDK surfaces, Hugging Face Qwen-based checkpoints. |
| Requirements | Python + PyTorch GPU stack per upstream; download scripts for 0.5B/1.5B/8B weights. |
| License | [Apache-2.0](https://github.com/gitchw/LCT/blob/e54e28468dbf6857a3e567ab883c4b875ffa237d/LICENSE). |
| Disclosure | Independent open model research—not TypeSafe-hosted Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Benchmark/latency tables are author-reported on RTX 3090 Ti; training/serving not re-run on the review host. |

## When to use

Use for **local open System One serving** with looped calibration confidence. Prefer hosted TypeSafe Jev when you need the official cloud model without managing checkpoints.

## How it works

Terminal layers loop with scale-keeping injection; confidence comes from trajectory stability/entropy rather than verbalized self-report; adaptive early exit trades depth for latency. FastAPI/SDK expose Choice/Noul/Score.

## Get started

```sh
git clone https://github.com/gitchw/LCT.git
cd LCT
git checkout e54e28468dbf6857a3e567ab883c4b875ffa237d
# e.g. python scripts/download_weights.py --scale 1.5b
# Follow README for serve/SDK and snake/ interactive bench
```

## Examples and demos

- HF model zoo links in README (`CaoHaoWei/Jev-LCT-*`).
- `snake/` dynamic decision bench adapted from community snake evals.

## Limits and data handling

Local GPU inference; remote HF downloads follow HF terms. Comparative accuracy/latency numbers are upstream-reported. Default branch is `master`.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit e54e284](https://github.com/gitchw/LCT/tree/e54e28468dbf6857a3e567ab883c4b875ffa237d). AI-assisted README and LICENSE inspection; download/serve not executed.
