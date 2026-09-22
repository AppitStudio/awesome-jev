# cmd-mod-jev-nudge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

[Command Code](https://commandcode.ai) mod that asks TypeSafe Jev at agent stop whether unfinished work warrants a nudge to continue (and skips nudging when waiting on the user or when the last nudge did nothing).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CommandCodeAI/cmd-mod-jev-nudge) |
| Maintainer | [CommandCodeAI](https://github.com/CommandCodeAI) / [Ahmad Awais](https://github.com/ahmadawais). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Command Code mod package **`cmd-mod-jev-nudge` 0.1.0** (`commandcode.mods` → `./src/index.ts`). |
| Requirements | Node.js ≥ 20; Command Code (`cmd login` / `CMD_API_KEY`). Jev is called via Command Code’s System One provider route with the user’s Command Code key (not a separate TypeSafe key in the documented path). |
| License | [MIT](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/blob/24d4b6cf6e227b57ab1b5b0ded2abad166ac4cf9/LICENSE). Command Code / upstream model usage billed per vendor terms. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pnpm test` / `vitest run`: **24 passed**. Demo referenced on X; no X reply posted from this listing. No live Command Code/Jev run here. |

## When to use

Use it when Command Code agents stop after a partial plan (“next I’ll…”) and you want a Jev-judged continue nudge. Prefer Stop-hook projects for Claude Code/Codex ([clear-head](clear-head.md), [hookgate](hookgate.md)) when you are not on Command Code.

## How it works

[`src/client.ts`](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/blob/24d4b6cf6e227b57ab1b5b0ded2abad166ac4cf9/src/client.ts) POSTs typed nudge questions to Command Code’s System One path; [`src/index.ts`](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/blob/24d4b6cf6e227b57ab1b5b0ded2abad166ac4cf9/src/index.ts) wires the stop-hook. If Jev fails, the run stops normally (fail-open to “no nudge”).

## Get started

```sh
cmd login
cmd mods add cmd-mod-jev-nudge
# From source at the reviewed commit:
git clone https://github.com/CommandCodeAI/cmd-mod-jev-nudge.git
cd cmd-mod-jev-nudge
git checkout 24d4b6cf6e227b57ab1b5b0ded2abad166ac4cf9
pnpm install
pnpm test
```

Live use goes through Command Code and can incur vendor charges.

## Examples and demos

- README multi-language “say hi” walkthrough.
- Upstream demo video linked from README ([X post](https://x.com/MrAhmadAwais/status/2102456912486989945)).
- `src/__tests__/` — offline vitest coverage.

## Limits and data handling

Stop-hook state/transcript excerpts may leave the host via Command Code’s provider route. Experimental mod; validate nudge thresholds in your workflow. This listing did not run a live Command Code session.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 24d4b6c](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/tree/24d4b6cf6e227b57ab1b5b0ded2abad166ac4cf9) (`0.1.0`, MIT). AI-assisted review of README, LICENSE, `src/client.ts`, `src/index.ts`. Offline vitest **24 passed**. No live Command Code/Jev. x_post_url retained: [X post](https://x.com/MrAhmadAwais/status/2102456912486989945)

Related: [clear-head](clear-head.md), [hookgate](hookgate.md), [mayi](mayi.md).
