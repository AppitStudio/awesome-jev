# ProbabilityBench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of text worlds with exact ground-truth class probabilities (peer review, covert transfer, credit risk), with an example that scores decision models such as TypeSafe Jev against the true probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ishida-lab/ProbabilityBench) |
| Maintainer | [ishida-lab](https://github.com/ishida-lab). Independently curated. |
| Format | Python package (`uv`) + Hugging Face dataset + paper |
| Requirements | Python, `uv`; an OpenRouter key to query decision models (about US$2 or less per model for a full run, per the README). |
| License | [MIT](https://github.com/ishida-lab/ProbabilityBench/blob/b376bef69edcd3376c5dcc06950f2ad2c41172b1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/decision_models.py`](https://github.com/ishida-lab/ProbabilityBench/blob/b376bef69edcd3376c5dcc06950f2ad2c41172b1/examples/decision_models.py) at the pinned commit. |

## When to use

- Evaluate whether Jev's reported probabilities match the true conditional probability, not just the label.
- Add your own decision model to the same protocol.
- Mismatch: Jev is reached through OpenRouter (`typesafe/jev-1.13`); results are the authors'.

## How it works

Each world renders memos from hidden variables with known outcome probabilities; `examples/decision_models.py run` sends cases to decision models on OpenRouter, saves their positive-class probabilities, and `score`/`plot` compare them with the exact probabilities and reported cost. Integration evidence: [`examples/decision_models.py`](https://github.com/ishida-lab/ProbabilityBench/blob/b376bef69edcd3376c5dcc06950f2ad2c41172b1/examples/decision_models.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ishida-lab/ProbabilityBench.git && cd ProbabilityBench
uv run python examples/decision_models.py run --limit 5
uv run python examples/decision_models.py score
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2610.17016](https://arxiv.org/abs/2610.17016)
- Dataset: [huggingface.co/datasets/ishidalab/probabilitybench](https://huggingface.co/datasets/ishidalab/probabilitybench)

## Limits and data handling

Synthetic memos go to OpenRouter and the model provider on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit b376bef69edc](https://github.com/ishida-lab/ProbabilityBench/tree/b376bef69edcd3376c5dcc06950f2ad2c41172b1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
