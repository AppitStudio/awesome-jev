# BookmarX by Peter Rauscher (Chrome extension that sorts your X bookmarks into folders with Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Scans the bookmarks you already have on X, suggests one of your existing bookmark folders for each with Jev, keeps low-confidence suggestions in a Review list, and files accepted results through the official X API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/peterrauscher/BookmarX) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/peterrauscher/BookmarX#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source, loaded unpacked; you supply your own TypeSafe key and an X developer app with bookmark API access (X Premium is needed for bookmark folders). Checked 2026-11-21. |
| Jev evidence | [`src/jev.js`](https://github.com/peterrauscher/BookmarX/blob/98d48b50a5bf11267664238cd65b726f7f9a0c0c/src/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [peterrauscher](https://github.com/peterrauscher). Independently curated. |
| Format | Chrome extension (no build step) |
| Platform and availability | Chrome or another Chromium browser (Manifest V3), loaded unpacked. |
| Jev's role | One narrow choice question per bookmark over your existing folder names; low-confidence answers are left for review instead of being filed. |
| Requirements | A TypeSafe API key, an X account with bookmark folders (X Premium), and an X developer app configured for user authentication with bookmark read/write access. |
| License | [MIT](https://github.com/peterrauscher/BookmarX/blob/98d48b50a5bf11267664238cd65b726f7f9a0c0c/LICENSE) |

## When to use

- Tidy a large pile of X bookmarks into folders you already made, reviewing only the unsure ones.
- Mismatch: no X Premium or no X developer access; BookmarX does not create folders.

## How it works

`src/jev.js` calls `https://api.typesafe.ai/v1/systemone` directly from the extension with one `choice` question per bookmark and reads back the choice, confidence and probabilities; folder reads and bookmark moves go through X's API. Integration evidence: [`src/jev.js`](https://github.com/peterrauscher/BookmarX/blob/98d48b50a5bf11267664238cd65b726f7f9a0c0c/src/jev.js).

## Get started

Load the folder as an unpacked extension, then add your keys in Settings.

```sh
git clone https://github.com/peterrauscher/BookmarX
# chrome://extensions -> Developer mode -> Load unpacked -> select the folder
# open BookmarX Settings: paste your TypeSafe key and X client ID
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video: [github.com/user-attachments/assets/887ea380-d825-4917-bd28-f7c348640635](https://github.com/user-attachments/assets/887ea380-d825-4917-bd28-f7c348640635)
- README: [github.com/peterrauscher/BookmarX/blob/98d48b50a5bf11267664238cd65b726f7f9a0c0c/README.md](https://github.com/peterrauscher/BookmarX/blob/98d48b50a5bf11267664238cd65b726f7f9a0c0c/README.md)

## Limits and data handling

Bookmark text, author information and URLs are sent to TypeSafe for classification; keys and OAuth tokens are stored in the browser's extension storage. There is no server of its own.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 98d48b50a5bf](https://github.com/peterrauscher/BookmarX/tree/98d48b50a5bf11267664238cd65b726f7f9a0c0c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
