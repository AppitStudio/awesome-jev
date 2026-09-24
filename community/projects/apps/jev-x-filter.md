# jev-x-filter

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome MV3 extension that filters X (Twitter) timeline spam with TypeSafe Jev typed decisions across six toggleable classes; high confidence only mutes/blocks, default dry-run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/harodggg/jev-x-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [GitHub README](https://github.com/harodggg/jev-x-filter) |
| Pricing and access | No app purchase fee for MIT source; TypeSafe key BYOK. Not a Chrome Web Store listing at review tip. Checked 2026-09-24. |
| Jev evidence | [README](https://github.com/harodggg/jev-x-filter/blob/9e17bc8bab6f0a4a33e21e73a43aaf3cc25fdf9b/README.md) describes Service Worker four-question Jev gate and category toggles. |
| Disclosure | Open source MIT. Independently curated; no affiliation. Listing is not an endorsement. Live X filtering not run. |
| Maintainer | [harodggg](https://github.com/harodggg). Independently curated. |
| Format | Application |
| Platform and availability | Chrome MV3 load-unpacked; `npm run package` builds a zip. |
| Jev's role | Jev classifies posts (spam/scam/ad/clickbait/AI-slop/farm + emotion/β/α helpers); extension hides and optionally mutes/blocks under policy. |
| Requirements | Chrome; TypeSafe API key; load unpacked extension. |
| License | [MIT](https://github.com/harodggg/jev-x-filter/blob/9e17bc8bab6f0a4a33e21e73a43aaf3cc25fdf9b/LICENSE). |

## When to use

Use to **filter** X feeds with calibrated Jev judgments and dry-run defaults. Prefer [Jev Content Guard](jev-content-guard.md) for general web-page scanning.

## How it works

Content scripts extract posts; Service Worker prefilters then asks Jev; results hide content and may plan mute/block only at high confidence (default rehearsal).

## Get started

```sh
git clone https://github.com/harodggg/jev-x-filter.git
cd jev-x-filter
git checkout 9e17bc8bab6f0a4a33e21e73a43aaf3cc25fdf9b
# chrome://extensions → Load unpacked; configure TypeSafe key per README
```

## Examples and demos

- README architecture diagram and changelog (v0.4.5).

## Limits and data handling

Post text reaches TypeSafe. Mute/block can affect your X account—keep dry-run until confident.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 9e17bc8](https://github.com/harodggg/jev-x-filter/tree/9e17bc8bab6f0a4a33e21e73a43aaf3cc25fdf9b). AI-assisted README inspection; live X/Jev not run.

Related: [Jev Content Guard](jev-content-guard.md), [JevSlop](jevslop.md).
