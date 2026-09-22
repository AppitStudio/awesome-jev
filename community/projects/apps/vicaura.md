# Vicaura

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted product-intelligence app that turns a product website or description into a markdown repo of features, ICP, messaging, and pricing strategy for use in coding agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://vicaura.com) |
| Tags | `Closed source` · `Pricing unverified` |
| Product homepage | [Vicaura](https://vicaura.com) |
| Pricing and access | Public homepage offers a Generate-repo workflow and Sign in; no public pricing page was found (`/pricing` returned 404). [Terms & Privacy](https://vicaura.com/terms-privacy) describe accounts, guest searches (normally tab-scoped and expiring), and optional paid subscriptions or one-time purchases via Stripe when offered. Checked **2026-09-22**; current plan prices, free-tier allowances, and checkout were not verified. |
| Jev evidence | Vendor-stated: the product author posted that the tool is [powered by Jev](https://x.com/mmmikhaeel/status/2102105486501822826) and extracts product features and business logic into markdown. The [homepage](https://vicaura.com) describes product-logic → markdown for coding agents. Implementation was not inspected; no live generate run was performed. |
| Disclosure | Closed source. The implementation was not inspected; Jev use is a vendor claim from the linked X post and product positioning, not independently observed API traffic. Pricing and access details remain partly unverified. Independently curated for Awesome Jev; no affiliation or commercial relationship with Vicaura. Inclusion is not endorsement. |
| Maintainer | [Mikhaeel](https://x.com/mmmikhaeel) (Chief prompting officer @ vicaura.com); contact [hello@vicaura.com](mailto:hello@vicaura.com). |
| Format | Hosted web application (Next.js) with account sign-in and markdown repo generation. |
| Platform and availability | Public web app at [vicaura.com](https://vicaura.com). Release stage and account requirements beyond the public Sign-in control were not fully verified. |
| Jev's role | Vendor claim: Jev powers extraction of product features, ICP, messaging, pricing strategy, and related product logic into markdown. Other providers listed in Terms (search, crawling, extraction, Google AI analysis) may participate; whether Jev is required for every path was not verified. |
| Requirements | Modern browser; product URL or description. Account/sign-in may be required when guest access is unavailable. Generated outputs should be reviewed before use. |
| License | Proprietary hosted service. Access governed by [Terms & Privacy](https://vicaura.com/terms-privacy). No public open-source license; [github.com/VicAura](https://github.com/VicAura) showed **0** public repositories on review. |

## When to use

Use Vicaura when you want structured markdown about another product's features, customer profile, messaging, or pricing strategy for agent-assisted building or competitive research. It is a hosted research product, not a self-hosted library. Do not treat generated markdown as verified legal, financial, or competitive fact without checking primary sources.

## How it works

The public landing page accepts a product website URL or product description and submits a generate-repo request. Vendor materials describe copying extracted product context into markdown files for coding agents. Terms state that production features may use search, crawling, extraction, analytics, and AI providers, and that outputs can include errors or inferred material.

Jev involvement is documented only by the author's public statement that the tool is powered by Jev. This catalog entry does not claim to have inspected TypeSafe API calls, question schemas, or confidence handling.

## Get started

This path follows the public homepage; it was not executed end-to-end during review (no account creation and no live generation).

1. Open [vicaura.com](https://vicaura.com).
2. Choose **Product website** or **Product description**, enter a non-sensitive public product URL or short description, and use **Generate repo**.
3. If the UI prompts for **Sign in**, complete the account flow shown by the product.
4. Review every generated markdown file and citations against the original product site before copying into an agent context.

Respect third-party site terms; do not use the service to bypass access controls. Provider and subscription charges may apply under the vendor's terms.

## Examples and demos

The [homepage](https://vicaura.com) is the verified public entry point. The author's [demo video on X](https://x.com/mmmikhaeel/status/2102105486501822826) illustrates the intended URL → markdown workflow; that recording was not independently reproduced here. No separate public API docs or open sample repository were found.

## Limits and data handling

Closed source: backend prompts, Jev questions, and scoring were not inspected. Terms warn that outputs may be inaccurate and that public-web research and AI providers process submitted URLs, descriptions, and related material. Guest searches are described as tab-scoped and short-lived; account and billing data follow the privacy notice. Exact retention, subprocessors in production, and paid-plan limits were not independently audited.

## Review and maintenance

Reviewed **2026-09-22** (Europe/Sofia) with AI assistance. Primary sources: [vicaura.com](https://vicaura.com) (HTTP 200), [Terms & Privacy](https://vicaura.com/terms-privacy) (last updated 25 August 2026), author X post [2102105486501822826](https://x.com/mmmikhaeel/status/2102105486501822826), and GitHub user [VicAura](https://github.com/VicAura) (`public_repos: 0`). `/pricing` returned 404. No signup, payment, or live generate was performed. Catalog de-dupe found no existing Vicaura listing.

Related: none in this directory yet for product-to-markdown research apps.
