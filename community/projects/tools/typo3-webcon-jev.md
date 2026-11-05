# Jev decisions for TYPO3 (TYPO3 14 extension with a backend module to write and try typed Jev decisions, powermail conditions and form routing)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TYPO3 14.3 extension (`webconsulting/webcon-jev`) that adds editor-managed decision records (choice, score and noul questions with a confidence threshold and a fallback), a backend module with a playground that shows the probability distribution and a call log with latency and cost, and optional powermail integrations: rule operators that consult a decision and a router that addresses a submission to the right receiver.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dirnbauer/typo3-webcon-jev) |
| Maintainer | [dirnbauer](https://github.com/dirnbauer). Independently curated. |
| Format | TYPO3 extension (PHP 8.4+, Composer package, GPL-2.0-or-later) |
| Requirements | TYPO3 14.3 LTS, PHP 8.4+, `netresearch/nr-vault` to hold the TypeSafe API token; powermail and powermail_cond (v14 forks) only for the optional routing and conditions. |
| License | [GPL-2.0-or-later](https://github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/composer.json) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Classes/Client/HttpJevClient.php`](https://github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/Classes/Client/HttpJevClient.php) at the pinned commit. |

## When to use

- Route a contact-form submission to the right department, or show a field only when Jev says the message is a bug report.
- Let editors write and test typed questions in the TYPO3 backend and see what each call cost.
- Mismatch: it needs the TYPO3 14 stack, and the powermail features depend on forks of powermail packages.

## How it works

`HttpJevClient.php` talks to `https://api.typesafe.ai/v1/systemone`; `DecisionRunner::run()` never throws and applies each decision's threshold and fallback, while `JevClientInterface::ask()` raises `JevException` for callers that handle errors themselves. Integration evidence: [`Classes/Client/HttpJevClient.php`](https://github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/Classes/Client/HttpJevClient.php).

## Get started

From the upstream README (not run on the review host):

```sh
composer require webconsulting/webcon-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (primitives, requirements, backend module): [github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/README.md](https://github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/README.md)
- Package metadata and license: [github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/composer.json](https://github.com/dirnbauer/typo3-webcon-jev/blob/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9/composer.json)

## Limits and data handling

Form text and field values used in a decision are sent to TypeSafe on your key. An answer below a decision's confidence threshold is not used. The repository has no LICENSE file; the GPL-2.0-or-later terms are declared in `composer.json` and the README.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 0d220f0ac636](https://github.com/dirnbauer/typo3-webcon-jev/tree/0d220f0ac636c69ccc4ac9076ce5248a6aaf69f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
