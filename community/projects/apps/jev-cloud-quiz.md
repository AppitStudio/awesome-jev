# Jev Cloud Quiz (Japanese web demo where Jev guesses whether a feature name is AWS, Azure or Google Cloud)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Japanese demo: pick one of 30 cloud feature names with brand words removed, and Jev returns a probability for AWS, Azure and Google Cloud, drawn as three bars. Ambiguous names show visibly split confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/minorun365/jev-cloud-quiz) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://dxtmc35dbmyei.cloudfront.net/) |
| Pricing and access | Free hosted demo; source Apache-2.0. Checked 2026-11-01. |
| Jev evidence | [`server/server.mjs`](https://github.com/minorun365/jev-cloud-quiz/blob/0157d670d78eaf7c6e6761624574930d79a10a6c/server/server.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [minorun365](https://github.com/minorun365). Independently curated. |
| Format | React web app with a Lambda API (AWS CDK) |
| Platform and availability | Any modern browser. |
| Jev's role | Picks the cloud provider with probabilities. |
| Requirements | None to try the hosted demo; Node.js, AWS and a TypeSafe key to deploy. |
| License | [Apache-2.0](https://github.com/minorun365/jev-cloud-quiz/blob/0157d670d78eaf7c6e6761624574930d79a10a6c/LICENSE) |

## When to use

- See calibrated probabilities on a simple choice question.
- Mismatch: a demo, not a cloud reference.

## How it works

The `/api/classify` endpoint (`server/server.mjs`, deployed via `infra/`) sends the feature name to Jev as a choice question and returns its `probabilities`; the key stays in Lambda (us-west-2). Integration evidence: [`server/server.mjs`](https://github.com/minorun365/jev-cloud-quiz/blob/0157d670d78eaf7c6e6761624574930d79a10a6c/server/server.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
export TYPESAFE_API_KEY=<key>
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [dxtmc35dbmyei.cloudfront.net/](https://dxtmc35dbmyei.cloudfront.net/)

## Limits and data handling

Japanese UI. The hosted demo uses the author's key and may be rate limited or removed. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 0157d670d78e](https://github.com/minorun365/jev-cloud-quiz/tree/0157d670d78eaf7c6e6761624574930d79a10a6c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
