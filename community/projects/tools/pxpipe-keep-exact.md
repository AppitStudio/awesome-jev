# pxpipe-keep-exact (pxpipe hook where Jev picks which ids, hashes, paths and numbers stay as text when old context is sent as images)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

`splitBlock` hook for pxpipe, which saves input tokens by sending old context as images: because image reading misses single characters in ids, hashes, paths and numbers (12/15 vs 15/15 on the author's verbatim test), the hook asks Jev which of those tokens matter, keeps only their lines as text and images the rest in the original order.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bigbizze/pxpipe-keep-exact) |
| Maintainer | [bigbizze](https://github.com/bigbizze). Independently curated. |
| Format | TypeScript library hook for pxpipe (MIT) |
| Requirements | Node.js with pnpm, pxpipe with the `splitBlock` hook from teamchong/pxpipe#360 (not merged on the reviewed date), and an OpenRouter key. |
| License | [MIT](https://github.com/bigbizze/pxpipe-keep-exact/blob/dcc47861e3a9abb79298a0433a12aaaf61c3d9c1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-selector.ts`](https://github.com/bigbizze/pxpipe-keep-exact/blob/dcc47861e3a9abb79298a0433a12aaaf61c3d9c1/src/jev-selector.ts) at the pinned commit. |

## When to use

- Keep exact identifiers readable while compressing long agent context into images.
- Mismatch: stock pxpipe today; it depends on an unmerged upstream hook.

## How it works

`src/jev-selector.ts` sends one `noul` question per candidate token position (about 240 characters of context each side, up to 150 per call) to OpenRouter's Decisions API with `typesafe/jev-1.14`. Decisions are cached on disk by sha256 of token and context, and if the split would not save tokens the block stays text. Integration evidence: [`src/jev-selector.ts`](https://github.com/bigbizze/pxpipe-keep-exact/blob/dcc47861e3a9abb79298a0433a12aaaf61c3d9c1/src/jev-selector.ts).

## Get started

Install the dependencies and wire the hook into a pxpipe build that has the `splitBlock` hook, as the README shows.

```sh
git clone https://github.com/bigbizze/pxpipe-keep-exact && cd pxpipe-keep-exact
pnpm install
pnpm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bigbizze/pxpipe-keep-exact/blob/dcc47861e3a9abb79298a0433a12aaaf61c3d9c1/README.md](https://github.com/bigbizze/pxpipe-keep-exact/blob/dcc47861e3a9abb79298a0433a12aaaf61c3d9c1/README.md)

## Limits and data handling

Token candidates and surrounding context from your conversation go to OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit dcc47861e3a9](https://github.com/bigbizze/pxpipe-keep-exact/tree/dcc47861e3a9abb79298a0433a12aaaf61c3d9c1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
