# Foreman

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An experimental Python supervisor that uses Jev to assess a running Codex worker and deterministic policy to steer, stop, retry, verify, or finish a software job.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thruwire/foreman) |
| Maintainer | [thruwire](https://github.com/thruwire) |
| Format | Python CLI and asynchronous supervision runtime; architectural experiment. |
| Jev's role | Ten `Noul` assessments over bounded worker/repository observations using `typesafe-sdk`, `AsyncTypeSafeClient.system_one`, and `jev-latest`. |
| Requirements | Python 3.11+; live runs require `TYPESAFE_API_KEY`, authenticated Codex CLI, and a target repository. The default backend requires `codex app-server`. |
| License | [MIT](https://github.com/thruwire/foreman/blob/3de1556a59b7a7e14daa1f89b2fc49080bbb8cce/LICENSE). |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use Foreman to study a supervisory loop that runs alongside a coding agent, inspect persisted decisions, or experiment with intervention policy. Its deterministic simulation provides a starting point without invoking either provider.

It is a developer experiment, not a validated quality gate or a security boundary. It currently runs one worker at a time, with a separate verification worker when policy requests one.

## How it works

The [Jev adapter](https://github.com/thruwire/foreman/blob/3de1556a59b7a7e14daa1f89b2fc49080bbb8cce/src/foreman/foreman/jev.py) submits ten named questions covering completion, requirements, tests, progress, drift, verification, and human intervention. See the [upstream integration explanation](https://github.com/thruwire/foreman#why-jev) for SDK and API documentation links.

An independent observation loop collects worker output, recent events, repository status, a bounded diff, and root `AGENTS.override.md` or `AGENTS.md` instructions. [Python policy](https://github.com/thruwire/foreman/blob/3de1556a59b7a7e14daa1f89b2fc49080bbb8cce/src/foreman/policy.py) applies thresholds and worker, retry, iteration, and steering limits. Codex performs the actual software work; Jev does not choose individual tools or files.

The default App Server backend can steer an active turn. `FOREMAN_CODEX_BACKEND=exec` selects the older subprocess backend, which cannot receive live steering. State and events are written under `.foreman/runs/<run-id>/` in the target repository.

## Get started

These commands follow the inspected source setup; installation and execution were not performed for this review. Start with the synthetic demo:

```sh
git clone https://github.com/thruwire/foreman.git
cd foreman
python3 -m venv .venv
source .venv/bin/activate
python -m pip install '.[dev]'
foreman demo --repo .
```

The demo uses simulated assessments and workers, needs no credentials or external services after dependency installation, and is designed to progress through implementation and verification to `FINISH`. It writes local run artifacts and reads repository observations; its output is not measured model behavior.

For a live run, provide `TYPESAFE_API_KEY` through your environment or the documented `.env` setup, install and authenticate Codex, and choose a repository whose changes you are prepared to review. Live execution sends repository context to TypeSafe and the coding provider and may incur their usage charges:

```sh
foreman run --repo ./my-project --job "Add rate limiting to the API and test it."
foreman runs --repo ./my-project
foreman inspect RUN_ID --repo ./my-project
```

Replace `./my-project` with the actual target path and `RUN_ID` with the reported identifier. This starts real coding work and can modify that repository. Follow the [installation and runtime instructions](https://github.com/thruwire/foreman#installation) for configuration.

## Examples and demos

- [Deterministic CLI demo](https://github.com/thruwire/foreman#deterministic-demo): simulated supervision with the same runtime, policy, persistence, and terminal rendering.
- [Integration tests](https://github.com/thruwire/foreman/blob/3de1556a59b7a7e14daa1f89b2fc49080bbb8cce/tests/test_integration.py): synthetic verification, steering, stuck-worker retry, and event-coalescing scenarios.
- [Live steering design](https://github.com/thruwire/foreman/blob/3de1556a59b7a7e14daa1f89b2fc49080bbb8cce/docs/steering.md): transport and intervention details; no separate hosted demo was established.

The documented test command is `python -m pytest`. The reviewed adapter and integration tests inject fake clients or workers; they do not establish Jev assessment quality.

## Limits and data handling

- Missing, nonnumeric, boolean, or nonfinite answers raise an assessment error. Finite values outside `[0, 1]` are clamped, rather than rejected; persisted assessments are normalized scores, not full raw SDK responses.
- The adapter configures retries for 429 and selected transient server errors within a timeout. Assessment failures handled by the runtime escalate the job and terminate active work. There is no separately calibrated uncertainty state; thresholds are experimental.
- Observations are incomplete. The inspected builder uses ordinary `git diff`, so staged changes and untracked file contents are not included in that diff; `test_results` is empty and verification evidence comes through worker records. Completion scores are not independent proof of correct code or passing tests.
- Jobs, diffs, output tails, root agent instructions, prior assessments, and recent events can reach TypeSafe. Codex also receives the job and works in the repository. Local state and event logs contain job and worker evidence; assess sensitive content before use. Bounding text is not secret redaction.
- The App Server backend requests `workspace-write` and `approvalPolicy: never`. Execution depends on the local Codex environment; Foreman is not an isolation system. Review its permissions before using live supervision.
- App Server compatibility, provider costs, failure recovery, and semantic thresholds were not validated live. No speed, accuracy, or productivity claims are established by this listing.

## Review and maintenance

Reviewed on **2026-09-19** at [commit `3de1556a59b7a7e14daa1f89b2fc49080bbb8cce`](https://github.com/thruwire/foreman/commit/3de1556a59b7a7e14daa1f89b2fc49080bbb8cce), package version **0.3.0**.

Inspected the README, MIT license, package metadata, CLI, Jev adapter, assessment schema, policy, observation builder, runtime, Codex transport settings, and adapter/integration tests. This was source inspection only: no dependency installation, test execution, Codex launch, provider requests, or quality evaluation. Upstream demo and test expectations are distinguished from observed results above.

Related: [Jev Review](jev-review.md) provides a separate MCP interface for software-quality assessments.
