# decisionpacks (versioned Jev decision packs with pinned models, validated answers and policy replay)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Node.js toolkit that wraps TypeSafe Jev judgments in portable packs: declared inputs, pinned models, response validation, deterministic gates, audit records and migration diffs that replay historical judgments without new inference.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/decisionpacks) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js 22+ CLI/library (MIT; no runtime deps) |
| Requirements | Node.js 22+ and `TYPESAFE_API_KEY` for live pack runs (fixture mode offline). |
| License | [MIT](https://github.com/gbesse/decisionpacks/blob/d9bda10ca3f4c8dd5b7192dce5af001c58f15e99/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/decisionpacks.mjs`](https://github.com/gbesse/decisionpacks/blob/d9bda10ca3f4c8dd5b7192dce5af001c58f15e99/bin/decisionpacks.mjs) at the pinned commit. |

## When to use

- Ship a decision as a versioned, testable dependency.
- Replay gates against historical judgments after a policy change.
- Mismatch: produces decisions only; your app owns actions.

## How it works

`bin/decisionpacks.mjs` validates packs and runs them against TypeSafe `/v1/systemone` or an explicit fixture provider. Integration evidence: [`bin/decisionpacks.mjs`](https://github.com/gbesse/decisionpacks/blob/d9bda10ca3f4c8dd5b7192dce5af001c58f15e99/bin/decisionpacks.mjs).

## Get started

Clone, run the offline demo and tests, then set a key for a live pack run.

```sh
git clone https://github.com/gbesse/decisionpacks.git && cd decisionpacks
npm run demo && npm test
export TYPESAFE_API_KEY=...
node bin/decisionpacks.mjs run packs/support-triage.json examples/billing-state.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/decisionpacks/blob/d9bda10ca3f4c8dd5b7192dce5af001c58f15e99/README.md](https://github.com/gbesse/decisionpacks/blob/d9bda10ca3f4c8dd5b7192dce5af001c58f15e99/README.md)

## Limits and data handling

Pack state is sent to TypeSafe on your key when live. Public alpha; no automatic retry.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit d9bda10ca3f4](https://github.com/gbesse/decisionpacks/tree/d9bda10ca3f4c8dd5b7192dce5af001c58f15e99). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
