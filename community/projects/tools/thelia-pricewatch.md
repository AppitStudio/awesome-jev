# PriceWatch (Thelia 3 competitor price watch where Jev judges only the narrow product-matching questions)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Thelia 3 e-commerce module that collects competitor offers (Google Shopping via DataForSEO), matches them to catalogue variants and reports price gaps in the back office. Code decides what it can see (GTIN equality, price gap, currency) and only narrow semantic questions go to Jev: same article, same variant, comparable price. Large gaps send Jev-only matches to a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thelia-modules/PriceWatch) |
| Maintainer | [thelia-modules](https://github.com/thelia-modules). Independently curated. |
| Format | Thelia 3 module (PHP) |
| Requirements | A Thelia 3 shop, a DataForSEO account, and a TypeSafe or OpenRouter key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Service/Jev/JevClient.php`](https://github.com/thelia-modules/PriceWatch/blob/bbe2eb86b67ee62b61095bf54513db9659d6000a/Service/Jev/JevClient.php) at the pinned commit. |

## When to use

- Monitor competitor prices with auditable matching.
- Mismatch: Thelia only; French e-commerce context.

## How it works

`Service/Jev/JevClient.php` sends typed judgments to `https://api.typesafe.ai/v1/systemone` or OpenRouter's System One endpoint (`jev-latest`), chosen in `Service/Settings/JevProvider.php`. Integration evidence: [`Service/Jev/JevClient.php`](https://github.com/thelia-modules/PriceWatch/blob/bbe2eb86b67ee62b61095bf54513db9659d6000a/Service/Jev/JevClient.php).

## Get started

From the upstream README (not run on the review host):

```sh
ddev exec php Thelia module:generate:model PriceWatch --generate-sql
ddev exec php Thelia module:schema:apply PriceWatch
ddev exec php Thelia module:activate PriceWatch
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/thelia-modules/PriceWatch#readme](https://github.com/thelia-modules/PriceWatch#readme)

## Limits and data handling

Product titles and competitor offer details go to TypeSafe or OpenRouter.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit bbe2eb86b67e](https://github.com/thelia-modules/PriceWatch/tree/bbe2eb86b67ee62b61095bf54513db9659d6000a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
