# Life Is Multiple Choice (인생은 객관식) by Taekkyun Kim (Korean web app that asks Jev your questions and reveals the answer as a ladder, coin toss or punch machine)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Next.js web app (and interactive CLI) in Korean for building a state and Choice, Noul, Score or Box questions and running them on Jev through OpenRouter. Results can show straight away or as a playful reveal: a ladder game for Choice, a coin toss for Noul, a punch-machine gauge for Score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kimtaekkyun/jevgame) |
| Maintainer | [kimtaekkyun](https://github.com/kimtaekkyun). Independently curated. |
| Format | Next.js web app plus a Node.js CLI |
| Requirements | Node.js 20.9+ and an OpenRouter key (`OPENROUTER_MODEL` defaults to `~typesafe/jev-latest`). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/app/api/decisions/route.ts`](https://github.com/kimtaekkyun/jevgame/blob/c6c1341b056545049ae0e34c8500d3904ecba276/src/app/api/decisions/route.ts) at the pinned commit. |

## When to use

- A fun way to learn Jev's four question types, for Korean speakers.
- Mismatch: production use; this is a playful demo.

## How it works

`src/app/api/decisions/route.ts` calls `alpha.decisions.create` from `@openrouter/sdk` on the server with the key kept in server env; `scripts/jev.mjs` is the CLI, with a `--dry-run` that prints the request only. Integration evidence: [`src/app/api/decisions/route.ts`](https://github.com/kimtaekkyun/jevgame/blob/c6c1341b056545049ae0e34c8500d3904ecba276/src/app/api/decisions/route.ts).

## Get started

Install, add your OpenRouter key to `.env.local`, and start the dev server or the CLI.

```sh
git clone https://github.com/kimtaekkyun/jevgame.git && cd jevgame
npm install && cp .env.example .env.local   # add OPENROUTER_API_KEY
npm run dev   # or: npm run jev -- --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Korean): [github.com/kimtaekkyun/jevgame/blob/c6c1341b056545049ae0e34c8500d3904ecba276/README.md](https://github.com/kimtaekkyun/jevgame/blob/c6c1341b056545049ae0e34c8500d3904ecba276/README.md)

## Limits and data handling

Inputs and images go to OpenRouter (not TypeSafe directly) and are billed to your key; the app stores no results. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit c6c1341b0565](https://github.com/kimtaekkyun/jevgame/tree/c6c1341b056545049ae0e34c8500d3904ecba276). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
