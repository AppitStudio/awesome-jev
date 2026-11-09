# Deep Bench (NFL rarity trivia that uses Jev via OpenRouter to judge answers outside its roster data)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Krillion-style NFL trivia where rarer answers gain more yards; a roster database grades most answers and `typesafe/jev-router` on OpenRouter adjudicates pre-2002 and edge-case answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/drc/deep-bench) |
| Maintainer | [drc](https://github.com/drc). Independently curated. |
| Format | Node + Cloudflare Workers game (MIT) |
| Requirements | Node 26, mise, and an `OPENROUTER_API_KEY` for Jev adjudication. |
| License | [MIT](https://github.com/drc/deep-bench/blob/d576b494aebdbc1da932427aca5bbf59631a1d0f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.js`](https://github.com/drc/deep-bench/blob/d576b494aebdbc1da932427aca5bbf59631a1d0f/server.js) at the pinned commit. |

## When to use

- Grade open-ended trivia answers beyond a dataset.
- Cache model verdicts for repeat answers.
- Mismatch: Jev only handles answers the roster DB cannot.

## How it works

`server.js` sets `JEV_MODEL = 'typesafe/jev-router'`, reads the OpenRouter key and caches verdicts in `data/jev-cache.json`; Jev assigns the rarity tier and explains it. Integration evidence: [`server.js`](https://github.com/drc/deep-bench/blob/d576b494aebdbc1da932427aca5bbf59631a1d0f/server.js).

## Get started

Run `mise trust` and the README quickstart tasks, adding your OpenRouter key.

```sh
git clone https://github.com/drc/deep-bench.git && cd deep-bench
mise trust
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/drc/deep-bench/blob/d576b494aebdbc1da932427aca5bbf59631a1d0f/README.md](https://github.com/drc/deep-bench/blob/d576b494aebdbc1da932427aca5bbf59631a1d0f/README.md)

## Limits and data handling

Unrecognized answers are sent to OpenRouter/TypeSafe.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit d576b494aebd](https://github.com/drc/deep-bench/tree/d576b494aebdbc1da932427aca5bbf59631a1d0f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
