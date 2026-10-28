# pi-jev-lazy-load (Pi extension that keeps tools and skills out of the first prompt, with optional Jev picking what to load)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that replaces most tool declarations and skill descriptions with a short index and loads them only when the prompt names them, the model asks, or (if you opt in) Jev decides the request needs them, shrinking the first model request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dantetekanem/pi-jev-lazy-load) |
| Maintainer | [dantetekanem](https://github.com/dantetekanem). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi 1.4.0-compatible extension APIs and Node.js 22.19+; a TypeSafe provider in Pi only for `jev` mode. |
| License | [MIT](https://github.com/dantetekanem/pi-jev-lazy-load/blob/f85e0ca0e7b7d72d9d2bee878aa4d6778e700e41/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.ts`](https://github.com/dantetekanem/pi-jev-lazy-load/blob/f85e0ca0e7b7d72d9d2bee878aa4d6778e700e41/index.ts) at the pinned commit. |

## When to use

- Cut startup tokens in Pi sessions with many tools and skills.
- Mismatch: default `local` mode works without Jev.

## How it works

`index.ts` calls Pi's `ctx.modelRegistry.classify()` with the configured classifier (default `typesafe/jev-latest`) when mode is `jev`. Integration evidence: [`index.ts`](https://github.com/dantetekanem/pi-jev-lazy-load/blob/f85e0ca0e7b7d72d9d2bee878aa4d6778e700e41/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/dantetekanem/pi-jev-lazy-load
# then /reload in Pi
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dantetekanem/pi-jev-lazy-load#readme](https://github.com/dantetekanem/pi-jev-lazy-load#readme)

## Limits and data handling

In `jev` mode the prompt and tool index go to TypeSafe through Pi. Local mode sends nothing extra.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit f85e0ca0e7b7](https://github.com/dantetekanem/pi-jev-lazy-load/tree/f85e0ca0e7b7d72d9d2bee878aa4d6778e700e41). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
