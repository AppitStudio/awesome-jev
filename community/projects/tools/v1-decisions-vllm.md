# v1-decisions-vllm

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Proposed vLLM `/v1/decisions` typed-decision endpoint (Jev-compatible `/v1/systemone` projection) with pluggable logit/encoder/canvas backends—independent self-hosted serving research.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Timiku/v1-decisions-vllm) |
| Maintainer | [Timiku](https://github.com/Timiku). Independently curated. |
| Format | vLLM overlay/patch targeting stock vLLM v0.30.0; Apache-2.0. |
| Requirements | vLLM environment per upstream; GPU/CPU as required by chosen backend/model. |
| License | [Apache-2.0](https://github.com/Timiku/v1-decisions-vllm/blob/23fbc042c4321a2dab2eb7bcbb8508a8a51a5ea6/LICENSE). Self-hosted—not TypeSafe-hosted Jev. |
| Disclosure | Independent of hosted TypeSafe Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from [vLLM Jev](vllm-jev.md) / [vLLM Jev (mode-io)](mode-io-vllm-jev.md). Install/serve not run on the review host. |

## When to use

Use when experimenting with a modular typed-decisions API on vLLM (including Laya encoder / DiffusionGemma canvas backends). Prefer existing vllm-jev servers for simpler stock serving.

## How it works

`/v1/decisions` unifies backends; `/v1/systemone` projects to TypeSafe’s request shape. Default `logit` backend reads option logprobs from generative checkpoints; `encoder`/`canvas` need vendored patches noted upstream.

## Get started

```sh
git clone https://github.com/Timiku/v1-decisions-vllm.git
cd v1-decisions-vllm
git checkout 23fbc042c4321a2dab2eb7bcbb8508a8a51a5ea6
# follow upstream for vLLM overlay build and serve
```

## Examples and demos

- Upstream README backend table and extension entry points.

## Limits and data handling

Self-hosted inference keeps requests on your infrastructure. Catalog checks did not build or serve vLLM.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 23fbc04](https://github.com/Timiku/v1-decisions-vllm/tree/23fbc042c4321a2dab2eb7bcbb8508a8a51a5ea6). AI-assisted README and license inspection; install/live paths not executed.
