# node-decision-model

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Zero-dependency Node.js 20+ library and CLI for decision models: one `Client` with OpenRouter as the default provider, TypeSafe's native API as a second, and Cloudflare Workers AI Clef as a third. Pre-1.0.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fraserxu/node-decision-model) |
| Maintainer | [fraserxu](https://github.com/fraserxu). Independently curated. |
| Format | npm library + `decision-model` CLI (ESM and CommonJS) |
| Requirements | Node.js 20+; `TYPESAFE_API_KEY`, `OPENROUTER_API_KEY`, or Cloudflare credentials. |
| License | [MIT](https://github.com/fraserxu/node-decision-model/blob/b78c8b82a7442817709cfb1a24a6b7b08d5e2fe3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Call Jev-style typed decisions from Node without provider lock-in.
- Mismatch: Pre-1.0 API may change between minor versions.

## How it works

`new Client().ask({ state, questions })` sends `noul`, `choice`, or `score` questions and returns calibrated probabilities keyed by question id. (Summarized from the upstream [README](https://github.com/fraserxu/node-decision-model/blob/b78c8b82a7442817709cfb1a24a6b7b08d5e2fe3/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `npm install node-decision-model`, or try `npx decision-model yesno "Is this urgent?" -f issue.json`.

## Limits and data handling

State is sent to the chosen hosted provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit b78c8b82a744](https://github.com/fraserxu/node-decision-model/tree/b78c8b82a7442817709cfb1a24a6b7b08d5e2fe3). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
