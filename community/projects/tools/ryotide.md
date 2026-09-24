# RYOTIDE

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Roll Your Own Typed Inference Decision Engine: Jev-style typed decisions from a single forward pass of a local LLM (MLX or PyTorch), measured on JevBench.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/csabag/ryotide) |
| Maintainer | [csabag](https://github.com/csabag). Independently curated. |
| Format | Python research package. |
| Requirements | Python; MLX (Apple Silicon) or PyTorch; local model weights. |
| License | [MIT](https://github.com/csabag/ryotide/blob/385d919da4ebd3a30c5c6a0f6f141c5d65b6d620/LICENSE). |
| Disclosure | Independent of official TypeSafe Jev weights. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live bench not re-run. |

## When to use

Use to **experiment** with local LLM logprob-style typed classifiers comparable to Jev. Prefer hosted TypeSafe Jev for production System One.

## How it works

One forward pass with masked logits yields typed answers; README ties measurement to JevBench (per upstream).

## Get started

```sh
git clone https://github.com/csabag/ryotide.git
cd ryotide
git checkout 385d919da4ebd3a30c5c6a0f6f141c5d65b6d620
# follow README for MLX/PyTorch setup
```

## Examples and demos

- README JevBench measurement notes.

## Limits and data handling

Runs locally; model licenses apply separately. Not a drop-in Jev replacement.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 385d919](https://github.com/csabag/ryotide/tree/385d919da4ebd3a30c5c6a0f6f141c5d65b6d620). AI-assisted README inspection; live MLX/PyTorch path not run.

Related: [AnyJev (Nokia Applied Research)](nokia-anyjev.md).
