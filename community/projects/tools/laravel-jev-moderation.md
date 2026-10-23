# Jev Moderation for Laravel (confidence-aware content moderation)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Laravel package that classifies any Eloquent model with Jev when it is saved and uses per-category probability thresholds to pass it, hold it for human review or block it, keeping an append-only history of every decision and review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/phoenix1331/laravel-jev-moderation) |
| Maintainer | [phoenix1331](https://github.com/phoenix1331). Independently curated. |
| Format | PHP package (Composer: phoenix1331/laravel-jev-moderation) |
| Requirements | PHP 8.3+; Laravel 12 or 13; a TypeSafe API key. |
| License | [MIT](https://github.com/phoenix1331/laravel-jev-moderation/blob/37109a3cf04f87ed5847ed22011ac8a0ea0ef9c9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Drivers/JevDriver.php`](https://github.com/phoenix1331/laravel-jev-moderation/blob/37109a3cf04f87ed5847ed22011ac8a0ea0ef9c9/src/Drivers/JevDriver.php) at the pinned commit. |

## When to use

- Moderate posts, comments or messages from jobs, APIs and seeders, not only HTTP requests.
- Send borderline content to a human instead of quietly passing it.
- Mismatch: headless; the Filament review queue is announced but not released yet.

## How it works

`src/Drivers/JevDriver.php` posts content to TypeSafe's `systemone` endpoint (base URL `https://api.typesafe.ai/v1`, `jev-latest` unless you pin a version) and records the answering model version; a fake driver keeps test suites offline. Integration evidence: [`src/Drivers/JevDriver.php`](https://github.com/phoenix1331/laravel-jev-moderation/blob/37109a3cf04f87ed5847ed22011ac8a0ea0ef9c9/src/Drivers/JevDriver.php).

## Get started

From the upstream README (not run on the review host):

```sh
composer require phoenix1331/laravel-jev-moderation
php artisan jev-moderation:install
php artisan jev-moderation:ping
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Documentation: [phoenix1331.github.io/laravel-jev-moderation/](https://phoenix1331.github.io/laravel-jev-moderation/)

## Limits and data handling

Moderated content is sent to TypeSafe. Thresholds need tuning on your own content.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 37109a3cf04f](https://github.com/phoenix1331/laravel-jev-moderation/tree/37109a3cf04f87ed5847ed22011ac8a0ea0ef9c9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
