# Sift (Chrome extension that reranks Google results with Jev and folds away sales pages and SEO filler)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that moves Google results that actually answer your query to the top and folds away sales pages and SEO filler. Each search gets one extra question about whether it is transactional ("buy nike pegasus 41"), so shopping searches keep their sales pages.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tylergibbs1/sift) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/tylergibbs1/sift#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free. Jev calls are billed to your own TypeSafe key. Checked 2026-10-28. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/tylergibbs1/sift/blob/14d979658adfe407490efda421b38e9082baae1f/src/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tylergibbs1](https://github.com/tylergibbs1). Independently curated. |
| Format | Chrome extension (Manifest V3, TypeScript) |
| Platform and availability | Chrome; build from source and load unpacked (no store listing verified). |
| Jev's role | Per-result relevance and page-type decisions, plus one search-intent question per query. |
| Requirements | Chrome, Node.js to build, and a TypeSafe API key. |
| License | [MIT](https://github.com/tylergibbs1/sift/blob/14d979658adfe407490efda421b38e9082baae1f/LICENSE) |

## When to use

- Cut through SEO-heavy results on research searches.
- Mismatch: Google Search only.

## How it works

`src/jev/client.ts` posts the query and result snippets to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and reorders or folds results from the answers. Integration evidence: [`src/jev/client.ts`](https://github.com/tylergibbs1/sift/blob/14d979658adfe407490efda421b38e9082baae1f/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tylergibbs1/sift && cd sift
npm install && npm run build   # load dist/ in chrome://extensions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tylergibbs1/sift#readme](https://github.com/tylergibbs1/sift#readme)

## Limits and data handling

Your queries and result snippets go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 14d979658adf](https://github.com/tylergibbs1/sift/tree/14d979658adfe407490efda421b38e9082baae1f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
