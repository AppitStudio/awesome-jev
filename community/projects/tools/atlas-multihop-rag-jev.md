# Atlas: multihop-rag-jev (tests whether Jev can choose which retrieved passages an answer model reads, on MultiHop-RAG)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local experiment app that runs each question in four modes (hybrid search, hybrid plus Jev filtering, regex keyword search, keyword search plus Jev) with one shared answer model, and shows the exact Jev questions, answers, kept passages, tokens and cost per mode, plus a benchmark page over the full MultiHop-RAG set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bytelabs-oss/multihop-rag-jev) |
| Maintainer | [bytelabs-oss](https://github.com/bytelabs-oss). Independently curated. |
| Format | Local Next.js-style web app with a Python document pipeline (no license file) |
| Requirements | Python 3.12, Node, `TYPESAFE_API_KEY` and a Vercel AI Gateway key (`AI_GATEWAY_API_KEY`) for the answer model. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/pipeline.mjs`](https://github.com/bytelabs-oss/multihop-rag-jev/blob/b75cfd6defae06eb55617694dc3af849d16fb787/server/pipeline.mjs) at the pinned commit. |

## When to use

- Measure whether a Jev relevance filter cuts RAG answer cost without hurting quality on your own documents.
- Inspect exactly what Jev kept or dropped for a question.
- Mismatch: a deployable RAG service; this is a local experiment.

## How it works

`server/pipeline.mjs` uses the TypeSafe SDK (`@typesafe-ai/sdk`) with `jev-latest` to ask, for each retrieved passage, whether it helps answer the question and then whether it adds anything to the passages already kept; only kept passages go to the answer model (`openai/gpt-5-mini`). Documents are chunked and embedded locally; the MultiHop-RAG corpus keeps its own licence. Integration evidence: [`server/pipeline.mjs`](https://github.com/bytelabs-oss/multihop-rag-jev/blob/b75cfd6defae06eb55617694dc3af849d16fb787/server/pipeline.mjs).

## Get started

Create the Python environment, download the document models, install Node dependencies and start the dev server, with both keys in `.env.local`.

```sh
python3.12 -m venv .venv && .venv/bin/pip install -r requirements.lock.txt
npm install
npm run dev -- --port 5173
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bytelabs-oss/multihop-rag-jev/blob/b75cfd6defae06eb55617694dc3af849d16fb787/README.md](https://github.com/bytelabs-oss/multihop-rag-jev/blob/b75cfd6defae06eb55617694dc3af849d16fb787/README.md)
- Product notes: [github.com/bytelabs-oss/multihop-rag-jev/blob/b75cfd6defae06eb55617694dc3af849d16fb787/PRODUCT.md](https://github.com/bytelabs-oss/multihop-rag-jev/blob/b75cfd6defae06eb55617694dc3af849d16fb787/PRODUCT.md)

## Limits and data handling

Passages go to TypeSafe and the answer model through Vercel AI Gateway on your keys; parsed chunks and embeddings are cached in the browser.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit b75cfd6defae](https://github.com/bytelabs-oss/multihop-rag-jev/tree/b75cfd6defae06eb55617694dc3af849d16fb787). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
