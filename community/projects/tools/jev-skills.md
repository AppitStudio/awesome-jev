# jev-skills

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code / Codex plugin: TypeSafe Jev decides which installed skills enter context each turn—always-on skill-list cost drops to zero tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eran-broder/jev-skills) |
| Maintainer | [eran-broder](https://github.com/eran-broder). Independently curated; not an upstream submission or endorsement. |
| Format | Claude Code / Codex plugin + TypeScript CLI (`src/`, `dist/`). |
| Requirements | Claude Code or Codex; `typesafe_api_key` (plugin config) / TypeSafe API access. |
| License | [MIT](https://github.com/eran-broder/jev-skills/blob/d1a7b9000408ca628881051bc442eb6e8b689151/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Upstream README cites measured latencies/costs—those figures were **not** re-measured here. Distinct from [Hermes Jev Skills](hermes-jev-skills.md). |

## When to use

Use it when a large skill library would otherwise bloat every turn. Prefer [Hermes Jev Skills](hermes-jev-skills.md) for Hermes-centric multi-skill routing beyond Claude Code/Codex hooks.

## How it works

Hooks on `UserPromptSubmit` and selected tool results build a compact state, ask one Noul per skill via [`src/jev/client.ts`](https://github.com/eran-broder/jev-skills/blob/d1a7b9000408ca628881051bc442eb6e8b689151/src/jev/client.ts), and inject only skills above threshold (once per session; compaction resets). Failures fail open.

## Get started

```sh
claude plugin marketplace add eran-broder/jev-skills
claude plugin install jev-skills@jev-skills --config typesafe_api_key=<key>
```

Or clone [tip d1a7b90](https://github.com/eran-broder/jev-skills/tree/d1a7b9000408ca628881051bc442eb6e8b689151) and follow README for Codex.

## Examples and demos

- README walkthrough video under `media/`.
- Fan-out helpers in `src/jev/fanout.ts`.

## Limits and data handling

Prompt fragments and tool snippets leave the host on live Jev calls. Skill bodies are still local files—only selected ones enter model context.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit d1a7b90](https://github.com/eran-broder/jev-skills/tree/d1a7b9000408ca628881051bc442eb6e8b689151). AI-assisted README/LICENSE/`src/jev/*` inspection. No live Claude Code/Codex or TypeSafe spend.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [SkillRanker](skillranker.md).
