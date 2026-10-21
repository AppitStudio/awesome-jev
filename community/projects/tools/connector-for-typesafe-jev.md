# Connector for TypeSafe Jev (WordPress)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

WordPress plugin that gives themes and plugins a typed way to ask Jev about content and branch on a probability, a named choice or a score with confidence, with the key managed by WordPress core's Connectors API; a companion plugin backs comment moderation with it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juanlentino/connector-for-typesafe-jev) |
| Maintainer | [juanlentino](https://github.com/juanlentino). Independently curated. |
| Format | WordPress plugin (PHP) |
| Requirements | WordPress 7.0+, PHP 7.4+, a TypeSafe API key. |
| License | [GPL-2.0](https://github.com/juanlentino/connector-for-typesafe-jev/blob/6ed6effabc5d7d795925689b0c2b939de3eaadb8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`includes/class-client.php`](https://github.com/juanlentino/connector-for-typesafe-jev/blob/6ed6effabc5d7d795925689b0c2b939de3eaadb8/includes/class-client.php) at the pinned commit. |

## When to use

- Spam-check or categorize comments and posts in a few lines of PHP.
- Gate actions on confidence instead of parsing model prose.
- Mismatch: 0.x, pending WordPress directory review; the public API may still change.

## How it works

`JevConnector\ask()` builds a System One request from your fields and questions and sends it through `includes/class-client.php`; answers come back as typed objects with `noul()`, choice and score helpers and `is_confident()`. Integration evidence: [`includes/class-client.php`](https://github.com/juanlentino/connector-for-typesafe-jev/blob/6ed6effabc5d7d795925689b0c2b939de3eaadb8/includes/class-client.php).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/juanlentino/connector-for-typesafe-jev.git wp-content/plugins/connector-for-typesafe-jev
# activate it, then add your TypeSafe key under the WordPress Connectors settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/juanlentino/connector-for-typesafe-jev/releases](https://github.com/juanlentino/connector-for-typesafe-jev/releases)
- Comment moderation add-on: [github.com/juanlentino/comment-analysis-for-typesafe-jev](https://github.com/juanlentino/comment-analysis-for-typesafe-jev)

## Limits and data handling

Content you ask about is sent to TypeSafe. Independent project, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 6ed6effabc5d](https://github.com/juanlentino/connector-for-typesafe-jev/tree/6ed6effabc5d7d795925689b0c2b939de3eaadb8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
