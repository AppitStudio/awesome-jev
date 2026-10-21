# picode-decisions-jev (Jev for COGNIX[WS])

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

COGNIX[WS] extension that lets TypeSafe Jev answer the agents' fast browser decisions, such as which page element matches a description and yes/no checks about a page, so agents act without reading the whole page each step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cognixws/picode-decisions-jev) |
| Maintainer | [cognixws](https://github.com/cognixws). Independently curated. |
| Format | COGNIX[WS] extension (Node.js, no dependencies) |
| Requirements | COGNIX[WS] (manifest version 11), Node.js, a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/cognixws/picode-decisions-jev/blob/9d919c8321efcf991b43646ffa7bb450c61e89da/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.mjs`](https://github.com/cognixws/picode-decisions-jev/blob/9d919c8321efcf991b43646ffa7bb450c61e89da/server.mjs) at the pinned commit. |

## When to use

- Speed up COGNIX[WS] browser agents with sub-second element picks and page checks.
- Choose `jev-preview` when agents need to locate things in screenshots.
- Mismatch: only useful inside COGNIX[WS].

## How it works

`server.mjs` serves `POST /decide`, adds the key and model, and forwards the System One request to TypeSafe over one kept-alive connection; `GET /status` reports setup state. Oversized pages get a 413 so COGNIX[WS] retries with less of the page. Integration evidence: [`server.mjs`](https://github.com/cognixws/picode-decisions-jev/blob/9d919c8321efcf991b43646ffa7bb450c61e89da/server.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
# In COGNIX[WS]: Extensions > Add, enter
https://github.com/cognixws/picode-decisions-jev
# then paste your TypeSafe key and pick Jev (TypeSafe) under Settings > Helper model
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- What it sends and settings table in the README: [github.com/cognixws/picode-decisions-jev#readme](https://github.com/cognixws/picode-decisions-jev#readme)

## Limits and data handling

The page's accessibility outline (and screenshots when locating) is sent to TypeSafe, with likely credentials masked by COGNIX[WS] first, per the README.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 9d919c8321ef](https://github.com/cognixws/picode-decisions-jev/tree/9d919c8321efcf991b43646ffa7bb450c61e89da). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
