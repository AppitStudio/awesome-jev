# basal

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent open typed-decision models for Polish and English (basal-1.5 mini 1.5B, 4.5B, max 11B) with an inference engine serving a `/v1/systemone`-style API and a public leaderboard that includes hosted Jev 1.13; not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rkinas/basal) |
| Product homepage | [basal.si5.pl](https://basal.si5.pl/) |
| Maintainer | [rkinas](https://github.com/rkinas). Independently curated. |
| Format | Model family + inference server + evaluation leaderboard |
| Requirements | A CUDA GPU (or Apple Silicon via MLX, or GGUF via Ollama/llama.cpp), Python 3.12 with uv, and Hugging Face downloads. No TypeSafe key needed. |
| License | [Apache-2.0 (engine); weights Apache-2.0 on Hugging Face](https://github.com/rkinas/basal/blob/c3cab778b8cac8f1cc40ddfc982c5c809570c1e7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run typed decisions locally when data must stay on your hardware, especially for Polish-language inputs.
- Benchmark an open decision model against hosted Jev with the same request format.
- Mismatch: on the maintainer's own leaderboard hosted Jev 1.13 scores higher than every basal model; choose basal for locality or cost, not accuracy.

## How it works

The model reads a state and answers a typed question by returning a probability for each allowed answer in one forward pass, scored in both option orders. `basal-serve` exposes `POST /v1/systemone`; README notes describe extensions (`multi`, `act`, `facts`). The README leaderboard (Werdykt v1, 2026-10-03) lists Jev 1.13.0 at 0.816 macro accuracy and basal-1.5-max at 0.773; these are maintainer measurements ([README](https://github.com/rkinas/basal/blob/c3cab778b8cac8f1cc40ddfc982c5c809570c1e7/README.md)).

## Get started

Install into a fresh environment and serve the 4.5B model (per the README; downloads weights):

```sh
uv venv --python 3.12 ~/basal-env && source ~/basal-env/bin/activate
uv pip install torch==2.11.0 --index-url https://download.pytorch.org/whl/cu128
uv pip install "basal[fp8] @ https://github.com/rkinas/basal/archive/refs/tags/v1.5.0.tar.gz"
basal-serve --model Remek/basal-1.5-4.5B --mode fast --port 8000
```

Self-hosted inference has no TypeSafe charge; GPU/hosting costs are yours.

## Examples and demos

- [Hugging Face collection](https://huggingface.co/collections/Remek/basal-15-6ac0de0e9199d121c6adac20) and the leaderboard at [basal.si5.pl](https://basal.si5.pl/). Scores are maintainer-reported, not reproduced here.

## Limits and data handling

Independent research models, not Jev and not endorsed by TypeSafe; compatibility is with the request format, not guaranteed behavior parity. Weights are fine-tuned from Bielik base models (Apache-2.0 per the model cards). Benchmark figures are self-reported.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit c3cab778b8ca](https://github.com/rkinas/basal/tree/c3cab778b8cac8f1cc40ddfc982c5c809570c1e7). Inspected the README (engines, leaderboard, quick start), the repository LICENSE, and Hugging Face model-card license metadata; weights were not downloaded and no inference was run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
