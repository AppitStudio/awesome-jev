# claude-jev by zachshallbetter (Claude Code plugin where Jev sorts, routes, triages and calibrates, with an optional prompt router and permission gate)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin built on the split "Jev decides, Claude writes". `/jev:jev sort`, `ask` and `route` sort, triages, flags or scores a pile of text (emails, tickets, invoices, logs, folders) with presets or your own questions, with a dry run, consent before anything leaves the machine and an "unsure" pile for you. `/jev:jev calibrate` checks whether Jev's confidence holds on your own labelled examples (a 66-message household set and HTML report ship with it). Optional, off by default: a prompt router that suggests one of four bundled helper agents, and a permission gate that auto-approves Bash commands Jev is sure are routine, behind a static risk list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zachshallbetter/claude-jev) |
| Maintainer | [zachshallbetter](https://github.com/zachshallbetter). Independently curated. |
| Format | Claude Code plugin (skill, agents and hooks; Python script; MIT OR Apache-2.0) |
| Requirements | Claude Code and a TypeSafe API key (`TYPESAFE_API_KEY`), or an OpenRouter key for its Jev route. |
| License | [MIT OR Apache-2.0](https://github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jev/scripts/jev.py`](https://github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/skills/jev/scripts/jev.py) at the pinned commit. |

## When to use

- Let Claude Code hand bulk sorting, routing and yes/no checks to a cheap typed model.
- Mismatch: tasks that need written answers; Jev only picks, scores and flags.

## How it works

`skills/jev/scripts/jev.py` calls `https://api.typesafe.ai` with a pinned `jev-1.13.0` (or `typesafe/jev-1.13` on OpenRouter); the same script doubles as an importable library, and `skills/jev/references/building.md` shows routing, guardrail and tool-gating patterns. Integration evidence: [`skills/jev/scripts/jev.py`](https://github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/skills/jev/scripts/jev.py).

## Get started

Add the marketplace and install the plugin in Claude Code, then set your key.

```sh
/plugin marketplace add zachshallbetter/claude-jev
/plugin install jev@claude-jev
# export TYPESAFE_API_KEY=... then: /jev:jev sort <folder>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/README.md](https://github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/README.md)
- Building guide: [github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/skills/jev/references/building.md](https://github.com/zachshallbetter/claude-jev/blob/71e5c0f75322e83150639302412ea5b77123d16f/skills/jev/references/building.md)

## Limits and data handling

Text you sort is sent to TypeSafe (or OpenRouter) on your key after a dry run and your consent. The router and permission gate are off by default; the gate never denies and your own deny rules still apply.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 71e5c0f75322](https://github.com/zachshallbetter/claude-jev/tree/71e5c0f75322e83150639302412ea5b77123d16f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
