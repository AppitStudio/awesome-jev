# jev-mem (must-lioncho)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Memory plugin for Claude Code, Codex, and Antigravity that keeps claude-mem style fast search as a first pass and lets Jev judge which past records are relevant to your prompt, so one good record goes in or none.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/must-lioncho/jev-mem) |
| Maintainer | [must-lioncho](https://github.com/must-lioncho). Independently curated. |
| Format | Node CLI + agent plugin |
| Requirements | Node; `JEV_API_KEY` (or Keychain entry); existing claude-mem records. |
| License | [MIT](https://github.com/must-lioncho/jev-mem/blob/90d593e40f05d25352a6b8d05fd54ca850650ed2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/jev-mem.mjs`](https://github.com/must-lioncho/jev-mem/blob/90d593e40f05d25352a6b8d05fd54ca850650ed2/bin/jev-mem.mjs) at the pinned commit. |

## When to use

- Cut tokens spent loading past-session memory.
- Mismatch: builds on claude-mem; separate from other projects named Jev-Mem.

## How it works

`bin/jev-mem.mjs` runs the search, sends candidates and the prompt to Jev, and injects only records Jev judges relevant. Integration evidence: [`bin/jev-mem.mjs`](https://github.com/must-lioncho/jev-mem/blob/90d593e40f05d25352a6b8d05fd54ca850650ed2/bin/jev-mem.mjs).

## Get started

From the upstream README: install the plugin for your agent and set `JEV_API_KEY`.

```sh
git clone https://github.com/must-lioncho/jev-mem
# see README for Claude Code / Codex install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README.kr.md (Korean)

## Limits and data handling

Prompt text and candidate records go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 90d593e40f05](https://github.com/must-lioncho/jev-mem/tree/90d593e40f05d25352a6b8d05fd54ca850650ed2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
