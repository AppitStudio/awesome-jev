# Preguntale a Jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

Simple no-login chat: ask a yes/no question and TypeSafe Jev returns Choice probabilities (sí / no / no_aplica) with confidence—Spanish UI, Vercel AI Gateway by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dariozfold6-wez2/JEV-CHAT) |
| Tags | `Source unverified` · `Free` · `BYOK` |
| Product homepage | [Hosted app](https://jev-chat-ten.vercel.app) — also the deploy target described in README. |
| Pricing and access | Hosted demo free at the Vercel URL (Gateway quotas apply). Optional `TYPESAFE_API_KEY` / Upstash rate limits. Checked **2026-09-24**. |
| Jev evidence | Inspected [`lib/jev.ts`](https://github.com/dariozfold6-wez2/JEV-CHAT/blob/2f2889fc0d2dfc5846770a1d707e7a4e12a6a319/lib/jev.ts): `experimental_evaluate` with model `typesafe-ai/jev`. |
| Disclosure | AI-assisted catalog review; no affiliation. **No LICENSE at tip.** Listing is not an endorsement. Hosted UI opened only as a public URL check—not a scored eval. |
| Maintainer | [dariozfold6-wez2](https://github.com/dariozfold6-wez2). Independently curated. |
| Format | Next.js app on Vercel (`/api/preguntar`). |
| Platform and availability | Web; deploy your own with `vercel` or `npm run dev`. |
| Jev's role | Sole judge for the Choice question; UI renders probabilities. |
| Requirements | Node.js; Vercel AI Gateway (default) or TypeSafe key; optional Upstash Redis. |
| License | **Unspecified** at tip (no LICENSE file). |

## When to use

Use it for a **quick public yes/no probability toy** in Spanish. Prefer richer chat assistants for multi-turn drafting.

## How it works

The API route sends the user text as Choice state to Jev (Gateway or direct TypeSafe) and returns option probabilities. Optional Upstash limits to 20 questions/IP/hour.

## Get started

```sh
git clone https://github.com/dariozfold6-wez2/JEV-CHAT.git
cd JEV-CHAT
git checkout 2f2889fc0d2dfc5846770a1d707e7a4e12a6a319
npm install
# vercel link && vercel env pull   # Gateway token, or set TYPESAFE_API_KEY
npm run dev
```

## Examples and demos

- Hosted demo: [jev-chat-ten.vercel.app](https://jev-chat-ten.vercel.app)
- Tunables documented in README (`lib/jev.ts`, rate limit, max length).

## Limits and data handling

Questions leave the browser to Vercel/TypeSafe. No account, but IP rate limiting is optional. Not a factual oracle—probabilities are model judgments.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 2f2889f](https://github.com/dariozfold6-wez2/JEV-CHAT/tree/2f2889fc0d2dfc5846770a1d707e7a4e12a6a319). AI-assisted README + `lib/jev.ts` inspection. No measured live eval budget.

Related: [Jev Asks Until Sure](jev-asks-until-sure.md), [Jev Chat Assistant](jev-chat-jarvis.md).
