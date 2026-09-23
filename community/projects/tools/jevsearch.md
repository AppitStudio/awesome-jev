# jevsearch

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

shadcn/ui registry block that adds a ⌘K site-search palette: a local keyword pass answers on the first keystroke, then TypeSafe Jev re-ranks the top hits by what the visitor meant.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kylemclaren/jevsearch) |
| Maintainer | [kylemclaren](https://github.com/kylemclaren). Self-submission by the maintainer. |
| Format | shadcn registry block (`jev-search`: React component, hook, lexical index, Fetch-API server handler, and a Next.js API route) plus an optional Markdown/MDX indexer block (`jev-search-indexer`). The repository also holds the Astro demo site and a benchmark. |
| Requirements | A React/Tailwind project set up for shadcn/ui, and `TYPESAFE_API_KEY` on the server for Jev ranking. The handler uses only the Fetch API, so it can be wired into Next.js, Astro, Remix, Hono, Bun, Deno, or Workers; the bundled route targets Next.js. |
| License | [MIT](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/LICENSE). |
| Disclosure | Submitted by the author with AI assistance (Claude Code). Listing is not an endorsement. |

## When to use

Use it for docs or marketing-site search where visitors type questions rather than exact page words, and you want keyword results immediately with a Jev re-rank shortly after. It needs no embeddings, vector database, or re-indexing job; the index is a JSON array of documents. It does not retrieve beyond its keyword candidates, so a page that never reaches the candidate pool cannot be ranked first. Prefer [jev-reranker](jev-reranker.md) or [jev-reranker (hotchpotch)](hotchpotch-jev-reranker.md) to rerank candidates from an existing search backend, and [Jev Search](../apps/jev-search.md) (distinct from this project) for web search.

## How it works

`GET /api/jev-search?q=…` first runs a weighted lexical scorer with prefixes, a light stemmer, and one-edit typo tolerance ([`src/lib/jev-search-core.ts`](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/src/lib/jev-search-core.ts)) and streams those hits as NDJSON. The top 20 hits then go to TypeSafe in one request ([`src/lib/jev-search-server.ts`](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/src/lib/jev-search-server.ts)): a Noul per candidate ("would the visitor be glad to land here?"), a Choice over all candidates for the single best page, and a Noul for whether any candidate answers the query. Hits are ordered by 0.75 × relevance + 0.25 × best-answer probability, hits under the threshold (default 0.15) are dropped, and the result is cached in memory. If TypeSafe errors or exceeds the timeout (default 4 s), keyword order stands. The registry definition is in [`registry.json`](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/registry.json).

## Get started

```sh
# In a shadcn/ui project
npx shadcn@latest add https://raw.githubusercontent.com/kylemclaren/jevsearch/1df37decb960b3c4826c71b41d3393c15a8f28d3/public/r/jev-search.json
echo 'TYPESAFE_API_KEY=your-key' >> .env.local

# Optional: index a folder of Markdown/MDX into lib/jev-search-index.json
npx shadcn@latest add https://raw.githubusercontent.com/kylemclaren/jevsearch/1df37decb960b3c4826c71b41d3393c15a8f28d3/public/r/jev-search-indexer.json
npx tsx scripts/jev-search-index.ts content/docs /docs
```

Then render `<JevSearch />` from `@/components/jev-search`. Each uncached query sends the query and up to 20 candidate titles, descriptions, and 320-character excerpts to TypeSafe and may incur charges.

## Examples and demos

- [Hosted demo](https://jevsearch.fly.dev) that searches the TypeSafe documentation (109 pages).
- `bun run bench` ([`bench/run.ts`](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/bench/run.ts)) compares it with Lunr, Fuse.js, Orama, MiniSearch, FlexSearch, and Pagefind on 41 labelled queries over that corpus. The author-reported results in [`bench/results.json`](https://github.com/kylemclaren/jevsearch/blob/1df37decb960b3c4826c71b41d3393c15a8f28d3/bench/results.json) are Hit@1 83% with Jev versus 41% for its keyword pass alone and 41% for Lunr, a 278 ms median uncached, and about $0.26 per thousand uncached searches. The benchmark calls the live API; it was not rerun for this listing.

## Limits and data handling

The query and candidate excerpts go over HTTPS to TypeSafe; the index and keyword pass stay on your server. The cache is in memory per process. The bundled sample index has three documents and must be replaced. The benchmark covers one corpus and was run by the author.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 1df37de](https://github.com/kylemclaren/jevsearch/tree/1df37decb960b3c4826c71b41d3393c15a8f28d3) by the maintainer. In a fresh clone, `bun install && bun run build` (shadcn registry build plus Astro build) passed; the build makes no TypeSafe calls. No live TypeSafe queries or benchmark runs were made for this review, and it makes no independent quality or accuracy claims.

Related: [jev-reranker](jev-reranker.md), [jev-reranker (hotchpotch)](hotchpotch-jev-reranker.md), [sieve](sieve.md), [Jev Search](../apps/jev-search.md).
