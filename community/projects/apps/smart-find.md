# Smart Find

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that works like Ctrl+F for questions: ask a page a question and TypeSafe Jev scores page passages so the answers are highlighted.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eduardoalba00/smart-find) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/eduardoalba00/smart-find#readme](https://github.com/eduardoalba00/smart-find#readme) |
| Pricing and access | Free MIT extension; each search is billed to your TypeSafe key (upstream reports US$0.0005–0.007). |
| Jev evidence | [`extension/jev.js`](https://github.com/eduardoalba00/smart-find/blob/1eab97a11f806c9d8354667e1522838151768eca/extension/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [eduardoalba00](https://github.com/eduardoalba00). Independently curated. |
| Format | Chrome extension (JavaScript) |
| Platform and availability | Chrome (load unpacked) |
| Jev's role | Jev scores each passage (with its section heading) against your question, 8 passages per request; code highlights matches and marks the scrollbar. |
| Requirements | Chrome; TypeSafe API key. |
| License | [MIT](https://github.com/eduardoalba00/smart-find/blob/1eab97a11f806c9d8354667e1522838151768eca/LICENSE) |

## When to use

- Find the part of a long page that answers a question by meaning, not exact words.
- Mismatch: Chrome only; accuracy figures are the author's own tests.

## How it works

The page is split into short passages; Jev scores them in parallel starting with visible text; passages above threshold are highlighted, otherwise it reports no match. (Summarized from the upstream [README](https://github.com/eduardoalba00/smart-find/blob/1eab97a11f806c9d8354667e1522838151768eca/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): load the `extension` folder unpacked in `chrome://extensions` and paste your TypeSafe key.

## Limits and data handling

Page passages and your question go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 1eab97a11f80](https://github.com/eduardoalba00/smart-find/tree/1eab97a11f806c9d8354667e1522838151768eca). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
