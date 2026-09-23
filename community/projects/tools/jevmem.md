# jevmem

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shared `JEVMEM.md` project memory for Claude Code, Cursor, and Codex: TypeSafe Jev decides whether each turn is worth remembering; optional LLM one-liners write the line.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Avinash-jetwani/jevmem) |
| Maintainer | [Avinash-jetwani](https://github.com/Avinash-jetwani). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node CLI / hooks / MCP **jevmem 0.4.2** (npm). |
| Requirements | Node (see package engines); `TYPESAFE_API_KEY`. Optional `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` for nicer one-line writes (deterministic extract works without). |
| License | [MIT](https://github.com/Avinash-jetwani/jevmem/blob/c3f150d78f25a41ba154a0357f95d37797135cc9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, package, `src/jev.ts`). Live hooks/TypeSafe were **not** run on the review host. Author-reported benchmark figures are not independently verified. |

## When to use

Use it when a team wants one git-reviewed memory file across Claude Code / Cursor / Codex and a fast typed gate on what to save. Prefer [Cairn Jev Lab](cairn-jev-lab.md) for memory-admission policy labs, or vault tools such as [Jev Second Brain](jev-second-brain.md) for note graphs.

## How it works

After each turn (Claude Code Stop hook; Cursor/Codex via MCP/rules; optional `jevmem watch`), [`src/jev.ts`](https://github.com/Avinash-jetwani/jevmem/blob/c3f150d78f25a41ba154a0357f95d37797135cc9/src/jev.ts) / [`src/decide.ts`](https://github.com/Avinash-jetwani/jevmem/blob/c3f150d78f25a41ba154a0357f95d37797135cc9/src/decide.ts) ask Jev whether to save, what kind, and whether it contradicts an existing line. Best-effort redaction runs before the API call ([SECURITY.md](https://github.com/Avinash-jetwani/jevmem/blob/c3f150d78f25a41ba154a0357f95d37797135cc9/SECURITY.md)). Decision metadata stays in `.jevmem/`; lines land in `JEVMEM.md`.

## Get started

```sh
npm install -g jevmem
export TYPESAFE_API_KEY=...
cd your-project
jevmem init --tool claude
```

Pin for review: [commit c3f150d](https://github.com/Avinash-jetwani/jevmem/tree/c3f150d78f25a41ba154a0357f95d37797135cc9). Live use sends scrubbed prompt (and sometimes reply) text to TypeSafe and may incur charges.

## Examples and demos

- README install and `jevmem why <id>` explainability.
- Upstream `results/` benchmarks (author-reported; not re-run here).

## Limits and data handling

Redaction is best-effort. Opt-in zero-retention flags are documented upstream with limits. Author-reported latency/cost figures are not independently verified. No live TypeSafe spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit c3f150d](https://github.com/Avinash-jetwani/jevmem/tree/c3f150d78f25a41ba154a0357f95d37797135cc9) (**0.4.2**, MIT). AI-assisted source review. No live hooks or TypeSafe calls.

Related: [Cairn Jev Lab](cairn-jev-lab.md), [Jev Second Brain](jev-second-brain.md), [clear-head](clear-head.md).
