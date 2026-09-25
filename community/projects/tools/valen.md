# Valen

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open multimodal System One–style decision model: text, images, and video in; probabilities over supplied candidates out—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Liuziyu77/Valen) |
| Maintainer | [Liuziyu77](https://github.com/Liuziyu77) / Valen-Team. Independently curated. |
| Format | Python package + training/eval scripts; Hugging Face preview weights and Spaces demo. |
| Requirements | Python 3.10+; Valen checkpoint plus Qwen3.5 base weights per upstream docs. |
| License | [Apache-2.0](https://github.com/Liuziyu77/Valen/blob/06251f9d9d3c06ea690be93b8696ccc66471f8c9/LICENSE). |
| Disclosure | Independent open model research—not TypeSafe-hosted Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Demo latency/quality figures are upstream-reported; training/inference not re-run on the review host. |

## When to use

Use for **local multimodal typed decisions** or to train on your own data. Prefer hosted TypeSafe Jev when you need the official cloud model without local GPU/weights ops.

## How it works

A shared decision head scores candidates without generating answer tokens. The repo covers data processing, SFT, experimental RLCD, inference, and evaluation.

## Get started

```sh
git clone https://github.com/Liuziyu77/Valen.git
cd Valen
git checkout 06251f9d9d3c06ea690be93b8696ccc66471f8c9
# Weights: https://huggingface.co/Valen-Team/Valen-Preview-0923
```

## Examples and demos

- [HF Spaces demo](https://huggingface.co/spaces/yuhangzang/Valen-Preview-0923).
- README Sokoban / blur-confidence demos (upstream-reported).

## Limits and data handling

Not official Jev. Local inference uses your hardware; remote Spaces/HF traffic follows those hosts' terms. Benchmark numbers are author-reported.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 06251f9](https://github.com/Liuziyu77/Valen/tree/06251f9d9d3c06ea690be93b8696ccc66471f8c9). AI-assisted README and LICENSE inspection; install/train/inference not executed.
