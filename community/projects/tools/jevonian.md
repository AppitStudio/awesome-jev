# jevonian

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Local proxy that accepts OpenAI, Anthropic, and Responses requests from a coding agent and asks one Jev call which model should serve the turn and how deeply that model should think, after code has already narrowed the candidates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xinyao27/jevonian) |
| Maintainer | [xinyao27](https://github.com/xinyao27). This is a maintainer submission, not an independent catalog review; I am the author of the project. |
| Format | Node.js CLI and local server (`jevonian` 0.0.1 on npm), plus a React dashboard for providers, routing, keys, logs, and spend. |
| Requirements | Node.js ≥ 22. At least one Jev channel with a key: `TYPESAFE_API_KEY` (direct `api.typesafe.ai`), `OPENROUTER_API_KEY`, `OPENCODE_API_KEY`, `AI_GATEWAY_API_KEY`, or `CLOUDFLARE_API_TOKEN` with an account id. At least one non-Jev provider for the routed turn itself, added with `jevonian add`. |
| License | [AGPL-3.0-only](https://github.com/xinyao27/jevonian/blob/1f912150bd9cfdb07e264a28c074638b587d7648/LICENSE). Provider inference and the brain channel are billed separately by their vendors. |
| Disclosure | Maintainer submission by the project author; no TypeSafe affiliation, and listing is not an endorsement. Verified here: offline suite `pnpm test` → **43 files, 450 tests passed** at commit 1f91215. **Not** verified here: any live Jev call, any routed provider turn, and any cost figure. The ledger's cost is an estimate from a local price table, not reconciled with a vendor invoice, and its cache-read figures are estimates because `prefixMatch` is still `unknown`. |

## When to use

Use it when a coding agent should keep working while the model behind it changes turn by turn: routine edits and tool loops do not need a frontier model, and architecture turns do. Point the agent at the loopback endpoint and ask for `jevonian/auto`.

It is the wrong tool if you want a hosted service, per-team policy, or a benchmark of routing quality — there is no comparison against a fixed-model baseline in the repository, so any cost saving you get is the router's estimate, not a measured result on your workload.

## How it works

For a `jevonian/auto` request, [`src/routing.ts`](https://github.com/xinyao27/jevonian/blob/1f912150bd9cfdb07e264a28c074638b587d7648/src/routing.ts) filters the configured providers first, dropping wire-incompatible models, models whose context window cannot hold the conversation, models that cannot reach the requested thinking-level floor, and providers whose quota window is already spent. Unknown quota is treated as neutral rather than as a failure.

Jev is then asked **one** `state` + `questions` call with two `choice` questions — which model, and how deeply it should think — whose criteria are built from the candidates that survived the filter. [`src/brain.ts`](https://github.com/xinyao27/jevonian/blob/1f912150bd9cfdb07e264a28c074638b587d7648/src/brain.ts) holds the channels. The direct one posts to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`; OpenRouter, OpenCode Zen, Vercel AI Gateway, Cloudflare Workers AI, and a custom SystemOne-compatible URL are also supported. Channels exist for failover only: a failed channel is skipped, a low-confidence verdict is kept and marked (`x-jevonian-brain: jev-low-confidence`), and if every channel fails the request errors rather than guessing a model.

Code keeps ownership of everything else. A pinned real model ID, an explicit `jevonian/plan` / `/execute` / `/utility` / `/chat`, or `routing.mode: "off"` skips Jev entirely, so pass-through costs nothing. `routing.brainPicksEffort: false` stops the effort question being asked at all. Every turn lands in a local ledger with the serving model and provider, the reason, real token usage, cache reads, and an estimated cost, and `/logs` shows the captured brain call beside the request it decided.

The state sent to Jev is the session context the decision needs: last user message, last assistant message, the session goal, recent messages, recent tool calls and results, consecutive failures, the previous model, turn count, an estimated token count, the candidate list, and the constraints code already applied. `fullPrompt: true` widens that to a verbatim transcript capped at 400k characters.

## Get started

```sh
npm install -g jevonian
jevonian init
jevonian add anthropic        # or any OpenAI-compatible provider
jevonian serve
```

Then point a client at the loopback endpoint:

```sh
curl http://127.0.0.1:8787/v1/chat/completions \
  -H 'content-type: application/json' \
  -d '{"model":"jevonian/auto","messages":[{"role":"user","content":"design a cache layer"}]}'
```

Run through the wizard on the Providers page, or `jevonian add`, to store the brain channel and its key; `jevonian doctor` reports configuration, provider, ledger, catalog, and pricing health. `jevonian launch claude` runs Claude Code against the proxy Ollama-style, remapping Opus/Sonnet/Haiku onto Jevonian models. Both the brain call and the served turn are billed by their providers.

From a source checkout the same commands run as `node dist/cli.mjs serve`.

## Examples and demos

- [`docs/brain.md`](https://github.com/xinyao27/jevonian/blob/1f912150bd9cfdb07e264a28c074638b587d7648/docs/brain.md) — channels, the state payload, and what happens on low confidence or total failure.
- [`docs/routing.md`](https://github.com/xinyao27/jevonian/blob/1f912150bd9cfdb07e264a28c074638b587d7648/docs/routing.md) — the deterministic filter table and the virtual-model rules.
- [`docs/cli.md`](https://github.com/xinyao27/jevonian/blob/1f912150bd9cfdb07e264a28c074638b587d7648/docs/cli.md) — every command, and the dashboard routes.
- The offline suite covers routing, quota gating, wire encoding, and brain parsing; it needs no network and no keys.

There is no separate hosted demo or recorded live run. I did not run a live Jev call or a routed provider turn while preparing this page, so nothing here should be read as a measured result.

## Limits and data handling

The compact state goes to whichever brain channel you configure on every automatic turn, so that vendor sees the last user message, recent messages, and recent tool calls and results; `fullPrompt: true` sends a verbatim transcript including the system prompt. Choose the channel with that in mind. `jevonian/auto` cannot work without a reachable brain — there is no offline fallback — and the ledger's cost and cache numbers are local estimates rather than billing records. Routing quality is not benchmarked in the repository, so no savings number here is transferable.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 1f91215](https://github.com/xinyao27/jevonian/tree/1f912150bd9cfdb07e264a28c074638b587d7648) (`0.0.1`, AGPL-3.0-only). Checks run here: `pnpm test` → **43 test files, 450 tests passed** in about 0.6s, and a read of `src/brain.ts`, `src/routing.ts`, `docs/brain.md`, `docs/routing.md`, and the CLI reference. Not run here: any live TypeSafe or provider request, `jevonian serve` against a real agent, and any cost measurement. This page is a maintainer submission and has not been independently verified by catalog maintainers.

Related: [codex-jev-router](codex-jev-router.md) and [jev-codex-router](jev-codex-router.md) route Codex turns through a similar loopback proxy, with the route computed by their own policy and Jev rather than by this candidate filter; [Jev Model Router](jev-model-router.md) routes subagent models from inside Claude Code.
