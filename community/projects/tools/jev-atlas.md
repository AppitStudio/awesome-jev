# Jev Atlas

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code / Codex skill that maps where a repository makes, avoids, or could make semantic decisions, kills weak Jev candidates with published rejection rules, then validates and implements the survivors from structured `.jev-atlas/` state (not brainstorm Markdown alone).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/v60samurai/jev-atlas) |
| Maintainer | [v60samurai](https://github.com/v60samurai) (Harshit Badiger). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill under `skills/jev-atlas/` (plugin `jev-atlas` **0.2.0** via `.claude-plugin/`); `install.sh` for Codex/Claude skill dirs. |
| Requirements | Claude Code and/or Codex with skills/plugins enabled. Mapping/validation that call TypeSafe need `TYPESAFE_API_KEY` (or the host's configured TypeSafe path). Companion **`typesafe-ai` skill** for API/question mechanics. |
| License | [MIT](https://github.com/v60samurai/jev-atlas/blob/e780e4d6f2f4eb72f6c7f6d5b92e7ab0041e8e10/LICENSE). TypeSafe usage billed separately when validation/implementation runs live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source review only (no automated test suite in-repo). No live TypeSafe calls. Distinct from [prompt2jev](prompt2jev.md) (prompt→decision package) and [decision-first](decision-first.md) (adopt/decline logging). |

## When to use

Use it when you want a disciplined search for System One fit in an existing codebase—including places the code currently refuses to decide—rather than a flat "where can I slap Jev?" list. Prefer [prompt2jev](prompt2jev.md) once a single judgment is already chosen and needs a verified request JSON.

## How it works

[`skills/jev-atlas/SKILL.md`](https://github.com/v60samurai/jev-atlas/blob/e780e4d6f2f4eb72f6c7f6d5b92e7ab0041e8e10/skills/jev-atlas/SKILL.md) defines Map / Consult / Validate / Implement / Sync modes. References under `skills/jev-atlas/references/` cover decision-surface inventory, triage gates, experiments, and state. Map writes at most eight anchored records into `.jev-atlas/`, opens a local review UI, and treats Markdown as export. API contracts stay with the `typesafe-ai` skill so this skill does not go stale on model versions.

## Get started

```sh
git clone https://github.com/v60samurai/jev-atlas.git
cd jev-atlas
git checkout e780e4d6f2f4eb72f6c7f6d5b92e7ab0041e8e10
./install.sh both          # or: claude plugin marketplace add v60samurai/jev-atlas
# Then ask the agent: "run Jev Atlas on this repo" / "validate JEV-003"
```

Live Validate/Implement paths that call TypeSafe send project-derived evidence and can incur charges. Install alone does not.

## Examples and demos

- `examples/` sample records (accepted component, rejected idea, new capability).
- README workflow diagram and rejection/anchor rules (author-documented; not re-run as live Atlas map here).

## Limits and data handling

The skill is read-only on your source except the `.jev-atlas/` state directory it writes. Live judgments leave the host. Most candidates are expected to be killed; "change nothing" is a valid result. This listing did not run a full Map against a private product repo.

## Review and maintenance

Reviewed on **2026-09-21** at [commit e780e4d](https://github.com/v60samurai/jev-atlas/tree/e780e4d6f2f4eb72f6c7f6d5b92e7ab0041e8e10): plugin **0.2.0**, MIT. AI-assisted source review of README, LICENSE, `SKILL.md`, `plugin.json`, `install.sh`, and references tree. No automated tests executed; no live TypeSafe calls.

Related: [prompt2jev](prompt2jev.md), [decision-first](decision-first.md), [ask-jev-skill](ask-jev-skill.md).
