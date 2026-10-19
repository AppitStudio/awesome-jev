# flowtape

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Records a user journey in a running Vite + React or Next.js app and exports it as JSON and a Claude Code prompt to replay and explore; Jev (TypeSafe) finds replay targets visually from screenshots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vvedantb/flowtape) |
| Maintainer | [vvedantb](https://github.com/vvedantb). Independently curated. |
| Format | npm package (Vite plugin, Next.js route handler, React overlay) |
| Requirements | Vite + React or Next.js dev server; `TYPESAFE_API_KEY` for Jev visual targeting; Claude Code to run exported prompts. |
| License | None (no LICENSE file) on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/vvedantb/status/2111936544093110391)). |
| Jev evidence | [`packages/flowtape/src/script/jev.ts`](https://github.com/vvedantb/flowtape/blob/453bf82f192f8316e268cf50367ab842bc89acee/packages/flowtape/src/script/jev.ts) at the pinned commit. |

## When to use

- Turn a manual click-through into a repeatable agent E2E prompt.
- Want replay to find buttons visually when selectors drift.
- Mismatch: dev-only tooling; no license file, so reuse terms are unclear.

## How it works

An in-app overlay records clicks and inputs during `vite dev` or `next dev`, then writes the flow to `.flowtape/` as JSON plus a Markdown prompt with goal, steps and assertions. `packages/flowtape/src/script/jev.ts` is a plain `fetch` client for `https://api.typesafe.ai/v1/systemone` that sends a page screenshot with `box` questions to locate targets during replay. Integration evidence: [`packages/flowtape/src/script/jev.ts`](https://github.com/vvedantb/flowtape/blob/453bf82f192f8316e268cf50367ab842bc89acee/packages/flowtape/src/script/jev.ts).

## Get started

From the upstream README: `npm install -D @vvedantb/flowtape`, add the Vite plugin (or the Next.js route handler) and mount the overlay in dev.

```sh
npm install -D @vvedantb/flowtape
# vite.config.ts: plugins: [flowtape(), react()]
claude "Follow @.flowtape/prompts/<flow>.md against the running app"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [flowtape-mu.vercel.app](https://flowtape-mu.vercel.app)
- [x.com/vvedantb/status/2111936544093110391](https://x.com/vvedantb/status/2111936544093110391)

## Limits and data handling

Screenshots of your running app go to TypeSafe when Jev targeting is on. No LICENSE file at the reviewed commit; listed as source available, not open source.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 453bf82f192f](https://github.com/vvedantb/flowtape/tree/453bf82f192f8316e268cf50367ab842bc89acee). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
