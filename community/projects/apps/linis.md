# Linis (Chromium extension that captures loaded page evidence, asks Jev which blocks are useful for your goal, and exports the originals)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 extension for Chrome and Brave: on click it collects the loaded page's blocks (text, headings, links, image descriptions) by snapshot or scroll capture, asks Jev which blocks fit your extraction goal, and lets you review the result and save Markdown, text or full JSON with the original evidence. No local server or build step. Works with your own TypeSafe key or through OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TheFindingPath/linis) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/TheFindingPath/linis#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (Apache-2.0); not in a browser store. You pay TypeSafe or OpenRouter for your own calls. Checked 2026-11-15. |
| Jev evidence | [`browsers/brave/extension/lib/jev.js`](https://github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/browsers/brave/extension/lib/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [TheFindingPath](https://github.com/TheFindingPath). Independently curated. |
| Format | Chromium extension (unpacked, JavaScript, Apache-2.0) |
| Platform and availability | Chrome and Brave (unpacked Manifest V3 extension; release ZIP buildable locally) |
| Jev's role | Jev decides which captured page blocks are useful evidence for your stated goal. |
| Requirements | Chrome or Brave (load unpacked) and your own TypeSafe or OpenRouter key. |
| License | [Apache-2.0 (owner code also offered under 0BSD)](https://github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/LICENSE) |

## When to use

- Pull the useful parts of long pages into a reviewable, exportable evidence file.
- Mismatch: sensitive pages; captured text, URLs and links go to the provider.

## How it works

`browsers/brave/extension/lib/settings.js` defines the TypeSafe provider (`https://api.typesafe.ai/v1/systemone`, `jev-latest`) and the OpenRouter decisions endpoint; `lib/jev.js` batches page blocks into Choice questions and validates each answer. Integration evidence: [`browsers/brave/extension/lib/jev.js`](https://github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/browsers/brave/extension/lib/jev.js).

## Get started

Load the extension folder unpacked, pick a provider and key in Settings, then extract a page.

```sh
git clone https://github.com/TheFindingPath/linis
# brave://extensions or chrome://extensions -> Developer mode -> Load unpacked
# select browsers/brave/extension, then add your key in Settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/README.md](https://github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/README.md)
- Privacy and permissions: [github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/PRIVACY.md](https://github.com/TheFindingPath/linis/blob/95d8c09e8bfa2eadb1390156e2d10105db37f821/PRIVACY.md)

## Limits and data handling

On each extraction, page blocks, title, URL, links and your goal go only to the provider you chose (TypeSafe or OpenRouter) with your key; automatic saving is on by default. Read the project's PRIVACY.md before use. Not a signed store release.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 95d8c09e8bfa](https://github.com/TheFindingPath/linis/tree/95d8c09e8bfa2eadb1390156e2d10105db37f821). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
