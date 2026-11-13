# Clorian for Laravel (confidence-aware typed decisions where Jev makes the obvious calls and unsure ones go to a person)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Laravel package that turns text on any Eloquent model or input (support tickets, listings, reviews, refunds, leads) into typed answers: Jev answers each declared question with a probability, confident results are applied automatically, unsure ones are queued for a human, and the recorded outcomes show when the thresholds can be trusted more.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/phoenix1331/laravel-clorian) |
| Maintainer | [phoenix1331](https://github.com/phoenix1331). Independently curated. |
| Format | Laravel package on Packagist (PHP, MIT) |
| Requirements | PHP with Laravel, Composer, and a TypeSafe key. |
| License | [MIT](https://github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Drivers/JevDriver.php`](https://github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/src/Drivers/JevDriver.php) at the pinned commit. |

## When to use

- Auto-triage tickets, listings or refunds in a Laravel app while sending uncertain cases to staff.
- Mismatch: decisions that must never be automated; keep those on the human path.

## How it works

`src/Drivers/JevDriver.php` posts `{model, state, questions}` to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default (configurable); `php artisan clorian:ping` runs one sample and reports the resolved model version and latency. A fake driver is included for tests. Integration evidence: [`src/Drivers/JevDriver.php`](https://github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/src/Drivers/JevDriver.php).

## Get started

Require the package, run the installer (publishes config and migrations), then ping Jev.

```sh
composer require phoenix1331/laravel-clorian
php artisan clorian:install
php artisan clorian:ping
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/README.md](https://github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/README.md)
- Changelog: [github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/CHANGELOG.md](https://github.com/phoenix1331/laravel-clorian/blob/81313b2de2195f51a96d161c01333d93264d65bf/CHANGELOG.md)

## Limits and data handling

The text fields you declare are sent to TypeSafe on your key; decisions and outcomes are stored in your own database.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 81313b2de219](https://github.com/phoenix1331/laravel-clorian/tree/81313b2de2195f51a96d161c01333d93264d65bf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
