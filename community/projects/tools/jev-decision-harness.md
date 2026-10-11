# jev-decision-harness

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

jev-decision-harness is a Claude Code plugin and CLI that adds bounded, typed Jev decisions around Claude Code hooks: prompt triage, Bash command risk scoring, failure classification and end-of-turn review, while deterministic policy keeps permissions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chhetri123/jev-decision-harness) |
| Maintainer | [chhetri123](https://github.com/chhetri123). Independently curated. |
| Format | Claude Code plugin and Node CLI |
| Requirements | Claude Code; Node.js 20+; a TypeSafe API key. |
| License | [MIT](https://github.com/chhetri123/jev-decision-harness/blob/8e17b9f01edd897c561bb5c57241e4e0a9ad8282/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Gate risky shell commands and add triage context in Claude Code without letting a model grant permissions.
- Mismatch: Claude Code only; Jev can only deny or ask, never allow.

## How it works

Hooks run deterministic rules first and only ask Jev narrow typed questions for cases no rule decides; errors or a missing key leave Claude Code unchanged. (Summarized from the upstream [README](https://github.com/chhetri123/jev-decision-harness/blob/8e17b9f01edd897c561bb5c57241e4e0a9ad8282/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Export `TYPESAFE_API_KEY`, install the plugin in Claude Code, and run `/jev-init` in a project.

## Limits and data handling

Prompts, commands and diffs summaries are sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 8e17b9f01edd](https://github.com/chhetri123/jev-decision-harness/tree/8e17b9f01edd897c561bb5c57241e4e0a9ad8282). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
