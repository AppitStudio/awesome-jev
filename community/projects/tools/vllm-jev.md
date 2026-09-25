# vLLM Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Native vLLM serving for Jev-style decision checkpoints: Choice, Noul, and Score over HTTP with automatic HF model prep.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Egbertjing/vllm-jev) |
| Maintainer | [Egbertjing](https://github.com/Egbertjing). Independently curated. |
| Format | Python package (`vllm-jev serve`) on top of vLLM. |
| Requirements | Python + uv; GPU/host suitable for vLLM; Hugging Face access for supported checkpoints (e.g. `ZefanCai/Open-Jev-2B`). |
| License | [Apache-2.0](https://github.com/Egbertjing/vllm-jev/blob/1ac226012d3e856c897f776106b7e4e9e6caca45/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **self-host Jev-compatible decision models** through vLLM batching/metrics instead of calling the hosted TypeSafe API.

## How it works

Launcher downloads/prepares a supported HF ID, then serves candidate decisions and probabilities via native vLLM protocols (scalar branches or marker-token scores per model format).

## Get started

```sh
git clone https://github.com/Egbertjing/vllm-jev.git
cd vllm-jev
git checkout 1ac226012d3e856c897f776106b7e4e9e6caca45
uv pip install .
vllm-jev serve ZefanCai/Open-Jev-2B
```

## Examples and demos

- README quickstart and `docs/guide.md`.
- Default listen `http://127.0.0.1:8795`.

## Limits and data handling

Not the hosted TypeSafe Jev service—compatibility depends on the checkpoint. Serving needs local GPU/resources; training is out of scope.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 1ac2260](https://github.com/Egbertjing/vllm-jev/tree/1ac226012d3e856c897f776106b7e4e9e6caca45). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [Open-Jev ecosystem listings](README.md#independent-model-research), [Mechanical Jev](mechanical-jev.md).
