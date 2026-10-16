# Jev Rules for WordPress

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Experimental WordPress plugin that queues posts for Jev classification against versioned rule packs and keeps an administrator review history; posts are never changed, and other plugins can enqueue posts and react to decisions through hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/wordpress-jev-rules) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | WordPress plugin (PHP 8.1+, release ZIP `v0.1.2`, experimental alpha) |
| Requirements | WordPress with PHP 8.1+, a TypeSafe API key in server configuration. |
| License | [MIT](https://github.com/gbesse/wordpress-jev-rules/blob/8263e4e2860906ea0fc7b293a665ca3196889d3f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`includes/runtime.php`](https://github.com/gbesse/wordpress-jev-rules/blob/8263e4e2860906ea0fc7b293a665ca3196889d3f/includes/runtime.php) at the pinned commit. |

## When to use

- Triage support or community posts in WordPress with a declared rule pack and a reviewable decision log.
- Let trusted plugin code enqueue posts and consume decisions through `jev_rules_decided`.
- Mismatch: experimental alpha; it records decisions but takes no action on posts itself.

## How it works

WordPress cron evaluates each queued post's title and text against the selected pack with a 30-second, no-redirect HTTP call; the key comes from `JEV_RULES_API_KEY` or `TYPESAFE_API_KEY`. Decisions are stored as private `jev_decision` posts, and a changed post or rule marks a queued result stale. Integration evidence: [`includes/runtime.php`](https://github.com/gbesse/wordpress-jev-rules/blob/8263e4e2860906ea0fc7b293a665ca3196889d3f/includes/runtime.php).

## Get started

From the upstream README (not run on the review host):

```sh
# wp-content/plugins/wordpress-jev-rules (from the v0.1.2 release ZIP), then in wp-config.php:
# define('JEV_RULES_API_KEY', getenv('TYPESAFE_API_KEY'));
# define('JEV_RULES_ENVIRONMENT', 'staging');
npm ci && npm test   # WordPress Playground verification
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Starter pack: `packs/support-triage.json`.
- Verification scope: `docs/verification.md`.

## Limits and data handling

Post titles and text go to TypeSafe on your key; decisions stay in your WordPress database under your host's retention.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 8263e4e28609](https://github.com/gbesse/wordpress-jev-rules/tree/8263e4e2860906ea0fc7b293a665ca3196889d3f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
