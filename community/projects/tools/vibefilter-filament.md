# Vibefilter for Filament

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Laravel Filament plugin that turns a sentence such as "The customer is angry." into a zero-shot table filter: TypeSafe Jev scores each row's probability that the statement is true, and the table keeps rows above your threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vibefilter/filament) |
| Maintainer | [vibefilter](https://github.com/vibefilter). Independently curated. |
| Format | Composer package for Filament |
| Requirements | PHP, Laravel with Filament; TypeSafe API key. |
| License | [MIT](https://github.com/vibefilter/filament/blob/709dc8f90c6b554b634ff975ccf98d6db8e93ec7/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let admin users filter reviews, tickets, or candidates by meaning instead of keywords.
- Mismatch: Every filtered row is sent to the hosted Jev API; costs scale with table size.

## How it works

The plugin adds a filter input; row text is sent to Jev as yes/no questions and the returned probabilities drive the threshold filter. (Summarized from the upstream [README](https://github.com/vibefilter/filament/blob/709dc8f90c6b554b634ff975ccf98d6db8e93ec7/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install with `composer require vibefilter/filament`, register the plugin in your Filament panel and configure your TypeSafe key.

## Limits and data handling

Row content is sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 709dc8f90c6b](https://github.com/vibefilter/filament/tree/709dc8f90c6b554b634ff975ccf98d6db8e93ec7). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
