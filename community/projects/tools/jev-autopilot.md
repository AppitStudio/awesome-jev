# jev-autopilot

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that keeps unattended sessions moving: TypeSafe Jev answers Claude's routine questions, screens every non-read-only tool call, and holds risky ones until you tap Proceed or Block on your phone via Telegram; falls back to the terminal when Jev is unreachable.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hmcdaniel03/jev-autopilot) |
| Maintainer | [hmcdaniel03](https://github.com/hmcdaniel03). Independently curated. |
| Format | Claude Code plugin (marketplace install) with hooks and `/autopilot` commands |
| Requirements | Claude Code; `TYPESAFE_API_KEY`; a Telegram bot token and pairing for phone approvals (guided by `/autopilot setup`). |
| License | [MIT](https://github.com/hmcdaniel03/jev-autopilot/blob/7584d38f0329906c17bade637e98bf30e39d1a39/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let long agent runs continue through routine questions without sitting at the terminal.
- Require a phone tap before destructive or risky tool calls while unattended.
- Mismatch: Jev is an added safety layer, not the only one; read the upstream threat model.

## How it works

Hooks in [`hooks/core.ts`](https://github.com/hmcdaniel03/jev-autopilot/blob/7584d38f0329906c17bade637e98bf30e39d1a39/hooks/core.ts) and [`hooks/register.ts`](https://github.com/hmcdaniel03/jev-autopilot/blob/7584d38f0329906c17bade637e98bf30e39d1a39/hooks/register.ts) intercept Claude's questions and tool calls; Jev suggests an answer or a hold decision and held calls go to Telegram. Without a key or when the API is down, questions are asked in the terminal as usual. Decision details: [`wiki/Jev-and-TypeSafe.md`](https://github.com/hmcdaniel03/jev-autopilot/blob/7584d38f0329906c17bade637e98bf30e39d1a39/wiki/Jev-and-TypeSafe.md).

## Get started

Install from the plugin marketplace, then run setup inside Claude Code:

```sh
claude plugin marketplace add hmcdaniel03/jev-autopilot
claude plugin install jev-autopilot@jev-autopilot
# inside Claude Code:
/autopilot setup
```

Each screened question or tool call is a Jev request billed to your TypeSafe key.

## Examples and demos

- README *How decisions are made* and *Threat model*.
- Decision log documentation: [`wiki/Decision-Log.md`](https://github.com/hmcdaniel03/jev-autopilot/blob/7584d38f0329906c17bade637e98bf30e39d1a39/wiki/Decision-Log.md).

## Limits and data handling

Questions, options and up to 900 characters of held commands/paths go to Telegram while autopilot is on; decision context goes to TypeSafe (upstream privacy section). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 7584d38f0329](https://github.com/hmcdaniel03/jev-autopilot/tree/7584d38f0329906c17bade637e98bf30e39d1a39). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
