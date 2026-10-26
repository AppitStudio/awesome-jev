# dsh-agent-dispatch (DeepSeek Harness: Jev advises whether to delegate a turn and to which agent)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness plugin that asks Jev once before each turn whether the work should be delegated and to which registered agent, and injects advice only when calibrated gates (dispatch band, confidence and margin, risk veto) pass; with no key or a failed call it stays silent; the key is read from the keychain first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fan56/dsh-agent-dispatch) |
| Maintainer | [fan56](https://github.com/fan56). Independently curated. |
| Format | DSH plugin (TypeScript, npm `@aiwayds/dsh-agent-dispatch`) |
| Requirements | DeepSeek Harness 0.1.7-rc.1 or later, Node 22+; a TypeSafe API key in the keychain, `TYPESAFE_API_KEY` or `JEV_API_KEY`. |
| License | [MIT](https://github.com/fan56/dsh-agent-dispatch/blob/9063d9f51084b48bdf1ec95155422559af4317be/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.ts`](https://github.com/fan56/dsh-agent-dispatch/blob/9063d9f51084b48bdf1ec95155422559af4317be/src/index.ts) at the pinned commit. |

## When to use

- Get delegation advice for a roster of DSH agents without naming models.
- Prefer silence over a wrong suggestion.
- Mismatch: advice only; the main model still decides. Distinct from the community dsh-jev-subagent-dispatch, which routes models.

## How it works

`src/index.ts` loads the key and, through the shared `@aiwayds/dsh-jev-core` client, sends the turn summary and agent roster to TypeSafe's System One API; only verdicts that clear the gates are injected as a hint. Integration evidence: [`src/index.ts`](https://github.com/fan56/dsh-agent-dispatch/blob/9063d9f51084b48bdf1ec95155422559af4317be/src/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install @aiwayds/dsh-agent-dispatch
dsh plugin add @aiwayds/dsh-agent-dispatch
# then add the package to the profile's bundles list, as the README explains
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/fan56/dsh-agent-dispatch#readme](https://github.com/fan56/dsh-agent-dispatch#readme)

## Limits and data handling

Turn summaries and agent names go to TypeSafe when a key is set.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 9063d9f51084](https://github.com/fan56/dsh-agent-dispatch/tree/9063d9f51084b48bdf1ec95155422559af4317be). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
