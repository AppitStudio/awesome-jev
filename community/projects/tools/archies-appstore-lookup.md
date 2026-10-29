# App Store Indexor (describe an app in plain words and get matching US top-chart apps scored by Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Natural-language lookup over Apple's public App Store charts: describe an app or its look ("habit tracker with streaks", "yellow bird icon"), local text and icon embeddings shortlist up to 120 apps, and one Jev request scores them; apps under 30% are dropped. Every field is marked verified, estimated or unavailable. Runs as a local Next.js site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/soloiaros/archies-appstore-lookup) |
| Maintainer | [soloiaros](https://github.com/soloiaros). Independently curated. |
| Format | Next.js app (TypeScript) |
| Requirements | Node.js and an OpenRouter or TypeSafe key. |
| License | [MIT](https://github.com/soloiaros/archies-appstore-lookup/blob/376d8aa51af028a7b01f598893e8313a091da44c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev/call.ts`](https://github.com/soloiaros/archies-appstore-lookup/blob/376d8aa51af028a7b01f598893e8313a091da44c/lib/jev/call.ts) at the pinned commit. |

## When to use

- Find apps by a vague memory of what they do or look like.
- Mismatch: US charts only; estimates are labeled as such.

## How it works

`lib/jev/call.ts` sends the query and shortlist to `https://openrouter.ai/api/v1/systemone` with `jev-latest`. Integration evidence: [`lib/jev/call.ts`](https://github.com/soloiaros/archies-appstore-lookup/blob/376d8aa51af028a7b01f598893e8313a091da44c/lib/jev/call.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/soloiaros/archies-appstore-lookup && cd archies-appstore-lookup
npm install && cp .env.example .env.local
npm run scrape:seed && npm run embed:pass
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/soloiaros/archies-appstore-lookup#readme](https://github.com/soloiaros/archies-appstore-lookup#readme)

## Limits and data handling

Queries and shortlisted app details go to OpenRouter.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 376d8aa51af0](https://github.com/soloiaros/archies-appstore-lookup/tree/376d8aa51af028a7b01f598893e8313a091da44c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
