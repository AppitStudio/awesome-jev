# Practical Data (Chrome extension that shades comparable table columns, with Jev deciding which columns and which end is better)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that colour-shades the comparable columns of HTML tables on any page. A small decision model picks which columns to shade and which end of each is better; code does the parsing, arithmetic and colours. The default Free provider forwards table text through the author's Cloudflare Worker to Jev; you can instead use your own TypeSafe key from the browser, or Cloudflare's Clef. The README reports 284 of 285 labelled columns matched on 26 pages, with labels and thresholds tuned on those pages.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/philrenaud/practical-data) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://practicaldata.dev) |
| Pricing and access | The extension is MIT and the default Free provider needs no key; it has a per-install daily request limit and the author's server funds the calls, so availability may change. Using your own key bills your TypeSafe account. Checked 2026-11-04. |
| Jev evidence | [`src/decide/model.ts`](https://github.com/philrenaud/practical-data/blob/d3995bfbe881d1a00a0cc3c8f04c57eb3164d7e7/src/decide/model.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [philrenaud](https://github.com/philrenaud). Independently curated. |
| Format | Chrome extension (TypeScript) plus a Cloudflare Worker proxy |
| Platform and availability | Desktop Chrome (Chrome Web Store listing and source build). |
| Jev's role | Decides which table columns are comparable and which end of each column is better; code shades them. |
| Requirements | Chrome (store install or build from source); optional own TypeSafe key. |
| License | [MIT](https://github.com/philrenaud/practical-data/blob/d3995bfbe881d1a00a0cc3c8f04c57eb3164d7e7/LICENSE) |

## When to use

- Make dense comparison tables readable at a glance without writing site-specific rules.
- Mismatch: the default Free provider sends table text through the author's server, and the accuracy figure is a regression check on tuned pages.

## How it works

`src/decide/model.ts` asks typed questions about each table near the viewport; the Worker config forwards them to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), or the browser calls TypeSafe directly with your key. Integration evidence: [`src/decide/model.ts`](https://github.com/philrenaud/practical-data/blob/d3995bfbe881d1a00a0cc3c8f04c57eb3164d7e7/src/decide/model.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/philrenaud/practical-data
npm ci
npm run build   # or install from the Chrome Web Store link in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with what leaves your browser, providers and permissions: [github.com/philrenaud/practical-data#readme](https://github.com/philrenaud/practical-data#readme)
- Site and demo: [practicaldata.dev](https://practicaldata.dev)

## Limits and data handling

With the default Free provider, table text, a random install id and your IP address reach the author's Worker (answers cached 30 days; table text not stored). With your own key the author receives nothing. A content script runs on all pages. Daily request limits apply to the Free provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit d3995bfbe881](https://github.com/philrenaud/practical-data/tree/d3995bfbe881d1a00a0cc3c8f04c57eb3164d7e7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
