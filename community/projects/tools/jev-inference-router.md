# jev-inference-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Observable TypeSafe Jev decision routing with local Apple Silicon LLM inference, retrieval, and reproducible evaluations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sunilmehta-si/jev-inference-router) |
| Maintainer | [sunilmehta-si](https://github.com/sunilmehta-si). Independently curated. |
| Format | Python FastAPI service |
| Requirements | Python; TypeSafe key; local LLM setup per README (Apple Silicon oriented). |
| License | [MIT](https://github.com/sunilmehta-si/jev-inference-router/blob/130f16681dba5c26fc938c74654726ff0c0d0f05/LICENSE) |
| Jev evidence | [`jev_router/decision.py`](https://github.com/sunilmehta-si/jev-inference-router/blob/130f16681dba5c26fc938c74654726ff0c0d0f05/jev_router/decision.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Prototype model-aware inference routing where Jev chooses the path and local models generate.
- Mismatch: Demo/lab oriented; Apple Silicon local inference path may not match every host.

## How it works

Requests hit a FastAPI app that calls TypeSafe Jev for routing decisions, then optional local generation/retrieval. (Summarized from the upstream [README](https://github.com/sunilmehta-si/jev-inference-router/blob/130f16681dba5c26fc938c74654726ff0c0d0f05/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install Python deps, set TypeSafe credentials, and run the FastAPI app.

## Limits and data handling

Routing prompts go to TypeSafe; generation may stay local. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 130f16681dba](https://github.com/sunilmehta-si/jev-inference-router/tree/130f16681dba5c26fc938c74654726ff0c0d0f05). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
