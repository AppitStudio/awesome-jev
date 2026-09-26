# laya-guardrails

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted Laya System One guardrails—typed checks instead of LLM-as-judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/javimp2003/laya-guardrails) |
| Maintainer | [javimp2003](https://github.com/javimp2003). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python FastAPI service targeting NVIDIA L4 / RunPod with Hugging Face `laya-pt-es-typed`. |
| Requirements | Python 3.10+; GPU recommended; Hugging Face model weights. |
| License | [Apache-2.0](https://github.com/javimp2003/laya-guardrails/blob/adec33c05a3d83934a41df4dcf65205be983af88/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when you want local System One-style guardrails in ES/PT without calling hosted Jev.

## How it works

State + typed noul/choice/score questions → probabilities → `config/policy.json` decides allow/block. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/javimp2003/laya-guardrails.git
cd laya-guardrails
git checkout adec33c05a3d83934a41df4dcf65205be983af88
# follow upstream README for model download and FastAPI serve
```

Pin revision `adec33c05a3d83934a41df4dcf65205be983af88` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent of TypeSafe hosted Jev. Spanish/Portuguese focus. Live GPU path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit adec33c](https://github.com/javimp2003/laya-guardrails/tree/adec33c05a3d83934a41df4dcf65205be983af88). AI-assisted README and LICENSE inspection; install/live paths not executed.
