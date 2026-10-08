# clef-webcam

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Runs Cloudflare's open-weight clef-flash decision model locally on an Apple Silicon Mac and turns live webcam frames into typed decisions (noul / choice / score) using the same question schema as Jev / System One, with Metal kernels that cut a webcam frame with three questions from ~840 ms to ~250 ms on the author's M5 Max.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lucataco/clef-webcam) |
| Maintainer | [lucataco](https://github.com/lucataco). Independently curated. |
| Format | Local FastAPI server (`server.py`) with a live demo page and benchmark script |
| Requirements | Apple Silicon Mac with 32 GB+ memory (~19 GB model), uv, and the `Cloudflare/clef-flash` weights from Hugging Face. No TypeSafe key. |
| License | [Apache-2.0](https://github.com/lucataco/clef-webcam/blob/40124a3f2909a97a3f2c6de8607532ab6bd48030/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Experiment with image states and editable questions before designing a Jev or Clef workflow.
- Benchmark local Clef latency on Apple Silicon.
- Mismatch: hosted TypeSafe Jev is text-only; this demo runs Clef, not Jev.

## How it works

[`server.py`](https://github.com/lucataco/clef-webcam/blob/40124a3f2909a97a3f2c6de8607532ab6bd48030/server.py) accepts a frame plus questions and returns probabilities; [`clef.py`](https://github.com/lucataco/clef-webcam/blob/40124a3f2909a97a3f2c6de8607532ab6bd48030/clef.py) loads the model and [`mps_kernels.py`](https://github.com/lucataco/clef-webcam/blob/40124a3f2909a97a3f2c6de8607532ab6bd48030/mps_kernels.py) replaces slow linear-attention fallbacks on MPS. Press `E` in the page to edit questions live.

## Get started

Download the weights and start the server (README *Quickstart*):

```sh
git clone https://github.com/lucataco/clef-webcam.git && cd clef-webcam
uv sync
uv run hf download Cloudflare/clef-flash --local-dir models/clef-flash
uv run uvicorn server:app --port 8787
```

No inference charges; runs locally.

## Examples and demos

- Speed/accuracy check: [`bench.py`](https://github.com/lucataco/clef-webcam/blob/40124a3f2909a97a3f2c6de8607532ab6bd48030/bench.py).
- README *Performance* table (author-measured on M5 Max).

## Limits and data handling

Webcam frames stay on the machine. Independent of Cloudflare and TypeSafe; performance figures are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 40124a3f2909](https://github.com/lucataco/clef-webcam/tree/40124a3f2909a97a3f2c6de8607532ab6bd48030). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
