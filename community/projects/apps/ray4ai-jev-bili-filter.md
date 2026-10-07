# Bilibili noise filter for Firefox (JEV)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Firefox (and Chrome) port of littlewindy123/jev-bili-filter: toggles for spoilers, trolling, ads and partisan chants, plus your own one-sentence rules, filter Bilibili comments and danmaku with TypeSafe Jev; adds local keywords that work without a key, per-item Canvas danmaku filtering, a block log and usage tracking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ray4AI/jev-bili-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Ray4AI/jev-bili-filter#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT extension; keyword filtering works with no key. Jev judging needs your own TypeSafe key (usage billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`background.js`](https://github.com/Ray4AI/jev-bili-filter/blob/0fee84fe1c0787ee94c621321848fd087cdb34c2/background.js) and [`core.js`](https://github.com/Ray4AI/jev-bili-filter/blob/0fee84fe1c0787ee94c621321848fd087cdb34c2/core.js) send one-question-per-item batches to `/v1/systemone`; README documents the request shape and token savings. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [Ray4AI](https://github.com/Ray4AI). Independently curated. |
| Format | Firefox MV3 extension (also loads in Chrome 121+) |
| Platform and availability | Firefox 140+ (temporary load or self-signed AMO package); Chrome/Edge 121+. |
| Jev's role | Judges whether each comment or danmaku line matches the enabled categories or your rules; keyword rules are local code. |
| Requirements | Firefox 140+ (or Chrome 121+); optional TypeSafe API key. |
| License | [MIT](https://github.com/Ray4AI/jev-bili-filter/blob/0fee84fe1c0787ee94c621321848fd087cdb34c2/LICENSE). |

## When to use

- Filter spoilers, ads or trolling in Bilibili comments and danmaku on Firefox.
- Use only local keywords with no API spend.
- Mismatch: community port; upstream design belongs to littlewindy123/jev-bili-filter.

## How it works

Rules and video context are sent once in `state` with one question per item (upstream reports ~180 input tokens per item vs ~578 in the original). Canvas danmaku are filtered by rewriting `seg.so` segments in the page world; a block log lets you add exemptions.

## Get started

Load as a temporary add-on (README *安装*), or install the zip from Releases:

```sh
git clone https://github.com/Ray4AI/jev-bili-filter.git
# Firefox: about:debugging#/runtime/this-firefox → Load Temporary Add-on → jev-bili-filter/manifest.json
```

Jev requests are billed to your TypeSafe key; keyword-only mode makes none.

## Examples and demos

- [Install](https://github.com/Ray4AI/jev-bili-filter/blob/0fee84fe1c0787ee94c621321848fd087cdb34c2/docs/INSTALL.md) and [testing notes](https://github.com/Ray4AI/jev-bili-filter/blob/0fee84fe1c0787ee94c621321848fd087cdb34c2/docs/TESTING.md).
- Upstream: [littlewindy123/jev-bili-filter](https://github.com/littlewindy123/jev-bili-filter).

## Limits and data handling

Comment and danmaku text from pages you view goes to TypeSafe when Jev is enabled; key stored locally. Token savings are upstream measurements. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 0fee84fe1c07](https://github.com/Ray4AI/jev-bili-filter/tree/0fee84fe1c0787ee94c621321848fd087cdb34c2). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
