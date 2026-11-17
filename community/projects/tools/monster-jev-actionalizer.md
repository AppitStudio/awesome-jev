# MonsterJevActionalizer by coredweller (D&D encounter helper where Jev picks each monster's turn from the legal options)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local web app for Dungeons & Dragons game masters: upload a monster stat block, track an encounter, and get a recommended turn for the monster. The app builds the legal options from the stat block and the encounter state, Jev picks among them, and you apply or override the result. Tests replay recorded Jev responses, so the checks run without live calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coredweller/MonsterJevActionalizer) |
| Maintainer | [coredweller](https://github.com/coredweller). Independently curated. |
| Format | Next.js web app (TypeScript, MIT) |
| Requirements | Node 24+ and `TYPESAFE_API_KEY` in `.env.local` (`JEV_MODEL` and `TYPESAFE_BASE_URL` optional). |
| License | [MIT](https://github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev/client.ts`](https://github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/lib/jev/client.ts) at the pinned commit. |

## When to use

- Let Jev suggest a sensible turn for each monster while you run combat.
- Mismatch: a full virtual tabletop or rules engine; you still apply and adjudicate the turn.

## How it works

`lib/jev/client.ts` is the server-only client for `POST /v1/systemone` at `https://api.typesafe.ai` with `jev-latest` by default; it is the only place the key is read. Integration evidence: [`lib/jev/client.ts`](https://github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/lib/jev/client.ts).

## Get started

Install, add your key and start the dev server.

```sh
git clone https://github.com/coredweller/MonsterJevActionalizer && cd MonsterJevActionalizer
npm install
cp .env.example .env.local   # set TYPESAFE_API_KEY=...
npm run dev                  # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design plan: [github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/docs/PLAN.md](https://github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/docs/PLAN.md)
- README: [github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/README.md](https://github.com/coredweller/MonsterJevActionalizer/blob/e03da5fb9a81fce800a486e64090961651118ebe/README.md)

## Limits and data handling

Stat blocks and encounter state go to TypeSafe on your key. Recommendations are suggestions; the game master applies or overrides them.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit e03da5fb9a81](https://github.com/coredweller/MonsterJevActionalizer/tree/e03da5fb9a81fce800a486e64090961651118ebe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
