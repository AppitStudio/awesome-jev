# OpenChoice-9B (CPU-first open decision model with a System One-compatible API)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open decision model built from Qwen3.5-9B plus a decision LoRA, merged to GGUF (about 5.8 GiB with the vision projector) and served on CPU: it returns probabilities for Choice, Score and Noul questions over a wire format compatible with TypeSafe's SDK, reads long inputs, and ships a LoRA fine-tuning kit that exports back to the same server. Not affiliated with TypeSafe; official JevBench scores pending.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lutr0/openchoice) |
| Maintainer | [lutr0](https://github.com/lutr0). Independently curated. |
| Format | Python server (llama.cpp) and GGUF weights |
| Requirements | Linux x86-64, uv, Git, Make and a C++17 compiler; 6-7 GiB RAM. |
| License | [Apache-2.0](https://github.com/lutr0/openchoice/blob/7c3a409de79475c94d3a797a3495acb0bd53ab78/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`openchoice/server.py`](https://github.com/lutr0/openchoice/blob/7c3a409de79475c94d3a797a3495acb0bd53ab78/openchoice/server.py) at the pinned commit. |

## When to use

- Run Jev-style typed decisions locally on CPU.
- Fine-tune on your own labels and serve the result.
- Mismatch: not TypeSafe's Jev; the author reports it trails Jev on every aggregate benchmark they compared.

## How it works

`openchoice/server.py` serves a `/v1/systemone`-compatible endpoint over the GGUF model; `openchoice/llamacpp.py` reads exact logits for each option. Integration evidence: [`openchoice/server.py`](https://github.com/lutr0/openchoice/blob/7c3a409de79475c94d3a797a3495acb0bd53ab78/openchoice/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/lutr0/openchoice && cd openchoice
uv run hf download lutr0/OpenChoice-9B --local-dir ./OpenChoice-9B-GGUF
uv run python -m openchoice.server --model ./OpenChoice-9B-GGUF --port 8768
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lutr0/openchoice#readme](https://github.com/lutr0/openchoice#readme)

## Limits and data handling

Runs on your hardware; nothing goes to TypeSafe. Base-model licence terms apply to the weights.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7c3a409de794](https://github.com/lutr0/openchoice/tree/7c3a409de79475c94d3a797a3495acb0bd53ab78). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
