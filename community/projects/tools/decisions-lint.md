# decisions-lint (lint PHP code against plain-language rules with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

PHP linter for rules static analysers cannot check, such as whether a method belongs to its class or whether a name says what the code does: each rule is a typed question a decision model answers, and each violation comes with the change that resolves it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/k-kinzal/decisions-lint) |
| Maintainer | [k-kinzal](https://github.com/k-kinzal). Independently curated. |
| Format | PHP CLI (Composer) |
| Requirements | PHP 8.0+ with cURL; a TypeSafe key, an OpenAI Decisions key, or a local OpenAI-compatible model. |
| License | [MIT](https://github.com/k-kinzal/decisions-lint/blob/099e7c64b7bb4bf6ef56a26ab4a17b8ba6791c87/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Provider/Jev/JevClient.php`](https://github.com/k-kinzal/decisions-lint/blob/099e7c64b7bb4bf6ef56a26ab4a17b8ba6791c87/src/Provider/Jev/JevClient.php) at the pinned commit. |

## When to use

- Enforce architecture and naming conventions in PHP code review.
- Swap between Jev, OpenAI Decisions and a local model.
- Mismatch: read-only mirror; Packagist publication was not confirmed at review time.

## How it works

`JevClient.php` posts to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default, set in `ProviderSettings.php`); rules live in `decisions.yaml`. Integration evidence: [`src/Provider/Jev/JevClient.php`](https://github.com/k-kinzal/decisions-lint/blob/099e7c64b7bb4bf6ef56a26ab4a17b8ba6791c87/src/Provider/Jev/JevClient.php).

## Get started

From the upstream README (not run on the review host). The repo is a read-only mirror of k-kinzal/php-ai-toolkit; if the Composer package is not available, install from source:

```sh
composer require --dev k-kinzal/decisions-lint
vendor/bin/decisions-lint init
export TYPESAFE_API_KEY=...
vendor/bin/decisions-lint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [k-kinzal.github.io/php-ai-toolkit/](https://k-kinzal.github.io/php-ai-toolkit/)
- Monorepo: [github.com/k-kinzal/php-ai-toolkit](https://github.com/k-kinzal/php-ai-toolkit)

## Limits and data handling

Code under review is sent to the configured provider.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 099e7c64b7bb](https://github.com/k-kinzal/decisions-lint/tree/099e7c64b7bb4bf6ef56a26ab4a17b8ba6791c87). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
