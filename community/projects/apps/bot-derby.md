# Bot Derby (Jev and OpenAI Decisions compete in a paper-trading experiment)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Public paper-trading experiment: Ferdi (TypeSafe Jev) and Bodi (OpenAI Decisions) each get $50,000 of simulated cash, the same stock evidence and the same legal action menu for five large US stocks, and a public scoreboard tracks how their portfolios diverge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Day-in-the-Country-LLC/bot-derby) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://botderby.dayinthecountry.co) |
| Pricing and access | Open source (MIT); the public scoreboard is free to view. Running your own needs your TypeSafe, OpenAI and Alpaca paper keys. Checked 2026-10-24. |
| Jev evidence | [`src/derby/decisions.ts`](https://github.com/Day-in-the-Country-LLC/bot-derby/blob/6bd1473844c51e35ea6e1d5b5df0ffb38baf78c2/src/derby/decisions.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Day-in-the-Country-LLC](https://github.com/Day-in-the-Country-LLC). Independently curated. |
| Format | Web app and trading engine (TypeScript, Node.js) |
| Platform and availability | Public web scoreboard; self-hosted engine from source. |
| Jev's role | Core: Jev is one of the two competing decision engines and picks an action from the legal menu each cycle. |
| Requirements | Node 22.13+ and pnpm; TypeSafe, OpenAI and Alpaca paper-trading keys to run your own. |
| License | [MIT](https://github.com/Day-in-the-Country-LLC/bot-derby/blob/6bd1473844c51e35ea6e1d5b5df0ffb38baf78c2/LICENSE) |

## When to use

- Watch two decision APIs make the same choices on the same evidence.
- Study a controlled design for comparing decision models over time.
- Mismatch: paper trading only, not trading advice; the README warns that a reachable site does not prove the season is active.

## How it works

`src/derby/decisions.ts` posts each bot's evidence and action menu to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) for Ferdi or to OpenAI's `/v1/decisions` for Bodi; code enforces the trading limits. Adapted from Mike Russell's MIT-licensed beebots. Integration evidence: [`src/derby/decisions.ts`](https://github.com/Day-in-the-Country-LLC/bot-derby/blob/6bd1473844c51e35ea6e1d5b5df0ffb38baf78c2/src/derby/decisions.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install --frozen-lockfile
pnpm derby:check   # tiny real AI requests; no trades
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Scoreboard: [botderby.dayinthecountry.co](https://botderby.dayinthecountry.co)
- README: [github.com/Day-in-the-Country-LLC/bot-derby#readme](https://github.com/Day-in-the-Country-LLC/bot-derby#readme)

## Limits and data handling

Simulated cash only. Market evidence is sent to TypeSafe and OpenAI. Results are the operator's own and were not verified here.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 6bd1473844c5](https://github.com/Day-in-the-Country-LLC/bot-derby/tree/6bd1473844c51e35ea6e1d5b5df0ffb38baf78c2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
