# DMLab TypeSafe Core (Jev for Magento 2)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Magento 2 module that connects a store to TypeSafe's Jev with one encrypted key, a pinned model version, a monthly token budget, a response cache, retries and a circuit breaker, shared by DMLab AI modules such as Catalog Enrich, which fills empty product filter attributes from descriptions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dmlab-work/module-typesafe-core) |
| Maintainer | [dmlab-work](https://github.com/dmlab-work). Independently curated. |
| Format | Magento 2 module (PHP, Composer `dmlab/module-typesafe-core`) |
| Requirements | Magento 2.4.9+, PHP 8.3 to 8.5 with ext-curl, and your own TypeSafe key. |
| License | [OSL-3.0](https://github.com/dmlab-work/module-typesafe-core/blob/987c72a50c9271d45bc57326a771b18e248d2dd5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Model/Client.php`](https://github.com/dmlab-work/module-typesafe-core/blob/987c72a50c9271d45bc57326a771b18e248d2dd5/Model/Client.php) at the pinned commit. |

## When to use

- Give Magento modules typed yes/no, choice and score answers about products without each one managing keys and spend.
- Fill empty product attributes from descriptions with the companion [Catalog Enrich](https://github.com/dmlab-work/module-catalog-enrich) module.
- Mismatch: on its own it adds no storefront or catalog behaviour.

## How it works

`Model/Client.php` builds `POST /v1/systemone` requests for each consumer module, sends batches in parallel with `evaluateMany()`, caches identical questions and accounts tokens and cost per module against a monthly budget. Admin settings live under Stores > Configuration > DMLab > TypeSafe. Integration evidence: [`Model/Client.php`](https://github.com/dmlab-work/module-typesafe-core/blob/987c72a50c9271d45bc57326a771b18e248d2dd5/Model/Client.php).

## Get started

From the upstream README (not run on the review host):

```sh
composer require dmlab/module-typesafe-core
bin/magento setup:upgrade
bin/magento dmlab:typesafe:ping
bin/magento dmlab:typesafe:usage
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Catalog Enrich module: [github.com/dmlab-work/module-catalog-enrich](https://github.com/dmlab-work/module-catalog-enrich)
- README developer example (evaluate with NoulQuestion and ChoiceQuestion)

## Limits and data handling

Product text goes to TypeSafe. Publisher is DMLab (dmlab.work).

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 987c72a50c92](https://github.com/dmlab-work/module-typesafe-core/tree/987c72a50c9271d45bc57326a771b18e248d2dd5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
