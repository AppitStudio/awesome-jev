# Exocortex (headless knowledge graph for your notes, transcripts and X bookmarks where Jev decides which people, products and topics each passage is about)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

CLI knowledge base on HelixDB (entity graph, BM25 and vectors in one database) for documents, transcripts, notes and X bookmarks, built for people and agents. Because embeddings could not separate passages that name a person from unrelated ones, Jev makes every judgement: category, salience, whether a passage is about the owner, whether a name deserves a node, whether two names are one thing, and which entities each passage really discusses. A link is written only at confidence 0.9 and checked twice. GLM writes only the missing names and profile drafts, and every name it proposes is checked by Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Konan69/exocortex) |
| Maintainer | [Konan69](https://github.com/Konan69). Independently curated. |
| Format | Bun/TypeScript CLI (`exo`) with HelixDB (MIT) |
| Requirements | Bun 1.3, Docker and the Helix CLI; `OPENROUTER_API_KEY` for Jev and GLM, and optionally `OPENAI_API_KEY` for query vectors. |
| License | [MIT](https://github.com/Konan69/exocortex/blob/12ff84cd06bd72dfd89fa0b1977ede01be9d735e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/ai.ts`](https://github.com/Konan69/exocortex/blob/12ff84cd06bd72dfd89fa0b1977ede01be9d735e/src/ai.ts) at the pinned commit. |

## When to use

- Build a personal or agent-readable knowledge graph whose links come from checked decisions, not embedding distance.
- Mismatch: drop-in vector search; it needs Helix, Docker and several model calls per passage.

## How it works

`src/ai.ts` wires Jev (`typesafe/jev-1.13`, set in `src/config.ts`) through OpenRouter's decisions API as an `effect/ai` `DecisionModel` with concurrency, pacing and retries; GLM and OpenAI embeddings are separate services. Integration evidence: [`src/ai.ts`](https://github.com/Konan69/exocortex/blob/12ff84cd06bd72dfd89fa0b1977ede01be9d735e/src/ai.ts).

## Get started

Install, configure keys and Helix, seed the taxonomy, ingest the fixture notes and search.

```sh
git clone https://github.com/Konan69/exocortex && cd exocortex
bun install --frozen-lockfile
cp .env.example .env && cp helix.example.toml helix.toml
bun exo.ts taxonomy --seed --yes
bun exo.ts ingest fixtures/notes
bun exo.ts search "solar greenhouse"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Konan69/exocortex/blob/12ff84cd06bd72dfd89fa0b1977ede01be9d735e/README.md](https://github.com/Konan69/exocortex/blob/12ff84cd06bd72dfd89fa0b1977ede01be9d735e/README.md)

## Limits and data handling

Passages go to OpenRouter (Jev and GLM) and optionally OpenAI on your keys; the graph stays in your local Helix. The maker reports 105 articles cost about $0.03 to label; the search evaluation figures are the maker's own.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 12ff84cd06bd](https://github.com/Konan69/exocortex/tree/12ff84cd06bd72dfd89fa0b1977ede01be9d735e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
