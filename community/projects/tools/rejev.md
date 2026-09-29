# ReJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible MiniCPM5-2B post-training for Jev-style single-letter Choice decisions, with sealed holdout evaluation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Joe-rq/ReJev) |
| Maintainer | [Joe-rq](https://github.com/Joe-rq). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python training/eval research repository. |
| Requirements | GPU/training stack per technical report; not a drop-in TypeSafe API client. |
| License | [MIT](https://github.com/Joe-rq/ReJev/blob/96342164325b744eac08e811314be8f4b1dbf10c/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent research; not affiliated with TypeSafe AI. |

## When to use

Use when studying how to post-train small decision models. Prefer TypeSafe hosted Jev for production judgments.

## How it works

Runs data → LoRA → constrained decoding evaluation for state+question+options → one decision. Aims to study mechanics, not claim Jev equivalence. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/Joe-rq/ReJev.git
cd ReJev
git checkout 96342164325b744eac08e811314be8f4b1dbf10c
# follow README / docs/report for training and eval
```

Pin revision `96342164325b744eac08e811314be8f4b1dbf10c` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Research reproduction; accuracy figures are upstream. Training not re-run on the review host. Not TypeSafe-affiliated.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 9634216](https://github.com/Joe-rq/ReJev/tree/96342164325b744eac08e811314be8f4b1dbf10c). AI-assisted README and LICENSE inspection; install/live paths not executed.
