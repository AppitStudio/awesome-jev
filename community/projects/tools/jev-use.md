# jev-use (shitianfang)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hand the steps of a Claude Code, Codex, or pi loop that produce no text — did the build pass, which element to click, is this command safe to run — to Jev, and take back the ones it should not decide.

**Not to be confused with** [Cua jev-use](cua-jev-use.md) (`trycua/cua` …/examples/jev-use), a separate browser/Driver chooser recipe already listed in this catalog, or the similarly named skill path inside [Jev-cu](jev-cu.md). This page is **[shitianfang/jev-use](https://github.com/shitianfang/jev-use)** (npm `jev-use`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shitianfang/jev-use) |
| Maintainer | [shitianfang](https://github.com/shitianfang). Self-submission by the project's author; inclusion is not an endorsement. No commercial relationship with TypeSafe. |
| Format | TypeScript library (npm `jev-use`) with a CLI, a stdio MCP server exposing two tools, a Claude Code plugin carrying a routing skill and an optional PreToolUse gate, and Codex and pi wiring. |
| Requirements | Node.js 20+. One provider key in the environment the agent runs in: `TYPESAFE_API_KEY`, `OPENROUTER_API_KEY`, or `AI_GATEWAY_API_KEY`. `JEV_BACKEND=mock` runs keyless and makes no network call. Only the MCP server imports third-party packages; the judgment path has no runtime dependencies. |
| License | [MIT](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/LICENSE). |

## When to use

Consider this when a coding-agent loop repeatedly spends a full model turn on a step whose output is not text: reading a command's output to decide whether it succeeded, choosing one of the elements or actions already enumerated in front of it, or rating how risky a proposed action is. Those steps are the ones `jev_judge` is shaped for.

It is the wrong tool when the step's product is content — a patch, a summary, a commit message. The library says so before any request is spent: `route({ producesContent: true, enumerable: true })` returns `{ to: "llm", reason: "writing" }` with no client and no key involved.

Two other mismatches are worth naming. Questions whose answer set cannot be enumerated are structurally outside the three primitives, and a state larger than roughly 30k tokens is handed back rather than truncated. Both are pre-call decisions, so neither costs a call.

## How it works

```text
step → route (deterministic) → screen questions → one batched backend call
     → verdicts with confidence → below threshold, hand the question back
```

`jev_judge` takes one `state` string and an array of typed questions, and returns one verdict per question in the order asked. The three question types map to Jev's primitives: [Noul](https://docs.typesafe.ai/primitives/noul) for the probability a statement is true, choice for one enumerated option, score for a position on ordered levels. Every question about the same state is meant to ride a single call; the [reference](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/docs/reference.md) documents the parameters, the state budget, and the default `confidence_threshold` of `0.75`.

That default drops to `0.4` on the Vercel AI Gateway, which returns no confidence field: [the adapter](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/src/backends/vercel.ts) substitutes the distribution margin, a different and uncalibrated quantity. For `noul` answers, where the API reports no confidence either, the value is computed as certainty, `2·|p − 0.5|`. Read `confidence` accordingly: it is not the same measurement on every backend.

`jev_gate` is the opt-in half. One proposed tool call goes in, and underneath it is a single allow/deny choice about that action. The [hook adapter](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/src/cli.ts) maps `deny` to `permissionDecision: "deny"`, `escalate` to `"ask"`, and prints nothing at all on `allow`, so an allowed action falls through to the harness's normal permission flow. **The gate can only deny or ask; it can never grant permission.**

Every boundary comes back in-band as a typed reason rather than an exception:

| reason | when | what the caller does |
| --- | --- | --- |
| `writing` | pre-call | the step needs new text or code; the LLM keeps it |
| `open_ended` | pre-call | nothing to enumerate, so no primitive fits |
| `oversized` | pre-call | state above the budget; shrink it or take the questions |
| `unsure` | post-call | confidence below the threshold; Jev's answer stays in `answer` as a prior |
| `unreachable` | on failure | the backend failed; proceed as if Jev were not there |

The `unreachable` path is worth checking against your own risk model: in [`src/judge.ts`](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/src/judge.ts) a backend exception converts every question in the batch into an escalation, so a dead backend hands work back instead of answering it, and the gate then asks rather than allowing.

## Get started

**Installation downloads npm packages and makes no inference request.** In the project where your agent runs:

```sh
npx -y jev-use install     # wires Claude Code, Codex and pi — whichever it finds
npx -y jev-use doctor      # resolves the backend and makes one live round trip
```

`doctor` is the only one of those two that calls a provider, so it needs a key and incurs that provider's usage charge.

**Keyless offline check**, from a separate source checkout. It uses the mock backend and contacts no provider:

```sh
git clone https://github.com/shitianfang/jev-use.git
cd jev-use
git checkout ccce36aba1c5a6a0a4c00c2490d4218954560b1c
npm ci --ignore-scripts --no-audit --no-fund
npm run build
node examples/demo.mjs
```

Expected output, from scripted mock answers rather than Jev:

```text
ci-142: merge (confidence 0.95, severity: routine) — no LLM tokens spent
ci-143: -> LLM (unsure, prior=rerun)
ci-144: -> LLM (writing)
```

The three lines are the three routes: acted on, handed back as a prior, and never sent at all. **The probabilities are written into the demo, so this establishes the routing code's behaviour and nothing about Jev's accuracy.**

As a library, the same contract is four exports:

```js
import { Jev, check, pick, rate } from "jev-use";

const jev = new Jev();                  // backend resolved from the environment
const { answers } = await jev.judge(state, {
  passed: check("Did the run fully succeed?"),
  next: pick("Next action?", { merge: "all green", rerun: "looks flaky", hold: "needs attention" }),
  risk: rate("How risky?", ["routine", "worth a look", "incident"]),
});
answers.next.escalate;   // true → this one is yours; answers.next.answer is only a prior
```

`new Jev({ backend: "mock" })` needs no key, and any object implementing the `JevBackend` interface can stand in for tests or a custom transport.

## Adaptation tips

- Put everything Jev may consider into `state`; it sees no other context, and the state is resent with each batch, so repeated content is repeated cost.
- Batch by state, not by question. The design assumes every question about one state arrives in one call.
- Scope the gate's matcher. Each gated tool call adds a network round trip, so gating every tool is a tax on the ones that were never risky.
- Decide what `unsure` means in your loop before you enable anything. The answer is still present and may be worth using as a prior, or worth discarding.
- Tune `confidence_threshold` on your own traffic, and per backend — the number means different things on a vendor confidence head and on the Vercel margin fallback.

## Examples and demos

- [Unit tests](https://github.com/shitianfang/jev-use/tree/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/test): 58 offline tests covering routing, screening, the verdict contract, the per-provider wire shapes, installation, and the MCP tool surface. Run `npm test` with no key.
- [`scripts/smoke.mjs`](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/scripts/smoke.mjs): `npm run smoke` spawns the built CLI and drives it with a real MCP client over stdio on the mock backend. Offline.
- [`examples/demo.mjs`](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/examples/demo.mjs): the keyless triage loop shown above.
- [`bench/examples/`](https://github.com/shitianfang/jev-use/tree/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/bench/examples): eleven scripts that each print their own measured result row. These make **live** calls and cost provider usage. The animated demos in the upstream README are recordings of these scripts.

## Limits and data handling

On any backend but `mock`, the `state` you assemble — tool output, file excerpts, proposed commands — is sent to the provider you configured. Nothing is redacted for you. `JEV_BACKEND=mock` keeps everything local and answers from a script. Provider retention is governed by whichever of TypeSafe, OpenRouter, or the Vercel AI Gateway you point it at.

The OpenRouter `decisions` endpoint is described upstream as alpha and may move. Wire shapes for all three providers are pinned by fixture tests rather than by live contract tests, so a silent provider change would surface at `jev-use doctor`, not in CI.

The gate reads an action's intent, not its outcome, and adds one round trip per matched call. Its allow path spends no LLM tokens; a deny or ask feeds a reason back to the model, which is the point of it.

The project's own measurements live in [`bench/RESULTS.md`](https://github.com/shitianfang/jev-use/blob/ccce36aba1c5a6a0a4c00c2490d4218954560b1c/bench/RESULTS.md) and are **author-measured, on one provider, one region, one day**; this review did not reproduce them. That file is worth reading before adoption mainly for what it reports against the project: on its context-compaction family, agreement scored below a constant answerer, and it publishes that result rather than dropping the family; it also records that the model selected one of three options zero times in eighty calls, and that a headline speed comparison shrinks from roughly fourteen times to three once the baselines are given constrained enum output. Treat every figure there as the author's own, and the per-family and negative sections as more informative than the headline.

## Review and maintenance

Reviewed on **2026-09-19** at [commit ccce36a](https://github.com/shitianfang/jev-use/tree/ccce36aba1c5a6a0a4c00c2490d4218954560b1c): package version 0.6.0, plugin manifest 0.6.0. AI-assisted source review by the maintainer covering the library, MCP server, CLI, hook adapter, skill, license, and examples; the maintainer reviewed and is responsible for this page. On Node.js 20.20.2 in a Linux container, `npm ci --ignore-scripts`, `npm run build`, `npm run typecheck`, and `npm test` (**58 tests across 7 files**) all passed; `npm run smoke` reported `smoke OK — stdio handshake, jev_judge x3 primitives, jev_gate`; `node examples/demo.mjs` produced the three lines quoted above.

Not checked: any live TypeSafe, OpenRouter, or Vercel request; installation into a real Claude Code, Codex, or pi profile; the PreToolUse gate running inside a harness; and every number in `bench/`, which was not re-run. No model-quality claim in this page rests on anything measured here.

Related: [Cua jev-use](cua-jev-use.md) is a different project with the same short name; [pi-warden](pi-warden.md) also places Jev judgments in front of agent actions, from inside Pi rather than through MCP; [fast-jev-compaction](fast-jev-compaction.md) and [jev-router](jev-router.md) apply Jev to two other points of the same loop.
