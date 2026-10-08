# jev-mod (VictorGambarini)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that hands small decisions to a decision model — Jev via TypeSafe, OpenRouter, Venice or OpenCode Zen (or your own server): per-turn routing lanes that set effort and model, the one installed skill a prompt needs, screening of AI-directed instructions after WebFetch / WebSearch / MCP / fetching Bash, and `/compact-jev`, a summary-free compaction keeping only turns marked *keep*. Every decision fails open. Distinct from the listed Discord bot *Jev-Mod (undeemed)*.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VictorGambarini/jev-mod) |
| Maintainer | [VictorGambarini](https://github.com/VictorGambarini). Independently curated. |
| Format | Claude Code plugin marketplace (`/plugin install jev-mod --marketplace VictorGambarini/jev-mod`) with a status-line script |
| Requirements | Claude Code; `TYPESAFE_API_KEY` (or another supported backend key) — key setup currently via `jev setup-key` from hermes-jev-skills or the environment. |
| License | [MIT](https://github.com/VictorGambarini/jev-mod/blob/66933855943cf5e7b634fa205ac575359c861a2e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Cut frontier-model spend on 'which model/effort/skill?' choices.
- Withhold instruction-like sentences from fetched pages before Claude reads them.
- Mismatch: thresholds were measured on Jev; other backends need their own tuning.

## How it works

[`src/core/jev.ts`](https://github.com/VictorGambarini/jev-mod/blob/66933855943cf5e7b634fa205ac575359c861a2e/src/core/jev.ts) calls the `systemone` protocol on the configured backend; features live under [`src/features/`](https://github.com/VictorGambarini/jev-mod/tree/66933855943cf5e7b634fa205ac575359c861a2e/src/features) (e.g. [`compact-jev/keep.ts`](https://github.com/VictorGambarini/jev-mod/blob/66933855943cf5e7b634fa205ac575359c861a2e/src/features/compact-jev/keep.ts)). After a failed call it stops asking for five minutes, so a down backend costs one timeout.

## Get started

Install the mod (README *Install*):

```sh
/plugin install jev-mod --marketplace VictorGambarini/jev-mod
export TYPESAFE_API_KEY=...
```

Each decision is a backend call billed by that provider; shares the daily budget set by jev-skills.

## Examples and demos

- README feature table and *Status line*.

## Limits and data handling

Prompts, skill lists and fetched text excerpts go to the chosen backend. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 66933855943c](https://github.com/VictorGambarini/jev-mod/tree/66933855943cf5e7b634fa205ac575359c861a2e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
