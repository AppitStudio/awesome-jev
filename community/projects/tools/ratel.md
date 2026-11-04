# Ratel (context-engineering SDK that selects tools and skills per turn, with an optional Jev retriever and reranker)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript, Python and Rust context-engineering layer that indexes an agent's tools and skills into a catalog and injects only the ones each turn needs. Ranking is BM25, semantic or hybrid by default; a rankers plugin (`ratelJevPlugin` / `ratel_jev_plugin`) wraps Jev as a reranker over BM25's candidates or as a standalone retriever, falling back to BM25 order when Jev is down. Runnable TypeScript and Python Jev retriever examples ship in `examples/`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ratel-ai/ratel) |
| Maintainer | [ratel-ai](https://github.com/ratel-ai). Independently curated. |
| Format | Rust core with TypeScript and Python SDKs (npm `@ratel-ai/sdk`, PyPI `ratel-ai`) |
| Requirements | Node.js and pnpm, or Python and uv; a `TYPESAFE_API_KEY` for the Jev plugin (the examples have a local stand-in without it). |
| License | [Apache-2.0 and MIT](https://github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/rankers/core/src/jev.rs`](https://github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/src/rankers/core/src/jev.rs) at the pinned commit. |

## When to use

- Let a typed model rerank a tool or skill catalog for the current query instead of loading every tool schema into the prompt.
- Mismatch: Jev is an optional ranker plugin, and the Jev plugin sends the query plus every candidate's searchable text to Jev.

## How it works

`src/rankers/core/src/jev.rs` asks Jev a `choice` question over candidate options (default `jev-latest` at `https://api.typesafe.ai`, key from `TYPESAFE_API_KEY`) and turns the probabilities into a ranking, using a tournament for large candidate sets. Integration evidence: [`src/rankers/core/src/jev.rs`](https://github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/src/rankers/core/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm add @ratel-ai/sdk   # TypeScript
pip install ratel-ai    # Python
TYPESAFE_API_KEY=... pnpm -F @ratel-ai/example-jev-retriever start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev retriever example (TypeScript) with sample output and failure behaviour: [github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/examples/jev-retriever-ts/README.md](https://github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/examples/jev-retriever-ts/README.md)
- Python version: [github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/examples/jev-retriever-python/README.md](https://github.com/ratel-ai/ratel/blob/8d78e70d6580bbb7973672cf83eeaa84154a9cd5/examples/jev-retriever-python/README.md)
- README: [github.com/ratel-ai/ratel#readme](https://github.com/ratel-ai/ratel#readme)

## Limits and data handling

With the Jev plugin, queries and candidate tool or skill text go to TypeSafe on your key; BM25, semantic and hybrid ranking stay in-process. The example output is from a single illustrative query and not a benchmark. The engine is Apache-2.0 and the SDKs and examples are MIT. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 8d78e70d6580](https://github.com/ratel-ai/ratel/tree/8d78e70d6580bbb7973672cf83eeaa84154a9cd5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
