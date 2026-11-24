# mini-jev-multimodal by Astitwa Agarwal (small open text+image decision model that trains and runs on an 8 GB laptop GPU)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent reproduction of the System One idea: Qwen3-VL-2B with LoRA adapters and an answer head that scores every allowed option of every question in one forward pass, for text and up to 8 images. Weights are on Hugging Face (Apache-2.0), with a paper, calibration and a Jev-compatible `/v1/systemone` server. Not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agarwalastitwa027-svg/mini-jev-multimodal) |
| Maintainer | [agarwalastitwa027-svg](https://github.com/agarwalastitwa027-svg). Independently curated. |
| Format | Python (PyTorch) model, training code and HTTP server |
| Requirements | Python 3.10+ and an NVIDIA GPU (8 GB is enough); about 4.5 GB of base-model download. No TypeSafe key. |
| License | [Apache-2.0](https://github.com/agarwalastitwa027-svg/mini-jev-multimodal/blob/0d8eeffec21b0071ec953145cbad015f86c2a699/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`serve.py`](https://github.com/agarwalastitwa027-svg/mini-jev-multimodal/blob/0d8eeffec21b0071ec953145cbad015f86c2a699/serve.py) at the pinned commit. |

## When to use

- Run a local, open Jev-style decision model on text and images without sending data to an API.
- Mismatch: if you need Jev itself; this is a 2B stand-in that the author says is weak on chess, music, routing, expert science and long-context retrieval.

## How it works

`serve.py` exposes `POST /v1/systemone` taking `model`, `state`, `questions` and optional `images` and returns choice, noul and score answers in Jev's shape; `infer.py` runs the same model from Python. Integration evidence: [`serve.py`](https://github.com/agarwalastitwa027-svg/mini-jev-multimodal/blob/0d8eeffec21b0071ec953145cbad015f86c2a699/serve.py).

## Get started

Create a virtualenv, install PyTorch and the requirements, and run the smoke test or the server.

```sh
git clone https://github.com/agarwalastitwa027-svg/mini-jev-multimodal.git && cd mini-jev-multimodal
pip install -r requirements.txt
python infer.py --run AstitwaAgarwal/multimodal-jev
python serve.py --run AstitwaAgarwal/multimodal-jev --port 8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model on Hugging Face: [huggingface.co/AstitwaAgarwal/multimodal-jev](https://huggingface.co/AstitwaAgarwal/multimodal-jev)
- README with base-vs-mini-Jev results: [github.com/agarwalastitwa027-svg/mini-jev-multimodal/blob/0d8eeffec21b0071ec953145cbad015f86c2a699/README.md](https://github.com/agarwalastitwa027-svg/mini-jev-multimodal/blob/0d8eeffec21b0071ec953145cbad015f86c2a699/README.md)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe. Latency and accuracy figures are the author's own (RTX 5070 Laptop). Requests over the declared limits return `Unsupported` rather than being truncated.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 0d8eeffec21b](https://github.com/agarwalastitwa027-svg/mini-jev-multimodal/tree/0d8eeffec21b0071ec953145cbad015f86c2a699). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
