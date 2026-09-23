# Jev Kitchen

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free public web demo: name a dish or cocktail and watch ingredient stickers rise; TypeSafe Jev judges which stickers belong.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://jev-kitchen.vercel.app) |
| Tags | `Closed source` · `Free` |
| Product homepage | [jev-kitchen.vercel.app](https://jev-kitchen.vercel.app) |
| Pricing and access | Free public demo with no signup required (`/recipe`, `/cocktail`). No pricing page; hosted on Vercel. Checked **2026-09-23**. Provider costs (if any) are on the operator, not the visitor. |
| Jev evidence | Product copy on [jev-kitchen.vercel.app/recipe](https://jev-kitchen.vercel.app/recipe) states ingredients are “Judged by Jev, a small AI model from TypeSafe.” Maker [issue #399](https://github.com/AppitStudio/awesome-jev/issues/399) and X posts ([main](https://x.com/nelsonpatrao/status/2102780634103939560), [video](https://x.com/nelsonpatrao/status/2102788177257722316)) describe the same. Implementation was **not** inspected (no public source repo); live sticker judgments were **not** instrumented on the review host. |
| Disclosure | Closed source. The implementation was not inspected; Jev use is a maker claim from issue #399, the live product copy, and X posts, not independently observed API traffic. Independently curated; maker is @nelsonpatrao. Listing is not an endorsement. |
| Maintainer | [Nelson (@nelsonpatrao)](https://x.com/nelsonpatrao). Self-submitted via Awesome Jev issue #399. |
| Format | Hosted web app (Vercel). |
| Platform and availability | Public web: [recipe](https://jev-kitchen.vercel.app/recipe), [cocktail](https://jev-kitchen.vercel.app/cocktail). |
| Jev's role | Maker claim: Jev judges which sticker ingredients match a named dish or cocktail for the search UI. |
| Requirements | Modern browser. No account. |
| License | Proprietary hosted demo; no public open-source license linked from the submission. |

## When to use

Use it as a playful demo of typed judgment over a large sticker vocabulary. Prefer searchable developer tools when you need reusable Jev integration code.

## How it works

The public `/recipe` and `/cocktail` pages present a sticker pile UI. Maker materials describe Jev deciding membership of ingredients for a named dish/cocktail. Backend prompts and TypeSafe calls were not inspected.

## Get started

1. Open [jev-kitchen.vercel.app/recipe](https://jev-kitchen.vercel.app/recipe) or [/cocktail](https://jev-kitchen.vercel.app/cocktail).
2. Name a dish or cocktail and observe which stickers rise.
3. Optional maker demos on X: [main post](https://x.com/nelsonpatrao/status/2102780634103939560), [video](https://x.com/nelsonpatrao/status/2102788177257722316).

No account creation was performed during review; homepage and `/recipe` returned HTTP 200.

## Examples and demos

- Live site paths above.
- Maker X posts with demo video (not independently re-recorded).

## Limits and data handling

Closed source: questions, thresholds, and API traffic were not inspected. Assume dish/cocktail names and related UI state may be sent to the hosting backend and any AI providers it uses. No public LICENSE.

## Review and maintenance

Reviewed **2026-09-23** (Europe/Sofia). Primary sources: live site HTTP 200, community issue #399, maker X posts. No public GitHub source in the submission. AI-assisted review; no live TypeSafe key used by the curator.

Related: [Shapeshift](shapeshift.md).
