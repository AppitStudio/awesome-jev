# llm-as-jev (Colab reproduction that fine-tunes Qwen3-0.6B into a Jev-style decision model)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Colab-friendly reproduction of the LLM-as-Jev recipe on `Qwen/Qwen3-0.6B` (full fine-tune, no LoRA), turning a causal LLM into a decision model that outputs a probability distribution over numbered options. In a single run the author reports macro ECE on six external sets falling from 0.262 to 0.118 and Banking77 accuracy rising from 0.185 to 0.603, and compares trends with the paper on 231 public JevBench items. Data and checkpoints are on Hugging Face.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hasnain1241/llm-as-jev) |
| Maintainer | [hasnain1241](https://github.com/hasnain1241). Independently curated. |
| Format | Python package + notebook |
| Requirements | Python 3 and a GPU (Colab works); Hugging Face access for the dataset and checkpoints. |
| License | [MIT](https://github.com/hasnain1241/llm-as-jev/blob/95ddb14e404b4e43e33907512c573ef4de16610c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`llm_as_jev/jevbench.py`](https://github.com/hasnain1241/llm-as-jev/blob/95ddb14e404b4e43e33907512c573ef4de16610c/llm_as_jev/jevbench.py) at the pinned commit. |

## When to use

- Experiment with training a small open model to answer Jev-style typed questions with calibrated probabilities.
- Mismatch: one seed and one 0.6B model; not TypeSafe's Jev and not a drop-in API.

## How it works

`jevbench.py` evaluates on public JevBench choice, noul and score items (never for training or checkpoint selection); `train.py` and `loss.py` run the fine-tune and `demo.py` shows option probabilities. Integration evidence: [`llm_as_jev/jevbench.py`](https://github.com/hasnain1241/llm-as-jev/blob/95ddb14e404b4e43e33907512c573ef4de16610c/llm_as_jev/jevbench.py).

## Get started

From the upstream README (not run on the review host):

```sh
from llm_as_jev import demo
demo.show(models, tok, "I lost my card", ["card arrival", "lost or stolen card", "exchange rate"])
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Checkpoints: [huggingface.co/Hasnain1241/llm-as-jev](https://huggingface.co/Hasnain1241/llm-as-jev)

## Limits and data handling

Runs locally; no TypeSafe API is called. Single-run results. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 95ddb14e404b](https://github.com/hasnain1241/llm-as-jev/tree/95ddb14e404b4e43e33907512c573ef4de16610c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
