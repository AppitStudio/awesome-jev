# pbi-orchestration-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill that turns multi-file implementation into Product Backlog Items for sub-agents (Codex, Antigravity, Claude Code Agent), with TypeSafe Jev involved in model routing and result review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/reeschan/pbi-orchestration-jev) |
| Maintainer | [reeschan](https://github.com/reeschan). Independently curated. |
| Format | Python · Claude Code skill |
| Requirements | Claude Code; optional Codex/Antigravity CLIs; TypeSafe key for Jev gates. |
| License | [MIT](https://github.com/reeschan/pbi-orchestration-jev/blob/dbc7feb024f7f31c1c2d8bbc9a959ef3dcbeaf77/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Orchestrate multi-agent coding with an explicit backlog and Jev checkpoints.
- Mismatch: Orchestrator still owns acceptance; Jev is advisory gating.

## How it works

Skill scripts call Jev helpers for routing/review decisions around PBI handoffs. Jev helpers: [`skills/pbi-orchestration-jev/jev/`](https://github.com/reeschan/pbi-orchestration-jev/tree/dbc7feb024f7f31c1c2d8bbc9a959ef3dcbeaf77/skills/pbi-orchestration-jev/jev).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/reeschan/pbi-orchestration-jev.git
# install skill per README (English/日本語)
```

## Limits and data handling

Task summaries sent to TypeSafe when Jev runs; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit dbc7feb024f7](https://github.com/reeschan/pbi-orchestration-jev/tree/dbc7feb024f7f31c1c2d8bbc9a959ef3dcbeaf77). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
