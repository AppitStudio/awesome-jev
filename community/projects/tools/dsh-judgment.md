# dsh-judgment

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness plugin that exposes one structured-judgment service: one state plus a batch of named choice, noul or score questions in, a batch of calibrated probability answers out, with validation, credentials, audit and metering.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/j62268781-alt/dsh-judgment) |
| Maintainer | [j62268781-alt](https://github.com/j62268781-alt). Independently curated. |
| Format | DeepSeek Harness (DSH) plugin |
| Requirements | DeepSeek Harness, a TypeSafe API key (or a compatible endpoint). |
| License | [MIT](https://github.com/j62268781-alt/dsh-judgment/blob/71d409488b5b2d2abe26731098f3bc72a19ed429/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client/config.js`](https://github.com/j62268781-alt/dsh-judgment/blob/71d409488b5b2d2abe26731098f3bc72a19ed429/client/config.js) at the pinned commit. |

## When to use

- Let other DSH plugins or your own agent loop ask Jev batched questions through one shared service.
- Keep thresholds and loop logic in the consumer while the plugin handles requests and accounting.
- Mismatch: adds no tools and no loop by itself; README is mainly in Chinese (English version in `README.en.md`).

## How it works

`client/config.js` defaults to `https://api.typesafe.ai/v1/systemone` with `typesafe/jev-1.13`; the plugin normalizes protocols, validates answers strictly and registers a `ctx.judgment` service that other plugins call directly. Integration evidence: [`client/config.js`](https://github.com/j62268781-alt/dsh-judgment/blob/71d409488b5b2d2abe26731098f3bc72a19ed429/client/config.js).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile <profile> add github:j62268781-alt/dsh-judgment
# then configure it under Settings > 决策 (Decisions)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: `README.en.md`.

## Limits and data handling

State and questions go to TypeSafe or your configured endpoint on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 71d409488b5b](https://github.com/j62268781-alt/dsh-judgment/tree/71d409488b5b2d2abe26731098f3bc72a19ed429). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
