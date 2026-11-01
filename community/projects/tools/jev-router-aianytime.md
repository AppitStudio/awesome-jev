# Jev Router by AIAnytime (OpenAI-compatible router where Jev picks the model, agent or tool for each request)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted, OpenAI-compatible endpoint: send `model="auto"` and Jev's typed choice, score and yes/no answers decide which configured model, agent or tool handles the request, with the routing reason returned alongside the response and a dashboard for traces.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AIAnytime/Jev-Router) |
| Maintainer | [AIAnytime](https://github.com/AIAnytime). Independently curated. |
| Format | Python (FastAPI) server, Docker Compose |
| Requirements | Python 3.11+ or Docker; a TypeSafe API key plus keys for the downstream models you route to. |
| License | [MIT](https://github.com/AIAnytime/Jev-Router/blob/798cb186d182e4ae7440acc56d96a4b2587fb4fe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_router/engine/jev_client.py`](https://github.com/AIAnytime/Jev-Router/blob/798cb186d182e4ae7440acc56d96a4b2587fb4fe/jev_router/engine/jev_client.py) at the pinned commit. |

## When to use

- Put one routing endpoint in front of several LLMs, agents or tools with explainable decisions.
- Mismatch: you still pay for and configure every downstream provider.

## How it works

`jev_router/engine/jev_client.py` calls TypeSafe (`JEV_BASE_URL`, default `https://api.typesafe.ai/v1`, model `jev-latest`) with typed routing questions about each request; the router maps the answers onto the models, agents and tools in its config. Integration evidence: [`jev_router/engine/jev_client.py`](https://github.com/AIAnytime/Jev-Router/blob/798cb186d182e4ae7440acc56d96a4b2587fb4fe/jev_router/engine/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AIAnytime/Jev-Router.git && cd Jev-Router
uv venv && uv pip install -e ".[dev]"
# or: docker compose up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README with curl examples: [github.com/AIAnytime/Jev-Router#readme](https://github.com/AIAnytime/Jev-Router#readme)

## Limits and data handling

Request text is sent to TypeSafe for routing and then to the chosen provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 798cb186d182](https://github.com/AIAnytime/Jev-Router/tree/798cb186d182e4ae7440acc56d96a4b2587fb4fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
