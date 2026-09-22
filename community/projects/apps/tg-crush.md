# tg-crush

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local real-time Telegram conversation coach: you write the draft; TypeSafe Jev scores quality, emotion fit, and timing before you send—plus live partner-message judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BrickerP/tg-crush) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/BrickerP/tg-crush#readme) — local UI on `127.0.0.1:3180`; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Requires `TYPESAFE_API_KEY` plus Telegram `TG_API_ID` / `TG_API_HASH` (my.telegram.org). TypeSafe usage can incur charges. |
| Jev evidence | Inspected [`src/jev.ts`](https://github.com/BrickerP/tg-crush/blob/ec1651cbd2094279a168692370f682a3730642a6/src/jev.ts): `@typesafe-ai/sdk` `systemOne` for emotion/intent/affinity/draft checks (`jev-1.13.0`). Offline `tsc --noEmit` clean; live smoke needs a key (not run). |
| Disclosure | Free source access does not include inference. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Not affiliated with Telegram or TypeSafe. Distinct from paste-based [Crush Monitor](crush-monitor.md). |
| Maintainer | [BrickerP](https://github.com/BrickerP). |
| Format | TypeScript local app (`tg-crush` 0.1.0): MTProto user client + localhost UI. |
| Platform and availability | Source build on Node.js **≥ 22.12**. Binds to `127.0.0.1:3180`. Real Telegram login; optional bot partner/autoplay for demos. |
| Jev's role | Judges inbound messages, session affinity, outbound ratings, and pre-send draft quality/timing; application code owns Telegram I/O and UI. Jev does not generate reply text. |
| Requirements | Node.js 22.12+, `TYPESAFE_API_KEY`, Telegram API id/hash; phone login once via `npm run login`. |
| License | [MIT](https://github.com/BrickerP/tg-crush/blob/ec1651cbd2094279a168692370f682a3730642a6/LICENSE). |

## When to use

Use it for **live Telegram** draft checks and partner-message labeling when you want structured Jev scores before sending. Prefer [Crush Monitor](crush-monitor.md) for offline WeChat-style paste analysis without a Telegram session. Treat scores as optional reference, not relationship advice.

## How it works

The local server logs in as your Telegram user (GramJS). Typing/inbound events trigger batched TypeSafe questions via `@typesafe-ai/sdk`. Draft checkup scores quality and timing separately. Chat text is sent to TypeSafe on live judgments; sessions stay on the machine running the client.

## Get started

```sh
git clone https://github.com/BrickerP/tg-crush.git
cd tg-crush
git checkout ec1651cbd2094279a168692370f682a3730642a6
npm ci --ignore-scripts
npm run check
# Live: cp .env.example .env; set TYPESAFE_API_KEY + TG_API_*; npm run login; npm start
# Open http://127.0.0.1:3180 — live analysis sends message text to TypeSafe
```

Optional demos without a second human: `npm run newbot` / `npm run partner` / `npm run autoplay` (still need Telegram + TypeSafe keys).

## Examples and demos

- Offline on the review host: `npm run check` (`tsc --noEmit`) clean.
- `npm run smoke` exercises fixtures against live Jev (requires key; **not run** here).

## Limits and data handling

One Telegram session file must not be shared across processes. Message text leaves the host on live TypeSafe calls. Upstream notes Chinese-language UX. No live TypeSafe/Telegram spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit ec1651c](https://github.com/BrickerP/tg-crush/tree/ec1651cbd2094279a168692370f682a3730642a6): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `src/jev.ts`, `src/config.ts`. **`npm run check` OK**; smoke/live not run.

Related: [Crush Monitor](crush-monitor.md), [Jev Anti-Spam Bot](jev-antispam-bot.md), [HookMeter](hookmeter.md).
