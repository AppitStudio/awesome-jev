# Penny (grocery receipt review for Grocy, with Jev suggesting storage and groups)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted receipt review for Grocy: upload a grocery receipt PDF, OpenAI extracts the lines, Jev suggests a storage location and product group for each product (low-confidence ones stay unassigned), and confirmed purchases are imported into Grocy stock.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YuryFilipovich/Penny) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/YuryFilipovich/Penny#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free source build. Uses your own OpenAI and TypeSafe keys. Checked 2026-10-24. |
| Jev evidence | [`server/extraction.ts`](https://github.com/YuryFilipovich/Penny/blob/07b3a5ebbf63c6371dddbc9715f95dc98e939517/server/extraction.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [YuryFilipovich](https://github.com/YuryFilipovich). Independently curated. |
| Format | Self-hosted web app (Svelte 5, Node.js) |
| Platform and availability | Self-hosted web app run from source. |
| Jev's role | Suggests storage locations and product groups; extraction uses OpenAI. |
| Requirements | Node.js 22.18+; OpenAI and Jev API keys; a Grocy instance and API key to import. |
| License | [Apache-2.0](https://github.com/YuryFilipovich/Penny/blob/07b3a5ebbf63c6371dddbc9715f95dc98e939517/LICENSE) |

## When to use

- Turn grocery receipts into Grocy stock without typing every line.
- Review and correct suggestions before anything is written.
- Mismatch: confirming a purchase is a real Grocy write that Penny cannot undo.

## How it works

`server/extraction.ts` posts batches of extracted products to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) and keeps only confident suggestions. Integration evidence: [`server/extraction.ts`](https://github.com/YuryFilipovich/Penny/blob/07b3a5ebbf63c6371dddbc9715f95dc98e939517/server/extraction.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
cp .env.example .env   # OPENAI_API_KEY, JEV_API_KEY, Grocy URL
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshots: [github.com/YuryFilipovich/Penny#readme](https://github.com/YuryFilipovich/Penny#readme)

## Limits and data handling

OpenAI receives the PDF; Jev receives product details. Uploads are processed in memory.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 07b3a5ebbf63](https://github.com/YuryFilipovich/Penny/tree/07b3a5ebbf63c6371dddbc9715f95dc98e939517). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
