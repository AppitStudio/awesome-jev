# Jev Chromium

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Electron browser agent that collects data across pages: Jev picks each click, focus, navigation or done step from the page's actionable elements, an OpenAI-compatible text model plans, fills and verifies, and results export as a cited table or CSV.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kolawong/jev-chromium) |
| Maintainer | [kolawong](https://github.com/kolawong). Independently curated. |
| Format | Electron desktop app (Node.js); README mainly in Chinese |
| Requirements | Node.js; `TYPESAFE_API_KEY` plus a key for an OpenAI-compatible text model (MiniMax by default, or DeepSeek/OpenAI). |
| License | [MIT](https://github.com/kolawong/jev-chromium/blob/bf69d9b612a91519c0e5a18a2afab1afbecb0cbb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/agent/model.js`](https://github.com/kolawong/jev-chromium/blob/bf69d9b612a91519c0e5a18a2afab1afbecb0cbb/src/agent/model.js) at the pinned commit. |

## When to use

- Gather names, prices and stock across a few product pages into a table where every cell cites its source page.
- Study a loop where Jev chooses browser actions and a separate step verifies completion against page evidence.
- Mismatch: no screenshot vision; complex iframes, Shadow DOM and Canvas pages are not fully supported; needs two providers.

## How it works

The agent observes DOM elements and page text, asks Jev (`jev-latest`, key from `TYPESAFE_API_KEY`) to choose the next action with probabilities, executes it in Chromium, and only marks a task done after independent checks of counts, sources and completion conditions, within default budgets (60 cycles, 12 pages). Integration evidence: [`src/agent/model.js`](https://github.com/kolawong/jev-chromium/blob/bf69d9b612a91519c0e5a18a2afab1afbecb0cbb/src/agent/model.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/kolawong/jev-chromium.git && cd jev-chromium
npm install
cp .env.example .env   # TYPESAFE_API_KEY and text-model key, if provided; otherwise set them in the app's settings
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Offline tests: `npm test` (unit + local-page browser tests with a deterministic model stand-in).

## Limits and data handling

Page text needed for each task goes to TypeSafe and the configured text model on your keys; settings are stored locally.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit bf69d9b612a9](https://github.com/kolawong/jev-chromium/tree/bf69d9b612a91519c0e5a18a2afab1afbecb0cbb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
