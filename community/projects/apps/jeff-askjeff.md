# Jeff by Deepu (a chatbot that cannot write: Jev picks each reply from a checked-in bank of 242 lines)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Chatbot whose every visible reply is a reviewed line committed to the repository. Local rules catch crisis and grief phrases first and answer without any model call; other messages go with up to four recent turns to Jev, which scores the candidate lines and safety and relevance signals in one request, and code applies thresholds to return one line. No generated text reaches the chat.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Deepusleepy/jeff) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://askjeff.vercel.app) |
| Pricing and access | Free hosted demo at askjeff.vercel.app (no sign-up described); self-hosting needs your own TypeSafe key and a Vercel account. Checked 2026-11-28. |
| Jev evidence | [`api/chat.js`](https://github.com/Deepusleepy/jeff/blob/58c9518464546580fad40475f0c3e0ec0e669865/api/chat.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Deepu](https://github.com/Deepusleepy). Independently curated. |
| Format | JavaScript web app + Vercel serverless function |
| Platform and availability | Web app on Vercel (static page + serverless API); hosted demo or self-host. |
| Jev's role | One Jev request per message scores the reply bank and classifies safety and relevance; local code picks the line and handles crisis phrases before Jev is called. |
| Requirements | Node.js 20.18.3+ and a TypeSafe API key to self-host. |
| License | [MIT](https://github.com/Deepusleepy/jeff/blob/58c9518464546580fad40475f0c3e0ec0e669865/LICENSE) |

## When to use

- People who want a chatbot whose output is fully pre-reviewed, or an example of ranking fixed replies with Jev.
- Mismatch: open-ended assistants; Jeff can only say lines from its bank.

## How it works

`api/chat.js` posts the conversation state and questions to `https://api.typesafe.ai/v1/systemone`; `lib/decide.js` applies the safety nets and thresholds and returns a line from `lib/bank.json`. Integration evidence: [`api/chat.js`](https://github.com/Deepusleepy/jeff/blob/58c9518464546580fad40475f0c3e0ec0e669865/api/chat.js).

## Get started

Clone, add your TypeSafe key, and run with the Vercel dev server.

```sh
git clone https://github.com/Deepusleepy/jeff && cd jeff
cp .env.example .env.local   # add TYPESAFE_API_KEY
npx vercel dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo: [askjeff.vercel.app](https://askjeff.vercel.app)
- Implementation reference: [github.com/Deepusleepy/jeff/blob/main/docs/FINAL_SPEC.md](https://github.com/Deepusleepy/jeff/blob/main/docs/FINAL_SPEC.md)

## Limits and data handling

Messages and recent turns go to TypeSafe. Jeff can still pick the wrong line or misread a message; crisis handling is phrase matching, not a support service.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 58c951846454](https://github.com/Deepusleepy/jeff/tree/58c9518464546580fad40475f0c3e0ec0e669865). Inspected the README, LICENSE, `api/chat.js` and the decision code at the pinned commit and confirmed the hosted demo loads (HTTP 200); not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
