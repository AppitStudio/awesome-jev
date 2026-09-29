# Deqio

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Run fast typed AI decision models (choice, score, yes/no) behind one local API with multiple engines and hardware backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ILuce/deqio) |
| Maintainer | [ILuce](https://github.com/ILuce). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python local decision-model server and browser UI. |
| Requirements | Python; model/backend hardware per chosen engine (MLX/MPS/CUDA as documented). |
| License | [MIT](https://github.com/ILuce/deqio/blob/41eeb1dc2eeda272b992f474adcb5d19a976e0bd/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent multi-engine host; not TypeSafe-hosted Jev. |

## When to use

Use when you want one local API in front of several System One–style engines. Prefer TypeSafe docs for the hosted Jev product.

## How it works

Exposes stable POST /v1/noul, /v1/choice, /v1/shared endpoints while swapping installed decision engines (including Open-Jev and other System One–style models). Independent of the TypeSafe hosted API. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ILuce/deqio.git
cd deqio
git checkout 41eeb1dc2eeda272b992f474adcb5d19a976e0bd
# follow upstream README for install, engine download, and deqio serve
```

Pin revision `41eeb1dc2eeda272b992f474adcb5d19a976e0bd` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Multi-engine host; not TypeSafe-hosted Jev. Author bench numbers not reproduced. Live engine serving not run on the review host.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 41eeb1d](https://github.com/ILuce/deqio/tree/41eeb1dc2eeda272b992f474adcb5d19a976e0bd). AI-assisted README and LICENSE inspection; install/live paths not executed.
