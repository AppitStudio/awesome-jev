# Tube Focus Mode

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that filters YouTube down to your channels, playlists and chosen topics: Jev scores each other video against your focus topics, and off-topic videos are blurred or blocked.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/OriolSegarra/tube-focus-mode) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/OriolSegarra/tube-focus-mode#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`src/lib/typesafe.ts`](https://github.com/OriolSegarra/tube-focus-mode/blob/85e4e9fd94dc3b24619a7ed939970b2bdb2c3f39/src/lib/typesafe.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [OriolSegarra](https://github.com/OriolSegarra). Independently curated. |
| Format | Chrome extension (Manifest V3, TypeScript) |
| Platform and availability | Chrome and Chromium browsers (unpacked source build) |
| Jev's role | Jev decides whether each non-allowlisted video matches your focus topics. |
| Requirements | Chrome/Chromium browser, Node.js 18+ to build, your own TypeSafe key. |
| License | [MIT](https://github.com/OriolSegarra/tube-focus-mode/blob/85e4e9fd94dc3b24619a7ed939970b2bdb2c3f39/LICENSE) |

## When to use

- Keep YouTube for tutorials or focus music without the recommendation rabbit hole.
- Set locked work hours when focus mode cannot be switched off.
- Mismatch: not on the Chrome Web Store yet; load unpacked from source.

## How it works

Pinned videos and allowed channels pass locally; everything else is asked to Jev (pinned to `jev-1.14.0`) as a yes/no question against your plain-language topics. The probability is cached per video and compared with your slider threshold. Integration evidence: [`src/lib/typesafe.ts`](https://github.com/OriolSegarra/tube-focus-mode/blob/85e4e9fd94dc3b24619a7ed939970b2bdb2c3f39/src/lib/typesafe.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/OriolSegarra/tube-focus-mode.git
cd tube-focus-mode
npm install
npm run build   # then Load unpacked -> dist
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshots in the upstream `screenshots/` folder.

## Limits and data handling

Video titles/metadata for non-allowlisted videos go to TypeSafe from your browser with your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 85e4e9fd94dc](https://github.com/OriolSegarra/tube-focus-mode/tree/85e4e9fd94dc3b24619a7ed939970b2bdb2c3f39). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
