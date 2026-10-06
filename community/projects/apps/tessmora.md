# Tessmora (MMA-RAG)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Tessmora (Chinese docs): self-hosted omni-modal agentic retrieval platform for documents, images, audio and video, with opt-in TypeSafe Jev semantic judgment for a simple-question intent fast path, choice reranking and citation-support diagnostics.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Champ-X/MMA-RAG) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Champ-X/MMA-RAG#readme) (source-built app; no separate website verified). |
| Pricing and access | Public source with **no LICENSE file** — not Open source. No app fee for the source build; you run Docker (MinIO, Qdrant, Redis), the backend and frontend, and bring keys for your chosen LLM/embedding providers plus `TYPESAFE_API_KEY` for the optional Jev features. Checked 2026-10-07. |
| Jev evidence | Inspected [`backend/app/core/llm/jev.py`](https://github.com/Champ-X/MMA-RAG/blob/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/backend/app/core/llm/jev.py), [`retrieval/processors/jev_intent.py`](https://github.com/Champ-X/MMA-RAG/blob/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/backend/app/modules/retrieval/processors/jev_intent.py) and [`generation/jev_citations.py`](https://github.com/Champ-X/MMA-RAG/blob/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/backend/app/modules/generation/jev_citations.py); maintainer evaluation write-ups under [`docs/research/jev`](https://github.com/Champ-X/MMA-RAG/tree/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/docs/research/jev). |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [Champ-X](https://github.com/Champ-X). Independently curated. |
| Format | Self-hosted web platform (FastAPI backend, web frontend, Docker services) + local CLI/skill |
| Platform and availability | Self-hosted (Docker Compose + Python 3.11+ + Node 18+); development-stage, no built-in user authentication — trusted networks only. |
| Jev's role | Optional and off by default: in Settings → Jev you can enable an intent fast path for simple questions, Jev choice reranking and per-citation or batched citation-support diagnostics. Query rewriting and final answers stay on the configured generative model; embeddings, VLM/ASR and cross-encoders do the rest. |
| Requirements | Docker and Docker Compose, Python 3.11+, Node.js 18+; provider keys for the generative/embedding models; `TYPESAFE_API_KEY` in `backend/.env` for Jev. |
| License | **No LICENSE file** in the reviewed tree — publicly readable source with unspecified reuse terms; not Open source. |

## When to use

- Self-host retrieval over mixed media (PDFs, images, audio, video) with traceable citations, and test whether Jev can shortcut simple-question intent detection.
- Compare an LLM reranker with Jev choice reranking or add citation-support diagnostics, using the maintainer's documented force modes for A/B runs.
- Mismatch: no built-in auth and permissive CORS; no LICENSE, so reuse terms are unspecified.

## How it works

Content is ingested per modality (agentic chunker, VLM + CLIP, ASR + CLAP, scene/shot/key-frame), retrieved with dense/sparse/visual channels and RRF fusion, and answered by a bounded read-only agent. Jev hooks sit at three points: [`jev_intent.py`](https://github.com/Champ-X/MMA-RAG/blob/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/backend/app/modules/retrieval/processors/jev_intent.py) classifies simple questions, a Jev choice rerank orders candidates, and [`jev_citations.py`](https://github.com/Champ-X/MMA-RAG/blob/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/backend/app/modules/generation/jev_citations.py) / `jev_citation_batch.py` diagnose whether citations support the answer. Settings persist via `GET/PUT /api/jev/settings`.

## Get started

Clone and follow the upstream Chinese quick start (Docker services, backend `.env`, frontend):

```sh
git clone https://github.com/Champ-X/MMA-RAG.git
cd MMA-RAG
# see README 快速开始: docker compose up -d (MinIO, Qdrant, Redis), configure backend/.env
# add TYPESAFE_API_KEY=... to backend/.env, restart the backend,
# then enable features under Settings → Jev 语义判断
```

Jev features send requests billed to your TypeSafe key; other configured providers bill separately.

## Examples and demos

- Maintainer Jev studies: [rerank experiments](https://github.com/Champ-X/MMA-RAG/tree/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/docs/research/jev), [intent fast path](https://github.com/Champ-X/MMA-RAG/tree/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/docs/research/jev-v2), [citation diagnostics](https://github.com/Champ-X/MMA-RAG/tree/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/docs/research/jev-v3) and [cross-round decisions](https://github.com/Champ-X/MMA-RAG/blob/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5/docs/research/JEV-DECISIONS.md).
- README chat and retrieval examples per modality (documents, images, audio, video, mixed).

## Limits and data handling

All Jev switches default off; maintainer results are upstream measurements, not reproduced here. Query text, candidate passages and answers go to TypeSafe when Jev features are on. No built-in authentication; chat sessions are in-process state. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 0cfb0096fc6c](https://github.com/Champ-X/MMA-RAG/tree/0cfb0096fc6ca06736c4dedfd42d6889c0d965e5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
