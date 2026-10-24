# Jev Workflow by cathy-kim (Claude Code plugin and guide for designing Jev decisions offline)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Community toolkit for designing typed decision workflows: a portable skill with Claude Code, Codex and Hermes adapters, offline examples, an illustrated guide, and an opt-in live client and stdio MCP server for TypeSafe System One, OpenAI Decisions and OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cathy-kim/jev-workflow) |
| Maintainer | [cathy-kim](https://github.com/cathy-kim). Independently curated. |
| Format | Claude Code plugin, agent skill and Python CLI/MCP server |
| Requirements | Claude Code or another skill-capable agent; Python for the scripts; a provider key only for live calls. |
| License | [MIT](https://github.com/cathy-kim/jev-workflow/blob/050656ddf6d26376feb39b1350ca6799982a7fa4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/jev/skills/jev-decisions/scripts/jev_workflow/client.py`](https://github.com/cathy-kim/jev-workflow/blob/050656ddf6d26376feb39b1350ca6799982a7fa4/plugins/jev/skills/jev-decisions/scripts/jev_workflow/client.py) at the pinned commit. |

## When to use

- Design and test Jev questions offline before wiring them into an app.
- Give a coding agent a skill for Noul, Choice and Score workflows.
- Mismatch: the guide is in Korean; live calls are off unless you pass --live.

## How it works

`jev_workflow/client.py` builds requests for TypeSafe `/v1/systemone` (or OpenAI Decisions or OpenRouter) and sends them only with `--live`; `decision_kit.py` provides the offline examples. Integration evidence: [`plugins/jev/skills/jev-decisions/scripts/jev_workflow/client.py`](https://github.com/cathy-kim/jev-workflow/blob/050656ddf6d26376feb39b1350ca6799982a7fa4/plugins/jev/skills/jev-decisions/scripts/jev_workflow/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add cathy-kim/jev-workflow
claude plugin install jev@jev-workflow
# then: /jev:jev-decisions Design a support-routing workflow. Keep it offline.
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Website and guide: [cathy-kim.github.io/jev-workflow/](https://cathy-kim.github.io/jev-workflow/)
- README: [github.com/cathy-kim/jev-workflow#readme](https://github.com/cathy-kim/jev-workflow#readme)

## Limits and data handling

Nothing is sent unless you run a live command; then your state goes to the chosen provider. Distinct from the listed gbesse Jev workflow.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 050656ddf6d2](https://github.com/cathy-kim/jev-workflow/tree/050656ddf6d26376feb39b1350ca6799982a7fa4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
