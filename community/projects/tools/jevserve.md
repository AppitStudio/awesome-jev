# JevServe

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Serve open-weight Jev-style decision models (Open-Jev, JPT, NeoHorse, Kev adapters) on an NVIDIA GPU behind typed Choice/Noul/Score requests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anonNo2/jevserve) |
| Maintainer | [anonNo2](https://github.com/anonNo2). Independently curated. |
| Format | Docker image + Python client |
| Requirements | Linux x86_64, NVIDIA GPU, Docker + NVIDIA Container Toolkit; model weights per their licenses. |
| License | [Apache-2.0](https://github.com/anonNo2/jevserve/blob/b80d4e178727b98a7bcd75f687a5cf392ce21bdc/LICENSE) |
| Jev evidence | [`validation/http.py`](https://github.com/anonNo2/jevserve/blob/b80d4e178727b98a7bcd75f687a5cf392ce21bdc/validation/http.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Run Jev-compatible open models locally for routing, urgency or rubric scoring.
- Mismatch: does not call TypeSafe; developer preview without certified numerical alignment.

## How it works

One image loads separately mounted weights through vLLM or Torch adapters and exposes typed question endpoints with queues, cancellation and health checks. (Summarized from the upstream [README](https://github.com/anonNo2/jevserve/blob/b80d4e178727b98a7bcd75f687a5cf392ce21bdc/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): pull/build the image, mount weights, and start the container per the Quick Start.

## Limits and data handling

Runs locally; check each model's license in docs/models.md. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit b80d4e178727](https://github.com/anonNo2/jevserve/tree/b80d4e178727b98a7bcd75f687a5cf392ce21bdc). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
