# grokbot-jev-skills

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ten Grok Bot agent skills, adapted from hermes-jev-skills, that hand small decisions — which search results to read, passage filtering and injection screening, mailbox sort, support triage, routine wake-ups, transcript cutting — to TypeSafe Jev through a `jev` CLI; fail-open, with documented redaction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fal3/grokbot-jev-skills) |
| Maintainer | [fal3](https://github.com/fal3). Independently curated. |
| Format | Skill pack with `install.sh` (pins the upstream `jev` CLI from hermes-jev-skills at a tested commit) |
| Requirements | Grok Bot (skills folder) or `--skills-dir`; Git; `TYPESAFE_API_KEY` (falls back to OpenRouter, Venice or OpenCode Zen keys if present — set `JEV_PROVIDER` to pin). |
| License | [MIT](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let an agent decide which search results to open, or whether a scheduled routine should notify the user.
- Screen retrieved passages for prompt injection before an agent reads them.
- Mismatch: a port — the CLI and most logic come from hermes-jev-skills (also listed); `jev ask` sends input unredacted.

## How it works

[`install.sh`](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/install.sh) clones the upstream client to a local folder, checks out the tested commit, writes a `jev` launcher and copies the skills (e.g. [`jev-search-loop`](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/skills/jev-search-loop/SKILL.md), [`jev-passage-filter`](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/skills/jev-passage-filter/SKILL.md), [`jev-routine-wake`](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/skills/jev-routine-wake/SKILL.md)) into the agent's skill folder only if it exists. Each skill tells the agent which `jev` command to run; every decision command exits 0 with a usable fallback. [`tools/verify_skills.py`](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/tools/verify_skills.py) and a mock Jev check the skills offline.

## Get started

Preview, then install:

```sh
git clone https://github.com/fal3/grokbot-jev-skills ~/.local/share/grokbot-jev-skills
bash ~/.local/share/grokbot-jev-skills/install.sh --check   # shows the plan, changes nothing
bash ~/.local/share/grokbot-jev-skills/install.sh
jev doctor
```

Each decision is a Jev request billed to the provider key in use.

## Examples and demos

- README *What Jev decides here* table (ten skills) and *Fail-open, and the two exceptions*.
- Upstream mapping per skill: [`NOTICE`](https://github.com/fal3/grokbot-jev-skills/blob/74721c8cdae3b022933c0e354d8b95a09099219f/NOTICE); the original pack is listed as [hermes-jev-skills](hermes-jev-skills.md).

## Limits and data handling

Commands send redacted, capped slices (emails, phones, tokens masked) except `jev ask`, which sends input as given (upstream). Independent project, not affiliated with TypeSafe or Grok Bot's maker; AppitStudio has no affiliation. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 74721c8cdae3](https://github.com/fal3/grokbot-jev-skills/tree/74721c8cdae3b022933c0e354d8b95a09099219f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
