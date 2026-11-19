# Best of Go by Mike Fridman (daily star rankings of 35,000 Go repositories, sorted into categories by Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free website that tracks daily star history for Go projects on GitHub with 50 or more stars (about 35,000 repositories) and ranks them by the stars they gained yesterday, this week, this month and of all time. Category pages cover about 86 categories (76 from awesome-go and 10 more for apps such as AI agents and LLM infrastructure). The maker says Jev read each repository's name, description and topics, picked a category with a confidence, and only assigned one at 90% or higher, which categorised over 14,000 repositories. An MCP server lets AI assistants search and rank the same data.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://bestofgo.dev) |
| Tags | `Closed source` · `Free` |
| Product homepage | [bestofgo.dev](https://bestofgo.dev) |
| Pricing and access | Free public website; no account needed to browse. Checked **2026-11-19**. The MCP server was not tested. |
| Jev evidence | Maker's claim: Mike Fridman's [X thread](https://x.com/_mfridman/status/2123405034192839011) (2026-11-19) says he had Jev sort the repositories into categories and explains the method (name, description and topics in; one category with a confidence out; assigned only at 90% or higher). The site's About page does not mention Jev. The implementation was not inspected. |
| Disclosure | Closed source (no public repository found for the site). Jev use is the maker's public claim, not independently observed API traffic; the categorisation is a batch job, so visiting the site does not call Jev. Independently curated for Awesome Jev; no affiliation or commercial relationship with the vendor. Inclusion is not an endorsement. Discovered via X ([post](https://x.com/_mfridman/status/2123405034192839011)). |
| Maintainer | [Mike Fridman](https://mfridman.com) ([@_mfridman](https://x.com/_mfridman), GitHub [mfridman](https://github.com/mfridman)). |
| Format | Public website (Go server, SQLite, htmx) with an MCP server. |
| Platform and availability | Web (hosted). |
| Jev's role | Maker's claim: picks one category per repository from a fixed list, with a confidence; low-confidence repositories stay uncategorised. |
| Requirements | A web browser. An MCP client only if you use the MCP server. |
| License | Proprietary website. No public repository found. |

## When to use

Use Best of Go to find popular or fast-rising Go libraries and apps by category, including categories awesome-go does not cover. Mismatch: a hand-curated list; categories are model-assigned and some repositories have none.

## How it works

The site refreshes GitHub data every hour and keeps daily star history. For categories, the maker describes a one-off classification: for each repository Jev read the name, description and GitHub topics, chose one category and reported how sure it was, and a repository was only placed at 90% confidence or more, never into a catch-all. No API calls were observed for this listing.

## Get started

1. Open [bestofgo.dev](https://bestofgo.dev) for trending repositories.
2. Browse [bestofgo.dev/categories](https://bestofgo.dev/categories) for the Jev-assigned categories.
3. Optionally add the MCP server described on the [About page](https://bestofgo.dev/about) to your AI assistant.

## Examples and demos

- [Maker's X thread](https://x.com/_mfridman/status/2123405034192839011) explaining the categorisation.
- [Category index](https://bestofgo.dev/categories).

## Limits and data handling

Categories are model judgments on repository metadata only (not code) and may be wrong; about 14,000 of 35,000 repositories have one. Star counts come from GitHub. The site's implementation and the classification prompts were not inspected.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) with AI assistance. Primary sources: [bestofgo.dev](https://bestofgo.dev) and [bestofgo.dev/about](https://bestofgo.dev/about) (fetched 2026-11-19) and the maker's [X thread](https://x.com/_mfridman/status/2123405034192839011) (2026-11-19). Catalog de-dupe found no existing Best of Go listing.
