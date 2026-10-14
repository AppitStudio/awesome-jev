# @contexera DSH jev plugin

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin monorepo whose `jev` package adds a TypeSafe Jev service for typed decisions alongside channel-gateway and context-continuity plugins.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Contexera/dsh-plugins) |
| Maintainer | [Contexera](https://github.com/Contexera). Independently curated. |
| Format | DSH plugins (TypeScript, pnpm monorepo) |
| Requirements | DeepSeek Harness; TypeSafe API key. |
| License | [MIT (package `packages/jev`; no root LICENSE)](https://github.com/Contexera/dsh-plugins/blob/86d4e3d2d6233985c91ed24bf8b85d338fd1eddb/packages/jev/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/jev/src/service.ts`](https://github.com/Contexera/dsh-plugins/blob/86d4e3d2d6233985c91ed24bf8b85d338fd1eddb/packages/jev/src/service.ts) at the pinned commit. |

## When to use

- Add Jev typed decisions to a DeepSeek Harness setup via the published `@contexera/dsh-jev` package.
- Mismatch: the MIT license is on the jev package; the monorepo root has no LICENSE.

## How it works

The jev package wraps request/response contracts and transport for System One calls; DSH hooks call it. Integration evidence: [`packages/jev/src/service.ts`](https://github.com/Contexera/dsh-plugins/blob/86d4e3d2d6233985c91ed24bf8b85d338fd1eddb/packages/jev/src/service.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see packages/jev/README.md for @contexera/dsh-jev setup in DeepSeek Harness
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tests: `packages/jev/tests/`.
- DSH patch: `packages/jev/cordis.patch.yml`.

## Limits and data handling

Inputs go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 86d4e3d2d623](https://github.com/Contexera/dsh-plugins/tree/86d4e3d2d6233985c91ed24bf8b85d338fd1eddb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
