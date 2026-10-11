# RimeJev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context-aware Chinese input candidate recommendations for Squirrel + Rime on macOS, using Jev in the cloud and/or local models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IIIIOvOIIII/RimeJev) |
| Maintainer | [IIIIOvOIIII](https://github.com/IIIIOvOIIII). Independently curated. |
| Format | macOS input-method add-on |
| Requirements | Apple Silicon macOS; Squirrel + Rime + Wanxiang; optional Jev API key (local-only mode needs none). |
| License | [GPL-3.0](https://github.com/IIIIOvOIIII/RimeJev/blob/1f227b44dafaaf945eb683f529b11869a045b833/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Get context-aware reordering of Rime Chinese candidates on macOS.
- Mismatch: non-macOS or non-Rime users; enhancement is off by default and cloud mode sends input context to Jev.

## How it works

Base input never waits on the model; recommendations arrive asynchronously, mark hits on the native first candidate, and place model picks in second/third slots, with global defaults and per-app overrides. (Summarized from the upstream [README](https://github.com/IIIIOvOIIII/RimeJev/blob/1f227b44dafaaf945eb683f529b11869a045b833/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Clone the repo and follow the upstream LLM_INSTALL.md (`uv sync --frozen`, checks, backup, install).

## Limits and data handling

In cloud mode, typing context is sent to the hosted Jev API; keys are stored in the macOS Keychain per upstream. Secure input fields are excluded per upstream. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 1f227b44dafa](https://github.com/IIIIOvOIIII/RimeJev/tree/1f227b44dafaaf945eb683f529b11869a045b833). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
