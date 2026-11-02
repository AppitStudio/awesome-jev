# OwnYourTimeline (Chrome and Edge extension that filters your X Home feed with a plain-language rule, classified by Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 extension that filters both X Home tabs with an instruction such as "Nothing political": it holds each timeline response, sends its posts (text, quotes, images) to Jev in one bulk request, and removes posts scoring 0.90 or more before X renders them. It fails open and has an optional Filtered tab.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/raghavio/ownyourtimeline) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/raghavio/ownyourtimeline#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; TypeSafe calls are billed to your own key. Checked 2026-11-03. |
| Jev evidence | [`src/provider.ts`](https://github.com/raghavio/ownyourtimeline/blob/5f5f278c8baae8d610fa2228557ac648ae658d1c/src/provider.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [raghavio](https://github.com/raghavio). Independently curated. |
| Format | Chrome / Edge extension (TypeScript) |
| Platform and availability | Chrome or Edge (load unpacked). |
| Jev's role | Scores each Home-feed post against your instruction. |
| Requirements | Chrome or Edge 120+, Node.js 22+ to build; your own TypeSafe API key. |
| License | [MIT](https://github.com/raghavio/ownyourtimeline/blob/5f5f278c8baae8d610fa2228557ac648ae658d1c/LICENSE) |

## When to use

- Hide a topic from your X feed without muting accounts or keywords.
- Mismatch: X Home only; not yet in a store, so you build and load it unpacked.

## How it works

`src/provider.ts` sends each Home response's posts and your instruction to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`) as one bulk request, and the content script removes posts above the threshold from the JSON before render. Integration evidence: [`src/provider.ts`](https://github.com/raghavio/ownyourtimeline/blob/5f5f278c8baae8d610fa2228557ac648ae658d1c/src/provider.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/raghavio/ownyourtimeline.git
cd ownyourtimeline
npm ci
npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How it works and privacy notes: [github.com/raghavio/ownyourtimeline#readme](https://github.com/raghavio/ownyourtimeline#readme)

## Limits and data handling

Post text, quotes, images and your instruction go directly to TypeSafe; a remembered key is stored unencrypted in extension storage. Each Home response is normally one billable call. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 5f5f278c8baa](https://github.com/raghavio/ownyourtimeline/tree/5f5f278c8baae8d610fa2228557ac648ae658d1c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
