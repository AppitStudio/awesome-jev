# Mori (RAG with whole-source context and Jev ranking)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

RAG for books, articles, lectures and podcasts that keeps the argument around a passage: semantic search finds 500 passages, Jev ranks relevance down to 100, and the answer packet holds one complete source unit, five summaries and the selected passages, with every run saved for audit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tiagovasc/mori-rag) |
| Maintainer | [tiagovasc](https://github.com/tiagovasc). Independently curated. |
| Format | Python library, CLI and local web interface |
| Requirements | Python; a TypeSafe API key; an embedding setup and an answer model of your choice (or the portable prompt handoff). |
| License | [MIT](https://github.com/tiagovasc/mori-rag/blob/e47a7ad661e3120a992525b1170b023f31c5d5df/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mori/providers.py`](https://github.com/tiagovasc/mori-rag/blob/e47a7ad661e3120a992525b1170b023f31c5d5df/mori/providers.py) at the pinned commit. |

## When to use

- Answer questions from long sources without losing qualifications around a quote.
- Keep reproducible run folders with Jev's ratings and the exact final prompt.
- Mismatch: research tool; you bring and ingest your own corpus.

## How it works

`mori/providers.py` sends each candidate passage and summary to Jev (`jev_url` defaults to `https://api.typesafe.ai/v1/systemone`, model `jev-latest`) for a relevance score and caches successful decisions; an optional LLM reranker is off by default. Integration evidence: [`mori/providers.py`](https://github.com/tiagovasc/mori-rag/blob/e47a7ad661e3120a992525b1170b023f31c5d5df/mori/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m mori --config examples/codex.toml query "Your question" --answer
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pipeline, settings and evidence files in the README: [github.com/tiagovasc/mori-rag#readme](https://github.com/tiagovasc/mori-rag#readme)

## Limits and data handling

Passages and summaries are sent to TypeSafe for ranking; answer-model access and billing are yours.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit e47a7ad661e3](https://github.com/tiagovasc/mori-rag/tree/e47a7ad661e3120a992525b1170b023f31c5d5df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
