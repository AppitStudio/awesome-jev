# X Semantic Filter (Chrome extension that folds low-value X posts by your plain-language rules, with Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that folds posts on X in real time: describe what you don't want in plain language, every post gets a probability per rule, and anything above your threshold collapses into a one-line bar you can expand. Backends are Jev, Cloudflare's Clef-omni (which also reads images) or an OpenAI-compatible model; bilingual Chinese and English UI, no backend of its own.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nixz0824/x-semantic-filter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Nixz0824/x-semantic-filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free. Model calls are billed to your own key. Checked 2026-10-28. |
| Jev evidence | [`src/background.js`](https://github.com/Nixz0824/x-semantic-filter/blob/a8c761d6492192c31fe0902d516b4e2f610ad74d/src/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Nixz0824](https://github.com/Nixz0824). Independently curated. |
| Format | Chrome extension (Manifest V3, JavaScript) |
| Platform and availability | Chrome or Chromium; load unpacked from source (no store listing verified). |
| Jev's role | Per-post decision: the probability that a post matches each of your rules. |
| Requirements | Chrome and a key for the chosen backend (TypeSafe for Jev). |
| License | [MIT](https://github.com/Nixz0824/x-semantic-filter/blob/a8c761d6492192c31fe0902d516b4e2f610ad74d/LICENSE) |

## When to use

- Clean up an X timeline by meaning rather than keywords.
- Mismatch: a relay Worker is needed where api.typesafe.ai is blocked.

## How it works

`src/background.js` sends post text and your rules to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) as Noul questions, caching probabilities by post and rule; `relay/worker.js` is an optional Cloudflare relay. Integration evidence: [`src/background.js`](https://github.com/Nixz0824/x-semantic-filter/blob/a8c761d6492192c31fe0902d516b4e2f610ad74d/src/background.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Nixz0824/x-semantic-filter
# chrome://extensions -> Developer mode -> Load unpacked -> select the folder
# then paste your TypeSafe API key in the options
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Nixz0824/x-semantic-filter#readme](https://github.com/Nixz0824/x-semantic-filter#readme)

## Limits and data handling

Text of posts you scroll past (and images, with Clef) goes to the chosen provider.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit a8c761d64921](https://github.com/Nixz0824/x-semantic-filter/tree/a8c761d6492192c31fe0902d516b4e2f610ad74d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
