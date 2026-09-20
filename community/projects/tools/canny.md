# Canny

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Warden for Claude Code and Codex CLI: an append-only session ledger and deterministic “done” gate, with optional TypeSafe Jev judgments that advise but never alone block.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qkal/Canny) |
| Maintainer | [qkal](https://github.com/qkal) / Kal. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI **canny-warden 0.1.0** — zero runtime dependencies; compiled `dist/` committed for git-based install. |
| Requirements | Node.js ≥ 22; git. Optional `TYPESAFE_API_KEY` for Jev advice (done-gate works offline from the ledger alone). |
| License | [MIT](https://github.com/qkal/Canny/blob/74bc3487370ae6d61cef69c5642cce504a8579cb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live agent hooks and live Jev were not run. |

## When to use

Use it when coding agents claim “done” without running checks, and you want a ledger-backed stop that only code can enforce. Prefer [jev-guard](jev-guard.md) or [toolgate](toolgate.md) for per-tool-call risk deny/ask/allow. Distinct from open PR #7 belay-style tooling: Canny’s hard blocks come from append-only facts (edits, exits, named checks), while Jev only classifies “claims done” / rule notes.

## How it works

Hooks record tool events into `~/.canny/sessions/`. On Stop, [`src/hook.ts`](https://github.com/qkal/Canny/blob/74bc3487370ae6d61cef69c5642cce504a8579cb/src/hook.ts) derives allow/block from the ledger (changed files without a passing check, repeated failures, secret patterns). [`src/jev.ts`](https://github.com/qkal/Canny/blob/74bc3487370ae6d61cef69c5642cce504a8579cb/src/jev.ts) posts optional Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); answers can annotate context but cannot alone refuse Stop. `canny replay` re-derives verdicts from stored facts and Jev logs.

## Get started

```sh
git clone https://github.com/qkal/Canny.git ~/.canny/src
cd ~/.canny/src
git checkout 74bc3487370ae6d61cef69c5642cce504a8579cb
# from a project you want guarded:
node ~/.canny/src/dist/cli.js init
```

Optional: `export TYPESAFE_API_KEY=…` for Jev advice. Live hooks send claim text and rule snippets to TypeSafe when a key is set. This listing did not install hooks or call live Jev.

## Examples and demos

- README session ledger walkthrough (math.js / `npm test` Stop sequence).
- Offline `test/hook.test.ts` and `test/jev.test.ts` — not executed on the review host.

## Limits and data handling

Ledger stores paths and outcomes, not file contents. With a key, judgment payloads leave the host for TypeSafe. Without a key, deterministic rules still gate Stop. Upstream latency anecdotes were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 74bc348](https://github.com/qkal/Canny/tree/74bc3487370ae6d61cef69c5642cce504a8579cb): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, `src/hook.ts`, and `package.json`. No live TypeSafe or agent-hook runs.

Related: [jev-guard](jev-guard.md), [jev-preflight](jev-preflight.md), [toolgate](toolgate.md).
