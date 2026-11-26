# pi-auto-goal-jev by Brian Kaplan (fork of the pi-auto-goal stop guard that can use Jev to judge whether the Pi agent stopped too early)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Stop guard for the Pi coding agent: when the agent settles, a judge decides whether stopping was acceptable or work is still missing, and if so sends the agent back with a system nudge naming the gap. This fork of maplezzk's pi-auto-goal adds one feature, judging with a Pi decision model such as `typesafe/jev-latest`, which answers two typed questions in one call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SoftwareDeployed/pi-auto-goal-jev) |
| Maintainer | [Brian Kaplan](https://github.com/SoftwareDeployed) (SoftwareDeployed); fork of maplezzk's pi-auto-goal. Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi with a `classify`-capable model registry and the TypeSafe provider (`TYPESAFE_API_KEY` or `/login typesafe`). |
| License | [MIT](https://github.com/SoftwareDeployed/pi-auto-goal-jev/blob/4b633d7abfd3e2d47441dcdb381ce9a66e5f2c8a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge-model.ts`](https://github.com/SoftwareDeployed/pi-auto-goal-jev/blob/4b633d7abfd3e2d47441dcdb381ce9a66e5f2c8a/src/judge-model.ts) at the pinned commit. |

## When to use

- Pi users whose agent often stops halfway through multi-step requests.
- Mismatch: hard task completion checks; the judge reads the conversation, not test results.

## How it works

`src/judge-model.ts` calls Pi's `ctx.modelRegistry.classify` with the decision model and asks whether the agent may stop and which rule applies; the verdict uses Jev's confidence and the nudge names the chosen rule. Older Pi versions without `classify` get an explicit error rather than a silent model switch. Integration evidence: [`src/judge-model.ts`](https://github.com/SoftwareDeployed/pi-auto-goal-jev/blob/4b633d7abfd3e2d47441dcdb381ce9a66e5f2c8a/src/judge-model.ts).

## Get started

Install from Git, then set the judge model to Jev.

```sh
pi install git:github.com/SoftwareDeployed/pi-auto-goal-jev
/config:auto-goal model typesafe/jev-latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Upstream project: [github.com/maplezzk/pi-extensions/tree/main/packages/pi-auto-goal](https://github.com/maplezzk/pi-extensions/tree/main/packages/pi-auto-goal)

## Limits and data handling

Every fully settled turn costs one judge call; the user request, answers and recent context go to the judge model's provider. Decision models do not appear in the panel's picker and must be set by config. Intended to track upstream pi-auto-goal.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 4b633d7abfd3](https://github.com/SoftwareDeployed/pi-auto-goal-jev/tree/4b633d7abfd3e2d47441dcdb381ce9a66e5f2c8a). Inspected the README (fork section), LICENSE and `src/judge-model.ts` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
