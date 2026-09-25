# Jevlike

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jevlike is an independent training starter for scoring a changing menu of text options in one pass. It explores a Jev-related input/output pattern without using official Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vinnylarouge/jevlike) |
| Maintainer | [vinnylarouge](https://github.com/vinnylarouge); package/license credits Minimal Labs. |
| Format | Python training, evaluation, and prediction CLIs; optional visual game examples. |
| Relationship to Jev | Independent option-scoring model, not TypeSafe's model, training method, API, or SDK. |
| Requirements | Python 3.10+, NumPy, PyTorch; CPU, Apple MPS, or CUDA. Optional Transformers and game dependencies. |
| License | [MIT code](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/LICENSE); external models, datasets, and game assets retain their terms. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use this to learn how to train a small classifier over variable-length option lists, compare a byte encoder with a frozen pretrained encoder, or examine evaluation against a shuffled-context control.

The default synthetic exercise is a local training workflow. It does not demonstrate general language understanding or equivalence to official Jev.

## How it works

The [`AttentionHead`](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/jevlike/model.py) projects option vectors into queries over context tokens. Each option obtains an attended context vector and a score; masked softmax produces a distribution over the supplied choices.

The default `TinyScorer` trains byte and position embeddings from scratch. The optional `FrozenTransformerScorer` keeps a pretrained encoder frozen while training the shared attention head. Its checkpoint stores the encoder name and trained parameters, so loading can require the external encoder again.

The [data pipeline](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/jevlike/data.py) uses JSONL rows containing `context`, `options`, and a zero-based `label`. It validates training rows and pads variable option counts. Prediction returns each supplied option with its probability.

The project has no TypeSafe API/model version: all inference in this path uses its own trained scorer.

## Get started

The [upstream quickstart](https://github.com/vinnylarouge/jevlike#quickstart) creates synthetic data and trains a small local model:

```sh
git clone https://github.com/vinnylarouge/jevlike.git
cd jevlike
git checkout 94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452
python3 -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
jevlike-data synthetic --output data/synthetic
jevlike-train data/synthetic/train.jsonl \
  --validation data/synthetic/validation.jsonl \
  --output runs/synthetic.pt --device cpu
jevlike-eval runs/synthetic.pt data/synthetic/test.jsonl --device cpu
```

Package installation requires downloads; after installation this default synthetic path requires no provider key, external training dataset, or remote inference. Expect a checkpoint and evaluation metrics; their values depend on the actual run.

Use `jevlike-predict` with that checkpoint, a `--context`, and at least two repeated `--option` arguments, as shown in the [prediction example](https://github.com/vinnylarouge/jevlike#quickstart). It prints an option/probability JSON array.

The [frozen-encoder instructions](https://github.com/vinnylarouge/jevlike#use-a-frozen-pretrained-encoder) add Transformers and a Hugging Face model download. That route has different memory, provenance, and licensing requirements.

Commands above were inspected, not executed during this review.

## Examples and demos

- [Synthetic data generator](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/jevlike/data.py): produces labeled local menus for the starter workflow.
- [Smoke test](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/tests/test_smoke.py): trains a tiny scorer on synthetic examples and checks loss reduction and normalization; not a generalization benchmark.
- [Doom example](https://github.com/vinnylarouge/jevlike/tree/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/examples/doom) and [chess example](https://github.com/vinnylarouge/jevlike/tree/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/examples/chess): apply the visual option scorer to controller keys using extra dependencies/checkpoints.
- [Selected demo film](https://github.com/vinnylarouge/jevlike/blob/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452/docs/jevre-demo-10s-bgm.mp4): upstream-selected activity windows, not representative game competence.

## Limits and data handling

- Default byte inputs truncate context to 192 bytes and each option to 32 bytes. Important distinctions beyond those limits can disappear; configure lengths for the task.
- The scorer must receive the complete option list. Softmax normalization does not establish calibration or correctness; application code must supply an abstention/review policy.
- The optional Hugging Face path stores a model name without an immutable revision in its configuration. Reproduction depends on external weights remaining compatible.
- Checkpoint loading uses `torch.load(..., weights_only=False)`, which can execute serialized Python content. The default workflow above loads your own trained checkpoint; upstream/downloaded checkpoints require trust in their source.
- The local default pipeline reads datasets and writes checkpoints/results on your machine. Model and Wikispeedia download paths contact external hosts; no TypeSafe request is involved.
- External data splits and labels need separate review. A synthetic-menu result, a selected gameplay clip, or a decoder timing comparison does not establish official Jev equivalence.
- Hardware/compute costs and optional external licenses remain separate from the MIT source license.

## Review and maintenance

Reviewed **2026-09-19**, commit [`94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452`](https://github.com/vinnylarouge/jevlike/tree/94f5fd1b0b11d52bbdfdf4e0ee6aa96b568f8452).

Inspected README, MIT license, dependency/CLI manifest, attention-head and encoder implementation, checkpoint loading, data validation, train/eval arguments, prediction output, and the synthetic smoke test. Recorded the exact revision with `git rev-parse HEAD`.

Source inspection only: no installation, training, checkpoint deserialization, games, tests, or benchmarks were run. Published performance/quality figures and selected gameplay outcomes were not independently verified.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev use cases: nine patterns developers are building](../../knowledge-base/articles/jev-use-cases.md) — Mentioned in the source article. Pattern 9: learn how a local option scorer imitates Jev's interface.
<!-- knowledge:backlinks:end -->
