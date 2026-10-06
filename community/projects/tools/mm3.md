# MM3

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Memory and decision layer for coding agents (Claude Code plugin, npm `@mvpscale/mm3`, CLI) that wraps TypeSafe Jev: the agent asks batches of yes/no and decision questions about a scoped piece of code and gets calibrated answers recorded in a ledger.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mvp-scale/mm3) |
| Maintainer | [mvp-scale](https://github.com/mvp-scale). Independently curated. |
| Format | Claude Code plugin + CLI (npm `@mvpscale/mm3`, 0.1.2 at review) |
| Requirements | Claude Code or Node 22.13+; a TypeSafe API key (stored in Claude Code secure storage or the OS keychain). |
| License | [Apache-2.0](https://github.com/mvp-scale/mm3/blob/7d6f7d1b1b09fc6c31d857f70c8877e2b1e457cb/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a coding agent cheap, structured second opinions on code questions linters and tests can't ask.
- Keep a ledger of which calibrated verdicts held up (`mm3 outcome`).
- Mismatch: beta; advice only — delete/deploy/pay decisions stay human.

## How it works

The agent writes a YAML request (goal, file scope, concerns, decisions); MM3 sends it through its TypeSafe adapter ([`src/classifier/typesafe/`](https://github.com/mvp-scale/mm3/tree/7d6f7d1b1b09fc6c31d857f70c8877e2b1e457cb/src/classifier/typesafe)) and returns answers with probabilities and `unsure`, recording request and result in the ledger.

## Get started

Install the plugin in Claude Code, or run the CLI with npx:

```sh
/plugin marketplace add mvp-scale/mm3
/plugin install mm3@mvp-scale
# or in a terminal (Node 22.13+):
npx @mvpscale/mm3 config
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *See it run*: an n8n request with 12 questions answered by `jev-1.13.0` (upstream-reported latency and cost).
- Docs on the answer contract, evidence and numbers.

## Limits and data handling

Beta; upstream says formal benchmarks are coming. Code excerpts in requests are sent to TypeSafe. A calibrated 0.9 is still wrong one time in ten (upstream wording). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 7d6f7d1b1b09](https://github.com/mvp-scale/mm3/tree/7d6f7d1b1b09fc6c31d857f70c8877e2b1e457cb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
