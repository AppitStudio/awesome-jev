# jev-corrective-rag

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Corrective RAG demo where triage, per-chunk grading, and answer verification use TypeSafe System One (Jev) typed gates instead of LLM judges; generation stays on a separate LLM. Includes a Streamlit UI, CLI, and bench harness with keyword-stub fallback when no TypeSafe key is set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sudeshkar/jev-corrective-rag) |
| Maintainer | [sudeshkar](https://github.com/sudeshkar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python Streamlit app + CLI/bench (MIT). |
| Requirements | Python 3 with `typesafe-sdk`, `groq`, `streamlit`, `python-dotenv`; `TYPESAFE_API_KEY` for live Jev gates; `GROQ_API_KEY` (or configured generator) for the generative step. |
| License | [MIT](https://github.com/sudeshkar/jev-corrective-rag/blob/f6ab2f5df9401da7d649fbfb3d9d436615d66130/LICENSE). TypeSafe and Groq usage have separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; no packaged unit tests found. Live Jev/Groq bench numbers were not re-measured. Upstream latency/LLM-call claims are vendor/author-reported. |

## When to use

Use it when you want a readable Corrective RAG reference that places routing, chunk relevance, and groundedness checks on typed System One calls. Prefer [llama-index-jev](llama-index-jev.md) or [jev-reranker](jev-reranker.md) for library-style retrieval helpers. Do not treat README bench tables as independently verified on this review host.

## How it works

[`src/gates.py`](https://github.com/sudeshkar/jev-corrective-rag/blob/f6ab2f5df9401da7d649fbfb3d9d436615d66130/src/gates.py) builds Noul/Choice/Score questions via `typesafe_sdk` and falls back to a keyword stub when `TYPESAFE_API_KEY` is absent. [`src/pipeline.py`](https://github.com/sudeshkar/jev-corrective-rag/blob/f6ab2f5df9401da7d649fbfb3d9d436615d66130/src/pipeline.py) sequences triage → BM25 retrieve → grade → generate → verify, with confidence floors for AUTO/REVIEW/ESCALATE. `app.py` is a Streamlit front end; `src/bench.py` compares Jev gates vs an LLM-judge baseline.

## Get started

```sh
git clone https://github.com/sudeshkar/jev-corrective-rag.git
cd jev-corrective-rag
git checkout f6ab2f5df9401da7d649fbfb3d9d436615d66130
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add keys for live runs
# Offline-ish UI with stub gates if no TYPESAFE_API_KEY:
# streamlit run app.py
# Bench (may call providers): python -m src.bench
```

This listing did not install the venv deps beyond source inspection and did not call TypeSafe or Groq.

## Examples and demos

- Upstream README architecture diagram and reported bench table (not re-run).
- Sample support corpus under `data/` (inspect locally).
- Keyword stub path when `TYPESAFE_API_KEY` is unset (documented in `app.py` / `gates.py`).

## Limits and data handling

Questions and passages leave the host on live Jev and generator calls. Stub mode is not equivalent to measured Jev latency. Early-access Jev availability and pricing change over time—check TypeSafe docs. Small sample sizes in author benches limit generalization.

## Review and maintenance

Reviewed on **2026-09-20** at [commit f6ab2f5](https://github.com/sudeshkar/jev-corrective-rag/tree/f6ab2f5df9401da7d649fbfb3d9d436615d66130): MIT. AI-assisted source review of README, LICENSE, `src/gates.py`, `src/pipeline.py`, and `app.py`. No unit-test suite present; live bench not executed. Syntax/structure of sources inspected only.

Related: [llama-index-jev](llama-index-jev.md), [jev-reranker](jev-reranker.md), [jegrep](jegrep.md), [neo4jev](neo4jev.md).
