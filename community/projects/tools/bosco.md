# bosco (OpenAI-compatible LLM router with a native POST /v1/systemone Jev path)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Dockerized OpenAI-compatible LLM router/proxy that also exposes `POST /v1/systemone` and forwards System One / Jev decision requests to a configured upstream, so one URL can serve both chat and typed decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AutreMachine/bosco) |
| Maintainer | [AutreMachine](https://github.com/AutreMachine). Independently curated. |
| Format | Python FastAPI router + Docker image (MIT) |
| Requirements | Docker or Python host and upstream LLM / System One endpoints you control. |
| License | [MIT](https://github.com/AutreMachine/bosco/blob/38682336edfcfb540ea1ea8c889a0c51eb39143d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`llm_router/api.py`](https://github.com/AutreMachine/bosco/blob/38682336edfcfb540ea1ea8c889a0c51eb39143d/llm_router/api.py) at the pinned commit. |

## When to use

- Front chat and System One clients with one router URL.
- Forward `/v1/systemone` Jev-shaped traffic to an upstream.
- Mismatch: router/proxy; you must configure the Jev/System One upstream yourself.

## How it works

`llm_router/api.py` implements `POST /v1/systemone` via `do_jev` / `handle(..., "systemone")`, forwarding the body to the leased upstream System One endpoint. Integration evidence: [`llm_router/api.py`](https://github.com/AutreMachine/bosco/blob/38682336edfcfb540ea1ea8c889a0c51eb39143d/llm_router/api.py).

## Get started

Pull the Docker image or run from source per README and point a System One upstream at a Jev-compatible server.

```sh
git clone https://github.com/AutreMachine/bosco.git && cd bosco
# docker pull autremachine/llm-router  # or follow README
# configure upstream systemone target
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AutreMachine/bosco/blob/38682336edfcfb540ea1ea8c889a0c51eb39143d/README.md](https://github.com/AutreMachine/bosco/blob/38682336edfcfb540ea1ea8c889a0c51eb39143d/README.md)

## Limits and data handling

Request bodies (including decision state/questions) are forwarded to your configured upstream. Review upstream retention.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 38682336edfc](https://github.com/AutreMachine/bosco/tree/38682336edfcfb540ea1ea8c889a0c51eb39143d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
