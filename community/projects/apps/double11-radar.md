# Double11 Radar by Yang (self-hosted Chinese deal-alert matcher that asks Jev whether each new deal fits your shopping needs)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Write shopping needs such as "tissues, not wet wipes" and the worker keeps collecting posts from the Xianbaoku deal feeds, asks Jev whether each new deal matches each need, and pushes confirmed matches to Bark and Feishu. Uncertain results wait in the web UI; failures are kept apart from "no match". Chinese README and UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhexin233-ui/double11-radar) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/zhexin233-ui/double11-radar#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build you self-host (Docker Compose on a NAS or server); your own TypeSafe key(s) are billed per Jev call, and the README notes each retry is a new paid call. No license file, so reuse terms are not granted. Checked 2026-11-24. |
| Jev evidence | [`src/lib/jev/client.ts`](https://github.com/zhexin233-ui/double11-radar/blob/ffe2e618e22840b57d0afac313489c8e3ece33e4/src/lib/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [zhexin233-ui](https://github.com/zhexin233-ui). Independently curated. |
| Format | Next.js 16 / TypeScript web app and worker |
| Platform and availability | Self-hosted Next.js web app and worker with SQLite, run with Docker Compose. |
| Jev's role | One Jev request per deal carries two questions per enabled need (is it relevant, is it an offer for it); a match is confirmed only when both answer `matched` with valid probabilities. |
| Requirements | Docker Compose (or Node.js and pnpm); a TypeSafe API key; optional Bark or Feishu webhooks. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Get pushed alerts only for deals that match your own written needs.
- Mismatch: regions outside the Chinese deal sites it collects from.

## How it works

`src/lib/jev/client.ts` posts `{ state, model, questions }` to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with the key kept server-side; `src/lib/worker/evaluator.ts` runs the judgement queue with key rotation and back-off. Integration evidence: [`src/lib/jev/client.ts`](https://github.com/zhexin233-ui/double11-radar/blob/ffe2e618e22840b57d0afac313489c8e3ece33e4/src/lib/jev/client.ts).

## Get started

Clone, fill `.env` (encryption key and admin password), and start the stack.

```sh
git clone https://github.com/zhexin233-ui/double11-radar.git && cd double11-radar
cp .env.example .env   # APP_ENCRYPTION_KEY, ADMIN_PASSWORD
docker compose up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/zhexin233-ui/double11-radar/blob/ffe2e618e22840b57d0afac313489c8e3ece33e4/README.md](https://github.com/zhexin233-ui/double11-radar/blob/ffe2e618e22840b57d0afac313489c8e3ece33e4/README.md)

## Limits and data handling

Deal text and your needs are sent to TypeSafe. It scrapes a third-party deal feed within its published rate limits; long outages can miss deals. No license file.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit ffe2e618e228](https://github.com/zhexin233-ui/double11-radar/tree/ffe2e618e22840b57d0afac313489c8e3ece33e4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
