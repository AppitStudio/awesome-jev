# Wald-Q4B

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-weight 4B decision model: calibrated probabilities for choice/noul/score with a Jev-compatible `/v1/systemone` API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/org2AI/wald-4b) |
| Maintainer | [org2AI](https://github.com/org2AI). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python serving kit + Hugging Face BF16 weights (`Harry19081/Wald-4B`). |
| Requirements | Linux NVIDIA GPU recommended; `uv`/HF download per README. Self-hosted only. |
| License | [Apache-2.0](https://github.com/org2AI/wald-4b/blob/704ec0f9286fb09029ca08547f7810e7a2009f95/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent of TypeSafe AI; Jev-compatible open weights, not hosted Jev. |

## When to use

Use when you need a self-hosted Jev-compatible 4B decision API. Prefer TypeSafe hosted Jev when you want the product API without GPU ops.

## How it works

Serves choice/noul/score with optional thinking effort over POST /v1/systemone. Explicitly independent of TypeSafe; contains no Jev weights. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/org2AI/wald-4b.git
cd wald-4b
git checkout 704ec0f9286fb09029ca08547f7810e7a2009f95
# hf download Harry19081/Wald-4B --revision v1.1; follow ./run.sh in upstream README
```

Pin revision `704ec0f9286fb09029ca08547f7810e7a2009f95` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Not affiliated with TypeSafe. Decision Index / JevBench figures are author-run. Live GPU serve not executed on the review host.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 704ec0f](https://github.com/org2AI/wald-4b/tree/704ec0f9286fb09029ca08547f7810e7a2009f95). AI-assisted README and LICENSE inspection; install/live paths not executed.
