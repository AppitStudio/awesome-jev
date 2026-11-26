# chunk-standalone by Hamza Ahmad Aslam (CLI that finds RAG chunks a reader cannot understand on their own and suggests keep, merge or split with Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Checks the chunks of a RAG knowledge base for ones that depend on text elsewhere ("as shown above", a list that continues in the next chunk, an unexplained "it") and suggests keep, merge with a neighbour or split for each. It takes Markdown, text or JSONL chunks, asks Jev narrow yes/no and multiple-choice questions, and sends unclear cases to a review list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/chunk-standalone) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/chunk-standalone/blob/3ea77c658e5295eb2c29b9c5c70d1ece890e7569/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/chunk-standalone/blob/3ea77c658e5295eb2c29b9c5c70d1ece890e7569/src/jev.mjs) at the pinned commit. |

## When to use

- Teams that chunk Markdown or text for retrieval and want a CI check that catches chunks which lose their meaning out of context.
- Mismatch: exact reproduction of your own chunker; the built-in splitters approximate common ones, so feed JSONL for your real chunks.

## How it works

`src/jev.mjs` sends each chunk with its neighbours to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`, 8 chunks per request) and code turns the probabilities into a verdict at `--threshold` (0.8). The exit code is 1 when a chunk needs a fix, so it can fail a CI job. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/chunk-standalone/blob/3ea77c658e5295eb2c29b9c5c70d1ece890e7569/src/jev.mjs).

## Get started

Install from npm, set your key and run it on a docs folder; try `--dry-run` first to see the chunks and questions.

```sh
npm install -g @hamzaahmadaslam/chunk-standalone
export TYPESAFE_API_KEY=...
chunk-standalone docs/ --dry-run   # nothing sent
chunk-standalone docs/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Worked example in the README: [github.com/hamzaahmadaslam/chunk-standalone#example](https://github.com/hamzaahmadaslam/chunk-standalone#example)

## Limits and data handling

Chunk text goes to TypeSafe. Jev sees the chunk and its neighbours, not what your pipeline adds at query time. English is where it is most accurate; text written to steer a model can move answers. The tool reports and never edits files; treat fix verdicts as suggestions.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 3ea77c658e52](https://github.com/hamzaahmadaslam/chunk-standalone/tree/3ea77c658e5295eb2c29b9c5c70d1ece890e7569). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
