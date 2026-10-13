# JevMail (Outlook)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Outlook add-in for Microsoft 365 work and school accounts, powered by TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/koh-henry/jevmail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/koh-henry/jevmail#readme) (source-built; no separate commercial homepage verified). |
| Pricing and access | Free source build; uses your own TypeSafe (or documented provider) key. Checked 2026-10-14. |
| Jev evidence | [`apps/api/src/jev/client.ts`](https://github.com/koh-henry/jevmail/blob/2f14d18f28478f399dad555c19114dae567cda79/apps/api/src/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [koh-henry](https://github.com/koh-henry). Independently curated. |
| Format | Outlook add-in |
| Platform and availability | Microsoft 365 Outlook (work/school) |
| Jev's role | Jev powers mail decisions inside the Outlook add-in API surface. |
| Requirements | Microsoft 365; TypeSafe API key; add-in sideload/deploy as upstream documents. |
| License | [Apache-2.0](https://github.com/koh-henry/jevmail/blob/2f14d18f28478f399dad555c19114dae567cda79/LICENSE) |

## When to use

- Use when you need: Outlook add-in for Microsoft 365 work and school accounts, powered by TypeSafe J…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `apps/api/src/jev/client.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: apps/api/src/jev/client.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 2f14d18f2847](https://github.com/koh-henry/jevmail/tree/2f14d18f28478f399dad555c19114dae567cda79). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
