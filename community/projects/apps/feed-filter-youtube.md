# Feed Filter (Chrome extension that blurs YouTube feed cards until Jev checks each video against goals you write)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Desktop Chrome extension for YouTube's home feed and watch sidebar: every card stays blurred until Jev has checked the video against your goals. Clearly on-goal videos get an ON GOAL badge, clearly off-goal ones are filtered out, and the rest show normally; any filtered card can be revealed with the reason or kept/hidden by hand. A dashboard shows what got through by goal and over time, and a daily call limit guards spending. An optional local Python proxy keeps the key out of the browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ranawaqas-ai/feed-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ranawaqas-ai/feed-filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); not in the Chrome Web Store. You pay TypeSafe for your own calls (a long evening with three goals can use a few thousand calls, per the maker). Checked 2026-11-16. |
| Jev evidence | [`extension/src/direct.js`](https://github.com/ranawaqas-ai/feed-filter/blob/fd0583c5a82cf8decd900606aeeb73ca82a40824/extension/src/direct.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ranawaqas-ai](https://github.com/ranawaqas-ai). Independently curated. |
| Format | Chrome extension (unpacked, JavaScript) with optional Python proxy (MIT) |
| Platform and availability | Desktop Chrome (unpacked Manifest V3 extension; YouTube home feed and watch sidebar) |
| Jev's role | Jev scores each recommended video against your written goals before the card is shown. |
| Requirements | Desktop Chrome (load unpacked) and your own TypeSafe API key; uv for the optional proxy. |
| License | [MIT](https://github.com/ranawaqas-ai/feed-filter/blob/fd0583c5a82cf8decd900606aeeb73ca82a40824/LICENSE) |

## When to use

- Keep YouTube recommendations aligned with what you actually want to watch.
- Mismatch: mobile or non-Chrome browsers; desktop Chrome only.

## How it works

`extension/src/direct.js` posts each video's details and your goal text to `https://api.typesafe.ai/v1/systemone` as a Noul question, with a 30-day cache, a daily cap and retries; `proxy/prompt.py` pins the evaluated request (`jev-1.14.0`). Integration evidence: [`extension/src/direct.js`](https://github.com/ranawaqas-ai/feed-filter/blob/fd0583c5a82cf8decd900606aeeb73ca82a40824/extension/src/direct.js).

## Get started

Load the extension folder unpacked; the setup page asks for your Jev key, goals and a daily call limit.

```sh
git clone https://github.com/ranawaqas-ai/feed-filter
# chrome://extensions -> Developer mode -> Load unpacked -> select feed-filter/extension
# optional local proxy: cp .env.example .env && uv run python -m proxy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ranawaqas-ai/feed-filter/blob/fd0583c5a82cf8decd900606aeeb73ca82a40824/README.md](https://github.com/ranawaqas-ai/feed-filter/blob/fd0583c5a82cf8decd900606aeeb73ca82a40824/README.md)

## Limits and data handling

For each video, title, channel, length, view count and Short status plus your goal text go to TypeSafe on your key; no cookies or watch history. The key sits in extension storage unless you use the local proxy. TypeSafe has no per-key spend limit, so set the daily cap.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit fd0583c5a82c](https://github.com/ranawaqas-ai/feed-filter/tree/fd0583c5a82cf8decd900606aeeb73ca82a40824). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
