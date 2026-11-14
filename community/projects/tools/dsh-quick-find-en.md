# dsh-quick-find-en (DeepSeek Harness plugin that finds a passage in the whole chat by meaning, with Jev ranking the matches)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

English plugin for DeepSeek Harness: describe what you are looking for and Jev ranks the passages of the whole session (including parts not yet rendered), then jumps to and highlights the sentence; Cmd/Ctrl+F still does local literal search. Extends the original `dsh-quick-find`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eliaweiss/dsh-quick-find-en) |
| Maintainer | [eliaweiss](https://github.com/eliaweiss). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript, MIT) |
| Requirements | DeepSeek Harness and a Vercel AI Gateway key with access to TypeSafe Jev. |
| License | [MIT](https://github.com/eliaweiss/dsh-quick-find-en/blob/89ba43362ad64d438d2f4aafc0ceca8f48144629/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`semantic.mjs`](https://github.com/eliaweiss/dsh-quick-find-en/blob/89ba43362ad64d438d2f4aafc0ceca8f48144629/semantic.mjs) at the pinned commit. |

## When to use

- Find an earlier decision or answer in a long agent chat when you don't remember the exact words.
- Mismatch: chats you cannot send off-machine; use the local text search instead.

## How it works

`semantic.mjs` calls the Vercel AI Gateway evaluate endpoint (`https://ai-gateway.vercel.sh/v1/evaluate`) with model `typesafe-ai/jev-1.14.0`; the key stays on the host and never reaches the page. Integration evidence: [`semantic.mjs`](https://github.com/eliaweiss/dsh-quick-find-en/blob/89ba43362ad64d438d2f4aafc0ceca8f48144629/semantic.mjs).

## Get started

Add the plugin to a DSH profile and disable the original quick-find first.

```sh
dsh plugin --profile <profile> add github:eliaweiss/dsh-quick-find-en
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/eliaweiss/dsh-quick-find-en/blob/89ba43362ad64d438d2f4aafc0ceca8f48144629/README.md](https://github.com/eliaweiss/dsh-quick-find-en/blob/89ba43362ad64d438d2f4aafc0ceca8f48144629/README.md)
- Original plugin: [github.com/WildPickledPepper/dsh-quick-find](https://github.com/WildPickledPepper/dsh-quick-find)

## Limits and data handling

Meaning search sends up to the newest 160 passages (60,000 characters) to the Vercel AI Gateway and TypeSafe on your key; older messages are skipped. Tool output and reasoning are not searched by meaning.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 89ba43362ad6](https://github.com/eliaweiss/dsh-quick-find-en/tree/89ba43362ad64d438d2f4aafc0ceca8f48144629). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
