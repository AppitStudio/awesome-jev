# GS1 by BIGAI (open-weight System One decision models from 0.8B to 9B with native Choice, Noul and Score heads)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Family of open-weight decision models (GS1-0.8B, 2B, 4B and 9B on Hugging Face) from the Beijing Institute for General Artificial Intelligence. A native decision head returns Choice, Noul and Score distributions with zero generated tokens; the runtime serves `POST /v1/systemone`, so the official TypeSafe SDK can point at it, and a playground compares it with hosted Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bigai-nlco/GS1) |
| Maintainer | [BIGAI NLCo Lab](https://github.com/bigai-nlco). Independently curated. |
| Format | Python runtime and Hugging Face weights (PyTorch) |
| Requirements | Python 3.11+, PyTorch 2.9.1 and Transformers 5.3.0; Linux with CUDA for the runtime. |
| License | [Apache-2.0](https://github.com/bigai-nlco/GS1/blob/f6c7b05469aef6fab3e803886b34167deaf44757/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gs1/api/app.py`](https://github.com/bigai-nlco/GS1/blob/f6c7b05469aef6fab3e803886b34167deaf44757/gs1/api/app.py) at the pinned commit. |

## When to use

- Run Jev-style typed decisions on your own GPU with an SDK-compatible endpoint.
- Mismatch: if you want TypeSafe's hosted Jev; GS1 is a separate model family.

## How it works

`gs1/api/app.py` exposes a TypeSafe-compatible `/v1/systemone` and `/v1/models`; `examples/typesafe_client.py` uses the TypeSafe Python SDK against it with `api_key="local"`. These are BIGAI's own models, not TypeSafe's Jev; the playground calls hosted Jev only if you export `TYPESAFE_API_KEY`. Integration evidence: [`gs1/api/app.py`](https://github.com/bigai-nlco/GS1/blob/f6c7b05469aef6fab3e803886b34167deaf44757/gs1/api/app.py).

## Get started

Clone, install with uv, then serve a model locally.

```sh
git clone https://github.com/bigai-nlco/GS1.git
cd GS1
uv sync --locked --extra serve --extra cuda
uv run gs1 serve --model bigai/GS1-0.8B --model-name GS1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/bigai-nlco/GS1/blob/f6c7b05469aef6fab3e803886b34167deaf44757/benchmark/results.md](https://github.com/bigai-nlco/GS1/blob/f6c7b05469aef6fab3e803886b34167deaf44757/benchmark/results.md)
- Models: [huggingface.co/collections/bigai/gs1](https://huggingface.co/collections/bigai/gs1)

## Limits and data handling

Decision Index figures (56.12 to 70.45) and latency claims are BIGAI's own. Weights download from Hugging Face; a GPU is needed for practical speed.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit f6c7b05469ae](https://github.com/bigai-nlco/GS1/tree/f6c7b05469aef6fab3e803886b34167deaf44757). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
