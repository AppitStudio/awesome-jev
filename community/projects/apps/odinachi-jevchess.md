# JevChess

[All projects](../README.md) · [Web apps](README.md#web-apps)

Mobile-friendly 3D browser chess where TypeSafe Jev chooses among legal moves instead of writing move text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Odinachi/jevchess) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Odinachi/jevchess#readme) (source-built; no separate commercial homepage verified). |
| Pricing and access | Free source build; uses your own TypeSafe (or documented provider) key. Checked 2026-10-14. |
| Jev evidence | [`server/typesafe-jev.js`](https://github.com/Odinachi/jevchess/blob/a74569016e1c465f653a9d260218633441c720cd/server/typesafe-jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Odinachi](https://github.com/Odinachi). Independently curated. |
| Format | Web app |
| Platform and availability | Web browser |
| Jev's role | Jev picks the next legal move from a closed option list. |
| Requirements | Node (or static host as documented); TypeSafe API key for Jev play. |
| License | [MIT](https://github.com/Odinachi/jevchess/blob/a74569016e1c465f653a9d260218633441c720cd/LICENSE) |

## When to use

- Use when you need: Mobile-friendly 3D browser chess where TypeSafe Jev chooses among legal moves in…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `server/typesafe-jev.js`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: server/typesafe-jev.js.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit a74569016e1c](https://github.com/Odinachi/jevchess/tree/a74569016e1c465f653a9d260218633441c720cd). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
