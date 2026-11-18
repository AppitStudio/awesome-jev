# Jetriever by imlrz (agent-memory retrieval service that has Jev score how useful each stored memory is for the current query)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Self-hosted Add/Search API for agent memory, with a paper (arXiv:2611.21478) and Docker packaging. It stores raw chunks per user, then calls the Decisions API with `~typesafe/jev-latest` to ask a Noul utility score for every stored chunk against the query, and returns the five highest-scoring chunks as evidence. Every candidate must score successfully, so an incomplete rerank is never returned as a valid top five. It does not write the final answer. English and Chinese READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/imlrz/Jetriever) |
| Maintainer | [imlrz](https://github.com/imlrz). Independently curated. |
| Format | Python service with SQLite and Docker Compose (MIT) |
| Requirements | Docker Compose and an OpenRouter key with access to the Decisions API (the configured model is `~typesafe/jev-latest`). |
| License | [MIT](https://github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/jev.py`](https://github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/app/jev.py) at the pinned commit. |

## When to use

- Rerank an agent's stored memories by how useful they are for the question, not by embedding similarity.
- Mismatch: a drop-in vector database; it scores every stored chunk for a user with one model call each, so large memories cost time and money.

## How it works

`app/jev.py` calls the Decisions API through OpenRouter (default model `~typesafe/jev-latest`, set by `JEV_MODEL` in `app/config.py`) once per candidate chunk and asks for a Noul utility score; `app/retriever.py` sorts by that score. Integration evidence: [`app/jev.py`](https://github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/app/jev.py).

## Get started

Copy `.env.example` to `.env`, fill in your OpenRouter key and a private service key, then start it with Docker Compose.

```sh
git clone https://github.com/imlrz/Jetriever && cd Jetriever
cp .env.example .env   # set OPENROUTER_API_KEY and JETRIEVER_API_KEY
docker compose up --build -d
curl http://127.0.0.1:8000/health
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2611.21478](https://arxiv.org/abs/2611.21478)
- Method card: [github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/docs/METHOD_CARD.md](https://github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/docs/METHOD_CARD.md)
- README: [github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/README.md](https://github.com/imlrz/Jetriever/blob/13efd943d48b52f26b25531cb9378a029dd4acf5/README.md)

## Limits and data handling

Every stored chunk for the user is sent to the model provider on each search (one call per chunk), so cost and latency grow with memory size. The service keeps data for 30 days by default and its audit logs hold hashed identifiers only. The paper's results are the authors' own and were not reproduced here.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 13efd943d48b](https://github.com/imlrz/Jetriever/tree/13efd943d48b52f26b25531cb9378a029dd4acf5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
