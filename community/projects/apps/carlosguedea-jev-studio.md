# Jev Studio (CarlosGuedea)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Spanish-language visual editor (React Flow + FastAPI) for building and running AI workflows where a `Jev Decision` node is the decision engine next to LLM, Python, HTTP, Condition and Output nodes; real backend execution with graph validation, decision branches and step logs, webhook / interval / cron triggers and SQLite history. Distinct from the listed *Jev Studio* CLI/MCP kit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CarlosGuedea/JEV-Studio) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/CarlosGuedea/JEV-Studio#readme) (self-hosted; no hosted version verified). |
| Pricing and access | No app fee; self-host with Docker. Real Jev nodes need your own `TYPESAFE_API_KEY` (billed by TypeSafe); without it a clearly labeled mock provider runs. Checked 2026-10-08. |
| Jev evidence | [`backend/app/providers/jev_typesafe.py`](https://github.com/CarlosGuedea/JEV-Studio/blob/3f828b478975a759c4730ec3db6688555247abbb/backend/app/providers/jev_typesafe.py) calls `POST /v1/systemone` (`jev-latest`); [`jev_mock.py`](https://github.com/CarlosGuedea/JEV-Studio/blob/3f828b478975a759c4730ec3db6688555247abbb/backend/app/providers/jev_mock.py) is the labeled simulation. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [CarlosGuedea](https://github.com/CarlosGuedea). Independently curated. |
| Format | Docker Compose web app (React + Vite frontend, FastAPI backend) |
| Platform and availability | Web browser against a self-hosted backend (Docker, or Node 20+ and Python 3.11+). |
| Jev's role | Decides the branch at each Jev Decision node; LLM nodes generate, code nodes compute. |
| Requirements | Docker (or Node 20+ / Python 3.11+); optional `TYPESAFE_API_KEY` in `.env`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Prototype decision-driven workflows visually before coding them.
- Automate small flows on webhooks or schedules with an execution history.
- Mismatch: Spanish UI/docs; Python nodes run code — keep it on a trusted host.

## How it works

The backend validates the graph, orders nodes topologically, follows decision branches with an anti-cycle limit and logs every step to SQLite; providers are swappable (`jev_factory.py`).

## Get started

Start with Docker (README *Instalación y ejecución*):

```sh
git clone https://github.com/CarlosGuedea/JEV-Studio.git && cd JEV-Studio
cp .env.example .env   # optional TYPESAFE_API_KEY
docker compose up --build
# frontend http://localhost:7100 · API http://localhost:8155
```

Each executed Jev Decision node is a Jev request billed to your key; LLM nodes bill their providers.

## Examples and demos

- README *Qué incluye* and *Arquitectura*.

## Limits and data handling

Workflow inputs go to TypeSafe and any configured LLM/HTTP targets. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 3f828b478975](https://github.com/CarlosGuedea/JEV-Studio/tree/3f828b478975a759c4730ec3db6688555247abbb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
