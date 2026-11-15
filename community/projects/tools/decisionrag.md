# DecisionRAG (multi-source search and Q&A where Jev jointly ranks local and web passages and gates answers when evidence is weak)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Search and contextual Q&A engine that retrieves from a 2.68-million-passage local Wikipedia index (DAPR Natural Questions) plus Tavily and TelemAI web search in parallel, then has Jev score all passages together in one shared context with Noul and Choice questions instead of cosine similarity. Gemini rewrites follow-up questions and writes the answer, but only when Jev's top score passes a 0.5 gate; otherwise it abstains. The maintainer reports Recall@10 rising from 75% to 85% on their benchmark.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nguyenvo09/decisionRAG) |
| Maintainer | [nguyenvo09](https://github.com/nguyenvo09). Independently curated. |
| Format | Python web app and CLI |
| Requirements | Python 3, `TYPESAFE_API_KEY`, `GEMINI_API_KEY`, and Tavily and TelemAI keys for web search; the local index must be downloaded and built. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decision_rag/jev_client.py`](https://github.com/nguyenvo09/decisionRAG/blob/59694fccbf45423f661edd471bc0b5aa23843241/decision_rag/jev_client.py) at the pinned commit. |

## When to use

- Rerank mixed local and web results with calibrated probabilities and abstain when none fit.
- Mismatch: a lightweight setup; the full local index is large.

## How it works

`decision_rag/jev_client.py` posts to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`); API failures raise unless a lexical fallback is explicitly allowed. Integration evidence: [`decision_rag/jev_client.py`](https://github.com/nguyenvo09/decisionRAG/blob/59694fccbf45423f661edd471bc0b5aa23843241/decision_rag/jev_client.py).

## Get started

Set the keys in `.env`, then start the web app or the CLI.

```sh
git clone https://github.com/nguyenvo09/decisionRAG && cd decisionRAG
pip install -r requirements.txt
# .env: TYPESAFE_API_KEY, GEMINI_API_KEY, TAVILY_API_KEY, TELEM_API_KEY
python -u app.py          # http://127.0.0.1:8501
python cli.py --telem -q "which is the fastest train in india"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshots and results: [github.com/nguyenvo09/decisionRAG/blob/59694fccbf45423f661edd471bc0b5aa23843241/README.md](https://github.com/nguyenvo09/decisionRAG/blob/59694fccbf45423f661edd471bc0b5aa23843241/README.md)

## Limits and data handling

Queries and retrieved passages go to TypeSafe, Google (Gemini), Tavily and TelemAI on your keys. TelemAI runs on a hackathon host (`hack.telem.ai`). Benchmark figures are the maintainer's. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 59694fccbf45](https://github.com/nguyenvo09/decisionRAG/tree/59694fccbf45423f661edd471bc0b5aa23843241). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
