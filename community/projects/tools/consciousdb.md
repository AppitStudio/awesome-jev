# ConsciousDB (graph-database-agnostic GraphRAG layer where Jev or local Laya makes every edge and routing decision)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Agentic GraphRAG framework you put on top of Neo4j, Memgraph, Apache AGE or Kùzu. Score, Noul and Choice questions verify edges at ingestion, route query intent, steer a custom A* traversal and gate hallucinations, answered by cloud Jev, local Laya, or both for ablation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bodepudimuneendra-netizen/ConsciousDB) |
| Maintainer | [bodepudimuneendra-netizen](https://github.com/bodepudimuneendra-netizen). Independently curated. |
| Format | Python framework |
| Requirements | Python, a supported graph database; `TYPESAFE_API_KEY` for the Jev backend (a CUDA GPU only for local Laya). |
| License | [Apache-2.0](https://github.com/bodepudimuneendra-netizen/ConsciousDB/blob/291b378fc0aeb3c3a3475b7fdfbe9f4aedfb762f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`graphrag_neo4j_laya/graphrag/models/jev.py`](https://github.com/bodepudimuneendra-netizen/ConsciousDB/blob/291b378fc0aeb3c3a3475b7fdfbe9f4aedfb762f/graphrag_neo4j_laya/graphrag/models/jev.py) at the pinned commit. |

## When to use

- Replace per-hop LLM calls in GraphRAG with fast typed decisions.
- Mismatch: the default backend is local Laya; set `DECISION_MODEL_BACKEND=jev` to use Jev.

## How it works

`graphrag/models/jev.py` implements the framework's decision-model interface against `https://api.typesafe.ai/v1/systemone` (`jev-1.13`), so every pipeline phase can switch between Jev, Laya and an ablation mode with one environment variable. Integration evidence: [`graphrag_neo4j_laya/graphrag/models/jev.py`](https://github.com/bodepudimuneendra-netizen/ConsciousDB/blob/291b378fc0aeb3c3a3475b7fdfbe9f4aedfb762f/graphrag_neo4j_laya/graphrag/models/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bodepudimuneendra-netizen/ConsciousDB.git
cd ConsciousDB/graphrag_neo4j_laya
pip install -r requirements.txt
cp .env.example .env   # set DECISION_MODEL_BACKEND=jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README architecture and phase tables: [github.com/bodepudimuneendra-netizen/ConsciousDB#readme](https://github.com/bodepudimuneendra-netizen/ConsciousDB#readme)

## Limits and data handling

Document chunks, entities and queries are sent to TypeSafe when the Jev backend is on. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 291b378fc0ae](https://github.com/bodepudimuneendra-netizen/ConsciousDB/tree/291b378fc0aeb3c3a3475b7fdfbe9f4aedfb762f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
