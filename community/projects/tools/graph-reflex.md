# GraphReflex (Neo4j measures, TypeSafe Jev decides, the LLM writes)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Open experiment that pairs a Neo4j knowledge graph with TypeSafe Jev as the fast decision layer for graph QA, with a live cockpit and an STaRK benchmark harness.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tukka25/graph-reflex) |
| Maintainer | [tukka25](https://github.com/tukka25). Independently curated. |
| Format | TypeScript app + benchmark harness (no SPDX license file on the reviewed commit) |
| Requirements | Node.js, a Neo4j instance, a TypeSafe API key, and an LLM key for answer writing. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/jev/client.ts`](https://github.com/tukka25/graph-reflex/blob/3a1b05c05086b618152ad89a4ca0cc22c3239e06/src/lib/jev/client.ts) at the pinned commit. |

## When to use

- Test whether a System One model makes graph agents faster and more reliable.
- Reproduce the STaRK benchmark comparison.
- Mismatch: experiment; no OSI license on the reviewed commit.

## How it works

`src/lib/jev/client.ts` posts typed questions to `https://api.typesafe.ai/v1/systemone` (shapes from the public OpenAPI) to pick graph actions. Integration evidence: [`src/lib/jev/client.ts`](https://github.com/tukka25/graph-reflex/blob/3a1b05c05086b618152ad89a4ca0cc22c3239e06/src/lib/jev/client.ts).

## Get started

Clone, configure Neo4j and keys per README, and start the cockpit or benchmark.

```sh
git clone https://github.com/tukka25/graph-reflex.git && cd graph-reflex
export TYPESAFE_API_KEY=...
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tukka25/graph-reflex/blob/3a1b05c05086b618152ad89a4ca0cc22c3239e06/README.md](https://github.com/tukka25/graph-reflex/blob/3a1b05c05086b618152ad89a4ca0cc22c3239e06/README.md)

## Limits and data handling

Graph context and questions are sent to TypeSafe and the LLM provider on your keys.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 3a1b05c05086](https://github.com/tukka25/graph-reflex/tree/3a1b05c05086b618152ad89a4ca0cc22c3239e06). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
