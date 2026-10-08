# atoma

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent coordination platform (hosted atoma.run or self-hosted, AGPL-3.0) that turns a request into checked work; TypeSafe Jev takes bounded decisions such as which agent or recipe takes a task and whether a plan is approved.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atoma-run/atoma) |
| Product homepage | [atoma.run](https://atoma.run) |
| Maintainer | [atoma-run](https://github.com/atoma-run) (repository moved from mgtf/atoma). Submitted via [issue #1210](https://github.com/AppitStudio/awesome-jev/issues/1210). |
| Format | Hosted web service and self-hostable source (under active development) |
| Requirements | Hosted: OAuth sign-in at atoma.run. Self-host: Node 24.20 (`.nvmrc`), macOS/Linux (or WSL2), model-provider keys (`ATOMA_MODEL_L1/L2/L3`); Jev is enabled when the host has `TYPESAFE_API_KEY` unless `ATOMA_JEV=0`. |
| License | [AGPL-3.0](https://github.com/atoma-run/atoma/blob/e85140ce3af18d67ed6665b64180104324332c8b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Hosted service at atoma.run; the submission (issue #1210) states Atoma is free, with Jev billed separately by TypeSafe and LLM usage by your providers (not independently verified). Upstream warns not to submit confidential or personal data. |

## When to use

- Evaluate an agent system where cheap typed decisions handle routing and plan approval while generative models do the work.
- Inspect per-decision latency and cost on a run timeline.
- Mismatch: confidential data (upstream explicitly warns against it); runs share learned prompts/recipes across organisations by design.

## How it works

Jev selects a registered agent/recipe (Choice), approves intermediate plans and results when evidence permits (Noul), detects duplicate recipes before learning them twice, and sets a worker's reasoning effort; uncertain or unavailable answers fall back to the generative models, and final delivery acceptance stays independent of Jev ([architecture guide](https://github.com/atoma-run/atoma/blob/e85140ce3af18d67ed6665b64180104324332c8b/docs/how-it-works.md)). The client in [`src/core/jev.ts`](https://github.com/atoma-run/atoma/blob/e85140ce3af18d67ed6665b64180104324332c8b/src/core/jev.ts) pins `jev-1.13.0` at `api.typesafe.ai/v1/systemone`, waits at most 2 s per decision and stops asking Jev after 3 failures in a run; questions live in [`src/core/jevQuestions.ts`](https://github.com/atoma-run/atoma/blob/e85140ce3af18d67ed6665b64180104324332c8b/src/core/jevQuestions.ts). Each decision is recorded on the run timeline with its latency and separate cost.

## Get started

Try the hosted console, or evaluate locally from source:

```sh
git clone https://github.com/atoma-run/atoma.git
cd atoma
nvm install && nvm use
npm ci
npm run doctor
export TYPESAFE_API_KEY=...   # optional; ATOMA_JEV=0 disables Jev
npm run run:build -- "a Node CLI that converts CSV to JSON"
npm run viz:serve             # run timeline in the console
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Live showcase of delivered runs at [atoma.run](https://atoma.run); decision record [`docs/jev-decisions-2026-09-28.md`](https://github.com/atoma-run/atoma/blob/e85140ce3af18d67ed6665b64180104324332c8b/docs/jev-decisions-2026-09-28.md) and calibration notes [`docs/jev-calibration-2026-10-07.md`](https://github.com/atoma-run/atoma/blob/e85140ce3af18d67ed6665b64180104324332c8b/docs/jev-calibration-2026-10-07.md).

## Limits and data handling

Under active development and not independently audited; decision context (task text, evidence excerpts) is sent to TypeSafe. Shared-learning design means prompts/recipes are readable by other organisations' runs on the same instance.

## Review and maintenance

Reviewed **2026-10-05**; refreshed **2026-10-08** (Europe/Sofia) for the repository move at [commit e85140ce3af1](https://github.com/atoma-run/atoma/tree/e85140ce3af18d67ed6665b64180104324332c8b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Details from issue #1210 are attributed to that submission. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
