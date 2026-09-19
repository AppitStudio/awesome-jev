# jev-rules

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Claude Code plugin that uses Jev to select project rules and codebase-map documents for each request and file change.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EliaAlberti/jev-rules) |
| Maintainer | [Elia Alberti](https://github.com/EliaAlberti) |
| Format | JavaScript / Node.js · Claude Code plugin and command hooks |
| Jev's role | Noul judgments select rule and map descriptions relevant to a prompt, or rules relevant to a file path. |
| Requirements | Claude Code with plugin support; Node.js with `util.parseEnv`; upstream specifies Node 20.12+, and this review used Node 24.11.1. A TypeSafe or Vercel AI Gateway key enables filtering. |
| Access and costs | Source installation; Claude Code access and provider inference are separate requirements and may incur charges. |
| License | [MIT](https://github.com/EliaAlberti/jev-rules/blob/9c8e25f67625075f6128c0b14ca3715ff6785d4a/LICENSE) |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use it when a Claude Code project has many instructions but each task needs only a few,
when file changes reveal a topic missing from a vague prompt, or when a project map is
too large to load in full. It supplies relevant context; it does not enforce policy or
block tool calls.

## How it works

The [hooks](https://github.com/EliaAlberti/jev-rules/blob/9c8e25f67625075f6128c0b14ca3715ff6785d4a/plugins/jev-rules/hooks/hooks.json)
read Markdown from `.claude/jev-rules/` and `.claude/jev-map/`.
Map documents from `.claude/.codebase-info/` are also supported. The
[Jev client](https://github.com/EliaAlberti/jev-rules/blob/9c8e25f67625075f6128c0b14ca3715ff6785d4a/plugins/jev-rules/hooks/lib/jev.mjs)
sends one typed question per candidate in a batched request. Direct TypeSafe calls use
`/v1/systemone`, `jev-latest`, and `noul`; the Vercel route uses its evaluation-model
endpoint with `typesafe-ai/jev` and `boolean` questions.

Application code applies a configurable probability threshold, default `0.6`, and inserts
selected rule bodies verbatim as hook context. Rule descriptions can include `applies`
and `does_not_apply` criteria. Rules marked `always: true` bypass Jev. By default, each
rule or map document is delivered once per session, including always rules; changed
bodies and clear/compaction events make them deliverable again. File judgments are cached.

## Get started

The [upstream instructions](https://github.com/EliaAlberti/jev-rules#install) describe
installation inside Claude Code:

```text
/plugin marketplace add EliaAlberti/jev-rules
/plugin install jev-rules@jev-rules
/reload-plugins
```

Clone the source to inspect the examples and run its dependency-free offline suite:

```sh
git clone https://github.com/EliaAlberti/jev-rules.git
cd jev-rules
npm test
```

Use a Node version that provides `util.parseEnv`; Node 21.6.1 failed during this review,
while Node 24.11.1 passed. Put rule Markdown files in your target project's
`.claude/jev-rules/`, using the supplied
[payment, deployment and spelling rules](https://github.com/EliaAlberti/jev-rules/tree/9c8e25f67625075f6128c0b14ca3715ff6785d4a/examples/rules)
as examples. The frontmatter `description` states when the rule applies, followed by
its instruction body. Map examples go in `.claude/jev-map/`.

For live filtering, configure `JEV_API_KEY` or `TYPESAFE_API_KEY`, or
`AI_GATEWAY_API_KEY` for Vercel, privately in the environment or `~/.jev-rules.env`.
The plugin also reads the target project's `.env`. Once enabled, prompts and rule/map
descriptions reach the selected provider and inference may be charged. A checkout task
should receive matching payment guidance if its probability meets the threshold;
that outcome depends on the model. Without a key, pending rules are included through
the fallback path instead of being classified.

## Examples and demos

- [Example rules and map documents](https://github.com/EliaAlberti/jev-rules/tree/9c8e25f67625075f6128c0b14ca3715ff6785d4a/examples) demonstrate frontmatter and topic-specific guidance.
- [Upstream demonstration](https://eliaalberti.github.io/jev-rules/) and [capture materials](https://github.com/EliaAlberti/jev-rules/tree/9c8e25f67625075f6128c0b14ca3715ff6785d4a/social) show a Claude Code session; these are upstream evidence, not a session reproduced in this review.
- [Offline tests](https://github.com/EliaAlberti/jev-rules/tree/9c8e25f67625075f6128c0b14ca3715ff6785d4a/test) cover selection, missing answers, errors, retries, caching, session delivery and hook envelopes with synthetic responses.

## Limits and data handling

Missing or invalid probabilities include the affected rule. Missing keys, network errors,
timeouts and HTTP failures include pending rules and list map-document pointers.
One retry is allowed for HTTP 429/529 within the configured deadline. The default deadline
is two seconds. This fallback preserves context when possible, not guaranteed delivery:
output budgeting can omit lower-probability rules, fixed/fallback rules can themselves
exceed the budget, and an unexpected top-level failure returns no context.

The file hook judges paths only. It observes Edit, Write, MultiEdit and NotebookEdit,
not changes through Bash, scripts or generators. Upstream documents that edit-hook context
can arrive with the first edit's result. Prompt manipulation and classification mistakes
can skip rules, so mandatory checks still belong in deterministic tooling.

Prompt requests send up to 24,000 characters plus candidate descriptions and criteria;
file requests send a relative path, or only the basename outside the project. Rule and
map bodies stay local except when a map's opening text supplies its missing description.
Session state is stored under the system temporary directory with restrictive permissions
and a week-old-file cleanup. Optional debug logs include prompt excerpts and file paths.

## Review and maintenance

Reviewed on **2026-09-19** at
[`9c8e25f67625075f6128c0b14ca3715ff6785d4a`](https://github.com/EliaAlberti/jev-rules/tree/9c8e25f67625075f6128c0b14ca3715ff6785d4a)
(version 0.3.0). Inspected the README, MIT license, package configuration, hooks,
Jev wire formats, loaders, rendering/fallback policy, session state, examples and tests.

Ran the six test files named by `npm test` using `node --test --test-reporter=spec`
under Node 24.11.1 with a cleared process environment: **101 tests passed**. Tests use
mocked provider responses and temporary projects/homes. An initial Node 21.6.1 run failed
because `util.parseEnv` was unavailable. No plugin installation, live API requests,
Claude Code integration session, or model-quality evaluation was performed. Upstream
cost, latency and token-saving claims were not independently validated.
