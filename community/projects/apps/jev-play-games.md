# Jev Play Games by Ege Bulut (watch Jev play 2048, Snake, a platformer and more live, with the odds of every move on screen)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Live site where Jev plays browser games (2048, Snake, a block-drop puzzle, Hill Climb, Super Jev Bros, a Freedoom raycaster) and shows the probability of each legal move as bars next to the game. Every move is one Jev choice question; the server owns the seeded game state, the viewer who presses Play live drives the session for everyone watching, and nothing is called when no one is watching. Every decision is recorded for exact replays.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ege-BULUT/jev-play-games) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://jev-play-games.vercel.app) |
| Pricing and access | Free to watch; the maintainer pays for Jev calls with a daily budget (live play pauses when it is spent; replays keep playing). Checked 2026-11-18. |
| Jev evidence | [`src/lib/jev.ts`](https://github.com/Ege-BULUT/jev-play-games/blob/dea49e24be8a1902a1388571b2bccb6b50ff6a5a/src/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Ege-BULUT](https://github.com/Ege-BULUT). Independently curated. |
| Format | Next.js app on Vercel with Supabase (no license file) |
| Platform and availability | Web (hosted at jev-play-games.vercel.app) |
| Jev's role | Picks one move per turn from the legal moves with a choice question; the page shows the returned probabilities. |
| Requirements | Nothing to watch; to run your own copy: Node.js, pnpm, a Vercel project with AI Gateway access to `typesafe-ai/jev`, and Supabase. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See how a decision model's move probabilities look in real time across simple games.
- Mismatch: reusable code under an open license; no license file is present.

## How it works

`src/lib/jev.ts` asks one `choice` question per turn through the AI SDK's `experimental_evaluate` on Vercel AI Gateway with model `typesafe-ai/jev`, and reads the per-move confidence from the provider metadata. Integration evidence: [`src/lib/jev.ts`](https://github.com/Ege-BULUT/jev-play-games/blob/dea49e24be8a1902a1388571b2bccb6b50ff6a5a/src/lib/jev.ts).

## Get started

Open the site and press Play live, or watch the last recording.

```sh
# watch: https://jev-play-games.vercel.app
# develop (needs your own Vercel + Supabase project):
pnpm install && vercel link && vercel env pull .env.local
node --env-file=.env.local scripts/migrate.mjs && pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [jev-play-games.vercel.app](https://jev-play-games.vercel.app)
- README: [github.com/Ege-BULUT/jev-play-games/blob/dea49e24be8a1902a1388571b2bccb6b50ff6a5a/README.md](https://github.com/Ege-BULUT/jev-play-games/blob/dea49e24be8a1902a1388571b2bccb6b50ff6a5a/README.md)

## Limits and data handling

No license file on the reviewed commit, so reuse terms are not granted. Live play is rate-limited (about 28 Jev calls a minute across all games), so real-time games run in slow motion. Viewing stores no personal data beyond the shared session.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit dea49e24be8a](https://github.com/Ege-BULUT/jev-play-games/tree/dea49e24be8a1902a1388571b2bccb6b50ff6a5a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
