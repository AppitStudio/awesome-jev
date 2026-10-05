# AgentRun

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Workflow language for the agents you already run: define repeatable steps, let TypeSafe Jev make focused typed checks (`@parcha/agentrun-jev`), and call an agent only when work needs investigation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Parcha-ai/agentrun) |
| Maintainer | [Parcha-ai](https://github.com/Parcha-ai). Independently curated. |
| Format | DSL/interpreter packages (beta) with scripted demo and Pi extension |
| Requirements | Node.js; `npx agentrun demo` needs no key. Live runs need `TYPESAFE_API_KEY` plus your own agent/tool adapters. |
| License | [Apache-2.0](https://github.com/Parcha-ai/agentrun/blob/29c65fcfeb61dbc879958d3116da46d1bfbc6186/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Turn a support or research flow into a testable workflow where Jev decides pass/escalate and an agent investigates only on failure.
- Rank or screen lists with Jev scores while code applies quotas and dedupes.
- Mismatch: single one-off decisions do not need a workflow runtime.

## How it works

Applications supply adapters: tools via `runEffect`, the existing agent via `runNode`, and Jev decisions via `createJevRunner()` as `runJudge`. The support example requires a source reference and a Jev `yes` with confidence ≥ 0.8, otherwise allows one agent attempt and re-checks ([README](https://github.com/Parcha-ai/agentrun/blob/29c65fcfeb61dbc879958d3116da46d1bfbc6186/README.md)).

## Get started

Run the scripted demo (no key), then install the Jev adapter for live runs:

```sh
npm install @parcha/agentrun-dsl@beta
npx agentrun demo
npm install @parcha/agentrun-dsl@beta @parcha/agentrun-jev@beta
export TYPESAFE_API_KEY=...
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Support-answer, typed-research, and rank-candidates examples in `examples/`; support quickstart in `docs/support-quickstart.md`.

## Limits and data handling

Packages are beta. Live Jev checks send workflow state to TypeSafe and incur charges; agent calls use your own model provider.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 29c65fcfeb61](https://github.com/Parcha-ai/agentrun/tree/29c65fcfeb61dbc879958d3116da46d1bfbc6186). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
