# aisdk/typesafe (native Jev decisions provider for the framework-agnostic PHP AI SDK)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Provider package for the PHP AI SDK (`aisdk/core`) that runs Jev decisions natively from PHP 8.3+: portable predicates map to TypeSafe `noul`, choices and scores to native criteria, and values, probabilities, confidence, usage and the raw response are kept. Works with any PSR-18 HTTP client.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/phpaisdk/typesafe) |
| Maintainer | [phpaisdk](https://github.com/phpaisdk). Independently curated. |
| Format | PHP package (Composer `aisdk/typesafe`) |
| Requirements | PHP 8.3+, `aisdk/core ^0.10.0` and a TypeSafe API key. |
| License | [MIT](https://github.com/phpaisdk/typesafe/blob/dee9f0c29f112f04a1b9ab3698a2bbc2522b8ace/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/TypeSafeProvider.php`](https://github.com/phpaisdk/typesafe/blob/dee9f0c29f112f04a1b9ab3698a2bbc2522b8ace/src/TypeSafeProvider.php) at the pinned commit. |

## When to use

- Add typed Jev decisions to a PHP app without a framework dependency.
- Mismatch: requires the PHP AI SDK core.

## How it works

`src/TypeSafeProvider.php` sends decision requests to `https://api.typesafe.ai/v1` with the chosen model (for example `jev-latest`) and maps answers back to the SDK's result types. Integration evidence: [`src/TypeSafeProvider.php`](https://github.com/phpaisdk/typesafe/blob/dee9f0c29f112f04a1b9ab3698a2bbc2522b8ace/src/TypeSafeProvider.php).

## Get started

From the upstream README (not run on the review host):

```sh
composer require aisdk/typesafe
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/phpaisdk/typesafe#readme](https://github.com/phpaisdk/typesafe#readme)

## Limits and data handling

Each decision request goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit dee9f0c29f11](https://github.com/phpaisdk/typesafe/tree/dee9f0c29f112f04a1b9ab3698a2bbc2522b8ace). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
