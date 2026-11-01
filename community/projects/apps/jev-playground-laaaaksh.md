# Jev Playground by Laaaaksh (hosted bring-your-own-key playground for TypeSafe Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Unofficial static web playground for trying Jev with your own TypeSafe key: paste a state (text or JSON), define questions, and see Jev's answers. A small relay function forwards your key to TypeSafe without logging it; you can also run your own copy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Laaaaksh/jev-playground) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://jev-playground-beta.vercel.app) |
| Pricing and access | Free hosted page and source (MIT); calls are billed to your own TypeSafe key. Checked 2026-11-01. |
| Jev evidence | [`lib/relay.mjs`](https://github.com/Laaaaksh/jev-playground/blob/c37ac319ba341d2678048f54bfd2098268c0e0cf/lib/relay.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Laaaaksh](https://github.com/Laaaaksh). Independently curated. |
| Format | Static web app plus one serverless relay (Vercel) |
| Platform and availability | Any modern browser; self-hostable. |
| Jev's role | The model being explored: answers the questions you define. |
| Requirements | A TypeSafe API key; Node.js to self-host. |
| License | [MIT](https://github.com/Laaaaksh/jev-playground/blob/c37ac319ba341d2678048f54bfd2098268c0e0cf/LICENSE) |

## When to use

- Try typed Jev questions in a browser before writing code.
- Mismatch: an exploration tool, not a production client.

## How it works

`lib/relay.mjs` forwards browser requests to the hard-coded `https://api.typesafe.ai/v1/systemone` with the visitor's key, enforcing same-origin, per-IP rate limits and body size limits and retrying 429/529. Integration evidence: [`lib/relay.mjs`](https://github.com/Laaaaksh/jev-playground/blob/c37ac319ba341d2678048f54bfd2098268c0e0cf/lib/relay.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm start
# open http://localhost:4747 and paste your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live: [jev-playground-beta.vercel.app](https://jev-playground-beta.vercel.app)

## Limits and data handling

Your key passes through the deployment's relay for each request (not stored); run your own copy if you prefer. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit c37ac319ba34](https://github.com/Laaaaksh/jev-playground/tree/c37ac319ba341d2678048f54bfd2098268c0e0cf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
