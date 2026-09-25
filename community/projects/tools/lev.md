# lev (Abhinavexists)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open System One decision model (Qwen3.5-4B LoRA): one state, many typed Choice/Noul/Score answers in one forward pass over `/v1/systemone`—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Abhinavexists/lev) |
| Maintainer | [Abhinavexists](https://github.com/Abhinavexists) / Interfaze-ai. Independently curated. |
| Format | Model + harness; weights on Hugging Face `interfaze-ai/lev`. |
| Requirements | Per upstream quickstart (serve container/GPU as documented); TypeSafe clients can retarget `base URL`. |
| License | [Apache-2.0](https://github.com/Abhinavexists/lev/blob/44a31fcd42d03616aa3072d6a060d5f3bca0726e/LICENSE). |
| Disclosure | Independent open model—not TypeSafe-hosted Jev. Upstream S1Bench figures are author-reported. AI-assisted catalog review; no affiliation. Live serve/bench not run on the review host. |

## When to use

Use to **run an open typed-decision model** with a TypeSafe-shaped wire protocol locally or on your GPU. Prefer hosted Jev for the official cloud model.

## How it works

lev answers all supplied typed questions in one forward pass from logits (zero output tokens). The harness measures against S1Bench manifests.

## Get started

```sh
git clone https://github.com/Abhinavexists/lev.git
cd lev
git checkout 44a31fcd42d03616aa3072d6a060d5f3bca0726e
# Follow README Quickstart / HF card: https://huggingface.co/interfaze-ai/lev
```

## Examples and demos

- Snake demo and S1Bench tables in the README; `docs/FINDINGS.md`.

## Limits and data handling

Not official Jev. Accuracy/latency claims are upstream-reported. Self-hosting keeps traffic on your infra once weights are local.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 44a31fc](https://github.com/Abhinavexists/lev/tree/44a31fcd42d03616aa3072d6a060d5f3bca0726e). AI-assisted README and LICENSE inspection; live inference not run.

Related: [TinyJev](tinyjev.md), [Malkuth](malkuth.md).
