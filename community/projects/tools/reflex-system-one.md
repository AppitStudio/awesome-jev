# Reflex System One

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Windows-first, self-contained launcher that installs a portable Python runtime, downloads pinned open decision-model checkpoints (Laya, Decider, Sol, Nox) and serves them on localhost through a System One–style `POST /v1/systemone` API, with a console demo mode, model manager and doctor/repair tools. Independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JRodrigoTech/reflex-system-one) |
| Maintainer | [JRodrigoTech](https://github.com/JRodrigoTech). Independently curated. |
| Format | Windows batch/Python launcher + local HTTP server |
| Requirements | Windows 10/11 x64; internet for first runtime/model downloads; NVIDIA GPU optional for some models and required for Sol and Nox. |
| License | [MIT](https://github.com/JRodrigoTech/reflex-system-one/blob/5bfda7af5b1d51aae43a2cf44eabc257fd2749ab/LICENSE) for Reflex code; models and third-party packages keep their own terms ([notices](https://github.com/JRodrigoTech/reflex-system-one/blob/5bfda7af5b1d51aae43a2cf44eabc257fd2749ab/THIRD_PARTY_NOTICES.md)). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Try local typed decisions on Windows with a Jev-shaped request, without setting up Python yourself.
- Mismatch: not official Jev; behavior depends on the selected open model.

## How it works

The server exposes `POST /v1/systemone`, `GET /v1/models` and `GET /health` on `127.0.0.1:1919`; model choices and qualification runs are recorded in [`manifests/`](https://github.com/JRodrigoTech/reflex-system-one/blob/5bfda7af5b1d51aae43a2cf44eabc257fd2749ab/manifests/models.json). See the upstream [README](https://github.com/JRodrigoTech/reflex-system-one/blob/5bfda7af5b1d51aae43a2cf44eabc257fd2749ab/README.md) for the request format and model table.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JRodrigoTech/reflex-system-one.git
cd reflex-system-one
.\reflex.bat
```

## Limits and data handling

Inference runs locally; the README states request and decision content is excluded from normal logs. Model downloads range from under 1 GiB to several GiB. Not run on the review host (Windows-only).

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 5bfda7af5b1d](https://github.com/JRodrigoTech/reflex-system-one/tree/5bfda7af5b1d51aae43a2cf44eabc257fd2749ab). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
