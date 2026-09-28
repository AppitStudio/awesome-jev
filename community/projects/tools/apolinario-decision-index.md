# Decision Index (apolinario)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproduce the Decision Index benchmark for typed decision engines (choice/noul) locally or as one Hugging Face Job.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/apolinario/decision-index) |
| Maintainer | [apolinario](https://github.com/apolinario). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python benchmark reproduction kit (`decision_index` package). |
| Requirements | Python; optional Hugging Face Jobs; engine/API credentials for the models you score. |
| License | [MIT](https://github.com/apolinario/decision-index/blob/87d4650b42b377c0291a89c1f1a879f9b31082bf/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent of TypeSafe AI; not an official TypeSafe benchmark. |

## When to use

Use when reproducing or extending the public Decision Index for System One–style engines. Prefer hosted TypeSafe docs for product API usage.

## How it works

Rebuilds the frozen Decision Index suite from public sources, runs engines with checkpoint/resume, scores with the leaderboard scorers, and computes the index. Not affiliated with TypeSafe AI. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/apolinario/decision-index.git
cd decision-index
git checkout 87d4650b42b377c0291a89c1f1a879f9b31082bf
# follow upstream README / pyproject for install and run (local or HF Job)
```

Pin revision `87d4650b42b377c0291a89c1f1a879f9b31082bf` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent benchmark kit; not TypeSafe-affiliated. Full suite/provider runs not executed on the review host. Leaderboard numbers are upstream-reported.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 87d4650](https://github.com/apolinario/decision-index/tree/87d4650b42b377c0291a89c1f1a879f9b31082bf). AI-assisted README and LICENSE inspection; install/live paths not executed.
