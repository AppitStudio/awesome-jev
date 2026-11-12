# divinci-table (AI Commander player where Jev picks each legal move)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

AI player and table server for four-player Commander (Magic: The Gathering): code knows the rules and lists the legal moves, and a System One model (TypeSafe's `jev-latest`, a self-hosted model or an open alternative) picks one and says how sure it is; people and AI seats share one game.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Divinci-AI/divinci-table) |
| Maintainer | [Divinci-AI](https://github.com/Divinci-AI). Independently curated. |
| Format | Game harness and table server (Python, Apache-2.0) |
| Requirements | Python 3.14 with numpy, card data fetched once from Scryfall, and `TYPESAFE_API_KEY` for Jev seats (the table also runs on rules and templates without a model). |
| License | [Apache-2.0](https://github.com/Divinci-AI/divinci-table/blob/e670db66fbaab9cd93b72ff2444c6bf70e1ef357/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/agents.py`](https://github.com/Divinci-AI/divinci-table/blob/e670db66fbaab9cd93b72ff2444c6bf70e1ef357/harness/agents.py) at the pinned commit. |

## When to use

- Play Commander with an AI seat that makes typed, explainable choices.
- Compare decision models on long game simulations.
- Mismatch: hobby project; game rules coverage is limited to what the engine models.

## How it works

`harness/agents.py` defines the Jev seat that posts each decision to `https://api.typesafe.ai/v1/systemone` (or a local `so1_server.py` / `DJEV_URL` endpoint) and falls back to a heuristic agent; `harness/README.md` collects the paired-comparison results. Integration evidence: [`harness/agents.py`](https://github.com/Divinci-AI/divinci-table/blob/e670db66fbaab9cd93b72ff2444c6bf70e1ef357/harness/agents.py).

## Get started

Install the requirements, fetch card data once, and start the table server.

```sh
pip install -r table/requirements.txt && python3 table/fetch_data.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Harness results: [github.com/Divinci-AI/divinci-table/blob/e670db66fbaab9cd93b72ff2444c6bf70e1ef357/harness/README.md](https://github.com/Divinci-AI/divinci-table/blob/e670db66fbaab9cd93b72ff2444c6bf70e1ef357/harness/README.md)

## Limits and data handling

Game states for AI decisions go to TypeSafe on your key when a Jev seat is used; the table can run offline.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit e670db66fbaa](https://github.com/Divinci-AI/divinci-table/tree/e670db66fbaab9cd93b72ff2444c6bf70e1ef357). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
