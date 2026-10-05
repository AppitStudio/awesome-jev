# atoma

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent coordination platform (hosted atoma.run or self-hosted, AGPL-3.0) that turns a request into checked work; TypeSafe Jev takes bounded decisions such as which agent or recipe takes a task and whether a plan is approved.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mgtf/atoma) |
| Product homepage | [atoma.run](https://atoma.run) |
| Maintainer | [mgtf](https://github.com/mgtf). Independently curated. |
| Format | Hosted web service and self-hostable source (under active development) |
| Requirements | Hosted: sign in at atoma.run. Self-host: pinned Node, macOS/Linux (or WSL2), model-provider keys; Jev is enabled when the host has `TYPESAFE_API_KEY` unless `ATOMA_JEV=0`. |
| License | [AGPL-3.0](https://github.com/mgtf/atoma/blob/5ad69908b7cdf06662ad5d73844b074e96c0e127/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Hosted service at atoma.run; pricing/terms not verified for this listing. Upstream warns not to submit confidential or personal data. |

## When to use

- Evaluate an agent system where cheap typed decisions handle routing and plan approval while generative models do the work.
- Inspect per-decision latency and cost on a run timeline.
- Mismatch: confidential data (upstream explicitly warns against it); runs share learned prompts/recipes across organisations by design.

## How it works

Jev selects a registered agent/recipe, approves intermediate plans and results when evidence permits, and avoids learning equivalent recipes; uncertain or unavailable answers fall back to the generative models, and final delivery acceptance stays independent of Jev ([architecture guide](https://github.com/mgtf/atoma/blob/5ad69908b7cdf06662ad5d73844b074e96c0e127/docs/how-it-works.md)).

## Get started

Try the hosted console, or evaluate locally from source:

```sh
git clone https://github.com/mgtf/atoma.git
cd atoma
nvm install && nvm use
npm ci
npm run doctor
export TYPESAFE_API_KEY=...   # optional; ATOMA_JEV=0 disables Jev
npm run run:build -- "a Node CLI that converts CSV to JSON"
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Live showcase of delivered runs at [atoma.run](https://atoma.run); decision record `docs/jev-decisions-2026-09-28.md`.

## Limits and data handling

Under active development and not independently audited; decision context (task text, evidence excerpts) is sent to TypeSafe. Shared-learning design means prompts/recipes are readable by other organisations' runs on the same instance.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 5ad69908b7cd](https://github.com/mgtf/atoma/tree/5ad69908b7cdf06662ad5d73844b074e96c0e127). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
