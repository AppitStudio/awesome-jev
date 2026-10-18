# SearchJev

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Firefox extension (Japanese UI) that asks Jev six questions about each Google result, then shows 0 to 100 scores and reorders the page to push mass-produced SEO and affiliate articles down and first-hand sources up; one click restores Google's order.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mita-pixels/searchjev) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://addons.mozilla.org/ja/firefox/addon/searchjev/) |
| Pricing and access | Free add-on (MIT); you pay your own TypeSafe usage. Checked 2026-10-18. |
| Jev evidence | [`extension/background.js`](https://github.com/mita-pixels/searchjev/blob/ae68e51afd993f59df9f63e709d9b4a27b5840ac/extension/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [mita-pixels](https://github.com/mita-pixels). Independently curated. |
| Format | Firefox extension (desktop and Android), published on addons.mozilla.org |
| Platform and availability | Firefox desktop and Android |
| Jev's role | Jev answers six typed questions per search result; the extension weights the answers into a score and reorders the page. |
| Requirements | Firefox; your own TypeSafe API key (the author estimates about 0.2 yen per search). |
| License | [MIT](https://github.com/mita-pixels/searchjev/blob/ae68e51afd993f59df9f63e709d9b4a27b5840ac/LICENSE) |

## When to use

- Get fewer SEO farm and affiliate pages at the top of Japanese Google searches.
- Tune weights for mass production, first-hand information, commercial intent and relevance, and preview them on your last search.
- Mismatch: tuned on Japanese queries; Google-only, and results Jev is unsure about are shown faded with a question mark.

## How it works

`background.js` sends each result's title, snippet, domain and path to `api.typesafe.ai/v1/systemone` with six questions in one call, in parallel per result; `defaults.js` turns the answers into a weighted overall score. An optional mode reads the article text only for results whose relevance was unclear. On 289 hand-labelled results the author reports AUC 0.80 against 0.76 for Google's own order. Integration evidence: [`extension/background.js`](https://github.com/mita-pixels/searchjev/blob/ae68e51afd993f59df9f63e709d9b4a27b5840ac/extension/background.js).

## Get started

From the upstream README (not run on the review host):

```sh
# Install from addons.mozilla.org, then paste your TypeSafe key in the options page.
npx web-ext@8 lint -s extension   # lint the source build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Firefox add-on page: [addons.mozilla.org/ja/firefox/addon/searchjev/](https://addons.mozilla.org/ja/firefox/addon/searchjev/)
- Privacy policy: `store/privacy-policy.md`.

## Limits and data handling

Search terms and result titles, snippets and URLs go to TypeSafe on your key; with the read-article mode on, about 2,500 characters of the page are sent too. The key and settings stay in the browser.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit ae68e51afd99](https://github.com/mita-pixels/searchjev/tree/ae68e51afd993f59df9f63e709d9b4a27b5840ac). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
