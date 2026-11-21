# Decision Desk by Florian Standhartinger (support-triage demo: one Jev-class call returns queue, priority, risk and next action)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

A small Node web demo where one decision-model call turns a support ticket into four typed, confidence-bearing answers (queue, priority, handling risk, next action), showing the real model, provider, latency and cost. It routes through a Jev-compatible gateway, so you can compare Jev with other System One-style models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fstandhartinger/decision-desk) |
| Maintainer | [fstandhartinger](https://github.com/fstandhartinger). Independently curated. |
| Format | Node.js web demo |
| Requirements | Node.js 20+. Uses the `jev-router.app.mintapis.com` gateway by default (`JEV_GATEWAY_URL` to change it); some gateway models allow public demo traffic without a key. |
| License | [MIT](https://github.com/fstandhartinger/decision-desk/blob/5f355c44ffdbff67d22eab77022b2b630d5f1349/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.js`](https://github.com/fstandhartinger/decision-desk/blob/5f355c44ffdbff67d22eab77022b2b630d5f1349/server.js) at the pinned commit. |

## When to use

- Demo multi-decision support triage with typed answers and visible confidence, cost and latency.
- Mismatch: a direct TypeSafe integration; it goes through a third-party gateway by default.

## How it works

`server.js` posts each ticket to `${JEV_GATEWAY_URL}/v1/systemone` with typed questions and reads model, provider, latency and cost from `X-Jev-*` headers; a per-IP rate limit and daily spend cap protect public deployments. Integration evidence: [`server.js`](https://github.com/fstandhartinger/decision-desk/blob/5f355c44ffdbff67d22eab77022b2b630d5f1349/server.js).

## Get started

Run locally with npm and open the page.

```sh
git clone https://github.com/fstandhartinger/decision-desk && cd decision-desk
npm start
# open http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/fstandhartinger/decision-desk/blob/5f355c44ffdbff67d22eab77022b2b630d5f1349/README.md](https://github.com/fstandhartinger/decision-desk/blob/5f355c44ffdbff67d22eab77022b2b630d5f1349/README.md)

## Limits and data handling

Ticket text is forwarded to the gateway and the selected model provider. Rate limits and spend counters are in memory.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 5f355c44ffdb](https://github.com/fstandhartinger/decision-desk/tree/5f355c44ffdbff67d22eab77022b2b630d5f1349). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
