# pi-jev-sentinel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Add TypeSafe Jev checks for coding-agent tool calls, tool outputs, and replies—shipping as a Pi extension plus a shared Claude Code / Codex CLI hook.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/harshwasan/pi-jev-sentinel) |
| Maintainer | [harshwasan](https://github.com/harshwasan) (Harsh Wasan). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension (`pi-jev-sentinel` 0.1.0) with `jev-sentinel-hook` binary for Claude Code and Codex. |
| Requirements | Pi coding agent for the extension path (`@earendil-works/pi-coding-agent` peer). Live judgments need `TYPESAFE_API_KEY`. Without a key, Pi fails closed to ask/approval rather than auto-allowing. Offline tests need no account. Node.js ≥ 22. |
| License | [MIT](https://github.com/harshwasan/pi-jev-sentinel/blob/eeee966a40257646c0193d386bb64228bfc2739e/LICENSE). |

## When to use

Use it when you want calibrated intent/risk judgments before tools run, injection screening on tool outputs, and reply checks that warn the user without writing back into the agent context. Prefer simpler local deny-lists when you do not need Jev probabilities or multi-host hooks.

**Distinct from catalogued [pi-jev](pi-jev.md)** (gate + output judge + `jev_ask`, shadow/fail-open defaults) and **[pi-warden](pi-warden.md)** (local policy holds plus Jev): sentinel emphasizes injection/off-task/risk screening, secret scrubbing before TypeSafe, optional pinned tasks, and fail-closed behavior when Jev or the key is unavailable. It also shares checks with Claude Code and Codex hooks.

## How it works

The [guard](https://github.com/harshwasan/pi-jev-sentinel/blob/eeee966a40257646c0193d386bb64228bfc2739e/src/guard.ts) posts to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. Before a tool call, Jev answers intent (choice) and risk (score); code maps probabilities to allow / ask / warn with Block highlighted. Tool outputs can be screened for agent instructions before the model reads them (Pi path); Claude/Codex hooks run the output check post-tool as documented upstream. Reply checks notify the user only. Secrets and credential-file contents are scrubbed with heuristics before leaving the machine. Settings under `~/.pi/agent` and the decision log are locally protected regardless of Jev's answer.

## Get started

Pi extension:

```sh
pi install git:github.com/harshwasan/pi-jev-sentinel
export TYPESAFE_API_KEY=...
```

Source inspection and offline tests:

```sh
git clone https://github.com/harshwasan/pi-jev-sentinel.git
cd pi-jev-sentinel
git checkout eeee966a40257646c0193d386bb64228bfc2739e
npm ci --ignore-scripts
npm test
npm run check
```

Claude Code / Codex hook setup is documented in [hooks/README.md](https://github.com/harshwasan/pi-jev-sentinel/blob/eeee966a40257646c0193d386bb64228bfc2739e/hooks/README.md) (`npm run build`, then example settings JSON). Live checks incur TypeSafe usage charges. This listing did not install into a live Pi, Claude Code, or Codex session.

## Examples and demos

- Upstream [docs/images](https://github.com/harshwasan/pi-jev-sentinel/tree/eeee966a40257646c0193d386bb64228bfc2739e/docs/images): recorded screenshots of injection catches, pinned-task asks, and reply flags (upstream evidence, not re-run here).
- [test/](https://github.com/harshwasan/pi-jev-sentinel/tree/eeee966a40257646c0193d386bb64228bfc2739e/test): Vitest coverage for guard and hook paths with fixtures.
- [sandboxes/](https://github.com/harshwasan/pi-jev-sentinel/tree/eeee966a40257646c0193d386bb64228bfc2739e/sandboxes): manual scenario fixtures; not executed for this listing.
- `npm run live-check` is billable and was not run.

## Limits and data handling

Tool names/arguments, redacted transcript/context projections, and screened outputs (as implemented) go to TypeSafe when a key is present. Heuristic secret scrubbing reduces leaks but does not guarantee none. Thresholds are operational policy, not measured security efficacy. Fail-closed asks still interrupt workflows when the model is unreachable. Hook semantics differ slightly from the Pi extension (see upstream hooks README).

## Review and maintenance

Reviewed on **2026-09-20** at [commit eeee966](https://github.com/harshwasan/pi-jev-sentinel/tree/eeee966a40257646c0193d386bb64228bfc2739e): package **0.1.0**, MIT. AI-assisted source review of `guard.ts`, `hook.ts`, `index.ts`, README, hooks examples, and license. On Node.js 22.19.0, **`npm test`: 106 passed** (2 files) and **`npm run check`** (`tsc --noEmit`) passed. No live TypeSafe calls or host installs were performed.

Related: [pi-jev](pi-jev.md), [pi-warden](pi-warden.md), [toolgate](toolgate.md).
