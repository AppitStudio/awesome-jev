# YouTube AI Video Filter by Hoàng Thành Tiến (Chrome and Edge extension that blurs YouTube videos whose titles Jev says match your blocking prompt)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Write a natural-language rule such as "block AI slop, brain rot and bad stock market news" and the extension checks YouTube titles against it. Matching videos are blurred, title and thumbnail, rather than removed, with a badge showing Jev's probability and a click-to-peek toggle; results are cached per rule and title.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tim-polodev/yt-ai-filter) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/tim-polodev/yt-ai-filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build, loaded unpacked; you supply a Command Code API key, and Jev calls are billed to that account. No license file, so reuse terms are not granted. Checked 2026-11-23. |
| Jev evidence | [`background/service-worker.js`](https://github.com/tim-polodev/yt-ai-filter/blob/3fe62751897e440763599c7e541053eaf0eb282b/background/service-worker.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tim-polodev](https://github.com/tim-polodev). Independently curated. |
| Format | Browser extension (Manifest V3, JavaScript) |
| Platform and availability | Chrome and Edge (Manifest V3), loaded unpacked; not on a store. |
| Jev's role | Jev answers one Noul question per video title in a batch ("should this video be blocked based strictly on the rule?"); the extension blurs titles above its threshold. |
| Requirements | Chrome or Edge; Node.js to build with a pre-filled key (or set the key in the popup); a Command Code API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Filter a YouTube feed by your own rule without removing videos you might still want to peek at.
- Mismatch: thumbnails or video content; only titles are judged.

## How it works

`background/service-worker.js` posts the rule and titles to the configured base URL's `/systemone` endpoint (default Command Code, model `typesafe/jev` or pinned `typesafe/jev-1.14.0`). Integration evidence: [`background/service-worker.js`](https://github.com/tim-polodev/yt-ai-filter/blob/3fe62751897e440763599c7e541053eaf0eb282b/background/service-worker.js).

## Get started

Build it (or skip the build and set the key in the popup), then load it unpacked.

```sh
git clone https://github.com/tim-polodev/yt-ai-filter && cd yt-ai-filter
cp .env.example .env   # CMD_API_KEY=...
npm run build          # then load dist/ in chrome://extensions (Developer mode)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tim-polodev/yt-ai-filter/blob/3fe62751897e440763599c7e541053eaf0eb282b/README.md](https://github.com/tim-polodev/yt-ai-filter/blob/3fe62751897e440763599c7e541053eaf0eb282b/README.md)

## Limits and data handling

Video titles and your rule are sent to Command Code (or the configured provider). No license file. Not an official TypeSafe or YouTube product.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 3fe62751897e](https://github.com/tim-polodev/yt-ai-filter/tree/3fe62751897e440763599c7e541053eaf0eb282b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
