# mods (iuliandita)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mods you can install one at a time, including optional TypeSafe Jev client injection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iuliandita/mods) |
| Maintainer | [iuliandita](https://github.com/iuliandita). Independently curated. |
| Format | Claude Code mods / hooks |
| Requirements | Claude Code; TypeSafe API key when enabling Jev-backed mods. |
| License | [MIT](https://github.com/iuliandita/mods/blob/5b249681824d76bb54381e39e71d497644a4081f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`shared/jev-client.inject.ts`](https://github.com/iuliandita/mods/blob/5b249681824d76bb54381e39e71d497644a4081f/shared/jev-client.inject.ts) at the pinned commit. |

## When to use

- Use when you need: Claude Code mods you can install one at a time, including optional TypeSafe Jev …
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `shared/jev-client.inject.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: shared/jev-client.inject.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 5b249681824d](https://github.com/iuliandita/mods/tree/5b249681824d76bb54381e39e71d497644a4081f). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
