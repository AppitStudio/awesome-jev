# The Pragmatic Engineer newsletter search

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free search over The Pragmatic Engineer newsletter archive, built on turbopuffer full-text search with Jev categorizing and reranking results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://www.pragmaticengineer.com/search) |
| Tags | `Closed source` · `Free` |
| Product homepage | [The Pragmatic Engineer newsletter search](https://www.pragmaticengineer.com/search) |
| Pricing and access | The search page is public and needs no account, checked **2026-11-13**. Results include paid newsletter articles, which need a paid subscription to read in full. |
| Jev evidence | The page footer credits Jev "for fast, low-cost, high-quality search result categorization", and the author [posted on X](https://x.com/GergelyOrosz/status/2121053731114643785) that he reranked search results with Jev. Closed source; the implementation was not inspected and TypeSafe traffic was not observed. |
| Disclosure | Closed source. The implementation was not inspected; Jev use comes from the page's own credits and the author's X post. AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Discovered via X ([post](https://x.com/GergelyOrosz/status/2121053731114643785)). |
| Maintainer | Gergely Orosz ([@GergelyOrosz](https://x.com/GergelyOrosz)), author of The Pragmatic Engineer. Independently curated. |
| Format | Hosted web search page (browser, JavaScript required) |
| Platform and availability | Any modern browser at [pragmaticengineer.com/search](https://www.pragmaticengineer.com/search) |
| Jev's role | Categorizes and reranks full-text search results from turbopuffer (per the page credits and the author's post). |
| Requirements | A browser with JavaScript; a paid subscription only to read paid articles. |
| License | Proprietary hosted page; no public source. |

## When to use

- Find past Pragmatic Engineer articles on a topic, with free and paid results filterable.
- See a production example of Jev used as a fast reranking and categorization layer on top of full-text search.
- Mismatch: searching other publications, or a self-hosted search stack.

## How it works

The page sends your query to the site's search backend, which runs full-text search on turbopuffer and, per the page credits, uses Jev to categorize the results; the author's X post says results are reranked with Jev and notes that turbopuffer now supports Jev reranking natively. The backend, prompts and questions were not inspected.

## Get started

Open [pragmaticengineer.com/search](https://www.pragmaticengineer.com/search), type a topic or a half-remembered article, and filter by free or paid access.

## Examples and demos

- Author's announcement with screenshot: [x.com/GergelyOrosz/status/2121053731114643785](https://x.com/GergelyOrosz/status/2121053731114643785)

## Limits and data handling

Closed source: Jev questions, ranking logic and data retention were not inspected. Queries go to the site's backend; the page uses Plausible analytics and logs result clicks. No live search was run on the review host.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia). Inspected the public page and its JavaScript bundle (footer credits naming turbopuffer and Jev; `/search/results` backend call) and the author's X post. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
