# FastBrain-9B (open non-autoregressive System One decision model that answers Jev-shaped requests in one pass)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open decision model built on a hybrid Qwen3.5-9B backbone with a 116M-parameter joint schema head: give it a JSON state and `choice`, `noul` or `score` questions and it scores every option of every question in a single prefill instead of generating text. Inference, training and evaluation code here; weights on Hugging Face. Not TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/camera-2018/FastBrain) |
| Maintainer | [camera-2018](https://github.com/camera-2018). Independently curated. |
| Format | Python package and model weights (Hugging Face `TypeScript/FastBrain-9B`) |
| Requirements | An NVIDIA GPU with 24 GB+ for full precision (smaller with quantization); Python. |
| License | [Apache-2.0](https://github.com/camera-2018/FastBrain/blob/8cfb604c19c512c11fe5fabdc497d90035a6d3b9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`fastbrain/modeling_fastbrain.py`](https://github.com/camera-2018/FastBrain/blob/8cfb604c19c512c11fe5fabdc497d90035a6d3b9/fastbrain/modeling_fastbrain.py) at the pinned commit. |

## When to use

- Run a Jev-style decision model on your own GPU.
- Mismatch: not TypeSafe's Jev; check quality on your own tasks.

## How it works

`fastbrain/modeling_fastbrain.py` provides `systemone()`, which takes a Jev `/v1/systemone` request body and returns answers in the same shape from one logit per allowed option. Integration evidence: [`fastbrain/modeling_fastbrain.py`](https://github.com/camera-2018/FastBrain/blob/8cfb604c19c512c11fe5fabdc497d90035a6d3b9/fastbrain/modeling_fastbrain.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/camera-2018/FastBrain.git && cd FastBrain
pip install -e .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Weights: [huggingface.co/TypeScript/FastBrain-9B](https://huggingface.co/TypeScript/FastBrain-9B)
- README: [github.com/camera-2018/FastBrain#readme](https://github.com/camera-2018/FastBrain#readme)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 8cfb604c19c5](https://github.com/camera-2018/FastBrain/tree/8cfb604c19c512c11fe5fabdc497d90035a6d3b9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
