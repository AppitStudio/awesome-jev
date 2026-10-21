# x-stamp (Jev labels for X posts)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome extension that stamps each X post as it scrolls into view with what it is for (news, hot take, builder ad, engagement bait and more) and what it is about, using Jev to pick the type and quote the post's own words.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/parker-brown-family/x-stamp) |
| Maintainer | [parker-brown-family](https://github.com/parker-brown-family). Independently curated. |
| Format | Chrome extension (unpacked, no build) |
| Requirements | Chrome or another Chromium browser; an OpenRouter key (Jev is called through OpenRouter, about $0.12 per thousand posts per the README). |
| License | [MIT](https://github.com/parker-brown-family/x-stamp/blob/5347295ee14f42d455918b0c05668c330cd85d18/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extension/lib/jev.js`](https://github.com/parker-brown-family/x-stamp/blob/5347295ee14f42d455918b0c05668c330cd85d18/extension/lib/jev.js) at the pinned commit. |

## When to use

- See at a glance which posts are news, opinion, self-promotion or engagement farming.
- Filter your feed by intent without reading every post.
- Mismatch: X only, and it calls Jev through OpenRouter rather than TypeSafe directly.

## How it works

`extension/lib/jev.js` sends each post's text to OpenRouter's `/v1/systemone` endpoint with typed questions; the stamp colour comes from the chosen type and the quoted phrase is picked from the post, never written. Integration evidence: [`extension/lib/jev.js`](https://github.com/parker-brown-family/x-stamp/blob/5347295ee14f42d455918b0c05668c330cd85d18/extension/lib/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/parker-brown-family/x-stamp.git
# chrome://extensions > Developer mode > Load unpacked > choose the extension/ folder
# paste your OpenRouter key in the options page
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Stamp types table in the README: [github.com/parker-brown-family/x-stamp#readme](https://github.com/parker-brown-family/x-stamp#readme)
- Agent install notes: [github.com/parker-brown-family/x-stamp/blob/main/AGENTS.md](https://github.com/parker-brown-family/x-stamp/blob/main/AGENTS.md)

## Limits and data handling

Post text is sent to OpenRouter for labelling. Not affiliated with X or TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 5347295ee14f](https://github.com/parker-brown-family/x-stamp/tree/5347295ee14f42d455918b0c05668c330cd85d18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
