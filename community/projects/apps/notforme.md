# NotForMe (Chrome extension that folds PR, product-launch and off-topic articles in Korean news lists using Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension (README in Korean and English) that collapses, blurs, dims or hides advertorial PR articles, product-launch pieces and off-topic stories in the article lists of ZDNet Korea, Yonhap, Hankyoreh and other Korean news sites. It only changes how the list is shown in your browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/x-mesh/notforme) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/x-mesh/notforme#readme) (source-built; no separate product site verified). |
| Pricing and access | Free (MIT); you supply a TypeSafe key. Checked 2026-11-01. |
| Jev evidence | [`extension/src/background.js`](https://github.com/x-mesh/notforme/blob/6fd503d765ae59cd60bf97dd377db280db2b883f/extension/src/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [x-mesh](https://github.com/x-mesh). Independently curated. |
| Format | Chrome extension (Manifest V3), unpacked install |
| Platform and availability | Chrome (desktop), unpacked extension. |
| Jev's role | Classifies each headline as PR, product launch or off-topic. |
| Requirements | Chrome; a TypeSafe key. |
| License | [MIT](https://github.com/x-mesh/notforme/blob/6fd503d765ae59cd60bf97dd377db280db2b883f/LICENSE) |

## When to use

- Declutter Korean news front pages of sponsored and launch coverage.
- Mismatch: supports a fixed list of Korean news sites.

## How it works

`extension/src/background.js` calls `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) from the extension's background worker with each headline and your filter settings; content scripts fold the flagged items. No relay server is needed. Integration evidence: [`extension/src/background.js`](https://github.com/x-mesh/notforme/blob/6fd503d765ae59cd60bf97dd377db280db2b883f/extension/src/background.js).

## Get started

From the upstream README (not run on the review host):

```sh
bash scripts/package.sh
# extract the archive from dist/, open chrome://extensions, enable Developer mode,
# Load unpacked, then enter your API key, endpoint and model in the popup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/x-mesh/notforme#readme](https://github.com/x-mesh/notforme#readme)

## Limits and data handling

Headlines and snippets on supported pages are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 6fd503d765ae](https://github.com/x-mesh/notforme/tree/6fd503d765ae59cd60bf97dd377db280db2b883f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
