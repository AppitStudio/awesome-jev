# openjevx

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-weight Jev-compatible System One decision server for jevx—local `/v1/systemone` from a Laya fine-tune.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muthuishere/openjevx) |
| Maintainer | [muthuishere](https://github.com/muthuishere). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go server + release binaries / Docker; HF model card. |
| Requirements | Binary or Docker; CPU or CUDA GPU; pairs with [jevx (muthuishere)](muthuishere-jevx.md). |
| License | [Apache-2.0](https://github.com/muthuishere/openjevx/blob/6fccc9b31fb00fb2804a4d5d224df0e3350d96b3/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent open weights; pairs with [jevx (muthuishere)](muthuishere-jevx.md). LICENSE file is Apache-2.0 (GitHub SPDX was NOASSERTION). |

## When to use

Use when you want a local open-weight System One backend for jevx instead of hosted TypeSafe. Prefer hosted Jev when you need the official model.

## How it works

Serves `POST /v1/systemone` on 127.0.0.1:21118 by default for jevx and other System One clients. Open weights fine-tuned from Laya with RLCD. GitHub license API reported NOASSERTION; repository `LICENSE` is Apache-2.0. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/muthuishere/openjevx.git
cd openjevx
git checkout 6fccc9b31fb00fb2804a4d5d224df0e3350d96b3
# or: npx git+https://github.com/muthuishere/openjevx.git && openjevx
# Docker: docker compose up -d --build
```

Pin revision `6fccc9b31fb00fb2804a4d5d224df0e3350d96b3` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent open weights; not official Jev. Server/model load not run on the review host. Distinct from hosted TypeSafe Jev and from the jevx client listing.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 6fccc9b](https://github.com/muthuishere/openjevx/tree/6fccc9b31fb00fb2804a4d5d224df0e3350d96b3). AI-assisted README and LICENSE inspection; install/live paths not executed.
