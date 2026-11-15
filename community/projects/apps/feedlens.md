# FeedLens (Chrome extension that tracks the LinkedIn posts you see and has Jev sort each one as In Focus or Off Topic for your own interests)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Local Chrome extension: you describe your interests in your own words, and FeedLens sends the text of each LinkedIn feed post you view to Jev as one Choice question (one option per interest plus irrelevant). A side panel shows today's In Focus and Off Topic totals, expanded posts and a by-interest breakdown, plus monthly history. Only IDs, classifications and timestamps are stored. LinkedIn is supported today; other networks are open for contributions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IuryCavalcante/FeedLens) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/IuryCavalcante/FeedLens#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); not in the Chrome Web Store. You pay TypeSafe for your own Jev calls. Checked 2026-11-15. |
| Jev evidence | [`background.js`](https://github.com/IuryCavalcante/FeedLens/blob/5b2b5307ba2bcabb9998474d656c02c28b0b5bab/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [IuryCavalcante](https://github.com/IuryCavalcante). Independently curated. |
| Format | Chrome extension (unpacked, JavaScript, MIT) |
| Platform and availability | Chrome (unpacked Manifest V3 extension; LinkedIn feed) |
| Jev's role | Jev classifies each viewed post into one of your interests or off topic. |
| Requirements | Chrome (load unpacked) and your own TypeSafe API key. |
| License | [MIT](https://github.com/IuryCavalcante/FeedLens/blob/5b2b5307ba2bcabb9998474d656c02c28b0b5bab/LICENSE) |

## When to use

- See how much of your feed matches what you actually want to follow.
- Mismatch: feeds other than LinkedIn, until an adapter is contributed.

## How it works

`background.js` posts each post's text to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` and a `choice` question built from your saved interests, and rejects unexpected answers. Integration evidence: [`background.js`](https://github.com/IuryCavalcante/FeedLens/blob/5b2b5307ba2bcabb9998474d656c02c28b0b5bab/background.js).

## Get started

Load the folder as an unpacked extension, then add your key and interests in Settings.

```sh
git clone https://github.com/IuryCavalcante/FeedLens
# chrome://extensions -> Developer mode -> Load unpacked -> select the FeedLens folder
# open the side panel -> Settings -> add your TypeSafe key and interests
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/IuryCavalcante/FeedLens/blob/5b2b5307ba2bcabb9998474d656c02c28b0b5bab/README.md](https://github.com/IuryCavalcante/FeedLens/blob/5b2b5307ba2bcabb9998474d656c02c28b0b5bab/README.md)
- Video demo: [youtu.be/abzU8UOxlV0](https://youtu.be/abzU8UOxlV0)

## Limits and data handling

Visible post text is sent to TypeSafe on your key; the key is kept in `chrome.storage.local`. Changes to LinkedIn's page structure can break capture.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 5b2b5307ba2b](https://github.com/IuryCavalcante/FeedLens/tree/5b2b5307ba2bcabb9998474d656c02c28b0b5bab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
