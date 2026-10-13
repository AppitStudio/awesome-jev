# Jevmail (hwong103)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hostable read-only Gmail triage where TypeSafe Jev sorts mail into trays you can correct (Cloudflare Worker + D1 + React PWA).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hwong103/jevmail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/hwong103/jevmail#readme) (source-built; no separate commercial homepage verified). |
| Pricing and access | Free source build; uses your own TypeSafe (or documented provider) key. Checked 2026-10-14. |
| Jev evidence | [`src/server/classification/jev.ts`](https://github.com/hwong103/jevmail/blob/c4ff43a2a64c2bb5d5c3f3a4bcb1e8d3d1cf6b51/src/server/classification/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [hwong103](https://github.com/hwong103). Independently curated. |
| Format | Web app |
| Platform and availability | Self-hosted web (Cloudflare Worker + React PWA) |
| Jev's role | Jev classifies messages into triage trays. |
| Requirements | Cloudflare; TypeSafe API key; Gmail OAuth as documented upstream. |
| License | [MIT](https://github.com/hwong103/jevmail/blob/c4ff43a2a64c2bb5d5c3f3a4bcb1e8d3d1cf6b51/LICENSE) |

## When to use

- Use when you need: Self-hostable read-only Gmail triage where TypeSafe Jev sorts mail into trays yo…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/server/classification/jev.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/server/classification/jev.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit c4ff43a2a64c](https://github.com/hwong103/jevmail/tree/c4ff43a2a64c2bb5d5c3f3a4bcb1e8d3d1cf6b51). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
