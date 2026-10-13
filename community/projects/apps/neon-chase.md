# Neon Chase

[All projects](../README.md) · [Web apps](README.md#web-apps)

Neon-style endless runner where TypeSafe Jev can drive realtime gameplay decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/susyimes/neon-chase) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/susyimes/neon-chase#readme) (source-built; no separate commercial homepage verified). |
| Pricing and access | Free source build; uses your own TypeSafe (or documented provider) key. Checked 2026-10-14. |
| Jev evidence | [`server/src/jev.ts`](https://github.com/susyimes/neon-chase/blob/b9e28827c77c8d41650417f40afdab5639619a0e/server/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [susyimes](https://github.com/susyimes). Independently curated. |
| Format | Web game |
| Platform and availability | Web (client/server) |
| Jev's role | Jev supplies realtime gameplay decisions to the runner. |
| Requirements | Node; TypeSafe API key for live Jev mode (offline fallback exists). |
| License | [MIT](https://github.com/susyimes/neon-chase/blob/b9e28827c77c8d41650417f40afdab5639619a0e/LICENSE) |

## When to use

- Use when you need: Neon-style endless runner where TypeSafe Jev can drive realtime gameplay decisio…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `server/src/jev.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: server/src/jev.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit b9e28827c77c](https://github.com/susyimes/neon-chase/tree/b9e28827c77c8d41650417f40afdab5639619a0e). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
