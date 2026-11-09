# jev-php (minimal PHP client for TypeSafe Jev with Laravel integration)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Minimal PHP client that sends state and typed questions to Jev and returns answers and actionable failures, with Laravel integration; transport today is Cloudflare Workers AI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ksilyanov/jev-php) |
| Maintainer | [ksilyanov](https://github.com/ksilyanov). Independently curated. |
| Format | PHP Composer package (MIT) |
| Requirements | PHP 8.2+, Composer (VCS repository entry; not on Packagist), Guzzle 7.8+, and Cloudflare Workers AI / AI Gateway credentials for `typesafe/jev`. |
| License | [MIT](https://github.com/ksilyanov/jev-php/blob/665a38c32d648df62841bd0c86b75a25d1a55aec/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Contracts/Jev.php`](https://github.com/ksilyanov/jev-php/blob/665a38c32d648df62841bd0c86b75a25d1a55aec/src/Contracts/Jev.php) at the pinned commit. |

## When to use

- Call Jev from PHP or Laravel apps.
- Test Jev-dependent code with a fake client.
- Mismatch: only the Cloudflare transport is implemented today.

## How it works

`Contracts/Jev.php` defines `evaluate($state, $questions)`; `Question.php` builds `noul`/`choice`/`score` questions and `Drivers/CloudflareDriver.php` sends them; `Testing/FakeJev.php` is a test double. Integration evidence: [`src/Contracts/Jev.php`](https://github.com/ksilyanov/jev-php/blob/665a38c32d648df62841bd0c86b75a25d1a55aec/src/Contracts/Jev.php).

## Get started

Add the GitHub VCS repository and `"ksilyanov/jev-php": "^0.1"` to `composer.json`, then configure the Cloudflare driver (Laravel 11/12 config is included).

```sh
composer config repositories.jev-php vcs https://github.com/ksilyanov/jev-php
composer require ksilyanov/jev-php:^0.1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ksilyanov/jev-php/blob/665a38c32d648df62841bd0c86b75a25d1a55aec/README.md](https://github.com/ksilyanov/jev-php/blob/665a38c32d648df62841bd0c86b75a25d1a55aec/README.md)

## Limits and data handling

State and questions go to Cloudflare Workers AI (Jev) on your account.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 665a38c32d64](https://github.com/ksilyanov/jev-php/tree/665a38c32d648df62841bd0c86b75a25d1a55aec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
