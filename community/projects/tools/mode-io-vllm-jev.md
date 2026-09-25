# vLLM Jev (mode-io)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Native vLLM serving for Jev-style Choice/Noul/Score checkpoints over HTTP (text and multimodal)—distinct from the separate [Egbertjing/vllm-jev](vllm-jev.md) listing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mode-io/vllm-jev) |
| Maintainer | [mode-io](https://github.com/mode-io). Independently curated. |
| Format | Python package (`vllm-jev serve`) on top of vLLM. |
| Requirements | GPU-capable host with vLLM; Hugging Face model ID (for example `ZefanCai/Open-Jev-2B`); `uv` install from the repo. |
| License | [Apache-2.0](https://github.com/mode-io/vllm-jev/blob/e8818126399765345c93b4069f05fd14845acb84/LICENSE). |
| Disclosure | Independent serving stack for open decision checkpoints—not TypeSafe-hosted Jev. Distinct owner/repo from Egbertjing/vllm-jev. AI-assisted catalog review; no affiliation. Live GPU serve not run on the review host. |

## When to use

Use to **batch and schedule** open Jev-compatible checkpoints under vLLM (including multimodal Valen/vjev paths documented upstream). Prefer Egbertjing/vllm-jev only when you specifically want that package's interface.

## How it works

`vllm-jev serve <HF_ID>` prepares a supported checkpoint and exposes native decision readouts (scalar branches or marker-token scores) as Choice/Noul/Score over HTTP.

## Get started

```sh
git clone https://github.com/mode-io/vllm-jev.git
cd vllm-jev
git checkout e8818126399765345c93b4069f05fd14845acb84
uv pip install .
vllm-jev serve ZefanCai/Open-Jev-2B
```

## Examples and demos

- README Sokoban and Open-Jev-2B concurrency GIFs (upstream-recorded).
- [docs/guide.md](https://github.com/mode-io/vllm-jev/blob/e8818126399765345c93b4069f05fd14845acb84/docs/guide.md) for models and flags.

## Limits and data handling

Requires a suitable GPU and downloads HF weights. Not a TypeSafe cloud endpoint. Demo metrics are upstream-reported.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit e881812](https://github.com/mode-io/vllm-jev/tree/e8818126399765345c93b4069f05fd14845acb84). AI-assisted README and LICENSE inspection; live vLLM serve not run.

Related: [vLLM Jev (Egbertjing)](vllm-jev.md), [TinyJev](tinyjev.md).
