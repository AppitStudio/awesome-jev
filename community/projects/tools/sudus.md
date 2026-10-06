# Sudus

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin (Claude Code, Codex, Muse; formerly Cairn) that keeps AI-assisted development tied to agreed scope, with an optional TypeSafe Jev evaluator (`typesafeai.enabled`) that measures the agent's draft at Consequential choices on five weighted dimensions instead of a harness review model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eas4ai/sudus) |
| Maintainer | [eas4ai](https://github.com/eas4ai). Independently curated. |
| Format | Agent plugin for Claude Code / Codex / Muse with the `sudus` command |
| Requirements | Node 24, Git 2.40+, Linux or macOS. Jev is optional: `typesafeai.enabled: true` and `TYPESAFEAI_API_KEY`; otherwise your harness's review model answers the brief. |
| License | [MIT](https://github.com/eas4ai/sudus/blob/f4e911809660a0b1427b3dea135abf26aa6e68bb/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep agents inside the agreed scope with requirement records and pass/fail mechanisms in Git.
- Swap a slow review-model sub-session for one typed Jev measurement at the few decisions that matter.
- Mismatch: Sudus does not run your agent and calls no model unless you enable the evaluator.

## How it works

At a Consequential choice the agent takes one measurement of its own draft: five scored dimensions over the same state. With `typesafeai.enabled` true, [`bin/typesafeai.mjs`](https://github.com/eas4ai/sudus/blob/f4e911809660a0b1427b3dea135abf26aa6e68bb/bin/typesafeai.mjs) sends them to Jev (`jev-1.13.0`) and combines the answers with configured weights against an `agent_ceiling`; with it off, `sudus measure --brief` prints a brief for your review model. The README reports both sources agreed on every draft in its in-tree benchmark (maintainer-reported).

## Get started

Install the plugin and enable the Jev evaluator in settings (live TypeSafe calls at Consequential choices):

```sh
# Claude Code
/plugin marketplace add eas4ai/sudus
/plugin install sudus@sudus
# enable Jev in settings: "typesafeai": { "enabled": true, "model": "jev-1.13.0" }
export TYPESAFEAI_API_KEY=your-key
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README sections *The evaluator: the agent's gut check* and *Set up jev in three steps*.
- `tests/typesafeai.test.mjs` for the evaluator client.

## Limits and data handling

Windows is not supported (hooks use symlinks and `$HOME`). The evaluator sends the draft state to TypeSafe. Note the key variable is `TYPESAFEAI_API_KEY` (not `TYPESAFE_API_KEY`). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit f4e911809660](https://github.com/eas4ai/sudus/tree/f4e911809660a0b1427b3dea135abf26aa6e68bb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
