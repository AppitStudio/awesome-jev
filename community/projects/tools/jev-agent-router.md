# jev-agent-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that picks the model and effort of every subagent from its task type, with Jev as an optional classifier.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CiroVilmer/jev-agent-router) |
| Maintainer | [CiroVilmer](https://github.com/CiroVilmer). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code 2.1.293+; optional TypeSafe API key for the Jev classifier. |
| License | [MIT](https://github.com/CiroVilmer/jev-agent-router/blob/9adb04f821fa99e4bd46b5dc551c82f7f712beee/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`router/src/clasificadores/jev.ts`](https://github.com/CiroVilmer/jev-agent-router/blob/9adb04f821fa99e4bd46b5dc551c82f7f712beee/router/src/clasificadores/jev.ts) at the pinned commit. |

## When to use

- Route reviews, builds, fixes and exploration subagents to different models and effort levels.
- Use Jev to classify ambiguous task types instead of keyword rules.
- Mismatch: Jev is optional; the default classifier is rule-based.

## How it works

When a subagent is deployed, the router classifies its task type; with Jev enabled it sends the task text as a choice question to `api.typesafe.ai/v1/systemone` and maps the answer to model and effort. Integration evidence: [`router/src/clasificadores/jev.ts`](https://github.com/CiroVilmer/jev-agent-router/blob/9adb04f821fa99e4bd46b5dc551c82f7f712beee/router/src/clasificadores/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add CiroVilmer/jev-agent-router
claude plugin install agent-router@jev-agent-router
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark script: `bench/jev-todos.mjs`.

## Limits and data handling

With Jev enabled, subagent task descriptions are sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 9adb04f821fa](https://github.com/CiroVilmer/jev-agent-router/tree/9adb04f821fa99e4bd46b5dc551c82f7f712beee). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
