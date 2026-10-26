# Jev Playground by gmassello (step-by-step Spanish-language Jev lessons via Vercel AI Gateway)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small local web playground, written in Spanish, that teaches Jev step by step through the Vercel AI Gateway: you try typed questions, see confidence and per-call cost, and read practical notes on calibrating thresholds, measuring limits and keeping the key server-side; it also compares the native TypeSafe API and Cloudflare Workers AI routes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gmassello/jev) |
| Maintainer | [gmassello](https://github.com/gmassello). Independently curated. |
| Format | Node.js web app |
| Requirements | Node.js 24+; a Vercel AI Gateway API key. |
| License | [MIT](https://github.com/gmassello/jev/blob/6ef356cc4f1ba526344c9bf7809b696a4b79dae5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.js`](https://github.com/gmassello/jev/blob/6ef356cc4f1ba526344c9bf7809b696a4b79dae5/server.js) at the pinned commit. |

## When to use

- Learn Jev's question types hands-on in Spanish before building on it.
- See confidence and gateway cost per call while experimenting.
- Mismatch: a teaching playground, not a library.

## How it works

`server.js` calls `typesafe-ai/jev` through the AI SDK on Vercel AI Gateway and returns the answer with `providerMetadata.typesafe.confidence` and the gateway cost, so the browser never holds the key. Integration evidence: [`server.js`](https://github.com/gmassello/jev/blob/6ef356cc4f1ba526344c9bf7809b696a4b79dae5/server.js).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # set AI_GATEWAY_API_KEY
npm ci
npm start              # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gmassello/jev#readme](https://github.com/gmassello/jev#readme)

## Limits and data handling

What you type goes to Vercel AI Gateway and on to TypeSafe; Jev is reached through the gateway, not called directly.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 6ef356cc4f1b](https://github.com/gmassello/jev/tree/6ef356cc4f1ba526344c9bf7809b696a4b79dae5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
