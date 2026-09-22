# stop-rules

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Stop-hook CLI for coding agents: splits each changed piece, asks TypeSafe Jev one yes/no question per piece and per written team rule, and hands violations back to the agent (supports a large set of agent harnesses plus optional team server).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/haystackeditor/stop-rules) |
| Maintainer | [haystackeditor](https://github.com/haystackeditor). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI **`stop-rules` 0.1.0** (`bin/stop-rules.mjs`) with optional hosted/team proxy (`TYPESAFE_API_KEY` on server). |
| Requirements | Node.js ≥ 20; own `TYPESAFE_API_KEY` / `TYPESAFE_API_KEY_FILE` or `stop-rules login --jev-key-stdin`; agent stop-hook wiring per `AGENT-SETUP.md`. |
| License | [MIT](https://github.com/haystackeditor/stop-rules/blob/77f0683c5f72740afc9d819bbec2d0070f5b419c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `npm run typecheck` + `npm run compile` inspected; live TypeSafe stop-hook runs not executed on the review host. Distinct from [JevGuard](jevguard.md) and [jev-rules](jev-rules.md). |

## When to use

Use it when you want **written coding rules enforced at stop time** with calibrated Jev yes/no judgments over each changed piece. Prefer [JevGuard](jevguard.md) for CLAUDE.md/AGENTS.md-derived PreToolUse/Stop rule packs, or [jev-pref](jev-pref.md) for preference linting of diffs. Do not treat Jev answers as automatic merge authority—agent/human policy still owns the response.

## How it works

Local engine parses languages via tree-sitter grammars, builds piece state, and calls `https://api.typesafe.ai/v1/systemone` (`jev-latest` default) with Noul questions. Optional team server proxies the same upstream with a shared key and auth token. Keys can live in env, a file, or `~/.config/stop-rules/jev-key` after login.

## Get started

```sh
git clone https://github.com/haystackeditor/stop-rules.git
cd stop-rules
git checkout 77f0683c5f72740afc9d819bbec2d0070f5b419c
npm ci --ignore-scripts
npm run typecheck
npm run compile
# Wire your agent per AGENT-SETUP.md; then:
# printf %s "$TYPESAFE_API_KEY" | node bin/stop-rules.mjs login --jev-key-stdin
```

Live stop hooks send code pieces and rule text to TypeSafe and may incur charges. This listing did not invoke a live hook.

## Examples and demos

- Offline on the review host: `npm run typecheck` clean; `npm run compile` refreshed bin/wasm checks and AWS template check.
- Upstream documents multi-agent setup and deploy targets (Fly/Heroku/Netlify/Vercel/AWS).

## Limits and data handling

Changed code and rule text leave the host on live judgments. Team mode holds a shared TypeSafe key on the server. Grammar coverage is limited to the shipped language set documented upstream.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 77f0683](https://github.com/haystackeditor/stop-rules/tree/77f0683c5f72740afc9d819bbec2d0070f5b419c): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, `src/engine.ts`. Offline typecheck + compile OK. No live TypeSafe stop-hook on the review host.

Related: [JevGuard](jevguard.md), [jev-rules](jev-rules.md), [jev-pref](jev-pref.md), [clear-head](clear-head.md).
