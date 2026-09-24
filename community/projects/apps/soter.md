# Soter

[All projects](../README.md) · [Discord bots](README.md#discord-bots)

Automated Discord moderation: TypeSafe Jev (OpenRouter Decisions) scores hate speech and spam per message; code deletes clear hits, flags borderline cases, and can timeout repeat violators.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frolleks/soter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [soter.frolleks.site](https://soter.frolleks.site) — also [hosted invite](https://discord.com/oauth2/authorize?client_id=1551459097826693130&permissions=1099645938896&integration_type=0&scope=bot) (early; not 24/7). |
| Pricing and access | MIT source self-host with Discord bot token + OpenRouter key; no app purchase fee, checked **2026-09-24**. Hosted invite is early-stage. OpenRouter/Jev usage billed separately. |
| Jev evidence | Inspected [`utils/jev.ts`](https://github.com/frolleks/soter/blob/4214e1a14531b72e202c79d60dbfb1fb85581ebd/utils/jev.ts): OpenRouter `alpha.decisions.create` with model `typesafe/jev-1.13` (Noul hate speech + Choice spam). Local thresholds delete / review / ignore. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer, Discord, OpenRouter, or TypeSafe. Listing is not an endorsement. Live moderation accuracy not measured here. |
| Maintainer | [frolleks](https://github.com/frolleks). Independently curated. |
| Format | Bun/TypeScript Discord bot. |
| Platform and availability | Self-host (`bun start`) or early hosted invite; Message Content intent + Manage Messages / Moderate Members required. |
| Jev's role | Per-message hate/spam judgments; Discord actions are code-owned. Optional `/report` also asks Jev over a message range. |
| Requirements | Bun; `DISCORD_TOKEN`; `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/frolleks/soter/blob/4214e1a14531b72e202c79d60dbfb1fb85581ebd/LICENSE). |

## When to use

Use it for **hands-off Discord hate/spam automation** with calibrated confidence gates. Prefer a review-only bot when you do not want automatic deletes/timeouts. Distinct from the Python [Jev Moderation Bot](jev-moderation-bot.md) listing.

## How it works

Each message becomes Jev state (content, account age, join date, recent messages). Hate Noul above 0.8 deletes; 0.5–0.8 flags mods; spam Choice drives logging/escalation. `/settings` configures exemptions, mod-log channel, and timeout thresholds.

## Get started

```sh
git clone https://github.com/frolleks/soter.git
cd soter
git checkout 4214e1a14531b72e202c79d60dbfb1fb85581ebd
bun install
cp .env.example .env   # DISCORD_TOKEN, OPENROUTER_API_KEY
bun start
```

Upstream documents invite scopes and `bun test` / `bun run eval` (live Jev cost per HateCheck case).

## Examples and demos

- README command list (`/report`, `/settings`, …).
- `bun run eval` against HateCheck samples (paid Jev calls; not run here).

## Limits and data handling

Message text and member metadata leave the host on OpenRouter Decisions. Hosted invite warns of early uptime and possible data deletion. Auto-delete/timeout needs careful Discord permissions review.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 4214e1a](https://github.com/frolleks/soter/tree/4214e1a14531b72e202c79d60dbfb1fb85581ebd). AI-assisted inspection of README, LICENSE, `utils/jev.ts`. No Discord install or live OpenRouter spend on the review host.

Related: [Jev Moderation Bot](jev-moderation-bot.md), [Jev Anti-Spam Bot](jev-antispam-bot.md).
