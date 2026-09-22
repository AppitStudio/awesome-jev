# Jevflix

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hybrid movie recommender: FAISS + BM25 narrow ~4,800 films to a shortlist, then TypeSafe Jev parses constraints and picks one title with a confidence gate that either answers or asks a follow-up.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ArielBubis/Jevflix) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Jevflix project homepage](https://github.com/ArielBubis/Jevflix) — source-run Streamlit app; no separate product site. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Needs a TypeSafe key for live Jev stages; optional Anthropic (or template) generator for explanations. Provider usage can incur charges; free-tier eligibility was not verified. |
| Jev evidence | Inspected [`movie_rec/jev_client.py`](https://github.com/ArielBubis/Jevflix/blob/a5b60dd8c1c360f4cef096d040cfd526dc582a2f/movie_rec/jev_client.py) posting to `https://api.typesafe.ai/v1/systemone` and [`movie_rec/agent_controller.py`](https://github.com/ArielBubis/Jevflix/blob/a5b60dd8c1c360f4cef096d040cfd526dc582a2f/movie_rec/agent_controller.py) orchestration (constraint parse → Choice → confidence gate). Live recommend not run on the review host. |
| Disclosure | Free source access does not include inference. AI-assisted, independently curated listing; no commercial relationship declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [ArielBubis](https://github.com/ArielBubis). |
| Format | Python Streamlit app + `movie_rec` library (`main.py` / `app.py`). |
| Platform and availability | Local web UI via Streamlit. Source-run prototype; no hosted public demo URL was verified. |
| Jev's role | Parses runtime/gore/specificity constraints and chooses among retrieval candidates; code owns hybrid retrieval, hard filters, confidence thresholding, and explanation text (template or separate LLM). |
| Requirements | Python 3.11+ recommended; `requirements.txt` (pandas, faiss-cpu, sentence-transformers, torch, httpx, streamlit, …). `TYPESAFE_API_KEY` for live Jev. Dataset under `dateset/` per upstream README. |
| License | [MIT](https://github.com/ArielBubis/Jevflix/blob/a5b60dd8c1c360f4cef096d040cfd526dc582a2f/LICENSE). |

## When to use

Use it when you want a **retrieval + calibrated pick** demo: local search shortlists films, Jev judges constraints and picks one title, and low confidence triggers a follow-up path. Prefer [Jev Search](jev-search.md) for general web/search agents rather than a fixed movie corpus.

## How it works

Stage 1 runs hybrid FAISS dense k-NN + BM25 (RRF fusion). Stage 2 asks Jev for constraint Noul/Choice questions, then a Choice over candidate labels. Application code applies hard filters and a confidence gate: high confidence goes to a fast explanation path; low confidence escalates to a System-2 style clarify/recommend path via the configured generator. [`movie_rec/jev_client.py`](https://github.com/ArielBubis/Jevflix/blob/a5b60dd8c1c360f4cef096d040cfd526dc582a2f/movie_rec/jev_client.py) documents the System One wire format.

## Get started

```sh
git clone https://github.com/ArielBubis/Jevflix.git
cd Jevflix
git checkout a5b60dd8c1c360f4cef096d040cfd526dc582a2f
python3 -m pip install -r requirements.txt
cp .env.example .env   # add TYPESAFE_API_KEY
streamlit run app.py   # or follow upstream README for main.py
```

Live recommend sends request text and candidate metadata to TypeSafe and may incur charges. This listing did not run a live recommend.

## Examples and demos

- Offline unit tests: `tests/test_jev_client.py`, `tests/test_agent_controller.py`, `tests/test_evaluate.py` (on the review host: **12 passed, 26 skipped** without heavy FAISS/torch fixtures).
- Offline eval JSON under `eval/` (author-reported ablations; not re-measured here).

## Limits and data handling

User request text and candidate descriptions leave the host on live System One calls. Movie corpus and embedding downloads can be large. README accuracy tables are upstream measurements. No live TypeSafe spend on the review host.

## Review and maintenance

Reviewed on **2026-09-22** at [commit a5b60dd](https://github.com/ArielBubis/Jevflix/tree/a5b60dd8c1c360f4cef096d040cfd526dc582a2f): MIT. AI-assisted source review of README, `movie_rec/jev_client.py`, `agent_controller.py`, LICENSE, and tests. Offline: lightweight pytest subset **12 passed / 26 skipped**. Full FAISS/torch path and live Jev not run.

Related: [Jev Search](jev-search.md), [JevSlop](jevslop.md), [RefGarden](refgarden.md).
