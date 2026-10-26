# Treg ("OpenRouter for agent tools": pay-per-call tool catalog whose tool search is judged by Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted tool registry from Superdesign: agents use one base URL and token to call thousands of priced endpoints (SEO, social, people and company enrichment, ads, scraping, media generation) without provider accounts, plus team keys and skills; tool search sends the query and candidates to Jev in one judge request, and Jev is also offered as a catalog endpoint.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/superdesigndev/treg) |
| Tags | `Source available` · `Paid` · `Commercial` |
| Product homepage | [Product homepage](https://treg.to) |
| Pricing and access | Pay per call, with prices shown per endpoint on [treg.to](https://treg.to) (from about one cent per the README); new verified accounts get $1.00 of free credit. Licence: Apache-2.0 with Additional Terms that forbid offering it as a hosted service to third parties without permission — source available, not OSI open source, despite the launch post's "fully open source" wording. Checked 2026-10-26. |
| Jev evidence | [`src/treg/application/catalog_find.py`](https://github.com/superdesigndev/treg/blob/616e7eaaf44b56978ae9cf2fca1189f04892ea36/src/treg/application/catalog_find.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Commercial: Treg is a paid hosted service; the listing is not paid placement. Discovered via X ([post](https://x.com/treg_ai/status/2114674262179188755)). |
| Maintainer | [superdesigndev](https://github.com/superdesigndev). Independently curated. |
| Format | Hosted service with CLI and agent skills (Python server) |
| Platform and availability | Web service at treg.to with a CLI and agent skills; self-hosting for your own organisation is permitted. |
| Jev's role | Search judge: `/catalog/find` sends the job description and recalled tools to Jev, which keeps or drops each candidate; Jev is also resold as the `typesafe.jev` endpoint. |
| Requirements | A treg.to account and token; self-hosting needs your own provider keys and a TypeSafe key for the search judge. |
| License | [Apache-2.0 with Additional Terms (source available; no hosted service for third parties without permission)](https://github.com/superdesigndev/treg/blob/616e7eaaf44b56978ae9cf2fca1189f04892ea36/LICENSE) |

## When to use

- Give an agent many paid data tools without signing up for each provider.
- Let agents find the right tool by describing the job.
- Mismatch: a commercial reseller; Jev calls made through Treg are relayed by Treg, not sent to TypeSafe by you.

## How it works

`src/treg/application/catalog_find.py` passes the query and recalled tools to `src/treg/infra/judge.py`, which posts one System One request to the configured TypeSafe URL and model; results are cached per query. Integration evidence: [`src/treg/application/catalog_find.py`](https://github.com/superdesigndev/treg/blob/616e7eaaf44b56978ae9cf2fca1189f04892ea36/src/treg/application/catalog_find.py).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://treg.to/install.sh | sh
# see the README for treg catalog find / treg call
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product: [treg.to](https://treg.to)
- README: [github.com/superdesigndev/treg#readme](https://github.com/superdesigndev/treg#readme)
- Launch post on X: [x.com/treg_ai/status/2114674262179188755](https://x.com/treg_ai/status/2114674262179188755)

## Limits and data handling

Queries, call parameters and results pass through Treg and the providers it routes to. Price, accuracy and "85% cheaper than Clay" claims are the vendor's, not verified here.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 616e7eaaf44b](https://github.com/superdesigndev/treg/tree/616e7eaaf44b56978ae9cf2fca1189f04892ea36). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
