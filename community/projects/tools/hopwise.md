# Hopwise (knowledge-graph traversal benchmark)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark (README in Vietnamese) where Jev picks which edge to follow at each node of a Neo4j knowledge graph built from Wikidata and SEC EDGAR: 26 of 60 questions right (43%) in a 4.2 s median for $0.07, against 25% for Gemma 4 12B and 27% for gpt-oss-20b.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Aohkne/hopwise) |
| Maintainer | [Aohkne](https://github.com/Aohkne). Independently curated. |
| Format | FastAPI backend and React dashboard over Neo4j, with crawled graph data |
| Requirements | Docker (for Neo4j), Python and Node; an OpenRouter key for Jev, plus Ollama or an NVIDIA NIM key for the comparison LLMs. |
| License | [Apache-2.0](https://github.com/Aohkne/hopwise/blob/f4fcb48d8a8f72cd5492613e0ce6e1f7de3c5b24/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/huuw_khoa/status/2111682717775757471)). |
| Jev evidence | [`backend/app/services/decision_models/jev.py`](https://github.com/Aohkne/hopwise/blob/f4fcb48d8a8f72cd5492613e0ce6e1f7de3c5b24/backend/app/services/decision_models/jev.py) at the pinned commit. |

## When to use

- See whether a decision model can walk a knowledge graph step by step faster and cheaper than handing the whole question to an LLM.
- Reuse the crawled football and VinFast graphs and the 60 generated ground-truth questions.
- Mismatch: one run per question on 60 questions; the author asks for feedback and lists missing parts in TODO.md.

## How it works

At each node the backend asks Jev a Choice question over the outgoing edges ("which edge leads to the answer?") and walks until it answers or hits a five-minute limit; the LLM baselines get the same graph tools. The dashboard replays each model's trace and keeps run history. Integration evidence: [`backend/app/services/decision_models/jev.py`](https://github.com/Aohkne/hopwise/blob/f4fcb48d8a8f72cd5492613e0ce6e1f7de3c5b24/backend/app/services/decision_models/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
docker compose up -d   # Neo4j
# then start backend/ (FastAPI) and frontend/ (Vite) as described in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's X post: [x.com/huuw_khoa/status/2111682717775757471](https://x.com/huuw_khoa/status/2111682717775757471)
- Trace animations for each model in `docs/images/`.

## Limits and data handling

Questions and graph neighbourhoods go to OpenRouter on your key (and to NVIDIA for gpt-oss). Results come from a single run per question.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit f4fcb48d8a8f](https://github.com/Aohkne/hopwise/tree/f4fcb48d8a8f72cd5492613e0ce6e1f7de3c5b24). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
