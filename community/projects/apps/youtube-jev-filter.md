# YouTube Jev Filter (Chrome extension that hides clickbait, hype and Shorts on YouTube using Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 Chrome extension: for each video card it sends the title, channel, length and description to Jev with three questions (clickbait yes/no, hype yes/no, substance score 0-3) and hides or dims the video when a threshold is crossed, with soft, normal and strict modes. Shorts are removed. Answers are cached per video ID; the README estimates about 3 cents per 1,000 videos. README in Russian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Vlad0n1m/youtube-jev-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Vlad0n1m/youtube-jev-filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; bring your own TypeSafe key (README estimates about 3 cents per 1,000 videos). Checked 2026-10-30. |
| Jev evidence | [`background.js`](https://github.com/Vlad0n1m/youtube-jev-filter/blob/856e531bfb1212e1956e7f33df9771a52b452ce7/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Vlad0n1m](https://github.com/Vlad0n1m). Independently curated. |
| Format | Chrome extension (unpacked) |
| Platform and availability | Desktop Chrome; load unpacked from the cloned repo (no Chrome Web Store listing verified). |
| Jev's role | Scores each video card for clickbait, hype and substance so the extension can hide or dim it. |
| Requirements | Desktop Chrome and a TypeSafe API key. |
| License | [MIT](https://github.com/Vlad0n1m/youtube-jev-filter/blob/856e531bfb1212e1956e7f33df9771a52b452ce7/LICENSE) |

## When to use

- Strip clickbait and low-substance videos from YouTube feeds when you go there to learn.
- Mismatch: not in the Chrome Web Store; video metadata is sent to TypeSafe.

## How it works

`background.js` queues requests (4 in parallel) to `api.typesafe.ai/v1/systemone` with `jev-latest`, retries on 429/5xx and caches answers; `content.js` applies the thresholds from `shared.js` to each card. Integration evidence: [`background.js`](https://github.com/Vlad0n1m/youtube-jev-filter/blob/856e531bfb1212e1956e7f33df9771a52b452ce7/background.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Vlad0n1m/youtube-jev-filter
# chrome://extensions -> Developer mode -> Load unpacked -> select the folder; paste your TypeSafe key in the popup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Eval cases: [github.com/Vlad0n1m/youtube-jev-filter/blob/856e531bfb1212e1956e7f33df9771a52b452ce7/scripts/cases.json](https://github.com/Vlad0n1m/youtube-jev-filter/blob/856e531bfb1212e1956e7f33df9771a52b452ce7/scripts/cases.json)

## Limits and data handling

Titles, channel names and descriptions of videos on the page are sent to TypeSafe; the key is kept in `chrome.storage.local`. Not affiliated with YouTube or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 856e531bfb12](https://github.com/Vlad0n1m/youtube-jev-filter/tree/856e531bfb1212e1956e7f33df9771a52b452ce7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
