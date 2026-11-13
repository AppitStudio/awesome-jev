# Jev World (Jev plays and referees games inside a LingBot World 2 generated video world)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experiment where LingBot World 2 generates an interactive video world from an image and prompt, Kimi K3 designs and replans the level, one Jev instance watches the frames and steers the player, and a second Jev scores progress from frames and a rubric; there is no game engine underneath.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/willemhelmet/jev-world) |
| Maintainer | [willemhelmet](https://github.com/willemhelmet). Independently curated. |
| Format | Local Next.js app (no license file) |
| Requirements | Node with pnpm; `REACTOR_API_KEY` for LingBot World 2, `TYPESAFE_API_KEY` (or `OPENROUTER_API_KEY` as fallback) for Jev, and an OpenAI-compatible key for the designer. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/server/providers.ts`](https://github.com/willemhelmet/jev-world/blob/ba9477ae599787f05c0b651b1f1f684b7fcc9883/lib/server/providers.ts) at the pinned commit. |

## When to use

- Experiment with a decision model as a fast controller and referee for a generated world.
- Mismatch: public deployment; the author says the API routes spend your keys and need auth before going public.

## How it works

`lib/server/providers.ts` sends frames and the current plan state to `https://api.typesafe.ai/v1/systemone` with `jev-latest` when `TYPESAFE_API_KEY` is set, or to OpenRouter's Decisions endpoint with `typesafe/jev-1.14`; the player asks which plan state it is in and whether to steer, search, act or interact, with a `ready` gate before interactions. The README logs runs, including failures where the world model never rendered an object. Integration evidence: [`lib/server/providers.ts`](https://github.com/willemhelmet/jev-world/blob/ba9477ae599787f05c0b651b1f1f684b7fcc9883/lib/server/providers.ts).

## Get started

Install with pnpm, copy the example env file and add your keys, then run locally.

```sh
pnpm install
cp .env.example .env.local
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with run log: [github.com/willemhelmet/jev-world/blob/ba9477ae599787f05c0b651b1f1f684b7fcc9883/README.md](https://github.com/willemhelmet/jev-world/blob/ba9477ae599787f05c0b651b1f1f684b7fcc9883/README.md)

## Limits and data handling

Frames go to TypeSafe or OpenRouter, Reactor and your designer provider on your keys.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit ba9477ae5997](https://github.com/willemhelmet/jev-world/tree/ba9477ae599787f05c0b651b1f1f684b7fcc9883). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
