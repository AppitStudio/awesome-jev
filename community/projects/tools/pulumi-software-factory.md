# Pulumi self-driving software factory

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pulumi example from the Pulumi org that deploys a self-driving software factory on AWS: a Qwen3-8B model on your own GPUs, Mastra Factory for coding agents, a Mastra agent, and an issue triage service where Jev accepts, rejects or asks for detail on each new item.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pulumi/devx-pulumi-software-factory) |
| Maintainer | [pulumi](https://github.com/pulumi). Independently curated. |
| Format | Pulumi infrastructure example (TypeScript + Python stacks on AWS EKS) |
| Requirements | AWS account with quota for 2 × `g6.2xlarge` GPU nodes, Pulumi account, Node.js 20+, Python 3.12, Docker, `kubectl`, `helm`; a Jev API key for the triage stack. |
| License | [Apache-2.0](https://github.com/pulumi/devx-pulumi-software-factory/blob/ea9cc5b38608ce106af5c5097051b9448d76ec6f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/triage/src/jevClient.ts`](https://github.com/pulumi/devx-pulumi-software-factory/blob/ea9cc5b38608ce106af5c5097051b9448d76ec6f/apps/triage/src/jevClient.ts) at the pinned commit. |

## When to use

- See a full agent platform described as infrastructure code, with Jev as the intake gate.
- Triage incoming work items before coding agents spend time on them.
- Mismatch: GPU stack costs about $2.2 per hour while up; bring-up takes roughly 45 minutes.

## How it works

Five Pulumi stacks deploy the model, a shared platform, Mastra Factory, a Mastra agent and a triage service. The triage pod's `apps/triage/src/jevClient.ts` calls `https://api.typesafe.ai/v1/systemone` to decide whether each new item is accepted, rejected or needs more detail, and records verdicts in a DynamoDB audit trail. One command tears everything down. Integration evidence: [`apps/triage/src/jevClient.ts`](https://github.com/pulumi/devx-pulumi-software-factory/blob/ea9cc5b38608ce106af5c5097051b9448d76ec6f/apps/triage/src/jevClient.ts).

## Get started

From the upstream README: configure each stack, set the Jev key as a Pulumi secret, then deploy in dependency order.

```sh
npm install
(cd stacks/triage && pulumi config set --secret jevApiKey "<your key>")
npm run orchestrate -- up
# tear down when done
npm run orchestrate -- down --yes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/items.txt (sample work items)
- scripts/board.sh and scripts/demo-agent.sh

## Limits and data handling

Deploys paid AWS resources; destroy it when done. Work item text goes to TypeSafe for triage.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit ea9cc5b38608](https://github.com/pulumi/devx-pulumi-software-factory/tree/ea9cc5b38608ce106af5c5097051b9448d76ec6f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
