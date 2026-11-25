# Nischay-1 by Ajeet Kumar Upadhyay (open-weight 8B text and vision decision model that answers Choice, Noul and Score questions in one forward pass)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Multimodal decision model post-trained from Google's Gemma-4 E4B (8B total, 3.89B active). Give it a state (text, JSON or up to four images) and typed `noul`, `choice` or `score` questions, and it returns a calibrated probability for every option without generating tokens. The author reports a tied #27 of 346 on the Jev Decision Index 0.4 text board.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://huggingface.co/Ajeet-001/nischay-1) |
| Maintainer | [Ajeet Kumar Upadhyay](https://huggingface.co/Ajeet-001). Independently curated. |
| Format | Hugging Face weights (safetensors) with a Python engine and setup script |
| Requirements | One CUDA GPU; `setup.sh` installs a pinned OneJev serving runtime with the author's patch and readout; Hugging Face CLI to download the weights. |
| License | [Apache-2.0](https://huggingface.co/Ajeet-001/nischay-1/blob/ce8f9a30dc551bc413be9547696a9dbeb13b9a9e/README.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ajeetkrup401/status/2125620540564181051)). |
| Jev evidence | [`engine.py`](https://huggingface.co/Ajeet-001/nischay-1/blob/ce8f9a30dc551bc413be9547696a9dbeb13b9a9e/engine.py) at the pinned release. |

## When to use

- Run Jev-shaped typed decisions over text and images on your own GPU.
- Mismatch: if you want TypeSafe's hosted Jev or a CPU-only model; this is a separate 8B model that needs a GPU.

## How it works

`engine.py` exposes a `DecisionModel` class that takes a `state`, optional images and Jev-style `questions` and returns `answers` with probabilities; `readout.json` and `calibration.json` hold the option readout and calibration. This is the author's own model, not TypeSafe's Jev, and no TypeSafe API is called. Integration evidence: [`engine.py`](https://huggingface.co/Ajeet-001/nischay-1/blob/ce8f9a30dc551bc413be9547696a9dbeb13b9a9e/engine.py).

## Get started

Download the weights and run the setup script on a CUDA machine, then call the engine from Python.

```sh
hf download Ajeet-001/nischay-1 --local-dir nischay-1 && bash nischay-1/setup.sh
# then: from engine import DecisionModel; DecisionModel("./nischay-1", device="cuda:0")
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model card: [huggingface.co/Ajeet-001/nischay-1](https://huggingface.co/Ajeet-001/nischay-1)
- Jev Decision Index board: [huggingface.co/spaces/multimodalart/jev-decision-index](https://huggingface.co/spaces/multimodalart/jev-decision-index)

## Limits and data handling

Not TypeSafe's Jev: an independent fine-tune of Gemma-4 E4B (check the Gemma base model's terms alongside the Apache-2.0 card). Decision Index ranks and latency figures are the author's report of the public board. Vision requests take one question per call. The setup installs a patched third-party serving runtime.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [Hugging Face revision ce8f9a30dc55](https://huggingface.co/Ajeet-001/nischay-1/tree/ce8f9a30dc551bc413be9547696a9dbeb13b9a9e). Inspected the model card, file list and `engine.py` at the pinned Hugging Face revision; the model was not downloaded or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
