# Tiny World (creature island and town simulation where residents choose actions with Jev or OpenAI Decisions)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Interactive simulation: give a world a direction ("Pip, go to the pond", "a thunderstorm arrives") and watch its residents decide. A creature island with ten personalities and twelve actions, and a larger town with road-following residents and an occasions calendar; each decision comes from Jev or OpenAI Decisions, with an API inspector showing tokens and cost. Automatic decisions are capped at 30 calls per session.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hank-go1/tiny-world) |
| Maintainer | [hank-go1](https://github.com/hank-go1). Independently curated. |
| Format | Next.js app on Cloudflare (TypeScript) |
| Requirements | Node.js 24 and an OpenRouter key for Jev (or an OpenAI key); worlds render without keys. |
| License | [MIT](https://github.com/hank-go1/tiny-world/blob/726417ae05058e64d0f0714754c0f81f8db6bd65/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/creature-decisions.ts`](https://github.com/hank-go1/tiny-world/blob/726417ae05058e64d0f0714754c0f81f8db6bd65/lib/creature-decisions.ts) at the pinned commit. |

## When to use

- See typed decisions drive game characters, with costs visible.
- Mismatch: a demo; Jev is used on the island only.

## How it works

`lib/creature-decisions.ts` sends each creature's state and action questions to `typesafe/jev-1.13` through OpenRouter, and `lib/decision-costs.ts` estimates the cost. Integration evidence: [`lib/creature-decisions.ts`](https://github.com/hank-go1/tiny-world/blob/726417ae05058e64d0f0714754c0f81f8db6bd65/lib/creature-decisions.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hank-go1/tiny-world && cd tiny-world
npm ci
cp .dev.vars.example .dev.vars   # add OPENROUTER_API_KEY
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/hank-go1/tiny-world#readme](https://github.com/hank-go1/tiny-world#readme)

## Limits and data handling

World state goes to OpenRouter or OpenAI when decisions run.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 726417ae0505](https://github.com/hank-go1/tiny-world/tree/726417ae05058e64d0f0714754c0f81f8db6bd65). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
