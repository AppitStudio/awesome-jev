# jevmem

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Project memory for Claude Code, Cursor, and Codex in a git-tracked `JEVMEM.md`: TypeSafe Jev decides which turns hold a decision, rule, bug, to-do, or failed approach, picks the saved lines relevant to each prompt, and checks Bash, Edit, and Write calls against saved rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Avinash-jetwani/jevmem) |
| Maintainer | [Avinash-jetwani](https://github.com/Avinash-jetwani), who also submitted this update. |
| Disclosure | Updated by the maintainer with AI assistance, from the upstream README, PRIVACY.md, and docs at tag v0.6.4. Benchmark figures are the author's own and not independently verified. Listing is not an endorsement. |
| Format | Claude Code plugin (in Anthropic's Claude plugin directory), Node CLI and hooks, and an MCP server (`io.github.Avinash-jetwani/jevmem` on the MCP Registry); **jevmem 0.6.4** (npm). |
| Jev's role | Jev decides save or skip and the kind of line after each turn, whether a new line reverses an old one, which saved lines are relevant to a prompt, whether a tool call may break a saved rule, and whether a line not written on this machine reads as instructions to an AI. Application code does the prefiltering, the file format, and the fallbacks. |
| Requirements | Node.js 20 or later; a TypeSafe API key (`jevmem key` saves it); Claude Code 2.1.273 or later for the directory plugin. An OpenAI, Anthropic, or OpenAI-compatible key only if the optional per-project LLM writer is turned on. |
| License | [MIT](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/LICENSE). |

## When to use

- You make decisions in Claude Code chats ("we use Postgres") and want them back next session without keeping `CLAUDE.md` up to date by hand; the team reviews the same file through git.
- Your project has rules worth checking before a command runs, such as never committing `.env`: the guard has Claude Code ask first.
- You mix tools: Codex (automatic while `jevmem watch` runs) and Cursor (when the agent calls the MCP tools) read and write the same file.

Rules that every task must follow still belong in `CLAUDE.md`: in the author's A/B, `CLAUDE.md` followed a convention that nothing in the prompt points to in 3 of 3 sessions, jevmem in 0 of 3. For other memory designs, see [jevmory](jevmory.md), [Cairn Jev Lab](cairn-jev-lab.md), or [Jev Second Brain](jev-second-brain.md).

## How it works

- **After each turn** (an async Claude Code `Stop` hook), [`src/decide.ts`](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/src/decide.ts) asks Jev whether the turn holds something worth keeping and what kind, and writes one line to `JEVMEM.md`. A line that a later turn reverses is marked superseded. Decision records stay in `.jevmem/`.
- **On each prompt**, [`src/recall.ts`](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/src/recall.ts) asks Jev which saved lines matter and adds them to Claude's context. A slow or failed call falls back to word matching.
- **Before Bash, Edit, and Write calls** (a `PreToolUse` hook), [`src/guardrail.ts`](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/src/guardrail.ts) picks saved rules that share words with the call, sends only those to Jev, and has Claude Code ask when a rule may break. The default mode is ask; block, warn, and off are settings. It fails open.
- **Lines not written on this machine** (a teammate's, a pull request's) are checked by Jev before recall and withheld when scored as instructions to an AI.
- **MCP server** ([`src/mcp.ts`](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/src/mcp.ts)): `add_memory`, `search_memory`, `list_memory`, and `audit_memory`.

## Get started

From the Claude plugin directory (Claude app: **Plugins → Discover → jevmem → Add**), then in a terminal:

```sh
npm install -g jevmem
jevmem key          # paste your TypeSafe API key
cd your-project
jevmem enable
```

Without the directory plugin, `jevmem init --tool claude` (or `cursor`, `codex`, `claude-desktop`, `all`) sets up hooks or MCP for that tool. `jevmem doctor` checks the setup. Live use sends scrubbed turn text to TypeSafe and is billed to your TypeSafe key. Full steps: [docs/install.md](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/docs/install.md).

## Examples and demos

- The [README](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/README.md) has a short film and step-by-step graphics of saving, recall, and a guard ask on a `.env` commit.
- [docs/guardrails.md](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/docs/guardrails.md) walks through guard modes and test commands.
- The [`results/`](https://github.com/Avinash-jetwani/jevmem/tree/v0.6.4/results) folder holds the author's benchmark and A/B outputs, with the scripts in [`scripts/`](https://github.com/Avinash-jetwani/jevmem/tree/v0.6.4/scripts).

## Limits and data handling

- Turn text is sent to TypeSafe (`api.typesafe.ai`, or the URL in `TYPESAFE_BASE_URL`) to be scored, after common secret shapes are scrubbed; scrubbing is best-effort. The optional writer sends text to OpenAI, Anthropic, or an OpenAI-compatible endpoint only when turned on. jevmem has no telemetry ([PRIVACY.md](https://github.com/Avinash-jetwani/jevmem/blob/v0.6.4/PRIVACY.md)).
- The guard is a backstop, not a sandbox: it can miss a rule that shares no words with the call.
- Cursor saves only when the agent calls the MCP tools; Codex saves automatically only while `jevmem watch` runs.
- With more than 250 live lines, only the 250 sharing the most words with the prompt are sent to Jev, so a relevant line can be missed.
- Local decision models are not supported yet: in the author's one-run test on an Apple M4 with Ollaya 0.9.0 (Oct 2, 2026), `winnow:e4b` got 60 of 66 held-out save/skip decisions right at 28.5 s per turn, against Jev's 65 of 66 at 0.23 s ([issue #15](https://github.com/Avinash-jetwani/jevmem/issues/15)).

## Review and maintenance

Updated on **2026-10-03** at [tag v0.6.4](https://github.com/Avinash-jetwani/jevmem/tree/v0.6.4) (commit `a0ffe7f`) by the maintainer, with AI assistance; facts taken from the README, PRIVACY.md, and docs at that tag. Author-reported results, not independently verified: in a 72-session A/B (24 tasks in three small projects, 3 runs each, Claude Code 2.1.281 with `claude-sonnet-5`), Claude followed the project's saved line in 66 of 72 sessions with jevmem, 67 of 72 with the same lines in `CLAUDE.md`, and 28 of 72 with no memory. On a held-out set of 274 tool calls, the guard caught 66 of 68 rule breaks with 3–4 false asks in 206 fine calls. The previous catalog entry was an independent AI-assisted review of 0.4.2 on 2026-09-23.

Related: [jevmory](jevmory.md), [Cairn Jev Lab](cairn-jev-lab.md), [Jev Second Brain](jev-second-brain.md), [clear-head](clear-head.md).
