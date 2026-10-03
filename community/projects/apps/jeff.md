# Jeff

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted bookshelf search and sort: visitors ask by mood, theme, or plot; TypeSafe Jev ranks books, articles, and newsletters on the shelf. Any visitor can upload a Goodreads CSV and publish a shelf with a link and QR code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://read.atharvashah.com) |
| Tags | `Closed source` · `Free` |
| Product homepage | [read.atharvashah.com](https://read.atharvashah.com) |
| Pricing and access | Free for visitors (no account, no visitor API key). Operator-paid Jev with stated caps (~$1/day, ~$5/month) then keyword fallback. No visitor pricing page. Checked **2026-10-04** from issue #949. |
| Jev evidence | Self-submission [issue #949](https://github.com/AppitStudio/awesome-jev/issues/949) (Atharva Shah via JevList) documents Noul/Choice design, measured latency/cost on a 1,186-item shelf, and live site behavior. Live homepage title “Jeff · A Bookshelf You Can Ask” (HTTP 200). Implementation was **not** inspected (no public source); TypeSafe API traffic was **not** captured on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Closed source. The implementation was not inspected; Jev use is a maker claim from issue #949 and the live product, not independently observed API traffic. Listing is not an endorsement. Live install/UI paths not run on the Linux review host. |
| Maintainer | Atharva Shah (self-submitted via JevList / Awesome Jev [issue #949](https://github.com/AppitStudio/awesome-jev/issues/949)). Independently curated listing. |
| Format | Hosted web bookshelf (closed source) |
| Platform and availability | Public web app (Netlify/Cloudflare edge; HTTP 200 on review) |
| Jev's role | Maker claim (issue #949): Search asks one Noul per item (~50/batch, parallel); Sorting asks one Choice per item into 21 categories; application code owns parsing, caching, the 35% cutoff, and spend caps. Model jev-latest on api.typesafe.ai/v1/systemone. |
| Requirements | Modern browser. No account for visitors. |
| License | Proprietary hosted product; repository is private. No public open-source license. |

## When to use

Use Jeff when you want a free hosted bookshelf you can query by meaning, or to publish a Goodreads shelf. Prefer open-source retrieval/ranking tools when you need inspectable System One integration code.

## How it works

Maker materials describe per-item Noul relevance scoring (batched) and Choice category sorting; code applies a 35% cutoff and spend caps, with keyword fallback past the operator budget. This catalogue entry does not claim to have inspected TypeSafe question schemas or live API traffic.

## Get started

1. Open [https://read.atharvashah.com](https://read.atharvashah.com).
2. Try a mood/theme/plot query on the operator shelf, or upload a Goodreads CSV to publish a visitor shelf.

Homepage returned HTTP 200 during review; no account creation and no instrumented live Jev traffic by the curator.

## Examples and demos

- Live product: [read.atharvashah.com](https://read.atharvashah.com)
- Submission: [AppitStudio/awesome-jev#949](https://github.com/AppitStudio/awesome-jev/issues/949)

## Limits and data handling

Closed source: prompts, thresholds, logging, and retention were not inspected. Assume queries and shelf/CSV content may be processed by the operator backend and TypeSafe. Uploaded shelves without plot text yield weaker results (maker-reported). Caps: 100 published shelves, 3,000 items/shelf (maker-reported).

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia). Primary sources: live site HTTP 200, [issue #949](https://github.com/AppitStudio/awesome-jev/issues/949). AI-assisted review; no live TypeSafe key used by the curator. Fixes #949.
