# XPostFilterPlus (Chrome extension that hides X posts by keyword or by Jev classification)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Unofficial Chrome extension that hides X posts using keyword rules with case, accent and symbol normalisation, plus optional semantic exclusion conditions judged by Jev, OpenAI Decisions or Cloudflare Clef with your own key; settings open over the X page and a chip counts hidden posts; Japanese and English documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doraTeX/XPostFilterPlus) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/doraTeX/XPostFilterPlus#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. AI classification is billed by the provider you choose. Checked 2026-10-27. |
| Jev evidence | [`src/shared/ai.js`](https://github.com/doraTeX/XPostFilterPlus/blob/683df2fbe3df15e574d0caa39ab7f66b8106bf45/src/shared/ai.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [doraTeX](https://github.com/doraTeX). Independently curated. |
| Format | Chrome extension (load unpacked) |
| Platform and availability | Chrome (load unpacked from the dist folder); not in the Chrome Web Store at review time. |
| Jev's role | Optional semantic filter: each post is checked against your exclusion conditions, one of three selectable providers. |
| Requirements | Chrome; for AI classification, a TypeSafe API key (or an OpenAI or Cloudflare account). |
| License | [MIT](https://github.com/doraTeX/XPostFilterPlus/blob/683df2fbe3df15e574d0caa39ab7f66b8106bf45/LICENSE) |

## When to use

- Hide X posts by meaning, not just keywords.
- Mismatch: version 0.1.0, load-unpacked install; distinct from the separately listed Jev X Blocker and x-post filters.

## How it works

`src/shared/ai.js` posts the post text and your conditions to `https://api.typesafe.ai/v1/systemone` with default `jev-1.13.0` when Jev is the selected provider. Integration evidence: [`src/shared/ai.js`](https://github.com/doraTeX/XPostFilterPlus/blob/683df2fbe3df15e574d0caa39ab7f66b8106bf45/src/shared/ai.js).

## Get started

From the upstream README (not run on the review host):

```sh
# build or use the dist folder, then chrome://extensions → Developer mode → Load unpacked → dist
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/doraTeX/XPostFilterPlus#readme](https://github.com/doraTeX/XPostFilterPlus#readme)

## Limits and data handling

With AI classification on, post text goes to the selected provider. Not affiliated with X Corp.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 683df2fbe3df](https://github.com/doraTeX/XPostFilterPlus/tree/683df2fbe3df15e574d0caa39ab7f66b8106bf45). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
