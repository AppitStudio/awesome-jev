# jev-audit (agent skill)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill (`SKILL.md`) for Claude Code, Codex, Cursor and similar agents that audits a codebase for brittle rules guessing at facts the data does not state, ranks where a Jev question could replace them, and writes one `JEV_OPPORTUNITIES.md` report with evidence, gap/stakes/fit scores, a replacement sketch that keeps reliable checks in code, cost and latency notes, and a measurement plan.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/idogoldd/skills) |
| Maintainer | [idogoldd](https://github.com/idogoldd). Independently curated. |
| Format | Agent skill (Markdown), installable with `npx skills` |
| Requirements | An agent that reads `SKILL.md` files. The skill itself makes no Jev calls. |
| License | [MIT](https://github.com/idogoldd/skills/blob/1815abf8fd9054413a4d3bf6d3cd0f0791943b07/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Find candidate places to adopt Jev in an existing codebase before writing any integration.
- Mismatch: it produces a report only; it does not change code or measure accuracy for you.

## How it works

The skill instructions are in [`skills/jev-audit/SKILL.md`](https://github.com/idogoldd/skills/blob/1815abf8fd9054413a4d3bf6d3cd0f0791943b07/skills/jev-audit/SKILL.md). It reads code and git history, and production samples only through a read-only route you allow.

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add idogoldd/skills --skill jev-audit
# then ask your agent: "Find Jev opportunities in this repo."
```

## Limits and data handling

Runs inside your coding agent, so code and any allowed samples are processed by that agent's model provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 1815abf8fd90](https://github.com/idogoldd/skills/tree/1815abf8fd9054413a4d3bf6d3cd0f0791943b07). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
