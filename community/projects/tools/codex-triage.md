# codex-triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Codex task triage dashboard with human-reviewed archiving and optional TypeSafe Jev analysis of tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WesleySmits/codex-triage) |
| Maintainer | [WesleySmits](https://github.com/WesleySmits). Independently curated. |
| Format | TypeScript local app/CLI. |
| Requirements | Node.js; local Codex task data; optional `TYPESAFE_API_KEY` for Jev analysis. |
| License | [MIT](https://github.com/WesleySmits/codex-triage/blob/b282619a776a0e35e88568fc1b2b44c2c782e746/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live triage UI not run. |

## When to use

Use to **review and archive** local Codex tasks with optional Jev help. Prefer Jev Runway for online token trimming during live Codex sessions.

## How it works

Local-first dashboard lists Codex tasks; humans archive; optional Jev analysis annotates items (per README).

## Get started

```sh
git clone https://github.com/WesleySmits/codex-triage.git
cd codex-triage
git checkout b282619a776a0e35e88568fc1b2b44c2c782e746
# npm install / run per README
```

## Examples and demos

- README local-first workflow notes.

## Limits and data handling

Task text may reach TypeSafe when Jev analysis is enabled. Archiving is human-gated.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit b282619](https://github.com/WesleySmits/codex-triage/tree/b282619a776a0e35e88568fc1b2b44c2c782e746). AI-assisted README inspection; live UI not run.
