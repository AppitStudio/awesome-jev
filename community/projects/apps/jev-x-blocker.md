# Jev X Blocker (Chrome extension that hides high-confidence porn and spam on X with your own Jev key)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Local-first Chrome extension that uses your own TypeSafe key to cover high-confidence pornographic, sexually suggestive and porn-funnel posts and replies on X with restorable placeholders, across timelines, search, profiles and threads; a refactor and extension of bugkiwi's elons-job; Chinese documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bit-cook/Jev-X-Blocker) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/bit-cook/Jev-X-Blocker#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free download from GitHub Releases. Jev calls are billed to your TypeSafe account. Without a key nothing is hidden. Checked 2026-10-26. |
| Jev evidence | [`src/shared/core.js`](https://github.com/bit-cook/Jev-X-Blocker/blob/4eee4cc4c69cc590558753f9817e02bb3dcce1cb/src/shared/core.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [bit-cook](https://github.com/bit-cook). Independently curated. |
| Format | Chrome Manifest V3 extension (JavaScript) |
| Platform and availability | Chrome and Edge (unpacked from the v1.0.0 release zip); not on the Chrome Web Store at review time. |
| Jev's role | Content judge: the username and post or reply text go to Jev, and items above the confidence threshold are hidden behind a placeholder. |
| Requirements | Chrome or Edge; a TypeSafe API key. |
| License | [MIT](https://github.com/bit-cook/Jev-X-Blocker/blob/4eee4cc4c69cc590558753f9817e02bb3dcce1cb/LICENSE) |

## When to use

- Clean NSFW spam out of X timelines and replies.
- Keep everything restorable rather than deleted.
- Mismatch: only covers this kind of content; TypeSafe is unavailable in some regions (HTTP 451), in which case nothing is hidden.

## How it works

`src/shared/core.js` posts the combined username and text to `https://api.typesafe.ai/v1/systemone` with `jev-latest` and applies the extension's rules to the answer. Integration evidence: [`src/shared/core.js`](https://github.com/bit-cook/Jev-X-Blocker/blob/4eee4cc4c69cc590558753f9817e02bb3dcce1cb/src/shared/core.js).

## Get started

From the upstream README (not run on the review host):

```sh
# download Jev-X-Blocker-v1.0.0.zip from Releases, unzip, then
# chrome://extensions → Developer mode → Load unpacked → pick the folder; paste your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Release v1.0.0: [github.com/bit-cook/Jev-X-Blocker/releases/tag/v1.0.0](https://github.com/bit-cook/Jev-X-Blocker/releases/tag/v1.0.0)
- README: [github.com/bit-cook/Jev-X-Blocker#readme](https://github.com/bit-cook/Jev-X-Blocker#readme)

## Limits and data handling

Usernames and post or reply text are sent to TypeSafe with your key. Derived from bugkiwi/elons-job (MIT).

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 4eee4cc4c69c](https://github.com/bit-cook/Jev-X-Blocker/tree/4eee4cc4c69cc590558753f9817e02bb3dcce1cb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
