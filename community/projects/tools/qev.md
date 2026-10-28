# Qev (open Jev-like decision models fine-tuned from Qwen, 0.8B to 9B, with weights on Hugging Face)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open decision models built by fine-tuning Qwen: give context, a question and candidate answers and get a choice with a probability for every option, across Choice, Noul and Score. Ships architecture, training and evaluation code, a Python interface and four checkpoint sizes on Hugging Face, with benchmarks against Jev and other open decision models (Kev, JevAny). Builds on Jared Palmer's Kev conventions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/QiqianFu/Qev) |
| Maintainer | [QiqianFu](https://github.com/QiqianFu). Independently curated. |
| Format | Python package with model weights |
| Requirements | Python 3.12 and PyTorch 2.8; a GPU for the larger sizes. No TypeSafe key needed. |
| License | [Apache-2.0](https://github.com/QiqianFu/Qev/blob/0760496c32ef3aef74eb1fc5b4a7213671e670df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`results/README.md`](https://github.com/QiqianFu/Qev/blob/0760496c32ef3aef74eb1fc5b4a7213671e670df/results/README.md) at the pinned commit. |

## When to use

- Run a Jev-style decision model locally or fine-tune one on your own labels.
- Mismatch: not TypeSafe's model; benchmark numbers are the author's.

## How it works

Qev adds a decision head to a Qwen backbone; `results/README.md` and `results/benchmarks.json` hold the comparison with Jev and other decision models. Integration evidence: [`results/README.md`](https://github.com/QiqianFu/Qev/blob/0760496c32ef3aef74eb1fc5b4a7213671e670df/results/README.md).

## Get started

From the upstream README (not run on the review host):

```sh
python3.12 -m venv .venv && source .venv/bin/activate
# install the PyTorch 2.8.0 build for your hardware first
python -m pip install -e .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Weights: [huggingface.co/AustinFu/Qev-4B](https://huggingface.co/AustinFu/Qev-4B)
- README: [github.com/QiqianFu/Qev#readme](https://github.com/QiqianFu/Qev#readme)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 0760496c32ef](https://github.com/QiqianFu/Qev/tree/0760496c32ef3aef74eb1fc5b4a7213671e670df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
