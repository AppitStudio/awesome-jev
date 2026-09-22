# LinkedIn Slop Filter

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension plus local Node proxy that stamps LinkedIn feed posts **Bait**, **Corp**, **Brag**, or **Slop** using TypeSafe Jev noul/choice judgments. Distinct from [Slop Mop](slop-mop.md) (multi-question writing scores + fold/highlight) and [JevSlop](jevslop.md) (note/article scoring).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter#slop-filter-for-linkedin) |
| Pricing and access | [Clone and load unpacked](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter#run-it); no app purchase fee. Bring a TypeSafe API key in the local `server/` `.env`. Inference usage can incur charges. Not on the Chrome Web Store (by design—key stays on localhost). Checked **2026-09-22**. |
| Jev evidence | [`server/jev.js`](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter/blob/de45793d610d4c72bc8f17f8c6a9bee0841e4e69/server/jev.js) POSTs `{state, model: jev-latest, questions}` to `https://api.typesafe.ai/v1/systemone` with two noul questions (`is_slop`, `is_corporate_slop`) and one choice (`category`); stamp label thresholds are in the same file. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; Chrome install and live LinkedIn/Jev not tested on the review host (`test/run.sh` needs a live key). |
| Maintainer | [Arpit-Khandelwal](https://github.com/Arpit-Khandelwal). Independently curated. |
| Format | Manifest V3 Chromium extension + local Node **≥ 20** proxy (`jev-slop-filter-server` **0.1.0**). |
| Platform and availability | Desktop Chromium / LinkedIn feed. Load `extension/` unpacked; run `server/` on `127.0.0.1:8787`. |
| Jev's role | Judges each visible post’s text; extension paints a rubber-stamp overlay with confidence. Application code maps scores to Bait/Corp/Brag/Slop. |
| Requirements | Chromium; Node 20+ for the local proxy; `TYPESAFE_API_KEY` (or documented env) in server `.env`. |
| License | [MIT](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter/blob/de45793d610d4c72bc8f17f8c6a9bee0841e4e69/LICENSE). |

## When to use

Use it for personal LinkedIn browsing when you want a visible stamp taxonomy on engagement-bait / corporate / brag posts rather than fold-or-highlight scoring. Prefer [Slop Mop](slop-mop.md) for hosted/self-host writing-quality checks with overrides, or [Polymorph](polymorph.md) for custom English collapse rules on other sites. Do not treat stamps as authorship detection or LinkedIn policy enforcement.

## How it works

1. The content script observes posts entering the viewport and asks the local proxy to judge the post text.
2. [`server/jev.js`](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter/blob/de45793d610d4c72bc8f17f8c6a9bee0841e4e69/server/jev.js) calls TypeSafe System One; the API key never ships in the extension bundle.
3. Thresholds map corporate noul / humblebrag / slop noul into stamp faces; the overlay keeps the post readable underneath.

## Get started

```sh
git clone https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter.git
cd jev-linkedin-slop-filter
git checkout de45793d610d4c72bc8f17f8c6a9bee0841e4e69
cp .env.example .env   # add TypeSafe key
cd server && npm start # http://127.0.0.1:8787
```

Load `extension/` unpacked at `chrome://extensions`, open LinkedIn feed, scroll. Live runs send post text to TypeSafe and can incur charges.

## Examples and demos

- Upstream `docs/demo.gif` shows live stamping.
- `test/run.sh` hits the live System One API with sample posts (not run without a key on the review host).

## Limits and data handling

Post text leaves the machine via the localhost proxy to `api.typesafe.ai`. The key stays in server env, not the extension. No Chrome Web Store distribution. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit de45793](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter/tree/de45793d610d4c72bc8f17f8c6a9bee0841e4e69): MIT. AI-assisted review of README, LICENSE, `server/jev.js`, extension files. No Chrome/live TypeSafe session.

Related: [Slop Mop](slop-mop.md), [Polymorph](polymorph.md), [JevSlop](jevslop.md), [ScrollPatrol](scrollpatrol.md).
