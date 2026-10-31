# language-plugin-dsh (DSH plugin that pins chat and artifact languages, with Jev as an optional language judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness (DSH) plugin that pins two languages independently: the chat reply language (by default it follows what you write) and the artifact language (identifiers, comments, docs, commits and PR bodies, `en-US` by default). Guards judge language with an offline stopword detector or Jev, which can name any language.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/farchanjo/language-plugin-dsh) |
| Maintainer | [farchanjo](https://github.com/farchanjo). Independently curated. |
| Format | DSH plugin (JavaScript) |
| Requirements | DeepSeek Harness; optional `TYPESAFE_API_KEY` for the `jev` decider. |
| License | [MIT](https://github.com/farchanjo/language-plugin-dsh/blob/ed13729b10bc56fc88c9fde1ddda9bb3c65cc324/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/decide.js`](https://github.com/farchanjo/language-plugin-dsh/blob/ed13729b10bc56fc88c9fde1ddda9bb3c65cc324/lib/decide.js) at the pinned commit. |

## When to use

- Keep code and commits in English while chatting in another language.
- Mismatch: `auto` mode only asks Jev when the offline detector cannot decide.

## How it works

`lib/decide.js` asks TypeSafe System One (`api.typesafe.ai/v1/systemone`, `jev-latest`) a `noul` plus a `choice` about the text's language; `auto` uses stopwords for six languages and Jev for anything else, with the offline detector as fallback. Integration evidence: [`lib/decide.js`](https://github.com/farchanjo/language-plugin-dsh/blob/ed13729b10bc56fc88c9fde1ddda9bb3c65cc324/lib/decide.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/farchanjo/language-plugin-dsh.git
/lang decide auto   # inside DSH
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/farchanjo/language-plugin-dsh#readme](https://github.com/farchanjo/language-plugin-dsh#readme)

## Limits and data handling

Text checked by the `jev` decider is sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit ed13729b10bc](https://github.com/farchanjo/language-plugin-dsh/tree/ed13729b10bc56fc88c9fde1ddda9bb3c65cc324). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
