# Forma (local-first website and UI builder where TypeSafe Jev picks design settings)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first website/app UI builder: describe a site and TypeSafe Jev selects design settings, component variants, typed fields, panels and section order; edit the result and export standalone HTML. A free hosted editor with limits is also offered.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GPTchatly/Forma) |
| Maintainer | [GPTchatly](https://github.com/GPTchatly). Independently curated. |
| Format | Node.js local app + hosted editor (MIT) |
| Requirements | Node.js 18.17+ and a TypeSafe or OpenRouter key; or use the hosted editor. |
| License | [MIT](https://github.com/GPTchatly/Forma/blob/05320e61c611a2f321dc677512a1c6dbefba6a3b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.mjs`](https://github.com/GPTchatly/Forma/blob/05320e61c611a2f321dc677512a1c6dbefba6a3b/server/jev.mjs) at the pinned commit. |

## When to use

- Get a first-pass site layout from a short description.
- Export standalone HTML you can edit.
- Mismatch: hosted editor is free with limits; local runs use your key.

## How it works

`server/jev.mjs` posts to `https://api.typesafe.ai/v1/systemone` (or OpenRouter `~typesafe/jev-latest` for `sk-or-` keys) with typed design questions. Integration evidence: [`server/jev.mjs`](https://github.com/GPTchatly/Forma/blob/05320e61c611a2f321dc677512a1c6dbefba6a3b/server/jev.mjs).

## Get started

Download the release ZIP or clone, run the start script, paste a key, and describe your site; or try forma.gptchatly.com.

```sh
git clone https://github.com/GPTchatly/Forma.git && cd Forma
export TYPESAFE_API_KEY=...
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/GPTchatly/Forma/blob/05320e61c611a2f321dc677512a1c6dbefba6a3b/README.md](https://github.com/GPTchatly/Forma/blob/05320e61c611a2f321dc677512a1c6dbefba6a3b/README.md)

## Limits and data handling

Your site description is sent to TypeSafe/OpenRouter on your key (or via the hosted editor).

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 05320e61c611](https://github.com/GPTchatly/Forma/tree/05320e61c611a2f321dc677512a1c6dbefba6a3b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
