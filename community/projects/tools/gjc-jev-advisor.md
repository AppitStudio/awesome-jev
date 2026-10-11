# jev-advisor (gjc-plugin)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugins for gajae-code (`gjc`). The `jev-advisor` plugin asks TypeSafe Jev for task-scoped `fast` / `balanced` / `strong` advice before subagent delegation, records bounded correlation with outcomes, and offers an offline descriptive report; advice is shadow-only by default and is not model routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jjongguet/gjc-plugin) |
| Maintainer | [jjongguet](https://github.com/jjongguet). Independently curated. |
| Format | gjc plugins (`jev-advisor`, `verification-receipts`, `ui-regression`) |
| Requirements | gajae-code; TypeSafe API key for jev-advisor. |
| License | [MIT](https://github.com/jjongguet/gjc-plugin/blob/b5554dcb448e804465e02c9fd18c0d429cd7a449/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Study whether delegated subagent tasks could run on a cheaper tier.
- Mismatch: Advice only; it does not route models or prove quality.

## How it works

Before a `task` call, each child assignment is sent to Jev (up to four sequential requests in an eight-second budget); results are journaled locally. (Summarized from the upstream [README](https://github.com/jjongguet/gjc-plugin/blob/b5554dcb448e804465e02c9fd18c0d429cd7a449/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `gjc plugin install ./jev-advisor --user` from a checkout, then `gjc plugin doctor`.

## Limits and data handling

Assignment text and shared context are sent to the TypeSafe API; journals stay under `~/.gjc-plugin`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit b5554dcb448e](https://github.com/jjongguet/gjc-plugin/tree/b5554dcb448e804465e02c9fd18c0d429cd7a449). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
