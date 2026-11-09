# ai-maestro-janitor (Claude Code janitor plugin with Jev-scored context compaction)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Session-scoped Claude Code plugin that reconciles todo lists, PRs and worktrees with the repo and handles rate-limit resume; its compaction scores transcript items with Jev before re-injecting context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Emasoft/ai-maestro-janitor) |
| Maintainer | [Emasoft](https://github.com/Emasoft). Independently curated. |
| Format | Claude Code plugin (Python/uv, MIT) |
| Requirements | Claude Code, uv, git, gh, and a TypeSafe or OpenRouter key for Jev compaction. |
| License | [MIT](https://github.com/Emasoft/ai-maestro-janitor/blob/3b81287f2dcfbf64ee7a31b1b8a5e2fd3077c8ab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/lib/jev_compaction.py`](https://github.com/Emasoft/ai-maestro-janitor/blob/3b81287f2dcfbf64ee7a31b1b8a5e2fd3077c8ab/scripts/lib/jev_compaction.py) at the pinned commit. |

## When to use

- Keep long Claude Code sessions consistent with the repo.
- Compact context by Jev relevance scores.
- Mismatch: Jev is used only for compaction.

## How it works

`jev_compaction.py` scores each old transcript item through Jev; `jevctx/jev.py` posts to `https://api.typesafe.ai/v1/systemone` (OpenRouter provider also included) and `/janitor-compact-context` runs it on demand. Integration evidence: [`scripts/lib/jev_compaction.py`](https://github.com/Emasoft/ai-maestro-janitor/blob/3b81287f2dcfbf64ee7a31b1b8a5e2fd3077c8ab/scripts/lib/jev_compaction.py).

## Get started

Install the plugin in Claude Code, run `/janitor-arm`, and set your Jev key for compaction.

```sh
git clone https://github.com/Emasoft/ai-maestro-janitor.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Emasoft/ai-maestro-janitor/blob/3b81287f2dcfbf64ee7a31b1b8a5e2fd3077c8ab/README.md](https://github.com/Emasoft/ai-maestro-janitor/blob/3b81287f2dcfbf64ee7a31b1b8a5e2fd3077c8ab/README.md)

## Limits and data handling

Transcript items are sent to TypeSafe/OpenRouter during compaction.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 3b81287f2dcf](https://github.com/Emasoft/ai-maestro-janitor/tree/3b81287f2dcfbf64ee7a31b1b8a5e2fd3077c8ab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
