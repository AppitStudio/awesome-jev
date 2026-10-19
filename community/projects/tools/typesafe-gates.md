# typesafe-gates

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript decision gates for LLM pipelines on Jev: define Score, Choice or yes/no questions per item, get probability tables, and keep the keep-rule, threshold and fail-open or fail-closed policy in your own code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mpointer/typesafe-gates) |
| Maintainer | [mpointer](https://github.com/mpointer). Independently curated. |
| Format | npm package (TypeScript) |
| Requirements | Node.js; `@typesafe-ai/sdk` 0.6+ as a peer dependency; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/mpointer/typesafe-gates/blob/ad35e952829631adff09982e1facbe57caba8d3b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/gate.ts`](https://github.com/mpointer/typesafe-gates/blob/ad35e952829631adff09982e1facbe57caba8d3b/src/gate.ts) at the pinned commit. |

## When to use

- Filter or screen items in a pipeline (relevance, spam, fact checks) with explicit thresholds.
- Need a stated behavior when the judge is unavailable.
- Mismatch: thin layer over the official SDK; you still choose thresholds.

## How it works

`defineGate` declares typed questions and a policy; `gate.run` asks Jev through `@typesafe-ai/sdk` and returns verdicts with probabilities, or `null` when Jev was unavailable. Bundled gates include relevance, fact-check and inbound screening, and usage can be recorded per call. Integration evidence: [`src/gate.ts`](https://github.com/mpointer/typesafe-gates/blob/ad35e952829631adff09982e1facbe57caba8d3b/src/gate.ts).

## Get started

From the upstream README: install with the SDK peer dependency and set `TYPESAFE_API_KEY`.

```sh
npm install typesafe-gates @typesafe-ai/sdk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- src/gates/ (relevance, fact-check, inbound-screen)

## Limits and data handling

Item text goes to TypeSafe. Gate quality depends on your questions and thresholds.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit ad35e9528296](https://github.com/mpointer/typesafe-gates/tree/ad35e952829631adff09982e1facbe57caba8d3b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
