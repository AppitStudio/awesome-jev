# Bookmark Finder

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local CLI and HTTP API that searches your GitHub stars and X bookmarks: SQLite + BM25 (and optional embeddings) retrieve candidates, then Jev optionally reranks them with a 0-3 relevance score and confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ismailucrn/bookmarkfinder) |
| Maintainer | [ismailucrn](https://github.com/ismailucrn). Independently curated. |
| Format | Node.js CLI + local HTTP API (backend MVP) |
| Requirements | Node.js 24+; GitHub token and/or X user token to sync; `JEV_API_KEY` only for reranking. |
| License | [MIT](https://github.com/ismailucrn/bookmarkfinder/blob/a72f0f724cde6cb0acbe3477e5baca00fcc52acc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/workers/jev.mjs`](https://github.com/ismailucrn/bookmarkfinder/blob/a72f0f724cde6cb0acbe3477e5baca00fcc52acc/src/workers/jev.mjs) at the pinned commit. |

## When to use

- Find a starred repo or bookmarked post by meaning when you only remember roughly what it did.
- Study a reranker that validates every Jev score and refuses non-official API URLs.
- Mismatch: local MVP without UI, OAuth or scheduled sync; search quality and cost not yet validated by the author.

## How it works

Candidates from BM25/embeddings are sent to Jev (`jev-latest` at `api.typesafe.ai/v1/systemone`) as a Score question per item; answers outside range or inconsistent with their probabilities are rejected, and without a key `relevanceScore` stays `null`. Integration evidence: [`src/workers/jev.mjs`](https://github.com/ismailucrn/bookmarkfinder/blob/a72f0f724cde6cb0acbe3477e5baca00fcc52acc/src/workers/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm run setup
npm run demo                          # offline sample, lexical only
npm run search -- "React analytics" --demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Connector behaviour: `docs/connectors.md`; status: `STATUS.md`.

## Limits and data handling

Saved items stay in local SQLite; with reranking on, Jev receives the query, title and up to 12,000 characters per candidate on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit a72f0f724cde](https://github.com/ismailucrn/bookmarkfinder/tree/a72f0f724cde6cb0acbe3477e5baca00fcc52acc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
