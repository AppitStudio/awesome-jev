# Quiet Feed (Chrome extension that hides rage bait and slop on X using Jev by default)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Manifest V3 extension that collapses rage bait, LLM slop and chosen topics on the X home timeline; Jev (`jev-latest`) is the default judge, with local GLiNER2.5-Decide or Fastino as alternatives.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/briwilcox/quiet-feed) |
| Maintainer | [briwilcox](https://github.com/briwilcox). Independently curated. |
| Format | Chrome/Brave extension, unpacked build (MIT) |
| Requirements | Node to build, Chrome or Brave, and your TypeSafe key for the Jev model. |
| License | [MIT](https://github.com/briwilcox/quiet-feed/blob/944b31db50273e7a4aaba0e04350c54ff48a9bdb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/background/jev.ts`](https://github.com/briwilcox/quiet-feed/blob/944b31db50273e7a4aaba0e04350c54ff48a9bdb/src/background/jev.ts) at the pinned commit. |

## When to use

- Filter your X feed without deleting anything.
- Compare Jev with a local decision model on the same filters.
- Mismatch: not in the Chrome Web Store; text only (no video analysis).

## How it works

`background/jev.ts` posts post text and labels to `https://api.typesafe.ai/v1/systemone`, validates results, caches decisions and enforces usage limits; every hide is reversible. Integration evidence: [`src/background/jev.ts`](https://github.com/briwilcox/quiet-feed/blob/944b31db50273e7a4aaba0e04350c54ff48a9bdb/src/background/jev.ts).

## Get started

Build per the README, load `dist/` unpacked, then paste your TypeSafe key and accept the data notice in Options.

```sh
git clone https://github.com/briwilcox/quiet-feed.git && cd quiet-feed
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/briwilcox/quiet-feed/blob/944b31db50273e7a4aaba0e04350c54ff48a9bdb/README.md](https://github.com/briwilcox/quiet-feed/blob/944b31db50273e7a4aaba0e04350c54ff48a9bdb/README.md)

## Limits and data handling

Post text and labels are sent to TypeSafe on your key when Jev is selected.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 944b31db5027](https://github.com/briwilcox/quiet-feed/tree/944b31db50273e7a4aaba0e04350c54ff48a9bdb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
