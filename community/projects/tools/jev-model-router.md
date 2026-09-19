# Jev Model Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Use Jev task assessments to choose Claude Code subagent models and main-conversation reasoning effort, with routing rules kept in inspectable TypeScript.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router) |
| Maintainer | [davila7 / Claude Code Templates](https://github.com/davila7/claude-code-templates). Curated from public sources; this listing is not an upstream submission or endorsement. No contributor affiliation was supplied. |
| Format | TypeScript Claude Code mod using early-access function hooks. |
| Requirements | Upstream documents Node.js 18+ for the installer, Claude Code 2.1.259+, and `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`. Jev routing requires a TypeSafe account and `typesafeApiKey`, or a Vercel AI Gateway account and `gatewayApiKey`, in plugin options. Bun runs the upstream policy tests. |
| Access and costs | MIT-licensed source. Claude Code access and provider inference costs are separate; no cost savings or free inference were verified. Without a configured Jev backend, the mod uses Claude Code's built-in classifier instead. |
| License | [MIT](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/LICENSE). |

## When to use

Explore this when Claude Code tasks vary between mechanical edits, ordinary engineering, and work needing deeper reasoning. It provides configurable model tiers, separate confidence thresholds for upgrades and downgrades, and logs explaining routing decisions.

It is specific to Claude Code's early-access hooks. It does not provide a general model gateway, guarantee the cheapest successful model, or enforce permissions and spending limits.

## How it works

The [policy module](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/hooks/policy.ts) sends three independent questions in one request:

- A **Choice** selects a task tier: mechanical/local, ordinary engineering, or hard/high-stakes work.
- A **Score** estimates reasoning effort across four levels.
- A **Noul** asks whether carrying out the task would itself change production, move real money, or alter irrecoverable data. The Gateway transport names this primitive `boolean`.

Code maps these answers to model aliases and effort levels. The defaults are `haiku`, `sonnet`, and `opus`; upgrading needs confidence of at least `0.3`, while downgrading needs `0.6`. A risk probability above `0.7` forces the deep tier and an effort floor. These are upstream policy defaults, not validated thresholds for your workload or authorization to execute an action.

The [hook implementation](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/hooks/jev-model-router.ts) classifies a submitted prompt before the turn, then reuses its routing decision throughout that turn. Separate subagent prompts are classified when agents spawn; forked agents are skipped.

| Routing option | Default | Effect |
| --- | --- | --- |
| `routeSubagentModel` | On | Selects the model for a spawned subagent. |
| `routeMainEffort` | On | Adjusts the main conversation's reasoning effort. |
| `routeMainModel` | Off | Allows main-conversation model switching; upstream warns that cache invalidation can outweigh savings. |

The direct TypeSafe path uses `POST /v1/systemone` with `jev-latest`. The alternative uses Vercel's experimental evaluation endpoint with `typesafe-ai/jev`. TypeSafe wins when both keys are configured unless `provider` explicitly selects a backend.

## Get started

Read the [reviewed installation and configuration instructions](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/README.md) first. The commands below follow upstream instructions; installation and host loading were not executed during this review.

From the project where you want the mod installed:

```sh
npx claude-code-templates@latest --mod productivity/jev-model-router
```

This downloads and runs the installer, writing the plugin into `.claude/skills/jev-model-router/`. `@latest` may install a later revision than the one reviewed here.

Configure `typesafeApiKey` or `gatewayApiKey` privately through Claude Code's plugin configuration. For automatic loading from a trusted project's skills directory, the reviewed instructions use the `pluginConfigs` key `jev-model-router@skills-dir`. For explicit loading with `--plugin-dir`, they use `jev-model-router`. The loading method matters: a key under the wrong plugin ID leaves options at their defaults. Do not commit keys to project files.

**Live use:** classification sends prompt content to the selected provider and may incur charges. The no-Jev-key fallback also invokes a model through Claude Code; it is not an offline demo. Start an interactive session with the plugin explicitly selected:

```sh
CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude --plugin-dir .claude/skills/jev-model-router
```

With logging enabled, upstream documents a startup line identifying the backend, followed by classification and routing messages. Main model switching remains off unless enabled. For automatic loading instead, launch `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude` in a trusted project; an untrusted project's plugin is not automatically loaded.

## Examples and demos

- [AI Templates component page](https://aitmpl.com/component/mod/productivity/jev-model-router): installation entry point and a transcript-style preview. This is not independent evidence of model quality or savings.
- [Upstream README](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/README.md): example log output, configuration, and loading diagnostics. No separate live demo was tested here.
- [Policy tests](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/tests/policy.test.ts): synthetic responses covering backend selection, parsing, thresholds, effort, queued prompts, and log formatting.

With Bun installed, run the upstream offline tests from a source checkout at the reviewed revision:

```sh
git clone https://github.com/davila7/claude-code-templates.git
cd claude-code-templates
git checkout 61bfcd1586bf1076f6d3cfa0436317c912811e6c
bun test cli-tool/components/mods/productivity/jev-model-router/tests
```

Cloning requires network access; the inspected policy tests use synthetic inputs and make no provider requests. This full Bun command was not run during the review.

## Limits and data handling

The direct TypeSafe request and answer fields align with the inspected [HTTP API documentation](https://docs.typesafe.ai/api). The Gateway transport is an experimental wire format, and Claude Code's [function-hook API](https://github.com/anthropics/claude-code/tree/main/mods) may change. End-to-end compatibility was not tested.

The Gateway path uses the highest reported probability as its confidence proxy. This is not necessarily equivalent to TypeSafe's [distribution-derived confidence](https://docs.typesafe.ai/confidence), so identical thresholds need not produce equivalent behavior across backends. Missing confidence prevents downgrades when the current tier is recognized; unknown model IDs are treated as upgrades. These policies require evaluation on representative tasks.

HTTP failures, parsing errors, and the default 800 ms classification deadline leave routing unchanged. The deadline races the HTTP request without explicitly cancelling it, so a timed-out request may still complete and incur usage. The built-in classifier path has no equivalent explicit timeout. Response validation is partial, including no comprehensive numeric-range checks.

With a Jev backend configured, main-loop classification sends the submitted prompt; subagent classification sends the subagent prompt, description, and agent type. These fields can contain private project content. The code logs parsed judgments and routing decisions, but does not retain the complete raw provider response for later evaluation.

Upstream's statement that nothing leaves the machine without a key should not be treated as a local-only guarantee: that path calls `$.model.classify`, which Anthropic's [type declarations](https://github.com/anthropics/claude-code/blob/main/mods/types/claude-code.d.ts) describe as a model completion. No Jev key means no Jev backend request; the host's model and data-handling configuration still apply.

## Review and maintenance

Reviewed on **2026-09-19** at [commit 61bfcd1](https://github.com/davila7/claude-code-templates/tree/61bfcd1586bf1076f6d3cfa0436317c912811e6c), plugin version **0.4.1**. AI-assisted inspection covered the README, MIT license, manifest, hooks, policy, and synthetic tests, plus current TypeSafe API documentation and Anthropic's hook declarations.

Six focused offline assertions passed under Node.js 22.19.0 with TypeScript stripping: direct-API Noul request construction, refusal of a low-confidence downgrade, acceptance of a high-confidence downgrade, risk-driven escalation, unchanged routing after invalid JSON, and abstention when two prompt decisions are pending. All inputs and responses were synthetic. These checks establish those policy branches, not Jev accuracy, savings, or host compatibility.

The full Bun suite, installer, Claude Code session, live provider requests, and end-to-end cost or quality evaluation were not run. The component page's embedded version differed from the reviewed upstream manifest; use the pinned source above for the review evidence.

Related: [fast-jev-compaction](fast-jev-compaction.md) manages agent context; [Support Router](../../../projects/support-router/README.md) demonstrates routing and review policies offline.
