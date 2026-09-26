# jev-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Route fresh Claude Code and Codex turns through a local proxy that asks Jev to choose a model, with deterministic fallback policy and inspectable routing exchanges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gargpratyush/jev-router) |
| Maintainer | [gargpratyush](https://github.com/gargpratyush) |
| Format | JavaScript / Node.js CLI launchers and loopback HTTP proxies; package version 0.3.0. |
| Jev's role | Chooses among available model IDs and scores task, reasoning, and tool complexity through the TypeSafe SDK's `systemOne` method. |
| Requirements | Node.js 20.12+, installed and authenticated Claude Code or Codex CLI, and `JEV_API_KEY` or `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/LICENSE). TypeSafe and coding-provider usage have separate account requirements and costs. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use this to experiment with per-turn model selection while retaining a coding CLI's usual interface, or to study how typed routing decisions can be combined with explicit overrides, confidence rules, and conversation state.

It is distinct from the [Jev Model Router](jev-model-router.md) Claude Code mod: this project wraps both coding CLIs with proxies rather than requiring Claude Code function hooks. Compatibility depends on their evolving request formats.

## How it works

The launchers start an HTTP server bound to `127.0.0.1`, point the CLI at it, and forward requests and authorization headers to the coding provider. A `jev-router` model-picker entry signals automatic routing; selecting a concrete model bypasses the selector.

The [routing client](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/src/router.mjs) sends the fresh prompt, current model, estimated context length, and candidate model IDs to TypeSafe. The inspected code depends on `@typesafe-ai/sdk` `^0.6.0` and does not pin a Jev model version explicitly.

The [configuration](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/src/config.mjs) defines typed model-choice and complexity questions. The [policy](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/src/policy.mjs) then resolves a tier, and proxy code rewrites the request to an exact model:

- Explicit model/tier phrases take precedence through regular-expression matching.
- Missing or unrecognized answers retain the current tier; the client catches request failures and imposes a three-second total deadline with at most one retry.
- Confidence below 0.3 prevents downgrades and limits upgrades; a separate context-size rule also prevents some downgrades. These are upstream policy choices, not validated quality guarantees.
- Tool-loop continuations reuse the chosen model. Main and subagent conversations have separate routing state.

## Get started

Install an authenticated coding CLI first and obtain a TypeSafe key. The source path avoids assuming that a registry release matches the reviewed commit:

```sh
git clone https://github.com/gargpratyush/jev-router.git
cd jev-router
git checkout 38da6b84ea01241bfc41fbddc0928d0f40a703f0
npm ci --ignore-scripts
```

Provide `JEV_API_KEY` through your environment or the user-level `~/.jev-router.env` file described in the [upstream setup](https://github.com/gargpratyush/jev-router#quick-start). Do not commit it. Project-local `.env` files are also loaded by the launchers.

The following are **live launch commands**. Prompts and routing metadata go to TypeSafe, and the coding session goes to Anthropic or OpenAI; provider charges or subscription limits can apply. The launched coding agent can use its configured tools and permissions.

```sh
# From the source checkout; choose one installed CLI:
node bin/jev-claude.mjs
node bin/jev-codex.mjs
```

For use in other working directories, upstream documents `npm link`, followed by `jev-claude` or `jev-codex`. Without a TypeSafe key the launchers start the ordinary CLI without routing. A successful routed turn displays a Claude status line or Codex commentary naming the selected model.

## Examples and demos

- [README interface examples and screenshots](https://github.com/gargpratyush/jev-router#claude-code-interface) show the model picker and explanation display; they are upstream examples, not this catalog's execution results.
- [Policy tests](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/test/policy.test.mjs) provide synthetic confident, uncertain, unavailable, override, and context-size cases.
- [Codex tests](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/test/codex.test.mjs) and [proxy tests](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/test/proxy.test.mjs) exercise request rewriting, routing state, and local status handling with test fixtures.

The packaged `/jev-explain` or `$jev-explain` skill reads stored routing exchanges instead of making another Jev request. No separate hosted demo was identified. `test/live-routing.mjs` requires provider access and is separate from `npm test`.

## Limits and data handling

The source sends **prompt text plus routing metadata** to TypeSafe, including current/candidate model IDs and estimated context length. This is more than the README's statement that only prompt text is sent. It does not send the full conversation through the inspected routing request; coding-provider traffic still passes through the local proxy.

Up to 20 recent decisions per session, including prompts and exact TypeSafe requests/responses, are stored in the operating-system temporary directory under `jev-claude`. Source code applies owner-only POSIX modes and prunes files older than seven days when writing status; those mode bits are not enforced by Windows. Debug logging can retain prompt excerpts, and `JEV_DUMP` writes full coding-request bodies.

Starting `jev-codex` installs or overwrites its bundled explanation skill at `~/.agents/skills/jev-router-explain/SKILL.md`. The Claude launcher adds its package directory to the session and attempts to restore the previous saved model setting on exit. Review these local effects before adoption.

Upstream reports development on Windows with Claude Code 2.1.101 and Codex 0.154.0. Those compatibility claims were not independently reproduced. Native request schemas, model availability, CLI settings, and Codex enterprise origins can affect operation. Routing thresholds and cost savings have not been evaluated by this catalog; regex overrides also do not establish a semantic understanding of user intent.

## Review and maintenance

Reviewed on **2026-09-19** at [commit `38da6b84ea01241bfc41fbddc0928d0f40a703f0`](https://github.com/gargpratyush/jev-router/tree/38da6b84ea01241bfc41fbddc0928d0f40a703f0).

Inspected the README, package manifest, MIT license, launchers, routing questions/client/policy, both proxy implementations, status persistence, and representative policy/proxy/Codex tests. This was a **source-only review**: no dependency installation, test execution, authenticated CLI launch, provider request, cross-platform validation, or routing-quality evaluation was performed.

See the [catalog validation scope](../../../docs/validation.md#community-project-checks) for the distinction between directory checks and upstream behavior.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [10 Jev project ideas with practical starting points](../../knowledge-base/articles/jev-project-ideas.md) — Mentioned in the source article. Build 6: choose a model for a coding-agent turn.
<!-- knowledge:backlinks:end -->
