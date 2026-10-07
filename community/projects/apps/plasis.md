# Plasis

[All projects](../README.md) · [Web apps](README.md#web-apps)

One text box that turns what you type into the right UI card (event, reminder, issue, checklist, bill split and more): one TypeSafe Jev call answers 15 typed intent questions in parallel while a deterministic parser reads dates and amounts; a free offline keyword classifier is the default, with measured agreement against Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shreyaspangal/plasis) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Live demo](https://plasisui.vercel.app) (reachable 2026-10-08; which classifier the demo uses was not verified). |
| Pricing and access | No fee; the live demo and the source build run offline by default. Online Jev needs your own TypeSafe key (or Vercel AI Gateway credits), billed by that provider. Checked 2026-10-08. |
| Jev evidence | [`src/app/api/intent/route.ts`](https://github.com/shreyaspangal/plasis/blob/8b8dd13409aedc3c5c9281e67dbf8e5d8d53ec03/src/app/api/intent/route.ts) calls Jev server-side; README documents the 15-question fan-out and the 85% card agreement on 101 sentences measured by the author. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [shreyaspangal](https://github.com/shreyaspangal). Independently curated. |
| Format | Next.js web app (Bun) with live demo |
| Platform and availability | Web browser; self-host with Bun 1.2+. Hosted demo on Vercel. |
| Jev's role | Classifies which card the typed text is and which signals (video call, urgency…) apply; code parses values and decides the card. |
| Requirements | Bun 1.2+; optional `TYPESAFE_API_KEY` (or `AI_GATEWAY_API_KEY`) in `.env.local`. |
| License | [MIT](https://github.com/shreyaspangal/plasis/blob/8b8dd13409aedc3c5c9281e67dbf8e5d8d53ec03/LICENSE). |

## When to use

- Try intent-to-UI classification where Jev picks the card and code fills values.
- Compare the offline scorer with Jev using the measurement scripts.
- Mismatch: a demo/prototype app; cards are stored locally in the browser.

## How it works

Each debounced keystroke goes to the server route, which asks Jev (or the offline classifier) 15 typed questions in one call; a small state machine only changes the card when a challenger wins twice or is very sure, and a deterministic parser extracts dates, amounts and names. Inspired by MIT Shapeshift (baseline commit noted upstream).

## Get started

Run locally (README *Quick start*); add a key to switch from `jev-offline` to Jev:

```sh
git clone https://github.com/shreyaspangal/plasis && cd plasis
bun install
cp .env.example .env.local   # optional: TYPESAFE_API_KEY=...
bun dev
```

With a key set, typing sends debounced Jev requests billed by TypeSafe (or Vercel AI Gateway).

## Examples and demos

- [Live demo](https://plasisui.vercel.app).
- README *What I built* and *How it works* (diagrams).

## Limits and data handling

Typed text goes to TypeSafe (or Vercel AI Gateway) only when a key is configured; keys stay server-side. Agreement figures are the author's measurements. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 8b8dd13409ae](https://github.com/shreyaspangal/plasis/tree/8b8dd13409aedc3c5c9281e67dbf8e5d8d53ec03). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
