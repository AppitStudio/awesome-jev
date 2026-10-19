# dsh-system1

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness (dsh) package that gives agents a `system1_decide` tool and plugins a `ctx.system1.decide()` API for yes/no, choice, score and image-box judgments, with TypeSafe Jev, Laya and Cloudflare Clef providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/exoticknight/dsh-system1) |
| Maintainer | [exoticknight](https://github.com/exoticknight). Independently curated. |
| Format | npm package / dsh plugin (Node.js) |
| Requirements | dsh; `TYPESAFE_API_KEY` for Jev, or a Laya server or Cloudflare account. |
| License | [Apache-2.0](https://github.com/exoticknight/dsh-system1/blob/d45e6c481b6b19df6ae9ff5b968700f346a7b82e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/providers/typesafe/adapter.js`](https://github.com/exoticknight/dsh-system1/blob/d45e6c481b6b19df6ae9ff5b968700f346a7b82e/lib/providers/typesafe/adapter.js) at the pinned commit. |

## When to use

- Give a dsh agent typed probabilities for gating, routing and scoring.
- Switch between hosted Jev and self-hosted decision models with one API.
- Mismatch: built for the dsh host; `box` needs newer Jev models.

## How it works

Requests and responses are validated per question, with cancellation, per-attempt timeouts and fallback models. `lib/providers/typesafe/adapter.js` maps calls to TypeSafe's hosted Jev models (PNG/JPEG input), and other providers implement the same public contract. Integration evidence: [`lib/providers/typesafe/adapter.js`](https://github.com/exoticknight/dsh-system1/blob/d45e6c481b6b19df6ae9ff5b968700f346a7b82e/lib/providers/typesafe/adapter.js).

## Get started

From the upstream README: `npm install dsh-system1` and add the package to the dsh profile you run.

```sh
npm install dsh-system1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README primitives table (noul, choice, score, box)
- README.zh-CN.md

## Limits and data handling

State text and images go to the selected provider. Model support for `box` varies.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit d45e6c481b6b](https://github.com/exoticknight/dsh-system1/tree/d45e6c481b6b19df6ae9ff5b968700f346a7b82e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
