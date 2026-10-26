# Tribar Connector for TypeSafe Jev (WordPress plugin for typed answers about content)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

WordPress connector for TypeSafe's System One API that gives themes and plugins a typed way to ask about content and get a probability, a named choice or a score to branch on, instead of parsing prose; version 0.x, pending review for the WordPress plugin directory.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juanlentino/tribar-connector-for-typesafe-jev) |
| Maintainer | [juanlentino](https://github.com/juanlentino). Independently curated. |
| Format | WordPress plugin (PHP) |
| Requirements | WordPress 7.0+, PHP 7.4+; a TypeSafe API key. |
| License | [GPL-2.0-or-later](https://github.com/juanlentino/tribar-connector-for-typesafe-jev/blob/7d2a9cd5edf2b7aa9d2d6ce4b72ae79b44f42e97/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`includes/class-client.php`](https://github.com/juanlentino/tribar-connector-for-typesafe-jev/blob/7d2a9cd5edf2b7aa9d2d6ce4b72ae79b44f42e97/includes/class-client.php) at the pinned commit. |

## When to use

- Branch WordPress templates or plugins on typed judgements about posts or comments.
- Avoid prompt handling in theme code.
- Mismatch: 0.x; the public API may change before 1.0.

## How it works

`includes/class-client.php` posts requests to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest` and returns typed results to calling code. Integration evidence: [`includes/class-client.php`](https://github.com/juanlentino/tribar-connector-for-typesafe-jev/blob/7d2a9cd5edf2b7aa9d2d6ce4b72ae79b44f42e97/includes/class-client.php).

## Get started

From the upstream README (not run on the review host):

```sh
# download the release zip and upload it in WordPress → Plugins → Add New
# then add your TypeSafe API key in the plugin settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/juanlentino/tribar-connector-for-typesafe-jev/releases](https://github.com/juanlentino/tribar-connector-for-typesafe-jev/releases)
- README: [github.com/juanlentino/tribar-connector-for-typesafe-jev#readme](https://github.com/juanlentino/tribar-connector-for-typesafe-jev#readme)

## Limits and data handling

The content you ask about goes to TypeSafe. GPL-2.0-or-later licensed.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 7d2a9cd5edf2](https://github.com/juanlentino/tribar-connector-for-typesafe-jev/tree/7d2a9cd5edf2b7aa9d2d6ce4b72ae79b44f42e97). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
