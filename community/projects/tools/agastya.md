# Agastya (training-free retrieval where Jev walks a document's table of contents and local embeddings rank the leaves)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Retrieval research code: Jev walks a document outline level by level, giving one noul probability per candidate section, and EmbeddingGemma ranks the leaves it keeps. No training or labels; the README reports the maintainer's benchmark against flat Jev ranking and embedding baselines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cars3/agastya) |
| Maintainer | [cars3](https://github.com/cars3). Independently curated. |
| Format | Python scripts + small HTTP server |
| Requirements | Python; a TypeSafe key; local EmbeddingGemma weights. |
| License | [MIT](https://github.com/cars3/agastya/blob/d457f105df414f6748a07e76976e494ad87b51a1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/cars3/agastya/blob/d457f105df414f6748a07e76976e494ad87b51a1/jev.py) at the pinned commit. |

## When to use

- Retrieve from long structured documents (books, manuals) with a ToC.
- Mismatch: research prototype; needs a usable outline per document.

## How it works

`jev.py` uses the TypeSafe SDK's `Noul` question against `jev-latest` for each candidate section with up to three levels of ToC lineage; `core.py` combines the kept leaves with embedding ranking and serves `POST /ask`. Integration evidence: [`jev.py`](https://github.com/cars3/agastya/blob/d457f105df414f6748a07e76976e494ad87b51a1/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
RAG_DATA=data/books/<book> python core.py --serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmarks in the README: [github.com/cars3/agastya#readme](https://github.com/cars3/agastya#readme)

## Limits and data handling

Queries and section titles are sent to TypeSafe. Benchmark numbers are the maintainer's own. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit d457f105df41](https://github.com/cars3/agastya/tree/d457f105df414f6748a07e76976e494ad87b51a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
