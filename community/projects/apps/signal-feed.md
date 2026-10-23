# Signal Feed (X and YouTube bait filter with Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chromium extension that folds ragebait, empty hype and engagement bait on the X timeline and YouTube before you scroll to them, each with the reason, highlights posts on topics you choose, and shows what the Jev calls cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/harish-anumula/signal-feed) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/harish-anumula/signal-feed#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free to load. Jev usage is billed to your OpenRouter key; the author measured about $0.02 per 1,000 posts on 2026-10-23. Checked 2026-10-23. |
| Jev evidence | [`extension/src/core.js`](https://github.com/harish-anumula/signal-feed/blob/8a93bf92869594146769b4604292febeaa2c959f/extension/src/core.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [harish-anumula](https://github.com/harish-anumula). Independently curated. |
| Format | Chromium extension (JavaScript) |
| Platform and availability | Chromium browsers, loaded unpacked from source or a release zip; Chrome Web Store listing announced as coming soon. |
| Jev's role | Jev answers one yes-or-no question per post (hide under your list?) plus one for highlights, in batches ahead of your scroll. |
| Requirements | Chrome, Edge, Brave or another Chromium browser; an OpenRouter API key. |
| License | [MIT](https://github.com/harish-anumula/signal-feed/blob/8a93bf92869594146769b4604292febeaa2c959f/LICENSE) |

## When to use

- Hide engagement bait on X and YouTube without blocking people.
- See the reason for every folded post and undo in one click.
- Mismatch: needs an OpenRouter key; it fails open when the key runs out.

## How it works

`extension/src/core.js` sends batches of posts to OpenRouter's decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with model `typesafe/jev-1.13` and caches answers for the browser session. Integration evidence: [`extension/src/core.js`](https://github.com/harish-anumula/signal-feed/blob/8a93bf92869594146769b4604292febeaa2c959f/extension/src/core.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Calibration eval and method: [github.com/harish-anumula/signal-feed/blob/main/eval/README.md](https://github.com/harish-anumula/signal-feed/blob/main/eval/README.md)

## Limits and data handling

Post text from your feed is sent to OpenRouter and TypeSafe; accuracy figures are the author's own on their feed.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 8a93bf928695](https://github.com/harish-anumula/signal-feed/tree/8a93bf92869594146769b4604292febeaa2c959f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
