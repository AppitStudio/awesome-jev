# Jev x AI SDK Form Router

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Next.js form router that uses Jev to route submissions by context, with an LLM fallback for uncertain cases.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ashiruus/jev-and-ai-sdk) |
| Maintainer | [ashiruus](https://github.com/ashiruus). Independently curated. |
| Format | Next.js + AI SDK sample |
| Requirements | Node 22+; pnpm; AI Gateway / Jev access. |
| License | [MIT](https://github.com/ashiruus/jev-and-ai-sdk/blob/22f0be33d62535f75b05cb67ead4c33935e90a21/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`app/actions.ts`](https://github.com/ashiruus/jev-and-ai-sdk/blob/22f0be33d62535f75b05cb67ead4c33935e90a21/app/actions.ts) at the pinned commit. |

## When to use

- Use when you need: Next.js form router that uses Jev to route submissions by context, with an LLM fallback fo…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `app/actions.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: app/actions.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 22f0be33d625](https://github.com/ashiruus/jev-and-ai-sdk/tree/22f0be33d62535f75b05cb67ead4c33935e90a21). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
