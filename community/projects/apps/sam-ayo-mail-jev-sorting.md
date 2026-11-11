# mail (keyboard-first unified inbox with Jev important-vs-promotions sorting)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Keyboard-first email client with one inbox for all your accounts and a remote MCP server for agents; its optional AI sorting asks Jev whether each conversation is a promotion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sam-ayo/mail) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://mail.demo.samayo.me) |
| Pricing and access | Free source build; no license file on the reviewed commit. Hosted-service pricing not published. You pay hosting and TypeSafe usage. Checked 2026-11-11. |
| Jev evidence | [`app/server/triage.server.ts`](https://github.com/sam-ayo/mail/blob/17e2bf79c7a7b19e834a92cf1fdce893d5e196e6/app/server/triage.server.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/sam_ayo__/status/2120300892549456227)). |
| Maintainer | [sam-ayo](https://github.com/sam-ayo). Independently curated. |
| Format | Web app (TypeScript, React Router on Workers, source only) |
| Platform and availability | Web (self-hosted; hosted demo available) |
| Jev's role | Jev decides whether each conversation is a promotion or important mail for inbox sorting. |
| Requirements | Node.js and pnpm, the database and encryption settings in `.env.example`, and `TYPESAFE_API_KEY` for AI sorting. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Split important mail from promotions with a typed classifier.
- Give an AI agent MCP access to several mailboxes.
- Mismatch: no license file, so the code is source-available, not open source; you host it yourself.

## How it works

`app/server/triage.server.ts` uses `@typesafe-ai/sdk` with `jev-1.14.0` choice and noul questions on a trimmed conversation text, and marks a thread as a promotion only above a probability threshold; sorting is off when no key is configured. Integration evidence: [`app/server/triage.server.ts`](https://github.com/sam-ayo/mail/blob/17e2bf79c7a7b19e834a92cf1fdce893d5e196e6/app/server/triage.server.ts).

## Get started

Clone, copy `.env.example` to `.env`, add your keys and run the dev server; a hosted demo is linked from the repository.

```sh
git clone https://github.com/sam-ayo/mail.git && cd mail
pnpm install && cp .env.example .env && pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo: [mail.demo.samayo.me](https://mail.demo.samayo.me)
- README: [github.com/sam-ayo/mail/blob/17e2bf79c7a7b19e834a92cf1fdce893d5e196e6/README.md](https://github.com/sam-ayo/mail/blob/17e2bf79c7a7b19e834a92cf1fdce893d5e196e6/README.md)

## Limits and data handling

Conversation text goes to TypeSafe when AI sorting is on; account credentials and thread summaries are stored encrypted in your database.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 17e2bf79c7a7](https://github.com/sam-ayo/mail/tree/17e2bf79c7a7b19e834a92cf1fdce893d5e196e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
