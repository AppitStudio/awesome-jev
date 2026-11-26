# Jev World Map by Troy Anderson (type a yes/no statement and watch Jev answer it for all 193 UN countries on a live D3 map)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Type a statement such as "drives on the left" or "is landlocked" and a Cloudflare Worker asks Jev whether it is true for each of the 193 UN member states, using only that country's record from a committed data snapshot. Answers stream back as NDJSON and colour a D3 map by probability, with a hatched "unsure" band in the middle.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TheHazeEffect/jev-world-map) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/TheHazeEffect/jev-world-map#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source. Live answers call Jev through Cloudflare Workers AI, which bills it separately from the free allowance (top up AI Gateway credits or add your own TypeSafe key); a mock mode needs no account. Checked 2026-11-26. |
| Jev evidence | [`worker/jev.js`](https://github.com/TheHazeEffect/jev-world-map/blob/1dcc047aa6a5c229e974459ab9018b7b4acb3f68/worker/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Troy Anderson](https://github.com/TheHazeEffect). Independently curated. |
| Format | Cloudflare Worker + static D3 web app (JavaScript) |
| Platform and availability | Web app you run yourself as a Cloudflare Worker (local `npm run dev` or `wrangler deploy`); no public hosted instance was verified. |
| Jev's role | One Jev request carries every country's record in the state and one `noul` question per country; the map treats a probability of 0.65 or more as true, 0.35 or less as false, and the rest as unsure. |
| Requirements | Node.js and npm; for live answers a Cloudflare account ID and Workers AI API token, plus Workers AI credit or a TypeSafe key added to AI Gateway. |
| License | [MIT](https://github.com/TheHazeEffect/jev-world-map/blob/1dcc047aa6a5c229e974459ab9018b7b4acb3f68/LICENSE) |

## When to use

- Show how Jev answers many typed questions against one shared state, or demo calibrated probabilities to a non-technical audience.
- Mismatch: questions that need maths, dates or counting, where TypeSafe documents Jev 1.13 as weaker; the map shows Jev's reading of a static data snapshot, not live facts.

## How it works

`worker/jev.js` builds one request with all countries in `state.countries` (keyed by ISO3) and one `noul` question per country, and posts it to Cloudflare's `ai/run` REST endpoint for the `typesafe/jev` model; `JEV_BATCH_SIZE` splits the countries across several requests so the map fills in batch by batch. Integration evidence: [`worker/jev.js`](https://github.com/TheHazeEffect/jev-world-map/blob/1dcc047aa6a5c229e974459ab9018b7b4acb3f68/worker/jev.js).

## Get started

Run it in mock mode first, then add Cloudflare credentials and set `MOCK_JEV=false` in `.dev.vars` for real Jev answers.

```sh
git clone https://github.com/TheHazeEffect/jev-world-map
cd jev-world-map
npm install
cp .dev.vars.example .dev.vars   # MOCK_JEV=true by default
npm run dev                      # http://localhost:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshot and results table: [github.com/TheHazeEffect/jev-world-map#results](https://github.com/TheHazeEffect/jev-world-map#results)

## Limits and data handling

The country data is a committed snapshot from REST Countries, so answers are only as current as that file. The README's 193/193 results for three prompts (about $0.0018 and under a second per run on jev-1.13.0) are the author's own. Prompts are sent to Cloudflare and TypeSafe along with the country data; mock mode answers are random.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 1dcc047aa6a5](https://github.com/TheHazeEffect/jev-world-map/tree/1dcc047aa6a5c229e974459ab9018b7b4acb3f68). Inspected the README, LICENSE, `worker/jev.js` and `wrangler.jsonc` at the pinned commit; the app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
