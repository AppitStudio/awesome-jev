# Family Feud Live (multiplayer party game whose optional AI host uses Jev to judge answers)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Jackbox-style multiplayer Family Feud fan game: the board runs on a TV, players join from phones by QR code, and an optional AI host writes surveys on any topic, speaks in character and judges fuzzy answers, with a local matcher first and Jev as the decision model for the guesses it cannot decide.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gocougs2020/family-feud) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://family-feud-self.vercel.app) |
| Pricing and access | Open source (MIT). The live demo is free to play; a self-deployed copy runs free with AI off. The AI host uses your own Vercel AI Gateway key and prepaid credits (BYOK for that mode); whether the public demo has the AI host on was not verified. Checked 2026-10-26. |
| Jev evidence | [`src/lib/ai.ts`](https://github.com/gocougs2020/family-feud/blob/f518a617f62a2090fd911636e8a33d36a6b179d6/src/lib/ai.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [gocougs2020](https://github.com/gocougs2020). Independently curated. |
| Format | Next.js web app (TypeScript) |
| Platform and availability | Web (TV or laptop screen plus phones); self-deploy on Vercel. |
| Jev's role | Optional answer judge: with the AI host on, guesses the local matcher cannot settle go to Jev, which picks the matching board answer or none. |
| Requirements | A browser to play; to deploy, a Vercel account and optionally a Vercel AI Gateway key for the AI host. |
| License | [MIT](https://github.com/gocougs2020/family-feud/blob/f518a617f62a2090fd911636e8a33d36a6b179d6/LICENSE) |

## When to use

- Run a party game night on one screen with phones as buzzers.
- Add strict or lenient AI judging without a chat model doing the matching.
- Mismatch: fan-made and unaffiliated with Family Feud or Fremantle; AI features need your own gateway key.

## How it works

`src/lib/ai.ts` routes answer judging to `typesafe-ai/jev` through Vercel AI Gateway (`AI_JUDGE_MODEL`), while survey writing, host lines and voice use other gateway models; without `AI_GATEWAY_API_KEY` no model is called. Integration evidence: [`src/lib/ai.ts`](https://github.com/gocougs2020/family-feud/blob/f518a617f62a2090fd911636e8a33d36a6b179d6/src/lib/ai.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gocougs2020/family-feud && cd family-feud
npm install && npm run dev
# optional AI host: set AI_GATEWAY_API_KEY in .env.local
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [family-feud-self.vercel.app](https://family-feud-self.vercel.app)
- README: [github.com/gocougs2020/family-feud#readme](https://github.com/gocougs2020/family-feud#readme)

## Limits and data handling

With the AI host on, guesses and board answers go to Vercel AI Gateway and on to TypeSafe for judging; other AI text and voice go to other gateway models. Key budgets cap spend.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit f518a617f62a](https://github.com/gocougs2020/family-feud/tree/f518a617f62a2090fd911636e8a33d36a6b179d6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
