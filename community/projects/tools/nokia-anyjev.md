# AnyJev (Nokia Applied Research)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Turn an open LLM into a Jev-style typed decision model (Choice/Noul/Score with probabilities) via position-debiasing and optional calibration/heads—no TypeSafe hosted Jev and no fine-tune required for L0. Distinct from any MorrisZJ/AnyJev fork; independent of official Jev weights.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nokia-applied-research/AnyJev) |
| Maintainer | [nokia-applied-research](https://github.com/nokia-applied-research) (authors: Jiamu Zhang, Tianze Yang, Yucheng Shi, Liang Wu). Independently curated; this entry is not an upstream submission or endorsement. Not affiliated with TypeSafe AI. |
| Format | Python package **`anyjev` 0.1.0** (PyPI; `pip install "anyjev[hf]"`). Transformers backend today; vLLM/SGLang on roadmap. |
| Requirements | Python ≥ 3.10; Hugging Face model weights for live LLM readout (`torch`/`transformers` extras). Offline `demo` with `--backend fake` needs no download. |
| License | [Apache-2.0](https://github.com/nokia-applied-research/AnyJev/blob/3cd8c6fcd9e90fc04214575ade6779da1e3f3704/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, pyproject, package layout). Live model downloads and reported BANKING77 numbers were **not** reproduced on the review host. Upstream benchmarks are author-reported. |

## When to use

Use it to study or deploy Jev-shaped decisions on your own open models with L0 (training-free), L1 (temperature), or L2 (closed-form early-exit heads). Prefer hosted [TypeSafe Jev](https://docs.typesafe.ai) when you want the official System One API; prefer [Open Alternative to Jev](open-alternative-jev.md) for other open-model comparison labs.

## How it works

`Decider` + backend read next-token distributions for typed questions. L0 averages cyclic option rotations and divides out a label prior; L1 adds temperature; L2 fits a small head on hidden states (~⅔ depth) from a few hundred labels. Every `Decision` carries its `level` for downstream gating.

## Get started

```sh
pip install "anyjev[hf]"
# or from source:
git clone https://github.com/nokia-applied-research/AnyJev.git
cd AnyJev
git checkout 3cd8c6fcd9e90fc04214575ade6779da1e3f3704
python -m demo.jev_mode --backend fake   # no download
```

## Examples and demos

- README usage with `Question.choice` / `noul` / `score`.
- `demo/` lifecycle scripts; shipped heads under `anyjev-heads/`.
- Bench docs: `docs/results_bench.md` (author-reported).

## Limits and data handling

Local inference sends prompts only to your chosen backend—not to TypeSafe. Not a drop-in replacement for official Jev behavior or pricing. Pre-Alpha classifiers. This listing did not download Qwen weights or re-run benches.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 3cd8c6f](https://github.com/nokia-applied-research/AnyJev/tree/3cd8c6fcd9e90fc04214575ade6779da1e3f3704) (**0.1.0**, Apache-2.0). AI-assisted source review of README, LICENSE, pyproject. No live model spend.

Related: [Open Alternative to Jev](open-alternative-jev.md), [Jev-Omni](jev-omni.md), [SemIf](semif.md).
