# dsh-auto-review-jev (DeepSeek Harness permission mode that reviews every tool call with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DSH plugin that adds a Jev Review permission mode: each native and PTC tool call is judged by TypeSafe Jev before run, with low/medium/high risk bands, confidence thresholds and safe fallback when the host lacks required extensions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xlennart/dsh-auto-review-jev) |
| Maintainer | [xlennart](https://github.com/xlennart). Independently curated. |
| Format | DeepSeek Harness plugin (Apache-2.0; Node ≥24.9) |
| Requirements | DSH ^0.2.2-rc.1 with host extensions documented upstream, and a TypeSafe key (default `https://api.typesafe.ai/v1`, model `jev-latest`). |
| License | [Apache-2.0](https://github.com/xlennart/dsh-auto-review-jev/blob/919a59c70d4a028e7f807671f21088bd57f78211/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone-adapter.ts`](https://github.com/xlennart/dsh-auto-review-jev/blob/919a59c70d4a028e7f807671f21088bd57f78211/src/systemone-adapter.ts) at the pinned commit. |

## When to use

- Review every tool call in a DSH session without a name whitelist.
- Keep medium/high actions behind explicit authorization.
- Mismatch: needs specific DSH host patches; missing integration fails closed.

## How it works

The plugin posts System One reviews to the configured endpoint; transport tests pin `/v1/systemone` behavior. Integration evidence: [`src/systemone-adapter.ts`](https://github.com/xlennart/dsh-auto-review-jev/blob/919a59c70d4a028e7f807671f21088bd57f78211/src/systemone-adapter.ts).

## Get started

Install the release tarball into DSH and select Jev Review in the permission UI.

```sh
export TYPESAFE_API_KEY=...
# install per README release tarball into DSH
# /permission jev-review
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/xlennart/dsh-auto-review-jev/blob/919a59c70d4a028e7f807671f21088bd57f78211/README.md](https://github.com/xlennart/dsh-auto-review-jev/blob/919a59c70d4a028e7f807671f21088bd57f78211/README.md)

## Limits and data handling

Tool call context is sent to TypeSafe on your key. Host extension gaps report `JEV_HOST_EXTENSION_REQUIRED`.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 919a59c70d4a](https://github.com/xlennart/dsh-auto-review-jev/tree/919a59c70d4a028e7f807671f21088bd57f78211). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
