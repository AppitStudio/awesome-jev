# japanese-jev (unofficial small Japanese decision model on Qwen3 + LoRA, benchmarked against the Jev API and used as a local-first cascade)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Unofficial reproduction of the System One approach for Japanese: a Qwen3-Base model (1.7B or 0.6B) with a LoRA adapter returns a probability per option in one forward pass for Choice, Noul and Score questions, trained on an 8 GB laptop GPU, and served behind a `/v1/systemone`-shaped FastAPI endpoint. The README compares its accuracy with the real Jev API (Jev 1.14 via OpenRouter) on the same items and tests a cascade that answers locally when confident and sends the rest to Jev. Weights are on Hugging Face.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bigrh0917/japanese-jev-release) |
| Maintainer | [bigrh0917](https://github.com/bigrh0917). Independently curated. |
| Format | Python package and CLI, LoRA weights on Hugging Face, eval sets |
| Requirements | Python, an NVIDIA GPU for local inference or training, and an OpenRouter or Vercel AI Gateway key to rerun the Jev comparison. |
| License | [MIT (data and weights have their own terms; see LICENSES.md)](https://github.com/bigrh0917/japanese-jev-release/blob/6af08f983dede33f292832848474c01c70265fa0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/eval_jev_api.py`](https://github.com/bigrh0917/japanese-jev-release/blob/6af08f983dede33f292832848474c01c70265fa0/scripts/eval_jev_api.py) at the pinned commit. |

## When to use

- Try a local Japanese decision model, or a local-first cascade that calls Jev only when unsure.
- Mismatch: a drop-in Jev replacement; it is a small unofficial model with lower accuracy on harder tasks.

## How it works

`scripts/eval_jev_api.py` sends the evaluation items to Jev through OpenRouter (`typesafe/jev-1.14`) or Vercel AI Gateway (`typesafe-ai/jev`) with the same request shape, to compare with the local model. Integration evidence: [`scripts/eval_jev_api.py`](https://github.com/bigrh0917/japanese-jev-release/blob/6af08f983dede33f292832848474c01c70265fa0/scripts/eval_jev_api.py).

## Get started

Install with uv, serve a trained run locally, and rerun the Jev comparison (see docs/usage.md).

```sh
git clone https://github.com/bigrh0917/japanese-jev-release && cd japanese-jev-release
uv sync && source .venv/bin/activate
japanese-jev serve --config configs/qwen3-1.7b-ja.json --work-dir runs/<dir>    # local /v1/systemone endpoint
export OPENROUTER_API_KEY=...
python scripts/eval_jev_api.py --via openrouter --limit 2    # compare with Jev on 2 items first
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bigrh0917/japanese-jev-release/blob/6af08f983dede33f292832848474c01c70265fa0/README.md](https://github.com/bigrh0917/japanese-jev-release/blob/6af08f983dede33f292832848474c01c70265fa0/README.md)
- Weights (1.7B): [huggingface.co/bigrh0917/japanese-jev-qwen3-1.7b-lora](https://huggingface.co/bigrh0917/japanese-jev-qwen3-1.7b-lora)

## Limits and data handling

The local model runs on your GPU; only the comparison or cascade fallback sends items to Jev on your OpenRouter or Vercel key. Not affiliated with TypeSafe. The maker notes the cascade threshold was chosen on the test set, so treat it as a rough guide.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 6af08f983ded](https://github.com/bigrh0917/japanese-jev-release/tree/6af08f983dede33f292832848474c01c70265fa0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
