# jev-interceptor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code `UserPromptSubmit` hook (repo `jev-setup`) that asks TypeSafe Jev a few typed questions about every prompt and tells Claude where the work should run — on Claude or an open-model lane (ClinePass via `pi`, or Codex) — returning the answer as `additionalContext`; a one-command installer also sets up companion skills, a fast Jev compaction plugin and a spend log, with OpenRouter as a backup path.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rayopavri/jev-setup) |
| Maintainer | [rayopavri](https://github.com/rayopavri). Independently curated. |
| Format | Claude Code plugin/skill + `setup.sh` installer |
| Requirements | macOS, Claude Code, git, Python 3.10+; TypeSafe API key; optional Node/`pi`, Codex and OpenRouter. |
| License | [MIT](https://github.com/rayopavri/jev-setup/blob/1e6dd83ed795b2822bfe72dcbeb47f434e2ca43f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Offload routine work from Claude to open-model lanes automatically.
- Mismatch: opinionated setup modelled on one Mac; many optional pieces.

## How it works

[`hooks/hooks.json`](https://github.com/rayopavri/jev-setup/blob/1e6dd83ed795b2822bfe72dcbeb47f434e2ca43f/hooks/hooks.json) runs [`scripts/jev-refine.py`](https://github.com/rayopavri/jev-setup/blob/1e6dd83ed795b2822bfe72dcbeb47f434e2ca43f/scripts/jev-refine.py) on each prompt; thresholds and wording live in the scripts. [`setup/manifest.json`](https://github.com/rayopavri/jev-setup/blob/1e6dd83ed795b2822bfe72dcbeb47f434e2ca43f/setup/manifest.json) lists what the installer adds.

## Get started

One-command install (README *Quick install*; add `--dry-run` to preview):

```sh
mkdir -p ~/.claude/skills
git clone https://github.com/rayopavri/jev-setup.git ~/.claude/skills/jev-interceptor
~/.claude/skills/jev-interceptor/setup.sh install --dry-run
```

One Jev request per prompt on your key; lanes bill their own providers.

## Examples and demos

- Routing report script: [`scripts/jev-routing-report.py`](https://github.com/rayopavri/jev-setup/blob/1e6dd83ed795b2822bfe72dcbeb47f434e2ca43f/scripts/jev-routing-report.py).

## Limits and data handling

Prompt text goes to TypeSafe (or OpenRouter as backup). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 1e6dd83ed795](https://github.com/rayopavri/jev-setup/tree/1e6dd83ed795b2822bfe72dcbeb47f434e2ca43f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
