# Jev Decision Skills for Coding Agents (Agent Skills that send bounded decisions to Jev via OpenCode)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable Agent Skills for OpenCode, Claude Code and Codex that send classification, fixed-choice, scoring and yes/no checks to Jev through OpenCode's decisions API, plus a sync skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Chillbok/opencode-jev-subagent) |
| Maintainer | [Chillbok](https://github.com/Chillbok). Independently curated. |
| Format | Agent Skills + Python helper (MIT) |
| Requirements | Python 3 and the OpenCode CLI connected once with `/connect` (reuses OpenCode Console credentials; no separate key). |
| License | [MIT](https://github.com/Chillbok/opencode-jev-subagent/blob/5afc83db70f01123f0c19846a546e324a5adebc4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jev-decision/scripts/opencode_decisions.py`](https://github.com/Chillbok/opencode-jev-subagent/blob/5afc83db70f01123f0c19846a546e324a5adebc4/skills/jev-decision/scripts/opencode_decisions.py) at the pinned commit. |

## When to use

- Replace prompt-and-parse with typed Jev answers in coding agents.
- Keep one skill set synced across tools.
- Mismatch: depends on OpenCode's experimental API and its current free tier.

## How it works

`opencode_decisions.py` calls OpenCode's local `/api/experimental/generate/decisions` with `jev-1.13-free` by default; the paid `jev-1.13` fallback needs explicit user approval. Integration evidence: [`skills/jev-decision/scripts/opencode_decisions.py`](https://github.com/Chillbok/opencode-jev-subagent/blob/5afc83db70f01123f0c19846a546e324a5adebc4/skills/jev-decision/scripts/opencode_decisions.py).

## Get started

Clone and give your agent the install prompt from the README for OpenCode, Claude Code or Codex.

```sh
git clone https://github.com/Chillbok/opencode-jev-subagent.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Chillbok/opencode-jev-subagent/blob/5afc83db70f01123f0c19846a546e324a5adebc4/README.md](https://github.com/Chillbok/opencode-jev-subagent/blob/5afc83db70f01123f0c19846a546e324a5adebc4/README.md)

## Limits and data handling

Decision inputs go through OpenCode to Jev on your connected account.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 5afc83db70f0](https://github.com/Chillbok/opencode-jev-subagent/tree/5afc83db70f01123f0c19846a546e324a5adebc4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
