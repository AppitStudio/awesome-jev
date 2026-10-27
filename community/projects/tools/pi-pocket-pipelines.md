# Pi Pocket Pipelines (visual LLM workflow editor for Pi Pocket, with Jev decision nodes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Drop-in extension for Pi Pocket that adds a drag-and-drop pipeline canvas: chained LLM calls, parallel scout agents, loops, branches, shell commands, human approvals and nested pipelines, checkpointed so a restart resumes a run; a Decision node uses Jev (direct or via OpenRouter) to pick a category or answer yes or no, returning unsure below its line.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stilllostinla/pi-pocket-pipelines) |
| Maintainer | [stilllostinla](https://github.com/stilllostinla). Independently curated. |
| Format | Pi Pocket extension (TypeScript) |
| Requirements | Pi Pocket; a TypeSafe or OpenRouter key for Decision nodes. |
| License | [MIT](https://github.com/stilllostinla/pi-pocket-pipelines/blob/e2c581342a2ce49b18d4627229efcb9f66c741cb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipelines.ts`](https://github.com/stilllostinla/pi-pocket-pipelines/blob/e2c581342a2ce49b18d4627229efcb9f66c741cb/pipelines.ts) at the pinned commit. |

## When to use

- Build branching agent workflows visually, with a typed decision at each fork.
- Mismatch: Pi Pocket only.

## How it works

`pipelines.ts` posts Decision nodes to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) or OpenRouter's `/v1/systemone` (`typesafe/jev-1.14`) and routes on the answer. Integration evidence: [`pipelines.ts`](https://github.com/stilllostinla/pi-pocket-pipelines/blob/e2c581342a2ce49b18d4627229efcb9f66c741cb/pipelines.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/stilllostinla/pi-pocket-pipelines && cd pi-pocket-pipelines
./install.sh   # then Menu → Extensions → Pipelines → on
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/stilllostinla/pi-pocket-pipelines#readme](https://github.com/stilllostinla/pi-pocket-pipelines#readme)

## Limits and data handling

Decision node inputs go to TypeSafe or OpenRouter.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit e2c581342a2c](https://github.com/stilllostinla/pi-pocket-pipelines/tree/e2c581342a2ce49b18d4627229efcb9f66c741cb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
