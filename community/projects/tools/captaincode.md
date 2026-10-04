# Captain Code

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One terminal that routes tasks across Claude Code, Codex, Cursor, and opencode models, with an optional Jev decision leg for triage, an action gate, and supervision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lemma-ventures/captaincode) |
| Product homepage | [captaincode.ai](https://captaincode.ai) |
| Maintainer | [lemma-ventures](https://github.com/lemma-ventures). Independently curated. |
| Format | CLI director for coding agents; Jev leg optional |
| Requirements | Go (`go install`) or source; the agent CLIs you already use; optional `TYPESAFE_API_KEY` from console.typesafe.ai for the Jev leg. |
| License | [MIT](https://github.com/lemma-ventures/captaincode/blob/3d5b594137ba165ec164dc1d2066c2a434630aae/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Hand a task to another agent when one hits a usage limit or refusal.
- Use Jev to triage tasks and gate risky worker actions, and measure it in shadow mode first.
- Mismatch: without a key, Captain Code still works; Jev-only features are disabled.

## How it works

A local director (`captain brain`) assigns tasks across agents. When configured, the Jev decision leg classifies tasks and judges what workers are about to do; upstream documents which Jev answers act and which are advisory.

## Get started

Install, initialize, and check the Jev leg:

```sh
go install github.com/lemma-ventures/captaincode/cmd/captaincode@latest
captain init
captain doctor
captain jev    # check the key and connection
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README section "Jev, the decision leg (optional)" and docs/CONFIGURATION.md.

## Limits and data handling

Jev calls send task text to TypeSafe and are billed; agent subscriptions are separate.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 3d5b594137ba](https://github.com/lemma-ventures/captaincode/tree/3d5b594137ba165ec164dc1d2066c2a434630aae). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
