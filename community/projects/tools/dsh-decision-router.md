# DSH Decision Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin (Chinese docs) for automatic model selection: when "Auto" is chosen, a separate decision model reads each turn and picks one of 2–6 user-defined routes (provider, model, effort); decision models are local Laya, d1-3B / d1-omni-600M, or — after explicit consent — the System One cloud API (Jev), with an explicit fallback route on timeout or low confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xinyang20/dsh-decision-router) |
| Maintainer | [xinyang20](https://github.com/xinyang20). Independently curated. |
| Format | DSH plugin (`dsh plugin --profile web add github:xinyang20/dsh-decision-router#v0.1.0`) |
| Requirements | DSH 0.2.0-rc.2 (verified host), Node 22.19+/24+, pnpm; local Laya/d1 setup or a TypeSafe key. |
| License | [MIT](https://github.com/xinyang20/dsh-decision-router/blob/b41caec54114657834ccde784d6417f858b0316c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Split DSH work across specialised execution models automatically.
- Keep routing local with Laya, or opt in to Jev.
- Mismatch: README says the cloud Jev path has not yet been verified with a real key.

## How it works

[`src/auto-model.js`](https://github.com/xinyang20/dsh-decision-router/blob/b41caec54114657834ccde784d6417f858b0316c/src/auto-model.js) asks the decision service per user turn and reuses the result for that turn's tool calls; [`local/decision-service.mjs`](https://github.com/xinyang20/dsh-decision-router/blob/b41caec54114657834ccde784d6417f858b0316c/local/decision-service.mjs) serves local models.

## Get started

Install into DSH (README):

```sh
dsh plugin --profile web add github:xinyang20/dsh-decision-router#v0.1.0
```

Local models are free; cloud mode bills your TypeSafe key.

## Examples and demos

- Laya evaluation script: [`scripts/evaluate-laya.mjs`](https://github.com/xinyang20/dsh-decision-router/blob/b41caec54114657834ccde784d6417f858b0316c/scripts/evaluate-laya.mjs).

## Limits and data handling

Cloud mode sends turn text to the System One API after consent; local failures never fall back to cloud. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit b41caec54114](https://github.com/xinyang20/dsh-decision-router/tree/b41caec54114657834ccde784d6417f858b0316c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
