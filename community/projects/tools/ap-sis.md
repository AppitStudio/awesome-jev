# apsis (Solana payment + rent-recovery app where TypeSafe Jev decides which empty token accounts are safe to close)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MLH Solana Hackathon app: pay someone and recover SOL locked in empty token accounts in the same transaction; Jev judges which empty accounts are junk, with a labelled rules fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0atxl/ap-sis) |
| Maintainer | [0atxl](https://github.com/0atxl). Independently curated. |
| Format | Next.js web app (no license file) |
| Requirements | Node, a Solana wallet, and a `TYPESAFE_API_KEY` (without it a rules-based fallback runs). |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/jev.ts`](https://github.com/0atxl/ap-sis/blob/1520a369ca3b1eded77bfa26d28c348ca35ee3b2/src/lib/jev.ts) at the pinned commit. |

## When to use

- Recover rent from dead token accounts safely.
- See a server-side Jev pattern in Next.js.
- Mismatch: no license file; ask the author before reuse.

## How it works

`src/lib/jev.ts` and `src/app/api/ai/jev/route.ts` call Jev (`jev-1.14.0` via `@typesafe-ai/sdk`) server-side with two questions per account and never show made-up confidence in fallback mode. Integration evidence: [`src/lib/jev.ts`](https://github.com/0atxl/ap-sis/blob/1520a369ca3b1eded77bfa26d28c348ca35ee3b2/src/lib/jev.ts).

## Get started

Run `npm install`, copy `.env.example` to `.env.local` with your key, and start the dev server.

```sh
git clone https://github.com/0atxl/ap-sis.git && cd ap-sis
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/0atxl/ap-sis/blob/1520a369ca3b1eded77bfa26d28c348ca35ee3b2/README.md](https://github.com/0atxl/ap-sis/blob/1520a369ca3b1eded77bfa26d28c348ca35ee3b2/README.md)

## Limits and data handling

Token-account metadata is sent to TypeSafe from the server.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 1520a369ca3b](https://github.com/0atxl/ap-sis/tree/1520a369ca3b1eded77bfa26d28c348ca35ee3b2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
