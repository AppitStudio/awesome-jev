# How Jev works by Ritchie King (interactive explainer of Jev's question types and batching, with puzzles answered by real requests)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Interactive web explainer for Jev: what its question types are, why batching many questions about one context is cheap, and a set of puzzles where each starts with a solution that runs but gets some cases wrong, and you fix it by changing what you ask Jev or what you do with the answers. The checks send your questions to Jev for real through the author's small proxy, which holds the key and enforces a daily budget, caching and per-visitor rate limits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ritchieking/jev) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://ritchiesking.com/jev/) |
| Pricing and access | Free to use; the author pays for Jev calls behind a daily budget cap. Checked 2026-11-18. |
| Jev evidence | [`src/tabs/Puzzles.tsx`](https://github.com/ritchieking/jev/blob/672e3795e0be11e51f10042d66ef264fced87079/src/tabs/Puzzles.tsx) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ritchieking](https://github.com/ritchieking). Independently curated. |
| Format | Static React page with a small Node.js proxy (no license file) |
| Platform and availability | Web (ritchiesking.com/jev/); self-hostable with your own key |
| Jev's role | Answers the explainer's live examples and puzzle checks; the proxy pins `jev-1.14.0` so recorded answers don't drift. |
| Requirements | A browser to use it; to run your own copy, Node.js and a `TYPESAFE_API_KEY` for the proxy. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Learn Jev's question types and batching hands-on before writing your own integration.
- Mismatch: official documentation; it is an independent explainer.

## How it works

`src/tabs/Puzzles.tsx` sends each puzzle's questions to the proxy in `server/`, which forwards them to `https://api.typesafe.ai/v1/systemone` with the pinned model; `shared/types.ts` is the contract between them. Integration evidence: [`src/tabs/Puzzles.tsx`](https://github.com/ritchieking/jev/blob/672e3795e0be11e51f10042d66ef264fced87079/src/tabs/Puzzles.tsx).

## Get started

Open the page and work through the Explainer, Performance and Puzzles tabs.

```sh
# use it: https://ritchiesking.com/jev/
# run locally:
git clone https://github.com/ritchieking/jev && cd jev && npm install
echo 'TYPESAFE_API_KEY=...' > .env
npm run dev:server & npm run dev   # http://localhost:5173/jev/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live page: [ritchiesking.com/jev/](https://ritchiesking.com/jev/)
- README: [github.com/ritchieking/jev/blob/672e3795e0be11e51f10042d66ef264fced87079/README.md](https://github.com/ritchieking/jev/blob/672e3795e0be11e51f10042d66ef264fced87079/README.md)

## Limits and data handling

No license file on the reviewed commit, so reuse terms are not granted. Puzzle inputs you type are sent to TypeSafe through the author's proxy. Independent; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 672e3795e0be](https://github.com/ritchieking/jev/tree/672e3795e0be11e51f10042d66ef264fced87079). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
