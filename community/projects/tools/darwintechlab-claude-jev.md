# claude-jev (darwintechlab)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin + MCP that exposes TypeSafe Jev Choice/Noul/Score tools (`jev_choice`, `jev_noul`, `jev_score`, `jev_ask`, `jev_doctor`) for fast typed agent decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/darwintechlab/claude-jev) |
| Maintainer | [darwintechlab](https://github.com/darwintechlab) ([darwintechlab.com](https://darwintechlab.com)). Independently curated. |
| Format | Claude Code plugin / MCP (`jev`). |
| Requirements | Claude Code ≥ 2.0; Node ≥ 20; `TYPESAFE_API_KEY` (live-only—no mock fallback). |
| License | [MIT](https://github.com/darwintechlab/claude-jev/blob/5063d50131eba36596f95c79bf6dd3e105bf38cb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/Claude sessions not run. Distinct from [claude-jev-funnel](claude-jev-funnel.md) and [claude-code-jev](claude-code-jev.md). |

## When to use

Use when Claude Code should **delegate small multi-choice judgments** to Jev with confidence labels (`auto` / `escalate`). Prefer [claude-jev-funnel](claude-jev-funnel.md) for bulk YES/NO triage of large item lists.

## How it works

Installing the plugin registers MCP tools and a skill so Claude can call typed System One questions; answers stay within the supplied options and include calibrated confidence (per README).

## Get started

```sh
claude plugin marketplace add darwintechlab/claude-openjev
claude plugin install claude-jev@openjev
# or: claude --plugin-dir .
export TYPESAFE_API_KEY=ts_...
# Restart Claude Code; run jev_doctor
```

Pin review tip: `5063d50131eba36596f95c79bf6dd3e105bf38cb`. See [SETUP.md](https://github.com/darwintechlab/claude-jev/blob/5063d50131eba36596f95c79bf6dd3e105bf38cb/SETUP.md).

## Examples and demos

- README support-ticket routing table with confidence thresholds.
- Live-only bench notes in README (p50 latency ~307 ms upstream-reported).

## Limits and data handling

Without `TYPESAFE_API_KEY`, calls fail explicitly. Agent context you pass reaches TypeSafe. No offline mock mode in this package.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 5063d50](https://github.com/darwintechlab/claude-jev/tree/5063d50131eba36596f95c79bf6dd3e105bf38cb). AI-assisted README and LICENSE inspection; live doctor check not run.

Related: [claude-jev-funnel](claude-jev-funnel.md), [askjev](askjev.md).
