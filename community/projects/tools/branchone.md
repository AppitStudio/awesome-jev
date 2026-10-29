# BranchOne by Necati Demir (open System One decision model that scores supplied choices from text and an optional image)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open decision model in the Jev category: send a situation, a question and 2–150 candidate descriptions (optionally one image) and it returns a probability per candidate and the selected ID. Built on Qwen3.5-0.8B-Base with LoRA adapters and a small scoring head shared across candidates; the release includes calibration and inference code, and a separate GitHub repo has data prep and training. Not TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://huggingface.co/ndemirdemir/BranchOne) |
| Maintainer | [ndemir](https://github.com/ndemir). Independently curated. |
| Format | Model weights and inference code (Hugging Face, transformers custom code) |
| Requirements | Linux x86-64, Python 3.13 and an NVIDIA CUDA GPU (Colab works). |
| License | [Apache-2.0](https://huggingface.co/ndemirdemir/BranchOne/blob/d3ce9ae4ca4fdf0502b028d47ebed38094836fe6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ndemir/status/2115798561640030268)). |
| Jev evidence | [`modeling_branchone.py`](https://huggingface.co/ndemirdemir/BranchOne/blob/d3ce9ae4ca4fdf0502b028d47ebed38094836fe6/modeling_branchone.py) at the pinned release. |

## When to use

- Try a small open choice model on your own GPU and train it on your labels.
- Mismatch: not TypeSafe's Jev; ten illustrative examples are not a benchmark.

## How it works

`modeling_branchone.py` encodes the situation and question once per candidate, scores each with the shared head and returns temperature-scaled probabilities and the selected ID. Integration evidence: [`modeling_branchone.py`](https://huggingface.co/ndemirdemir/BranchOne/blob/d3ce9ae4ca4fdf0502b028d47ebed38094836fe6/modeling_branchone.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m uv tool run --from huggingface-hub==1.33.0 hf download ndemirdemir/BranchOne --local-dir BranchOne
python3 BranchOne/install.py --venv .venv
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's write-up: [n.demir.io/articles/branchone-system-one-decision-model/](https://n.demir.io/articles/branchone-system-one-decision-model/)
- Training code (no license file on the reviewed commit): [github.com/ndemir/BranchOne](https://github.com/ndemir/BranchOne)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe. The Apache-2.0 license covers the Hugging Face release; the GitHub training repo had no license file when reviewed.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [Hugging Face revision d3ce9ae4ca4f](https://huggingface.co/ndemirdemir/BranchOne/tree/d3ce9ae4ca4fdf0502b028d47ebed38094836fe6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
