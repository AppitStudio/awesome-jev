# OnBrief (check text against your own nested rules with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Next.js web app where you paste text, pick a rule set you wrote, and Jev judges each rule and sub-rule with a tick or cross; users bring their own TypeSafe key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samaksh-bajaj/on-brief) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/samaksh-bajaj/on-brief#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source; no license file on the reviewed commit. Users supply their own TypeSafe key; Supabase and hosting costs are yours. Checked 2026-11-10. |
| Jev evidence | [`src/server/typesafe.ts`](https://github.com/samaksh-bajaj/on-brief/blob/4539794b526879e1773082ce7d98f7664cfa9517/src/server/typesafe.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [samaksh-bajaj](https://github.com/samaksh-bajaj). Independently curated. |
| Format | Next.js web app with Supabase (TypeScript, source only) |
| Platform and availability | Web (self-hosted Next.js + Supabase; source build) |
| Jev's role | Jev judges whether the text meets each user-written rule and sub-rule. |
| Requirements | Node.js, a Supabase project (auth, database, Vault), and a TypeSafe API key per user; optional `TYPESAFE_DEMO_API_KEY` for a signed-out demo. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Check copy or briefs against a house style or compliance checklist.
- See a nested-rule pattern built on per-rule Jev questions.
- Mismatch: no license file and no public hosted URL verified; self-host it.

## How it works

`src/server/typesafe.ts` builds a `TypeSafeClient` from the user's stored key and phrases each rule as a Jev question (the author notes the wording was the best of nine tried); `src/server/check.ts` rolls sub-rule results up so a rule passes only when all parts do. Integration evidence: [`src/server/typesafe.ts`](https://github.com/samaksh-bajaj/on-brief/blob/4539794b526879e1773082ce7d98f7664cfa9517/src/server/typesafe.ts).

## Get started

Apply `supabase/migrations/`, fill `.env.local` from `.env.example`, then run the dev server.

```sh
git clone https://github.com/samaksh-bajaj/on-brief.git && cd on-brief
npm install && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/samaksh-bajaj/on-brief/blob/4539794b526879e1773082ce7d98f7664cfa9517/README.md](https://github.com/samaksh-bajaj/on-brief/blob/4539794b526879e1773082ce7d98f7664cfa9517/README.md)

## Limits and data handling

Pasted text goes to TypeSafe on the user's key; keys are stored in Supabase Vault.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 4539794b5268](https://github.com/samaksh-bajaj/on-brief/tree/4539794b526879e1773082ce7d98f7664cfa9517). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
