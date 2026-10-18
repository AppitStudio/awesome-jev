# Tab Land

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that finds any tab fast, groups tabs by the job you are doing, and closes stale ones; with a Jev key, Jev double-checks each group, removes tabs that do not fit, and names groups.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/robin-anil/tab-land) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/robin-anil/tab-land#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-19. |
| Jev evidence | [`src/lib/jev.js`](https://github.com/robin-anil/tab-land/blob/f994849b2128ff099c0840d533ebef89bc2ebe20/src/lib/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [robin-anil](https://github.com/robin-anil). Independently curated. |
| Format | Chrome extension (MV3) |
| Platform and availability | Chrome (load unpacked from source; no Chrome Web Store listing verified). |
| Jev's role | Optional judge that asks typed questions like whether tabs serve one goal and what kind of work a tab is. |
| Requirements | Chrome; optional TypeSafe Jev key (works without one). |
| License | [Apache-2.0](https://github.com/robin-anil/tab-land/blob/f994849b2128ff099c0840d533ebef89bc2ebe20/LICENSE) |

## When to use

- Tame dozens of tabs with task-based groups and quick switching.
- Want an optional Jev check on heuristic grouping.
- Mismatch: load-unpacked install; Jev is optional.

## How it works

Heuristics (opener links, switching patterns, shared title words) build groups; `src/lib/jev.js` then calls the System One API to confirm membership and name groups. Integration evidence: [`src/lib/jev.js`](https://github.com/robin-anil/tab-land/blob/f994849b2128ff099c0840d533ebef89bc2ebe20/src/lib/jev.js).

## Get started

From the upstream README: download the repo, load it unpacked in `chrome://extensions`, then optionally paste a Jev key in settings and click Test.

```sh
git clone https://github.com/robin-anil/tab-land
# chrome://extensions > Developer mode > Load unpacked
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README About Jev section
- src/lib/jev.js

## Limits and data handling

With a key, tab titles and URLs go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit f994849b2128](https://github.com/robin-anil/tab-land/tree/f994849b2128ff099c0840d533ebef89bc2ebe20). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
