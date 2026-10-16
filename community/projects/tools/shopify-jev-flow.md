# Shopify Jev Flow

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Shopify Flow action that returns a typed Jev decision (finite route, calibrated confidence, explicit `reviewRequired`) instead of prose; the first example routes return requests to auto-approve, manual review or reject.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/shopify-jev-flow) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js server + Shopify Flow action extension template |
| Requirements | Node.js; a Shopify app and Shopify CLI for deployment; server-side `TYPESAFE_API_KEY` and `SHOPIFY_API_SECRET` for live mode. |
| License | [MIT](https://github.com/gbesse/shopify-jev-flow/blob/bf4dcc95d95d4a4ce41e78d497a2bdebe0bf07aa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/server.js`](https://github.com/gbesse/shopify-jev-flow/blob/bf4dcc95d95d4a4ce41e78d497a2bdebe0bf07aa/src/server.js) at the pinned commit. |

## When to use

- Send return requests through a reviewable Jev decision inside Shopify Flow, with low-confidence cases forced to manual review.
- Prototype offline with fixture mode before connecting a store.
- Mismatch: source template, not a published App Store app; you supply durable storage, tenant auth and rate limits.

## How it works

Live mode verifies Shopify's HMAC over the raw body, then posts the subject to `https://api.typesafe.ai/v1/systemone` with a 10 s timeout; probabilities and thresholds must stay in [0,1], low confidence becomes `manual_review`, and `decisionId` plus an append-only audit record make replays idempotent. Integration evidence: [`src/server.js`](https://github.com/gbesse/shopify-jev-flow/blob/bf4dcc95d95d4a4ce41e78d497a2bdebe0bf07aa/src/server.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gbesse/shopify-jev-flow.git && cd shopify-jev-flow
npm test
npm run demo
JEV_FIXTURE=1 npm start   # fixture mode: no network calls
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Adoption check walkthrough: `examples/adoption-check.md`.

## Limits and data handling

In live mode, the request subject goes to TypeSafe on your key; keep customer data in `subject` minimal, as the README advises.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit bf4dcc95d95d](https://github.com/gbesse/shopify-jev-flow/tree/bf4dcc95d95d4a4ce41e78d497a2bdebe0bf07aa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
