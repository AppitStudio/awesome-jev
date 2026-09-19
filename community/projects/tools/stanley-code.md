# Stanley Code

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An experimental TypeScript CLI that routes natural-language requests into bounded Jev workflows for finding code, reviewing changes, and triaging failures, with an optional Pi coding-agent fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/devagrawal09/stanley-code) |
| Maintainer | [Dev Agrawal](https://github.com/devagrawal09). Independent community project. |
| Format | Source-built CLI and extensible workflow runtime. |
| Jev's role | Selects an eligible workflow and answers typed questions about bounded code or log evidence; deterministic code validates answers and produces advisory findings. |
| Requirements | Node.js 22.18+, Git, a target Git repository, and `TYPESAFE_API_KEY` for live requests. Optional Pi installation and separate model credentials for coding-agent delegation. |
| Access | MIT source; live TypeSafe and optional Pi-provider usage may incur charges. Upstream describes version 0.1.0 as unreleased and directs users to build from source. |
| License | [MIT](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/LICENSE). |
| Disclosure | AI-assisted catalog review. Contributor affiliation/commercial relationships were not supplied; inclusion is not an endorsement. |

## When to use

Use Stanley to locate relevant files, compare a diff with its requested task, screen changes for correctness or test gaps, or triage saved test failures and review comments. It also offers specialized security, performance, compatibility, and change-summary workflows. Reports identify examined evidence and work left unchecked.

Its distinct extension path lets a repository provide trusted workflows that gather evidence in code and call Jev through a shared judge interface. An optional coding agent can draft further workflows for a person to review and promote. These experiments do not establish software correctness or replace tests and human review.

## How it works

The [router](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/src/cli/router.ts) combines deterministic capability checks with a Jev choice over built-in and repository workflow metadata. Code requires confidence of at least 0.6, selected probability of at least 0.55, and a margin of at least 0.15; uncertain or unavailable selections become `cannot_tell`.

Selected built-ins gather bounded Git hunks, file excerpts, or supplied input. The [SDK adapter](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/src/adapters/jev.ts) uses `@typesafe-ai/sdk` 0.6.0 and `TypeSafeClient.systemOne`; the inspected default model is `jev-1.13.0`, overridable through `TYPESAFE_MODEL`. Validation checks answer keys, types, probabilities, and distributions. Application policy turns accepted answers and exact code signals into findings, parked items, and coverage information.

Trusted modules under `.stanley/workflows/` extend the workflow registry. They can compose requests and call the budgeted `judge` function. If no workflow supports a request and Pi is available, the CLI can delegate the task and queue a detached improvement worker. Candidate workflows are staged under `.stanley/candidates/`; activation requires `--promote-candidate`. The [architecture](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/docs/architecture.md) describes these boundaries.

## Get started

Build the reviewed source with Node.js 22.18 or newer. Installation downloads dependencies; the checks below use fake Jev and fake coding-agent implementations and need no provider credentials:

```sh
git clone https://github.com/devagrawal09/stanley-code.git
cd stanley-code
git checkout 29d4c829e9c8a1f2992639ea8ba13f25f0930fa2
npm ci --ignore-scripts
npm run check
node dist/cli.js --help
```

The check command runs lint, typechecking, tests, a build, and a CLI smoke test. The smoke test creates a temporary Git repository and exercises routing, reports, delegation, candidate validation, promotion, and reuse with fakes. There is no general `--offline` CLI option. Do not install the older `jev-code` placeholder package as a substitute.

For a live review, set `TYPESAFE_API_KEY` in your process environment. The following sends the request and selected repository evidence to TypeSafe and may incur charges; it was not run during this review:

```sh
node dist/cli.js "Review these changes for correctness bugs" \
  --repo /absolute/path/to/your-repository --no-agent --no-persist --json
```

Replace the target path with your Git repository containing changes. Inspect `output.data.findings`, `parked`, `coverage`, and `notChecked`; an empty findings list is not approval. `--no-agent` disables Pi delegation and improvement jobs, but still loads trusted repository workflows. Review any installed workflows before invoking Stanley. `--no-persist` disables built-in run records, not arbitrary workflow side effects.

## Examples and demos

- [CLI smoke test](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/scripts/smoke-cli.ts): 37 synthetic cases, including the delegate → improve → promote → reuse sequence.
- [Stale TODO workflow](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/examples/workflows/stale-todo-audit.ts): reads up to 20 TODO/FIXME comments from `src/app.ts`, asks fixed-choice questions, and applies a probability threshold in code. Using it normally requires live Jev access.
- [Upstream usage guide](https://github.com/devagrawal09/stanley-code/blob/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2/README.md): requests, input conventions, source installation, and extension setup. No separate hosted demo was established.

## Limits and data handling

- Findings are advisory. Changed-code analyses do not execute tests, benchmark the program, inspect deployed consumers, or establish security. Uncertain evidence and budget limits remain visible in reports. Thresholds were not calibrated by this review.
- The executor bounds requests, time, and estimated token usage, validates responses, and owns transient retries. These controls do not bound arbitrary operations performed by trusted workflow code or an external agent.
- TypeSafe receives redacted routing information and the selected workflow's evidence, which can include source code, diffs, and log excerpts. Secret filtering is best effort. Built-in records under `.stanley/runs/` include request/response evidence and decisions after redaction; they can still contain sensitive code. Workflows control their own persistence.
- Repository workflows execute in-process with the user's privileges. Pi delegation and background improvement can modify the repository and inherit the environment, including credentials. The inspected Pi invocation includes `--no-approve`; candidate validation is not an execution sandbox. Delegated results are the agent's account, not Stanley-verified changes.
- The interface is experimental and source-only at the reviewed revision. Live TypeSafe compatibility, Pi integration, provider costs, and model quality were not validated. Upstream reports Linux CI and leaves Windows untested.

## Review and maintenance

Reviewed on **2026-09-19** at commit [`29d4c829e9c8a1f2992639ea8ba13f25f0930fa2`](https://github.com/devagrawal09/stanley-code/commit/29d4c829e9c8a1f2992639ea8ba13f25f0930fa2), package version **0.1.0**.

Inspected the README, MIT license, package metadata, SDK adapter, answer validation, routing and policy, workflow runtime and loader, recording, Pi adapter, improvement flow, reference workflow, and tests. Installed dependencies with `npm ci --ignore-scripts --no-audit --no-fund` and ran `npm run check` on macOS with Node.js 24.19.0 in a separate temporary checkout and credential-free environment. Lint, typechecking, build, all **191 tests**, and all **37 CLI smoke cases** passed. These were synthetic checks; no live Jev request or real coding agent was run. Catalog validation is recorded in the listing's publication change.

Related: [Jev Review (Dev Agrawal)](jev-review-devagrawal.md) offers staged review findings and a local dashboard; [Foreman](foreman.md) supervises a running Codex worker.
