# Orphaned Films

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free movie browser and player for public-domain films on archive.org (orphanedfilms.com) where Jev decided offline which TMDB film each upload really is and which films lead each collection shelf.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amponce/archive-movie-browser) |
| Tags | `Open source` · `Free` |
| Product homepage | [orphanedfilms.com](https://www.orphanedfilms.com) (behind a Cloudflare bot check; not loaded by the review host). |
| Pricing and access | Free web site; no account or key needed to browse and watch. Self-hosting is a free MIT source build; rebuilding the Jev index needs your own TMDB and OpenRouter keys. Checked 2026-10-06. |
| Jev evidence | [README: How films get identified](https://github.com/amponce/archive-movie-browser/blob/44a5df13eed0a246a246a5df87576515215d05c8/README.md#how-films-get-identified) and `scripts/build-poster-index.mjs` / `scripts/build-collections.mjs` document the offline `typesafe/jev-1.13` decisions written to `public/poster-index.json` and `public/collections.json`; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [amponce](https://github.com/amponce). Independently curated. |
| Format | Web app (static site + API functions) with an MCP server |
| Platform and availability | Web browser; self-host with Node.js. |
| Jev's role | Offline decision step: Jev picks which TMDB candidate (or none) an archive.org upload is, with a confidence, and chooses shelf highlights and strays; the site reads the stored decisions, so visitors trigger no Jev calls. |
| Requirements | None to browse. To self-host: Node.js; optional TMDB key for live matching; TMDB + OpenRouter keys only to rebuild the index. |
| License | [MIT](https://github.com/amponce/archive-movie-browser/blob/44a5df13eed0a246a246a5df87576515215d05c8/LICENSE). |

## When to use

- Browse and stream archive.org's public-domain films with correct titles, posters and details instead of messy upload names.
- Study a pattern: spend a few cents once on offline Jev decisions and serve them as static data with no per-request model cost.
- Mismatch: films are hosted and streamed by the Internet Archive; availability and rights are theirs, not this app's.

## How it works

`npm run index` gives Jev (`typesafe/jev-1.13` via OpenRouter) each upload's title and description plus a handful of TMDB candidates and asks which film it is, or none, and how sure. Below 0.7 the app shows a generated cover instead of risking a wrong poster. Collection shelves use Jev again to pick highlights and drop strays only when it is at least 0.8 sure. Weekly workflows refresh both files and open pull requests for review.

## Get started

Self-host per the README (no keys needed to run; index rebuilds make live OpenRouter calls):

```sh
git clone https://github.com/amponce/archive-movie-browser.git
cd archive-movie-browser
npm install
npm run dev        # http://localhost:3000
# optional: npm run index  (needs TMDB_API_KEY and OPEN_ROUTER_API_KEY in .env.local)
```

Browsing is free and makes no Jev calls. Rebuilding the index is billed by OpenRouter; upstream reports about 3 cents per 750 uploads and under a dollar for 16,387 decisions.

## Examples and demos

- Maintainer evaluation: on 80 hand-labelled hard search results, 67 right with 0 wrong posters vs 43 right and 5 wrong for the in-browser heuristics (README; not reproduced).
- `public/collections.json` lists every film Jev left out of a shelf with its confidence, for easy correction.

## Limits and data handling

Jev decisions are stored and can be wrong; users can correct entries by PR (`"m": 1` marks a manual fix). The live site was not loaded from the review host (Cloudflare challenge). Film availability depends on archive.org and TMDB.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 44a5df13eed0](https://github.com/amponce/archive-movie-browser/tree/44a5df13eed0a246a246a5df87576515215d05c8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
