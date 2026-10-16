# typesafe-ai PHP client

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial PHP 8.4 client for the Jev System One API: typed request objects for Noul, Choice and Score (plus experimental Box with images), typed responses with confidence and usage, and a mock HTTP client for tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/basi/typesafe-ai-php-client) |
| Maintainer | [basi](https://github.com/basi). Independently curated. |
| Format | PHP library (Composer, VCS repository) |
| Requirements | PHP 8.4+, Composer; a TypeSafe API key. |
| License | [MIT](https://github.com/basi/typesafe-ai-php-client/blob/a4c6de505232186d9caf2d924b9e761dc514176b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Client.php`](https://github.com/basi/typesafe-ai-php-client/blob/a4c6de505232186d9caf2d924b9e761dc514176b/src/Client.php) at the pinned commit. |

## When to use

- Route or score support messages from a Laravel, Symfony or plain PHP app with Jev.
- Unit-test your decision code with the bundled mock client and request-body assertions.
- Mismatch: unofficial and not on Packagist yet; add the GitHub repo as a Composer VCS repository.

## How it works

`Client::withGuzzle($key)` sends a `SystemOneRequest` (state plus named question objects) to `https://api.typesafe.ai/v1/systemone` and returns a `SystemOneResponse` or `TypedSystemOneResponse`; the README stresses reading `confidence` before acting on Choice and Score answers. Integration evidence: [`src/Client.php`](https://github.com/basi/typesafe-ai-php-client/blob/a4c6de505232186d9caf2d924b9e761dc514176b/src/Client.php).

## Get started

From the upstream README (not run on the review host):

```sh
composer config repositories.typesafe-ai-php-client vcs https://github.com/basi/typesafe-ai-php-client
composer require basi/typesafe-ai-php-client:^0.2
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start and Box/image docs in the README; more in `docs/`.

## Limits and data handling

State goes to TypeSafe on your key; the library stores nothing.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit a4c6de505232](https://github.com/basi/typesafe-ai-php-client/tree/a4c6de505232186d9caf2d924b9e761dc514176b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
