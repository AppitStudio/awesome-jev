# email-labeller (ViteHub Gmail labeller that uses Jev for messages no rule matches)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

ViteHub worker that labels new Gmail messages with deterministic rules first, then asks Jev (via the Vercel AI Gateway model `typesafe-ai/jev`) when no rule matches. Preview mode never writes to Gmail.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vite-hub/email-labeller) |
| Maintainer | [vite-hub](https://github.com/vite-hub). Independently curated. |
| Format | ViteHub / Nitro TypeScript worker (MIT) |
| Requirements | Node.js 24.15+, pnpm, a ViteHub Executor with Gmail, a Vercel AI Gateway key that can call `typesafe-ai/jev`, and a Cloudflare account. |
| License | [MIT](https://github.com/vite-hub/email-labeller/blob/0bb22f1db0d0fc295b02aa0dfc1eee2026bd5dde/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/agents/labeller.ts`](https://github.com/vite-hub/email-labeller/blob/0bb22f1db0d0fc295b02aa0dfc1eee2026bd5dde/server/agents/labeller.ts) at the pinned commit. |

## When to use

- Auto-label inbox mail after rules fall through.
- Preview labels without changing Gmail.
- Mismatch: depends on ViteHub Executor and Vercel AI Gateway access to typesafe-ai/jev.

## How it works

`server/agents/labeller.ts` builds a Vercel gateway client with model `typesafe-ai/jev` and applies the chosen label when rules do not match. Integration evidence: [`server/agents/labeller.ts`](https://github.com/vite-hub/email-labeller/blob/0bb22f1db0d0fc295b02aa0dfc1eee2026bd5dde/server/agents/labeller.ts).

## Get started

From the upstream README (not run on the review host):

```sh
corepack enable && pnpm install --frozen-lockfile
cp .env.example .env   # fill gateway and ViteHub tokens
pnpm dev               # then use the preview API; preview never writes Gmail
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vite-hub/email-labeller/blob/0bb22f1db0d0fc295b02aa0dfc1eee2026bd5dde/README.md](https://github.com/vite-hub/email-labeller/blob/0bb22f1db0d0fc295b02aa0dfc1eee2026bd5dde/README.md)

## Limits and data handling

Message headers, labels and up to 4,000 characters of plain-text body are sent through the gateway to Jev. Preview/backfill admin paths do not write an Invocation journal.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 0bb22f1db0d0](https://github.com/vite-hub/email-labeller/tree/0bb22f1db0d0fc295b02aa0dfc1eee2026bd5dde). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
