# Zevals

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript AI-agent testing library (OpenCX Labs) for end-to-end conversation evals, whose `aiAssertion` judge can be a `JevClient` — TypeSafe Jev via OpenRouter, Cloudflare, Vercel or HTTP — giving calibrated yes/no verdicts with thresholds and borderline flags.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/opencx-labs/zevals) |
| Maintainer | [opencx-labs](https://github.com/opencx-labs). Independently curated. |
| Format | TypeScript library (npm `@zevals/core`, 0.3.0 at review) |
| Requirements | Node.js; any test runner; `OPENROUTER_API_KEY` (or another configured Jev route) for the Jev judge. |
| License | [MIT](https://github.com/opencx-labs/zevals/blob/fef993ae85b96cf3dca23646c615a64d6a79c06c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Test support agents end to end ("the agent transferred the chat to a human") with repeatable assertions.
- Spot vague assertions via `p≈0.5` borderline results.
- Mismatch: Jev returns no prose; use `explainFailures` with an LLM judge for reasons.

## How it works

`zevals.openRouterJevClient()` (or the Cloudflare/Vercel/HTTP variants in [`packages/core/src/criteria/`](https://github.com/opencx-labs/zevals/tree/fef993ae85b96cf3dca23646c615a64d6a79c06c/packages/core/src/criteria)) asks Jev a yes/no question about the scoped transcript; the assertion passes when the probability reaches the threshold and `reason` reports the probability.

## Get started

Install the core package and use a Jev judge in an assertion:

```sh
npm install @zevals/core
export OPENROUTER_API_KEY=...
# const client = zevals.openRouterJevClient();
# zevals.aiAssertion({ judge: client, prompt: 'The agent transferred the chat to a human', threshold: 0.5 })
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Jev as the Judge* section (upstream production-replay cost/latency figures).

## Limits and data handling

Cost, latency and malformed-output figures are upstream; not reproduced. Transcripts are sent to the configured provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit fef993ae85b9](https://github.com/opencx-labs/zevals/tree/fef993ae85b96cf3dca23646c615a64d6a79c06c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
