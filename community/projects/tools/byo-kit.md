# byo-kit (bring-your-own-data and bring-your-own-key for static demos, with a Jev Decisions helper)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Two dependency-free Web Components for static demos: a drop zone that reads JSON, NDJSON or CSV in the browser, and a masked key field that keeps the visitor's API key in memory or session storage; includes a network-call counter, CSV export that blocks formula injection, an optional CORS relay, and an `openrouterDecide` helper that calls Jev through OpenRouter's Decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dallascrilley/byo-kit) |
| Maintainer | [dallascrilley](https://github.com/dallascrilley). Independently curated. |
| Format | JavaScript library (single file) |
| Requirements | A browser; the visitor's OpenRouter key for Jev calls. |
| License | [MIT](https://github.com/dallascrilley/byo-kit/blob/1165573fd43e9f4f8cae061a629e785fd020ba80/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/openrouter.js`](https://github.com/dallascrilley/byo-kit/blob/1165573fd43e9f4f8cae061a629e785fd020ba80/src/core/openrouter.js) at the pinned commit. |

## When to use

- Let visitors try a Jev demo with their own data and key, without a server holding either.
- Mismatch: the Jev helper is one part of a general demo kit.

## How it works

`src/core/openrouter.js` sends `{state, questions}` to OpenRouter's Decisions API with `typesafe/jev-1.14` as the default model and checks each answer against its question. Integration evidence: [`src/core/openrouter.js`](https://github.com/dallascrilley/byo-kit/blob/1165573fd43e9f4f8cae061a629e785fd020ba80/src/core/openrouter.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/dallascrilley/byo-kit && cd byo-kit
node tools/static-server.mjs . 8787   # open http://127.0.0.1:8787/example/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dallascrilley/byo-kit#readme](https://github.com/dallascrilley/byo-kit#readme)

## Limits and data handling

Data stays in the browser. With the Jev helper, the state and questions go to OpenRouter and TypeSafe with the visitor's own key.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 1165573fd43e](https://github.com/dallascrilley/byo-kit/tree/1165573fd43e9f4f8cae061a629e785fd020ba80). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
