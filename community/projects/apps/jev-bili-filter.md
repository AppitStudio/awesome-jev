# B站降噪 · JEV (Bilibili noise filter)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Original Chrome/Edge extension (Chinese, with English README) that filters Bilibili comments and plain-text danmaku on the page with TypeSafe Jev: four toggles — spoilers, trolling, ads and fandom flame wars — plus one-sentence custom rules, no blocklists or prompts to maintain. Upstream of the listed Firefox port.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/littlewindy123/jev-bili-filter) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/littlewindy123/jev-bili-filter#readme) · [install guide](https://github.com/littlewindy123/jev-bili-filter/blob/de9b9838c638a81f4df2d30a8fc1c24cdef8ddc7/docs/INSTALL.md) |
| Pricing and access | No subscription; download `jev-bili-filter.zip` from [GitHub Releases](https://github.com/littlewindy123/jev-bili-filter/releases) (v0.1.0 preview). Jev calls use your own TypeSafe key. Checked 2026-10-08. |
| Jev evidence | [`background.js`](https://github.com/littlewindy123/jev-bili-filter/blob/de9b9838c638a81f4df2d30a8fc1c24cdef8ddc7/background.js) and [`core.js`](https://github.com/littlewindy123/jev-bili-filter/blob/de9b9838c638a81f4df2d30a8fc1c24cdef8ddc7/core.js) send text to be judged (plus reply context and video title/description) to the official TypeSafe endpoint. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [littlewindy123](https://github.com/littlewindy123). Independently curated. |
| Format | Chromium MV3 extension (load unpacked from the release zip) |
| Platform and availability | Chrome / Edge desktop. |
| Jev's role | Classifies each comment and danmaku against your enabled categories and custom rules. |
| Requirements | Chromium browser and a TypeSafe API key. |
| License | [MIT](https://github.com/littlewindy123/jev-bili-filter/blob/de9b9838c638a81f4df2d30a8fc1c24cdef8ddc7/LICENSE). |

## When to use

- Keep danmaku on while hiding spoilers and trolling.
- Describe a new kind of noise in one sentence instead of keyword lists.
- Mismatch: probabilistic filtering can miss or over-hide items.

## How it works

The content script collects comments and danmaku, Jev judges them per enabled category, and matches are hidden in place.

## Get started

Install the release zip (README):

```sh
# download jev-bili-filter.zip from Releases, unzip, keep the folder
# chrome://extensions → Developer mode → Load unpacked
# open the 「B站降噪」 panel → paste TypeSafe API key → 保存并连接
```

Jev calls billed to your TypeSafe key.

## Examples and demos

- [English README](https://github.com/littlewindy123/jev-bili-filter/blob/de9b9838c638a81f4df2d30a8fc1c24cdef8ddc7/README.en.md).
- Firefox port: [Ray4AI/jev-bili-filter](https://github.com/Ray4AI/jev-bili-filter).

## Limits and data handling

Text to be judged, reply context and video title/description go to TypeSafe; no cookies. Independent of Bilibili and TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit de9b9838c638](https://github.com/littlewindy123/jev-bili-filter/tree/de9b9838c638a81f4df2d30a8fc1c24cdef8ddc7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
