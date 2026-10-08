# IronBee Express

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Goal-driven browser agent: each step is one TypeSafe Jev decision over the page's offered controls plus one IronBee DevTools call that acts and returns the next snapshot, so model output never becomes a selector, coordinate or script; after the run it reviews the final page and API responses (and backend traces with IronBee), and runs can be recorded and replayed without the engine.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ironbee-ai/ironbee-express) |
| Maintainer | [ironbee-ai](https://github.com/ironbee-ai). Independently curated. |
| Format | Node CLI and web UI (`npm run dev -- ui`, `http://127.0.0.1:15986`) |
| Requirements | Node; `TYPESAFE_API_KEY`; IronBee DevTools browser runtime. |
| License | [Elastic License 2.0](https://github.com/ironbee-ai/ironbee-express/blob/5e547b7844f1e52a1e6fbd8bedb1b2a926b79a49/LICENSE) — source available, not an OSI open-source license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run one-sentence browser tasks (log in, add to cart, check out) without writing assertions.
- Record a run once and replay it without model calls.
- Mismatch: tied to IronBee DevTools as the browser layer.

## How it works

[`src/engine/jev.ts`](https://github.com/ironbee-ai/ironbee-express/blob/5e547b7844f1e52a1e6fbd8bedb1b2a926b79a49/src/engine/jev.ts) / [`src/engine/systemone.ts`](https://github.com/ironbee-ai/ironbee-express/blob/5e547b7844f1e52a1e6fbd8bedb1b2a926b79a49/src/engine/systemone.ts) ask Jev to pick an action, option or value only from what the snapshot offers; a deeper reasoning model is used only where the README describes a fallback.

## Get started

Build and start the UI (README *Quick start*):

```sh
git clone https://github.com/ironbee-ai/ironbee-express.git && cd ironbee-express
npm install && npm run build
echo 'TYPESAFE_API_KEY=…' > .env
npm run dev -- ui
```

Each step and the review are Jev calls billed to your key (README demo: $0.00054 for a 9-action order run — author-reported).

## Examples and demos

- README demo GIF: sign-in to completed order on IronBee's e-shop demo (9 actions, 6.7 s — author-reported).

## Limits and data handling

Page control text and goal go to TypeSafe. Elastic License 2.0 terms apply. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 5e547b7844f1](https://github.com/ironbee-ai/ironbee-express/tree/5e547b7844f1e52a1e6fbd8bedb1b2a926b79a49). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
