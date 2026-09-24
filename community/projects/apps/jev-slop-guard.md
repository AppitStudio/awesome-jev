# Jev Slop Guard

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome Manifest V3 extension that scores and stamps AI-slop labels on X and LinkedIn feed posts using TypeSafe Jev as you scroll.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davertor/jev-slop-guard) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [GitHub README](https://github.com/davertor/jev-slop-guard) |
| Pricing and access | No app purchase fee; source build / load unpacked. TypeSafe (or configured) inference is BYOK and can incur charges. Checked 2026-09-24. |
| Jev evidence | [README](https://github.com/davertor/jev-slop-guard/blob/6b4557033caf547a4f885e0193bb30abd5e727a2/README.md) and extension sources describe TypeSafe Jev scoring of X/LinkedIn feed posts; see also [PRIVACY.md](https://github.com/davertor/jev-slop-guard/blob/6b4557033caf547a4f885e0193bb30abd5e727a2/PRIVACY.md). |
| Disclosure | Open source MIT. Independently curated; no affiliation. Listing is not an endorsement. Chrome install and live feed scoring not tested on the review host. Distinct from [LinkedIn Slop Filter](jev-linkedin-slop-filter.md) and [JevSlop](jevslop.md). |
| Maintainer | [davertor](https://github.com/davertor). Independently curated. |
| Format | Application |
| Platform and availability | Chrome MV3 extension (`chrome-mv3` / WXT-style entrypoints). Source-build. |
| Jev's role | Classifies feed post text for AI-slop style signals with typed Jev judgments; UI stamps scores on the feed. Does not claim to rewrite posts. |
| Requirements | Chromium browser; TypeSafe API key in extension settings. |
| License | [MIT](https://github.com/davertor/jev-slop-guard/blob/6b4557033caf547a4f885e0193bb30abd5e727a2/LICENSE). |

## When to use

Use to **label** slop in social feeds while browsing. Prefer [LinkedIn Slop Filter](jev-linkedin-slop-filter.md) for LinkedIn-only local proxy setups, or [Jev Content Guard](jev-content-guard.md) for general page toxicity/fraud categories.

## How it works

Content scripts observe feed nodes, send text to the background Jev client, and render stamps from returned probabilities (per extension sources).

## Get started

```sh
git clone https://github.com/davertor/jev-slop-guard.git
cd jev-slop-guard
git checkout 6b4557033caf547a4f885e0193bb30abd5e727a2
npm ci && npm run build   # per package scripts
# load unpacked dist/chrome output; set TypeSafe key
```

## Examples and demos

- `PRIVACY.md` and `docs/`.
- `chrome-mv3` package tree.

## Limits and data handling

Feed text leaves the browser to TypeSafe when scoring. Platform DOM changes can break selectors.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 6b45570](https://github.com/davertor/jev-slop-guard/tree/6b4557033caf547a4f885e0193bb30abd5e727a2). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [LinkedIn Slop Filter](jev-linkedin-slop-filter.md), [Jev Content Guard](jev-content-guard.md), [JevSlop](jevslop.md).
