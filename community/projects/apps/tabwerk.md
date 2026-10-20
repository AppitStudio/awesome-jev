# Tabwerk

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

German-language Chrome extension for people with many tabs: quick search, groups, sorting, duplicates, page watchers and full history, where exact work is done in code and optional Jev calls answer the semantic questions (find a tab by description, suggest groups, rank priority, judge watcher conditions).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DigitalIQ/tabwerk) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://chromewebstore.google.com/detail/tabwerk/jimalfhplojokembebogjlplobgoobdg) |
| Pricing and access | Free MIT extension; Jev calls are billed to your own OpenRouter or TypeSafe key. Checked 2026-10-21. |
| Jev evidence | [`src/lib/jev.js`](https://github.com/DigitalIQ/tabwerk/blob/c42d03b64ffa4ee81e57c39aed8221239f1ad052/src/lib/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [DigitalIQ](https://github.com/DigitalIQ). Independently curated. |
| Format | Chrome extension (JavaScript, Manifest V3) |
| Platform and availability | Chrome Web Store; interface in German. |
| Jev's role | Optional: Jev handles the semantic features (find, group, prioritise, duplicate content, watchers); everything else works without it. |
| Requirements | Chrome; optional Jev access through OpenRouter or TypeSafe (your own key). |
| License | [MIT](https://github.com/DigitalIQ/tabwerk/blob/c42d03b64ffa4ee81e57c39aed8221239f1ad052/LICENSE) |

## When to use

- Find a tab by describing it in your own words.
- Get group and clean-up suggestions with a confidence per tab.
- Mismatch: the interface is German.

## How it works

`src/lib/jev.js` sends tab titles, addresses or page excerpts with Choice, Score or Noul questions to Jev through OpenRouter or TypeSafe, depending on your setting; searching, sorting, deduplication by address, history and sessions run locally in code. Integration evidence: [`src/lib/jev.js`](https://github.com/DigitalIQ/tabwerk/blob/c42d03b64ffa4ee81e57c39aed8221239f1ad052/src/lib/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
# Install from the Chrome Web Store, then add an OpenRouter or TypeSafe key in the settings to enable Jev features
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Feature table in the README: [github.com/DigitalIQ/tabwerk#readme](https://github.com/DigitalIQ/tabwerk#readme)

## Limits and data handling

With Jev enabled, tab titles, addresses or page excerpts are sent to OpenRouter or TypeSafe. Without a key, only the code-based features run.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit c42d03b64ffa](https://github.com/DigitalIQ/tabwerk/tree/c42d03b64ffa4ee81e57c39aed8221239f1ad052). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
