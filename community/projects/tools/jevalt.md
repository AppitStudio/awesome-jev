# JevAlt

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open Jev-API–compatible Choice/Score/Noul models (EN/TR/DE) for CPU (~4 GB RAM); independent of hosted Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mertkayacs/jevalt) |
| Maintainer | [mertkayacs](https://github.com/mertkayacs). Independently curated. |
| Format | Python · open decision models (Apache-2.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/mertkayacs/jevalt/blob/eedfe68c45043062eff4f9068996c60c5417a4b0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Independent open decision models—not TypeSafe-hosted Jev. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/mertkayacs/jevalt.git
cd jevalt
git checkout eedfe68c45043062eff4f9068996c60c5417a4b0
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit eedfe68c4504](https://github.com/mertkayacs/jevalt/tree/eedfe68c45043062eff4f9068996c60c5417a4b0). AI-assisted README and license inspection; install/live paths not executed.
