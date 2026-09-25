# pi-typesafe-approve

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that auto-approves routine Bash commands with a System One / Jev decision model and escalates flagged or unsure commands to a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Davidasx/pi-typesafe-approve) |
| Maintainer | [Davidasx](https://github.com/Davidasx). Independently curated. Distinct from [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md). |
| Format | TypeScript Pi extension; user-supplied endpoint/model/key. |
| Requirements | Pi agent; configured System One-compatible endpoint (TypeSafe, OpenRouter Decisions/System One, OpenJEV, or local relay). |
| License | [MIT](https://github.com/Davidasx/pi-typesafe-approve/blob/726788811f0e75c76c04a561ee5a06785ea34cf0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Pi/TypeSafe paths not run on the review host. |

## When to use

Use when Pi should **triage shell commands** cheaply with typed Jev decisions instead of prompting on every Bash call. Prefer bash-guard when you want classification-focused policy with 1Password `op://` key refs as in that extension.

## How it works

Before execution, the extension asks the configured System One model about the command; routine commands pass, flagged/obfuscated ones escalate, and unreachable models fail open so the agent does not wedge.

## Get started

```sh
git clone https://github.com/Davidasx/pi-typesafe-approve.git
cd pi-typesafe-approve
git checkout 726788811f0e75c76c04a561ee5a06785ea34cf0
pi install ./
# Then /typesafe-approve to set endpoint, model, and API key
```

## Examples and demos

- `config.example.json` and README deployment table (TypeSafe / OpenRouter / OpenJEV / local).
- Decision log at `decisions.jsonl` beside config (mode `0600`, size-capped).

## Limits and data handling

Command text goes to the configured endpoint. API keys may be literals or `${ENV}` references. Fail-open on model outage is intentional per upstream.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 7267888](https://github.com/Davidasx/pi-typesafe-approve/tree/726788811f0e75c76c04a561ee5a06785ea34cf0). AI-assisted README and LICENSE inspection; Pi install not executed.
