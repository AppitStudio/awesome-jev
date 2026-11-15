# Raindrop Autosort (Chrome extension that saves the current tab to Raindrop.io and lets Jev pick the collection and tags)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Unofficial Manifest V3 extension for Raindrop.io: you list your collections with a short criterion each, and when you save a tab Jev reads the page and picks one collection from that list, plus up to four tags from your tag vocabulary. If Jev is unsure (below 0.7 by default), the bookmark goes to a fallback collection, and the popup lets you change it before saving. Rules can force a collection; a keyboard shortcut and a right-click menu save without the popup. English and Korean docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/x-mesh/raindrop-autosort) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/x-mesh/raindrop-autosort#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); not in the Chrome Web Store. Requires a Raindrop.io account; you pay TypeSafe for your own calls. Checked 2026-11-16. |
| Jev evidence | [`lib/classify.js`](https://github.com/x-mesh/raindrop-autosort/blob/f07afff5ef7bc4602adc4629a77432d2a9883283/lib/classify.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [x-mesh](https://github.com/x-mesh). Independently curated. |
| Format | Chrome extension (unpacked, JavaScript, MIT) |
| Platform and availability | Chrome and other Chromium browsers (unpacked Manifest V3 extension) |
| Jev's role | Jev picks the Raindrop.io collection and tags for each saved page from your own list and criteria. |
| Requirements | Chrome or another Chromium browser (load unpacked), a Raindrop.io account, and a Jev API key. |
| License | [MIT](https://github.com/x-mesh/raindrop-autosort/blob/f07afff5ef7bc4602adc4629a77432d2a9883283/LICENSE) |

## When to use

- Keep a Raindrop.io library sorted by your own written criteria.
- Mismatch: users who want new collections created automatically; it never creates collections.

## How it works

`lib/settings.js` sets the endpoint to `https://api.typesafe.ai/v1/systemone`; `lib/classify.js` sends one request with a Choice over your candidate collections and a yes/no question per tag, then applies the confidence floor and fallback. Integration evidence: [`lib/classify.js`](https://github.com/x-mesh/raindrop-autosort/blob/f07afff5ef7bc4602adc4629a77432d2a9883283/lib/classify.js).

## Get started

Load the repository folder unpacked, paste your Jev key in Options, add your collections with criteria and test the connections.

```sh
git clone https://github.com/x-mesh/raindrop-autosort
# chrome://extensions -> Developer mode -> Load unpacked -> select the folder
# Options -> paste Jev key -> Add my collections -> Test connections
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/x-mesh/raindrop-autosort/blob/f07afff5ef7bc4602adc4629a77432d2a9883283/README.md](https://github.com/x-mesh/raindrop-autosort/blob/f07afff5ef7bc4602adc4629a77432d2a9883283/README.md)

## Limits and data handling

Page title, description, selected text and the start of the article text go to TypeSafe on your key; on X and Threads only the focal post is read. Not made or endorsed by Raindrop.io.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit f07afff5ef7b](https://github.com/x-mesh/raindrop-autosort/tree/f07afff5ef7bc4602adc4629a77432d2a9883283). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
