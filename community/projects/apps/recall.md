# Recall (Chrome history search with a local index, browsing stats and optional Jev ranking)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Desktop Chrome extension for finding a page you remember visiting. It builds a local index of your history, shows a browsing overview, and if you opt in with your own TypeSafe key, Jev re-ranks a shortlist of local matches by meaning.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ebuojr/recall) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ebuojr/recall#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download and source (MIT); Jev ranking uses your own TypeSafe key. Checked 2026-11-01. |
| Jev evidence | [`extension/src/jev.ts`](https://github.com/ebuojr/recall/blob/ba874990c810c8daee9fb91ee3926405be410e59/extension/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ebuodev/status/2116837838901727461)). |
| Maintainer | [ebuojr](https://github.com/ebuojr). Independently curated. |
| Format | Unpacked Chrome extension (TypeScript), zip from GitHub Releases |
| Platform and availability | Desktop Chrome (unpacked extension). |
| Jev's role | Optional re-ranking of a local shortlist of history matches. |
| Requirements | Desktop Chrome; an optional TypeSafe API key for Jev ranking. |
| License | [MIT](https://github.com/ebuojr/recall/blob/ba874990c810c8daee9fb91ee3926405be410e59/LICENSE) |

## When to use

- Find a half-remembered page by topic or phrase instead of exact title words.
- Mismatch: local search works without Jev; Jev only re-orders a shortlist.

## How it works

Search runs on a local index first; with Jev ranking enabled, `extension/src/jev.ts` sends the query and a shortlist of page titles and links to TypeSafe `api.typesafe.ai`, and the returned scores re-order the results. The full history index stays in the browser. Integration evidence: [`extension/src/jev.ts`](https://github.com/ebuojr/recall/blob/ba874990c810c8daee9fb91ee3926405be410e59/extension/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# download recall-chrome-v0.3.1.zip from GitHub Releases, extract it,
# then chrome://extensions > Developer mode > Load unpacked
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Synthetic demo page (no keys, no model calls): [github.com/ebuojr/recall/releases/download/v0.3.1/recall-demo.html](https://github.com/ebuojr/recall/releases/download/v0.3.1/recall-demo.html)
- Announcement on X: [x.com/ebuodev/status/2116837838901727461](https://x.com/ebuodev/status/2116837838901727461)

## Limits and data handling

Only the query and shortlisted titles and links go to TypeSafe when Jev ranking is on; history stays local. Unpacked experiment, not a Chrome Web Store listing. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit ba874990c810](https://github.com/ebuojr/recall/tree/ba874990c810c8daee9fb91ee3926405be410e59). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
