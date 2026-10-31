# Jev abstract art playground (turns a prompt into abstract art through 80+ parallel Jev decisions)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web playground that turns a natural-language prompt into abstract art by asking Jev typed questions about 80+ renderer characteristics (palette, composition, form) in parallel, rechecking uncertain choices, then rendering with canvas-sketch. It compares latency and cost against a reasoning model and against generating the art directly with AI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/carollia-99/jev-determinism-and-abstraction) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://jev-abstract-art.vercel.app/) |
| Pricing and access | Hosted demo free to use at review time (no sign-in seen); local builds need your own AI Gateway key. Checked 2026-10-31. |
| Jev evidence | [`server/compose-with-jev.js`](https://github.com/carollia-99/jev-determinism-and-abstraction/blob/2f7bec2fbd6d71ccce14d350e20dbce2e015017a/server/compose-with-jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/CarolLiang7/status/2116255609477591106)). |
| Maintainer | [carollia-99](https://github.com/carollia-99). Independently curated. |
| Format | Web app (Vercel; Node server + canvas-sketch) |
| Platform and availability | Browser (hosted demo on Vercel). |
| Jev's role | Makes every renderer decision (visual direction plus 80+ characteristics) as typed choices. |
| Requirements | Hosted demo in a browser, or a local build with a Vercel AI Gateway key for `typesafe-ai/jev-1.14.0`. |
| License | No LICENSE file (all rights reserved by default) on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See how fast, repeatable typed decisions can drive a generative renderer.
- Mismatch: the decision space must be enumerated up front, so output is limited to the renderer's characteristics.

## How it works

`server/compose-with-jev.js` asks Jev (`typesafe-ai/jev-1.14.0` through the AI Gateway) for a visual thesis, rechecks low-confidence answers, then resolves each renderer characteristic as a choice; `server/route-with-jev.js` routes the prompt. Integration evidence: [`server/compose-with-jev.js`](https://github.com/carollia-99/jev-determinism-and-abstraction/blob/2f7bec2fbd6d71ccce14d350e20dbce2e015017a/server/compose-with-jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [jev-abstract-art.vercel.app/](https://jev-abstract-art.vercel.app/)
- Post on X: [x.com/CarolLiang7/status/2116255609477591106](https://x.com/CarolLiang7/status/2116255609477591106)

## Limits and data handling

Prompts go to the Vercel AI Gateway and TypeSafe. No LICENSE file at the reviewed commit: the source is public but no reuse rights are granted. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 2f7bec2fbd6d](https://github.com/carollia-99/jev-determinism-and-abstraction/tree/2f7bec2fbd6d71ccce14d350e20dbce2e015017a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
