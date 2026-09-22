# Jev Asks Until Sure

[All projects](../README.md) · [Web apps](README.md#web-apps)

Twenty-questions style web game: the app keeps asking until TypeSafe Jev’s calibrated confidence crosses a threshold—or it gives up and says so. Hosted demo and MIT source.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mintannn/jev-asks-until-sure) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Hosted demo](https://jev.mintan.org/) — play in the browser; operator may lend infrastructure/keys subject to their limits, or run locally with your own key. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Hosted play is free at the demo URL (HTTP 200). Local/live play needs `TYPESAFE_API_KEY`; TypeSafe usage can incur charges. |
| Jev evidence | Inspected [`lib/jev.ts`](https://github.com/mintannn/jev-asks-until-sure/blob/a710210670c87824cc00b81833d5914864ae0e0c/lib/jev.ts): server-side client posts batched noul/choice/score questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with 429/529 backoff; API routes under `app/api/` keep the key off the client. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source inspected; `tsc`/eslint reported upstream issues on the review host; live TypeSafe games not run. |
| Maintainer | [mintannn](https://github.com/mintannn). Independently curated. |
| Format | Next.js 16 app (`package.json` name `jev` **0.1.0**, private). |
| Platform and availability | Web; hosted [jev.mintan.org](https://jev.mintan.org/) (HTTP 200 checked) or local `npm run dev` / `npm run build`. |
| Jev's role | Supplies calibrated probabilities for diagnostic questions and the final guess/give-up gate. Application code owns UI, question schedule, language toggle, and stop conditions. |
| Requirements | Node.js for local build; `TYPESAFE_API_KEY` in `.env.local` for live diagnose routes. |
| License | [MIT](https://github.com/mintannn/jev-asks-until-sure/blob/a710210670c87824cc00b81833d5914864ae0e0c/LICENSE). |

## When to use

Use it when you want a **playable demo of confidence-threshold questioning** with TypeSafe Jev. Prefer [Jev Chess](jevchess.md) or [Jev 2048](jev-2048.md) for board-game Choice loops. Do not treat game success rate as a general Jev quality claim.

## How it works

Server routes call `ask()` in `lib/jev.ts` to batch typed questions over game state. The UI (`app/bareru.tsx`) presents questions and ends when confidence clears a threshold or the give-up path fires. The API key stays server-side.

## Get started

```sh
git clone https://github.com/mintannn/jev-asks-until-sure.git
cd jev-asks-until-sure
git checkout a710210670c87824cc00b81833d5914864ae0e0c
npm ci
# Optional offline: npm run lint  # reported react-hooks issues upstream at review time
echo "TYPESAFE_API_KEY=..." > .env.local
npm run dev
# Or open https://jev.mintan.org/
```

Live diagnose calls send game state to TypeSafe and may incur charges. This listing did not play a live game.

## Examples and demos

- Hosted demo: [jev.mintan.org](https://jev.mintan.org/) (HTTP 200 on the review host).
- Offline: source + `lib/jev.ts` inspected; `npm run lint` reported upstream react-hooks errors (disclosed; not treated as a listing blocker for the public demo).

## Limits and data handling

Game answers and diagnostic state leave the host on live Jev calls. Hosted demo key/rate limits are operator-controlled and were not fully characterized beyond HTTP 200. UI copy is bilingual (EN/JA).

## Review and maintenance

Reviewed on **2026-09-22** at [commit a710210](https://github.com/mintannn/jev-asks-until-sure/tree/a710210670c87824cc00b81833d5914864ae0e0c): MIT. AI-assisted source review of README, LICENSE, `lib/jev.ts`, `app/api/diagnose/route.ts`. Hosted demo HTTP 200. No live TypeSafe play on the review host.

Related: [Jev Chess](jevchess.md), [Jev 2048](jev-2048.md), [Jev Column Race](jev-column-race.md).
