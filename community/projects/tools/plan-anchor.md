# plan-anchor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code and Codex skill that records facts you state while planning as numbered anchors, turns them into typed questions for TypeSafe Jev, and runs gates against the plan and the delivered work, quoting your words back when something drifts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/randlee/plan-anchor) |
| Maintainer | [randlee](https://github.com/randlee). Independently curated. |
| Format | Agent skill (Claude Code, Codex) |
| Requirements | Claude Code or Codex; `TYPESAFE_API_KEY` plus explicit opt-in `PLAN_ANCHOR_ALLOW_REMOTE_JUDGE=1`. |
| License | [MIT](https://github.com/randlee/plan-anchor/blob/7c1f1ce1795a8a307e165180d760e00cbdd07f53/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Stop long planning sessions from silently dropping concrete instructions.
- Mismatch: Requires Jev; anchor and plan text is sent to the hosted API.

## How it works

Anchors are captured verbatim and checked against a testability rubric; at each gate the skill asks Jev typed questions per anchor and reports drift. (Summarized from the upstream [README](https://github.com/randlee/plan-anchor/blob/7c1f1ce1795a8a307e165180d760e00cbdd07f53/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install the skill into Claude Code or Codex per the upstream README and set the API key and opt-in variable.

## Limits and data handling

Without the key and opt-in the skill refuses and sends nothing; with them, scoped text goes to `api.typesafe.ai`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 7c1f1ce1795a](https://github.com/randlee/plan-anchor/tree/7c1f1ce1795a8a307e165180d760e00cbdd07f53). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
