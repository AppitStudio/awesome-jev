# jev-ground

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evidence-grounded factuality verification for LLM and agent outputs using a Jev provider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/johnyoonh/jev-ground) |
| Maintainer | [johnyoonh](https://github.com/johnyoonh). Independently curated. |
| Format | TypeScript library |
| Requirements | Node; TypeSafe API key for the Jev provider. |
| License | [MIT](https://github.com/johnyoonh/jev-ground/blob/e4c9494be6e7058218fe22c3d39c9e5eced8f6dc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/providers/jev.ts`](https://github.com/johnyoonh/jev-ground/blob/e4c9494be6e7058218fe22c3d39c9e5eced8f6dc/src/providers/jev.ts) at the pinned commit. |

## When to use

- Use when you need: Evidence-grounded factuality verification for LLM and agent outputs using a Jev …
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/providers/jev.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/providers/jev.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit e4c9494be6e7](https://github.com/johnyoonh/jev-ground/tree/e4c9494be6e7058218fe22c3d39c9e5eced8f6dc). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
