# factory (Claude Code plugin that works a GitHub Project board, with optional Jev decision points)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that takes cards from a GitHub Project board through Build, QA and Review lanes, each run by its own subagent (or Codex), and opens merged PRs with evidence; optional Jev decision points start in shadow mode, logging Jev's answer next to Claude's so you can check agreement and spend before letting Jev decide.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/benbooth493/factory) |
| Maintainer | [benbooth493](https://github.com/benbooth493). Independently curated. |
| Format | Claude Code plugin with Python scripts |
| Requirements | Claude Code and a GitHub Project; a Vercel AI Gateway key for the optional Jev points. |
| License | [MIT](https://github.com/benbooth493/factory/blob/d8b646118976e1457c83eb304987e86ae77aefb8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev.py`](https://github.com/benbooth493/factory/blob/d8b646118976e1457c83eb304987e86ae77aefb8/scripts/jev.py) at the pinned commit. |

## When to use

- Hand a backlog of well-specified cards to coding agents with QA and review gates.
- Trial Jev on routing and grading decisions in shadow mode first.
- Mismatch: Jev is optional and reached through Vercel AI Gateway.

## How it works

`scripts/jev.py` calls `typesafe-ai/jev` through Vercel AI Gateway for each enabled decision point and records agreement and cost (`jev.py report`). Integration evidence: [`scripts/jev.py`](https://github.com/benbooth493/factory/blob/d8b646118976e1457c83eb304987e86ae77aefb8/scripts/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add benbooth493/factory
/plugin install factory@factory
python3 scripts/jev.py check   # optional Jev connectivity check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/benbooth493/factory#readme](https://github.com/benbooth493/factory#readme)

## Limits and data handling

Card and PR context goes to Vercel AI Gateway and TypeSafe at enabled Jev points; code work runs through your own Claude Code session.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit d8b646118976](https://github.com/benbooth493/factory/tree/d8b646118976e1457c83eb304987e86ae77aefb8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
