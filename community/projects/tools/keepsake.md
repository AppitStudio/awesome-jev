# Keepsake (X saves for your agents)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local, searchable library of the posts you like and bookmark on X: a Chrome extension captures saves, a Node service stores them in SQLite and Markdown, and Jev classifies each save and ranks the library for natural-language questions from a CLI and MCP server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brianbolze/keepsake) |
| Maintainer | [brianbolze](https://github.com/brianbolze). Independently curated. |
| Format | Local service, Chrome extension, CLI and MCP server (Node.js 24+) |
| Requirements | macOS (Linux untested), Node.js 24+, Chrome; optional `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/brianbolze/keepsake/blob/27c8b5306a7e8c67b5f4234835d932315faf3514/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/brianbolze/keepsake/blob/27c8b5306a7e8c67b5f4234835d932315faf3514/src/jev.ts) at the pinned commit. |

## When to use

- Let your coding agent search what you saved on X.
- Sort saves into type, topics and work or personal automatically.
- Mismatch: without a key, saves stay unclassified and search falls back to keywords.

## How it works

`src/jev.ts` sends captured post text and page excerpts to Jev for classification and semantic ranking; a persistent ledger caps spend at $20 per data directory and caches judgments. Integration evidence: [`src/jev.ts`](https://github.com/brianbolze/keepsake/blob/27c8b5306a7e8c67b5f4234835d932315faf3514/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run build
npm start
# put TYPESAFE_API_KEY=your-key in .env, then load extension/ unpacked in Chrome
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start and MCP setup in the README: [github.com/brianbolze/keepsake#readme](https://github.com/brianbolze/keepsake#readme)

## Limits and data handling

Post text and fetched excerpts go to TypeSafe; images, video and browsing history do not. Not affiliated with X.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 27c8b5306a7e](https://github.com/brianbolze/keepsake/tree/27c8b5306a7e8c67b5f4234835d932315faf3514). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
