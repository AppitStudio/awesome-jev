# FilmHunch

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hostable movie finder: describe a film any way you like and TypeSafe Jev scores film cards and full profiles against your exact sentence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eduardoalba00/film-hunch) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/eduardoalba00/film-hunch#readme](https://github.com/eduardoalba00/film-hunch#readme) |
| Pricing and access | Free MIT source; upstream reports ~US$0.05 per search in TypeSafe/embedding costs on your keys (not verified here). |
| Jev evidence | [`apps/api/lib/jev.js`](https://github.com/eduardoalba00/film-hunch/blob/5e726f90f1ded03ad2047c3249c2c3dc6e7629da/apps/api/lib/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [eduardoalba00](https://github.com/eduardoalba00). Independently curated. |
| Format | Web app (JavaScript monorepo) |
| Platform and availability | Web (self-hosted Node API + web app) |
| Jev's role | Jev scores short cards for the 5,000 most-rated films plus ~300 retrieved candidates, then re-scores the top 40 on full profiles; code merges and streams results. |
| Requirements | Node.js; film dataset build per README; TypeSafe key and embedding provider key. |
| License | [MIT](https://github.com/eduardoalba00/film-hunch/blob/5e726f90f1ded03ad2047c3249c2c3dc6e7629da/LICENSE) |

## When to use

- Vibe-based film search ("sci-fi with no spaceships") where keyword search misses obvious answers.
- Mismatch: Self-host only; quality figures are the author's own small eval.

## How it works

Retrieval (vector + keyword) proposes candidates alongside a fixed popular-film set; Jev scores each card in batches of 16, re-scores finalists on longer profiles, and a small popularity bonus breaks near-ties. (Summarized from the upstream [README](https://github.com/eduardoalba00/film-hunch/blob/5e726f90f1ded03ad2047c3249c2c3dc6e7629da/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): clone the repo, build the film data and set keys per the README, then start the API and web app.

## Limits and data handling

Search text and film cards go to TypeSafe; results are cached 72 hours. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 5e726f90f1de](https://github.com/eduardoalba00/film-hunch/tree/5e726f90f1ded03ad2047c3249c2c3dc6e7629da). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
