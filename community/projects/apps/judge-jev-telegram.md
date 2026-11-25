# judge-jev by Mikhail Levchenko (Telegram Guest Mode bot that answers yes/no and pick-one questions about a message with Jev probabilities)

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Cloudflare Worker behind the Telegram bot @judge_jev_bot: mention it in any chat (Guest Mode) with a question, or reply to a message with `/is_this_true`, `/classify a | b` or `/judge`, and it returns Jev's probabilities for each option. The Worker owns parsing, thresholds and formatting; Jev only returns typed Noul and Choice answers. Examples are in Russian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mishkun/judge-jev) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Mishkun/judge-jev#readme) (source-built; no separate product site verified). |
| Pricing and access | The public bot has no payment step (the README describes none); self-hosting needs your own OpenRouter key and a Cloudflare account. Checked 2026-11-26. |
| Jev evidence | [`src/jev.ts`](https://github.com/Mishkun/judge-jev/blob/ff7f4552414566436dbfb3acab6e677db03f86f1/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Mikhail Levchenko](https://github.com/Mishkun). Independently curated. |
| Format | TypeScript Cloudflare Worker |
| Platform and availability | Telegram (public bot @judge_jev_bot, or self-host the Cloudflare Worker). |
| Jev's role | Jev answers one Noul or Choice question per command about the replied-to text or caption; the Worker sorts the options by probability and bolds the top one. |
| Requirements | To self-host: Node.js, Wrangler, a Telegram bot token with Guest Mode enabled, and an OpenRouter key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Get a quick probability on a yes/no or pick-one question in a Telegram chat.
- Mismatch: fact-checking; `/is_this_true` returns a model probability, not evidence, and the README says so.

## How it works

`src/jev.ts` calls OpenRouter's Decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with the Jev model; `docs/jev-api.md` records the OpenRouter and TypeSafe request and response contract. No database or chat history is used. Integration evidence: [`src/jev.ts`](https://github.com/Mishkun/judge-jev/blob/ff7f4552414566436dbfb3acab6e677db03f86f1/src/jev.ts).

## Get started

Use the public bot, or deploy your own Worker with Wrangler secrets.

```sh
git clone https://github.com/Mishkun/judge-jev
cd judge-jev
npm install
npx wrangler secret put JEV_OPENROUTER_TOKEN
npx wrangler secret put TELEGRAM_BOT_TOKEN
npx wrangler secret put TELEGRAM_WEBHOOK_SECRET
npm run deploy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Public bot: [t.me/judge_jev_bot](https://t.me/judge_jev_bot)
- API notes: [github.com/Mishkun/judge-jev/blob/ff7f4552414566436dbfb3acab6e677db03f86f1/docs/jev-api.md](https://github.com/Mishkun/judge-jev/blob/ff7f4552414566436dbfb3acab6e677db03f86f1/docs/jev-api.md)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. The replied text and the question are sent to OpenRouter (a third-party host) and its provider; the project does not claim zero retention. Treat the probabilities as a model's opinion, not proof.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit ff7f45524145](https://github.com/Mishkun/judge-jev/tree/ff7f4552414566436dbfb3acab6e677db03f86f1). Inspected the README, `docs/jev-api.md` and the Worker's Jev client at the pinned commit; the bot was not used on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
