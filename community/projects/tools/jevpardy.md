# JEVPARDY! (party trivia where friends name answers on their phones and Jev judges each one live)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Multiplayer category-listing game in an arcade style: the host picks topics, OpenAI writes a secret deck of questions ("Name a 90s boy band"), players join with a 4-letter code, and Jev judges every answer live, forgiving typos, catching repeats like "München" after "Munich" and rating how obscure each answer is.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mongj/jevpardy) |
| Maintainer | [mongj](https://github.com/mongj). Independently curated. |
| Format | Cloudflare Worker game with Durable Objects (TypeScript; no license file) |
| Requirements | A Cloudflare account (Workers Free plan works), Node.js with Yarn, a TypeSafe key, and an OpenAI key to write questions (mock judge and writer run without keys). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/worker/judge/jev.ts`](https://github.com/mongj/jevpardy/blob/6ce9f808ba6be4f69580ced84612b123aa15392b/src/worker/judge/jev.ts) at the pinned commit. |

## When to use

- Run a phone-based trivia game night with fair, typo-tolerant judging.
- Mismatch: if you need a hosted public instance; you deploy your own.

## How it works

`src/worker/judge/jev.ts` sends one request per submission to `https://api.typesafe.ai/v1/systemone` (`JEV_MODEL`, default `jev-latest`) with `noul` questions for validity and duplicates (thresholds 0.7 and 0.75), and Jev also vets the question deck. The README reports about 900 tokens per judgment on `jev-1.14.0`. Integration evidence: [`src/worker/judge/jev.ts`](https://github.com/mongj/jevpardy/blob/6ce9f808ba6be4f69580ced84612b123aa15392b/src/worker/judge/jev.ts).

## Get started

Deploy your own Worker with Wrangler after setting the two secrets.

```sh
yarn install
yarn wrangler secret put TYPESAFE_API_KEY
yarn wrangler secret put OPENAI_API_KEY
yarn deploy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mongj/jevpardy/blob/6ce9f808ba6be4f69580ced84612b123aa15392b/README.md](https://github.com/mongj/jevpardy/blob/6ce9f808ba6be4f69580ced84612b123aa15392b/README.md)

## Limits and data handling

Topics, questions and player answers go to TypeSafe and OpenAI on the deployer's keys; nothing persists after a game ends.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 6ce9f808ba6b](https://github.com/mongj/jevpardy/tree/6ce9f808ba6be4f69580ced84612b123aa15392b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
