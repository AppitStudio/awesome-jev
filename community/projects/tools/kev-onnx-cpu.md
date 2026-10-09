# kev-onnx-cpu

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Minimal-dependency Python inference for the open Kev 0.6B typed-decision model (ONNX q4f16) using only `onnxruntime` and `numpy`: a pure-Python port of the reference preprocessing with `choice`/`score`/`noul` questions answered in one forward pass, verified against the `open-jev` reference implementation. Independent of hosted TypeSafe Jev. Japanese and English READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kazuhito00/kev-onnx-cpu) |
| Maintainer | [Kazuhito00](https://github.com/Kazuhito00). Independently curated. |
| Format | Python library (`kev_decide`) + demo/verification scripts |
| Requirements | Python 3.10+, `numpy`, `onnxruntime` (GPU builds optional); about 330 MB of model files downloaded from GitHub Releases or Hugging Face. No API key. |
| License | [Apache-2.0](https://github.com/Kazuhito00/kev-onnx-cpu/blob/1ec2de632bff16b4bcb29073febbd4fd440cd8df/LICENSE); model weights follow the original model's license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run Jev-style typed decisions fully offline on CPU with very few dependencies.
- Mismatch: not official Jev; text-only, 4-bit builds only.

## How it works

[`kev_decide/`](https://github.com/Kazuhito00/kev-onnx-cpu/blob/1ec2de632bff16b4bcb29073febbd4fd440cd8df/kev_decide/protocol.py) builds the `[STATE]`/`[Q]`/`[OPT]` sequence and decodes per-option probabilities. The README reports bit-level agreement with `open-jev` on 12/12 golden cases and CPU latency figures (maintainer's results; not reproduced here).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Kazuhito00/kev-onnx-cpu
cd kev-onnx-cpu
uv sync
uv run download_model.py
uv run demo_inference_text.py
```

## Limits and data handling

Everything runs locally after the model download (SHA-256 checked by the script). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 1ec2de632bff](https://github.com/Kazuhito00/kev-onnx-cpu/tree/1ec2de632bff16b4bcb29073febbd4fd440cd8df). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
