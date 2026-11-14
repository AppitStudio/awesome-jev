# JevRouter (blacksinisterx) (LLM router where Jev rates a task's complexity, type, reasoning need and latency sensitivity and picks the cheapest model tier that can handle it)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

FastAPI service and React dashboard: one Jev request asks four questions about a prompt (a 0–4 complexity score, a task-type choice, and yes/no on multi-step reasoning and latency sensitivity), then a tier policy picks fast, balanced or frontier and the cheapest model in a small catalog that covers it, with a cost comparison against always using the top model. Mock-first: the default provider makes no API calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blacksinisterx/jev-router) |
| Maintainer | [blacksinisterx](https://github.com/blacksinisterx). Independently curated. |
| Format | Python FastAPI backend with a Vite/React dashboard; public demo on Vercel (mock mode) |
| Requirements | Python 3 and Node.js; `TYPESAFE_API_KEY` with `JEV_PROVIDER=typesafe` for live Jev (default `JEV_PROVIDER=mock` needs no key). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/BlackSinisterx/status/2121619170001629687)). |
| Jev evidence | [`backend/app/providers/typesafe.py`](https://github.com/blacksinisterx/jev-router/blob/24f949a3477ad84337e718960cb47903ebdf3047/backend/app/providers/typesafe.py) at the pinned commit. |

## When to use

- See how typed Jev signals can drive a cheapest-capable-model routing policy.
- Mismatch: a production gateway; the model catalog is a small illustrative table and actual LLM calls are not made by the router.

## How it works

`backend/app/providers/typesafe.py` posts to `https://api.typesafe.ai/v1/systemone`; `backend/app/questions.py` defines the four questions and `backend/app/policy.py` maps the answers to a tier. A third provider, `jev_agent`, sends requests to `jev-agent.com`, a third-party host, not TypeSafe; the README's live screenshots were made with that provider. Integration evidence: [`backend/app/providers/typesafe.py`](https://github.com/blacksinisterx/jev-router/blob/24f949a3477ad84337e718960cb47903ebdf3047/backend/app/providers/typesafe.py).

## Get started

Clone, run the backend and frontend, and switch the provider to `typesafe` with your key for live routing.

```sh
git clone https://github.com/blacksinisterx/jev-router && cd jev-router
# see README: start backend (FastAPI) and frontend (Vite)
export JEV_PROVIDER=typesafe TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo (mock mode): [jev-router-ten.vercel.app](https://jev-router-ten.vercel.app)
- README: [github.com/blacksinisterx/jev-router/blob/24f949a3477ad84337e718960cb47903ebdf3047/README.md](https://github.com/blacksinisterx/jev-router/blob/24f949a3477ad84337e718960cb47903ebdf3047/README.md)
- Maker's X post with demo video: [x.com/BlackSinisterx/status/2121619170001629687](https://x.com/BlackSinisterx/status/2121619170001629687)

## Limits and data handling

With `typesafe`, prompts are sent to TypeSafe on your key; with `jev_agent`, they go to the third-party jev-agent.com host. The hosted demo stays in mock mode. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 24f949a3477a](https://github.com/blacksinisterx/jev-router/tree/24f949a3477ad84337e718960cb47903ebdf3047). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
