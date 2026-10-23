# Jev DevTools (React inspector for Jev requests)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Drop-in React inspector for TypeSafe Jev, inspired by TanStack Query Devtools: a drawer that records your app's Jev requests and shows animated flows from context to questions to answers, choice probability bars, score and noul values, request history, retries and raw payloads.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/diegoag64/jev-devtools) |
| Maintainer | [diegoag64](https://github.com/diegoag64). Independently curated. |
| Format | React component and server adapter (TypeScript) |
| Requirements | React 18 or 19 (Next.js App Router supported); Node.js; a TypeSafe API key in your server environment. |
| License | [MIT](https://github.com/diegoag64/jev-devtools/blob/9c47af062fe193bbe1d03ba939054e7e7b6f08fd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/diegoarias941/status/2113459990048452806)). |
| Jev evidence | [`packages/jev-devtools/server/recorder.ts`](https://github.com/diegoag64/jev-devtools/blob/9c47af062fe193bbe1d03ba939054e7e7b6f08fd/packages/jev-devtools/server/recorder.ts) at the pinned commit. |

## When to use

- See what each Jev call received and returned while you build.
- Tune questions and criteria by comparing probabilities across calls.
- Mismatch: a development-time prototype, not a production monitor.

## How it works

`server/recorder.ts` wraps the official `@typesafe-ai/sdk` `TypeSafeClient` on your server, recording each request, answer, retry and TypeSafe request id so the drawer can display them. Integration evidence: [`packages/jev-devtools/server/recorder.ts`](https://github.com/diegoag64/jev-devtools/blob/9c47af062fe193bbe1d03ba939054e7e7b6f08fd/packages/jev-devtools/server/recorder.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- 28-second demo and playground in the README: [github.com/diegoag64/jev-devtools#readme](https://github.com/diegoag64/jev-devtools#readme)
- Next.js guide: [github.com/diegoag64/jev-devtools/blob/main/docs/nextjs.md](https://github.com/diegoag64/jev-devtools/blob/main/docs/nextjs.md)

## Limits and data handling

Recorded requests (including state sent to Jev) are kept for display in your dev environment; Jev calls go to TypeSafe with your key. Not published to npm yet; the README installs from a local package build.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 9c47af062fe1](https://github.com/diegoag64/jev-devtools/tree/9c47af062fe193bbe1d03ba939054e7e7b6f08fd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
