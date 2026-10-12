# pi-rm-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that auto-approves safe recursive `rm` commands via a decision model (default `typesafe/jev-latest`) and defers or denies everything else.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sdougbrown/pi-rm-guard) |
| Maintainer | [sdougbrown](https://github.com/sdougbrown). Independently curated. |
| Format | Pi extension |
| Requirements | Pi; classifier configured (Jev default; Clef or local router models supported). |
| License | [MIT](https://github.com/sdougbrown/pi-rm-guard/blob/b264355c2f5b990aa164759e25f36ea0ca8ddad8/LICENSE) |
| Jev evidence | [`src/decisions-provider.ts`](https://github.com/sdougbrown/pi-rm-guard/blob/b264355c2f5b990aa164759e25f36ea0ca8ddad8/src/decisions-provider.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Reduce approval prompts for routine cleanup while keeping risky deletes gated.
- Mismatch: scoped to `rm -r` style commands only.

## How it works

Matching commands are sent with context to the configured classifier; confident safe verdicts approve, others defer or deny. (Summarized from the upstream [README](https://github.com/sdougbrown/pi-rm-guard/blob/b264355c2f5b990aa164759e25f36ea0ca8ddad8/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the extension in Pi and set the `classifier` option per the README.

## Limits and data handling

Command text and paths go to the classifier provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit b264355c2f5b](https://github.com/sdougbrown/pi-rm-guard/tree/b264355c2f5b990aa164759e25f36ea0ca8ddad8). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
