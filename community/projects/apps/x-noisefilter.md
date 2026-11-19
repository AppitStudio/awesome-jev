# Noisefilter for X by tpa339 (Chrome extension that collapses low-substance and engagement-bait posts, rated by Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension (Manifest V3) that rates every post in your X timeline, search, lists and profiles with two Jev yes/no questions: does it say something concrete, and is it mainly built for reaction (rage bait, clickbait). Posts that fail are collapsed, not hidden. An optional switch rates replies under an open post for relevance and substance. Near-duplicate texts and emoji-only replies are caught locally without a call, up to 10 posts go in one request, and your last few manual markings are sent as examples. UI and docs are in German.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tpa339/x-noisefilter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/tpa339/x-noisefilter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you pay OpenRouter for the Jev calls on your own key. Checked 2026-11-19. |
| Jev evidence | [`extension/background.js`](https://github.com/tpa339/x-noisefilter/blob/467439edf7acbc24142aa695d55a86a498d278b7/extension/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tpa339](https://github.com/tpa339). Independently curated. |
| Format | Chrome extension (JavaScript) |
| Platform and availability | Chrome (desktop), loaded as an unpacked extension. |
| Jev's role | Answers two `noul` questions per post (substance, bait) and two per reply (relevance, substance); the extension collapses posts by fixed thresholds. |
| Requirements | Chrome with developer mode and an OpenRouter API key. |
| License | [MIT](https://github.com/tpa339/x-noisefilter/blob/467439edf7acbc24142aa695d55a86a498d278b7/LICENSE) |

## When to use

- Read X with low-substance and bait posts folded away, judged per post rather than by keyword.
- Mismatch: an X client or a store-published extension; it is loaded unpacked.

## How it works

`extension/background.js` posts batched `noul` questions with model `typesafe/jev-1.14` to OpenRouter's `/api/alpha/decisions` endpoint, including your recent markings as examples. Integration evidence: [`extension/background.js`](https://github.com/tpa339/x-noisefilter/blob/467439edf7acbc24142aa695d55a86a498d278b7/extension/background.js).

## Get started

Load the `extension/` folder as an unpacked extension and add your OpenRouter key on the options page.

```sh
git clone https://github.com/tpa339/x-noisefilter
# chrome://extensions → Developer mode → Load unpacked → x-noisefilter/extension
# then open the extension options and paste your OpenRouter key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tpa339/x-noisefilter/blob/467439edf7acbc24142aa695d55a86a498d278b7/README.md](https://github.com/tpa339/x-noisefilter/blob/467439edf7acbc24142aa695d55a86a498d278b7/README.md)

## Limits and data handling

The text of posts you scroll past (and quoted posts) is sent to OpenRouter and TypeSafe. Image-only and video-only posts are not rated. Thresholds are the author's choices.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 467439edf7ac](https://github.com/tpa339/x-noisefilter/tree/467439edf7acbc24142aa695d55a86a498d278b7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
