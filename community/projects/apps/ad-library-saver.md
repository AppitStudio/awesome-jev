# Ad Library Saver by Jim Banks (Chrome extension that saves Meta Ad Library ads as you scroll and has Jev tag their format, call to action and funnel stage)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 Chrome extension for competitor ad research. As you scroll the Meta Ad Library, each ad that comes into view is saved to a database inside the extension (copy, headline, call-to-action button, landing URL with tracking parameters stripped, media, run dates, country). Jev tags each ad's format, call to action and funnel stage, three at a time, and everything exports to CSV. Saving and export work without a key; only tagging needs one.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jimbanks/ad-library-saver) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/jimbanks/ad-library-saver#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-18. |
| Jev evidence | [`background.js`](https://github.com/jimbanks/ad-library-saver/blob/7c935db97a1bbec17abd50dd9d1b0fe36812a7e0/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jimbanks](https://github.com/jimbanks). Independently curated. |
| Format | Chrome extension (Manifest V3, JavaScript, MIT) |
| Platform and availability | Chrome, loaded unpacked (not on the Chrome Web Store); English Meta UI only |
| Jev's role | Tags each saved ad with format, call to action and funnel stage using typed questions. |
| Requirements | Chrome with Developer mode, and a TypeSafe key for tagging (set in the extension options). |
| License | [MIT](https://github.com/jimbanks/ad-library-saver/blob/7c935db97a1bbec17abd50dd9d1b0fe36812a7e0/LICENSE) |

## When to use

- Build a tagged, exportable swipe file of a competitor's Meta ads.
- Mismatch: a reliable scraper; it depends on the visible English text of Meta's page and can break when Meta changes it.

## How it works

`background.js` queues saved ads and posts each one's copy and structure to `https://api.typesafe.ai/v1/systemone`; `questions.js` holds the typed questions. Integration evidence: [`background.js`](https://github.com/jimbanks/ad-library-saver/blob/7c935db97a1bbec17abd50dd9d1b0fe36812a7e0/background.js).

## Get started

Load the folder unpacked in `chrome://extensions`, paste your TypeSafe key in the options page, and run the built-in test with an invented ad.

```sh
git clone https://github.com/jimbanks/ad-library-saver
# chrome://extensions -> Developer mode -> Load unpacked -> pick the folder
# options page -> paste TypeSafe key -> "Test with an invented ad"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jimbanks/ad-library-saver/blob/7c935db97a1bbec17abd50dd9d1b0fe36812a7e0/README.md](https://github.com/jimbanks/ad-library-saver/blob/7c935db97a1bbec17abd50dd9d1b0fe36812a7e0/README.md)

## Limits and data handling

Ad text you browse is sent to TypeSafe on your key for tagging. It parses Meta's page by visible text, so changes there can stop saves; check Meta's terms before collecting ads at scale. Not run here.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 7c935db97a1b](https://github.com/jimbanks/ad-library-saver/tree/7c935db97a1bbec17abd50dd9d1b0fe36812a7e0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
