# Agent Approve by Agent Approve LLC (iPhone and Apple Watch approvals for AI coding agents, with Jev-powered Policy Rules that check each action)

[All projects](../README.md) · [iOS apps](README.md#ios-apps)

Monitor Claude Code, Codex, Cursor and other coding agents from an iPhone or Apple Watch and approve or deny their requests away from the keyboard. Version 0.9 adds Policy Rules powered by Jev: rules you write (with examples and counterexamples) are checked against agent actions that the Allow, Deny and Ask lists have not already decided.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://agentapprove.com) |
| Tags | `Closed source` · `Paid` · `Commercial` |
| Product homepage | [agentapprove.com](https://agentapprove.com) |
| Pricing and access | Paid subscription: Solo $7.99/month (5,000 AI credits, 3 agents or subagents at once) and Pro $14.99/month (15,000 AI credits, 7 at once), chosen in the app; eligible new subscribers get a 7-day free trial with 2,000 AI credits ([pricing](https://agentapprove.com/pricing), checked 2026-11-26). Rule checks through Agent Approve Fast use plan credits; no separate TypeSafe key is needed. |
| Jev evidence | Vendor statements: the [0.9 changelog](https://agentapprove.com/changelog) (21 Nov 2026) says "Jev is the default decision model behind Agent Approve Fast", the [pricing page](https://agentapprove.com/pricing) lists "Check actions with Policy Rules powered by Jev", and the maker's [launch post on X](https://x.com/agentapprove/status/2125009080440025264) credits @typesafeai. The implementation was not inspected. |
| Disclosure | Closed source, commercial product with paid plans and a trial. Source was not inspected; Jev use is the vendor's public statement, not independently observed API traffic. Independently curated for Awesome Jev; no affiliation or commercial relationship with the vendor. Inclusion is not an endorsement or a purchase recommendation. Discovered via X ([post](https://x.com/agentapprove/status/2125009080440025264)). |
| Maintainer | Agent Approve LLC ([@agentapprove](https://x.com/agentapprove/status/2125009080440025264) on X). |
| Format | iPhone and Apple Watch app with a hosted relay service and agent hooks. |
| Platform and availability | iPhone and Apple Watch app (App Store) plus an installer that adds hooks to the coding agents on your computer (Cursor, Claude Code, Codex, Antigravity, OpenCode, Pi, Hermes, OpenClaw, OpenHands, VS Code Copilot, Copilot CLI, Windsurf). |
| Jev's role | Per the vendor, Jev is the default decision model behind Agent Approve Fast: it checks each undecided agent action against your Policy Rules, with a per-rule match threshold; you can connect your own decision-model provider instead. |
| Requirements | An iPhone (Apple Watch optional), a paid Solo or Pro plan after the trial, and a computer running a supported coding agent; agent events pass through Agent Approve's cloud. |
| License | Proprietary app and service. The [agentapprove](https://github.com/agentapprove) GitHub organization publishes the Agent Event Protocol and a decision-policy-rules research repo under custom terms; the app itself is not public. |

## When to use

Use Agent Approve if you leave coding agents running and want to approve or block their tool calls from your phone or watch, with written rules that Jev checks so routine actions do not all need a tap. Mismatch: if you need a self-hosted or open-source approval gate, or you cannot send agent activity through a third-party cloud.

## How it works

Per the vendor, the installer adds hooks to your coding agents. Each event goes through Agent Approve's cloud to the app. Allow, Deny and Ask lists are applied first; an action they have not already decided is checked against your Policy Rules (library rules or your own definitions, examples and counterexamples, up to 16 per policy) by Jev through Agent Approve Fast, or by a decision-model provider you connect. Anything left goes to your phone or watch for a tap. No API calls, questions or thresholds were observed for this listing.

## Get started

This path follows the vendor's public pages; it was not executed.

1. Install Agent Approve on your iPhone from the App Store ([download page](https://agentapprove.com)).
2. Run the installer on your computer to set up hooks for your agents, then scan the QR code to pair your device and choose a privacy level.
3. Choose Solo or Pro in the app (7-day trial for eligible new subscribers), add Policy Rules, and approve requests from your phone or watch.

## Examples and demos

- [0.9 launch post with video](https://x.com/agentapprove/status/2125009080440025264) (vendor material).
- [Changelog: Policy Rules powered by Jev](https://agentapprove.com/changelog) (vendor material).

## Limits and data handling

Closed source: how Jev is called and which parts of an agent action it sees were not inspected. Hooks send agent events through Agent Approve's cloud; the vendor says you choose a privacy tier, retention period and end-to-end encryption, and that rule evaluation through Agent Approve Fast uses zero-data-retention controls, including its fallback routes (vendor claims, not verified). Rule checks consume plan AI credits. A policy check is a judgment aid, not a security boundary; review what your agents can do without approval.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) with AI assistance. Primary sources: [agentapprove.com](https://agentapprove.com), the [pricing page](https://agentapprove.com/pricing) and the [changelog](https://agentapprove.com/changelog) (all fetched 2026-11-26), and the vendor's [X post](https://x.com/agentapprove/status/2125009080440025264) (2026-11-23). No download, sign-up or live use.
