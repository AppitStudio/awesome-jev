# Codex Jev Router (suenot)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Use a typed Jev decision to choose a Codex subagent model and reasoning effort when a parent agent delegates work.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suenot/codex-jev-router) |
| Maintainer | [suenot](https://github.com/suenot); this is a maintainer submission prepared with Codex assistance. |
| Format | Node.js command-line router, installer, and English/Russian setup guides. |
| Requirements | Node.js 20+, Codex with subagents, and either a Jev credential or a separately running compatible local decider. |
| License | [MIT](https://github.com/suenot/codex-jev-router/blob/c31f1bcc9c792d526c5b6ca0bbbc2bad8bfdf695/LICENSE). |
| Disclosure | Source and documentation were inspected for this listing. No independent cost or latency measurement was performed. |

## When to use

Use it to give delegated Codex tasks an explicit model and reasoning setting. The parent agent remains responsible for deciding whether a subagent helps and for passing a short, sanitized summary to the router before spawning one.

## How it works

[`src/router.mjs`](https://github.com/suenot/codex-jev-router/blob/c31f1bcc9c792d526c5b6ca0bbbc2bad8bfdf695/src/router.mjs) asks one Jev `Choice` for the task tier and one `Noul` for exceptional difficulty. Code applies confidence thresholds, keeps reviewers on Sol high by default, and falls back to Sol high when the decision is unavailable. A verified Sol failure can select Sol ultra. [`src/decider.mjs`](https://github.com/suenot/codex-jev-router/blob/c31f1bcc9c792d526c5b6ca0bbbc2bad8bfdf695/src/decider.mjs) supports hosted Jev and optional compatible local HTTP or command backends.

The installer backs up existing Codex configuration, adds routing instructions to `AGENTS.md`, and configures subagent role files. This is an instruction-driven workflow; the project does not claim automatic interception of every spawn.

## Get started

From the [setup guide](https://github.com/suenot/codex-jev-router/blob/c31f1bcc9c792d526c5b6ca0bbbc2bad8bfdf695/README.md):

```sh
gh repo clone suenot/codex-jev-router
cd codex-jev-router
npm ci
npm run check
node scripts/install.mjs --dry-run
node scripts/install.mjs
npm run doctor -- --live
```

Inspect the dry run before installation. The live doctor check needs the selected decider to be configured and reachable. Hosted Jev sends the task summary to TypeSafe and may incur inference charges.

## Examples and demos

The [direct routing example](https://github.com/suenot/codex-jev-router/blob/c31f1bcc9c792d526c5b6ca0bbbc2bad8bfdf695/README.md#direct-routing-and-retry) shows how to pass a task summary and use the returned `model` and `reasoning_effort`. There is no separate hosted demo.

## Limits and data handling

A parent agent must sanitize summaries; common secret patterns trigger a local fallback, but this cannot detect every private value. Hosted Jev receives the summary, while a local backend can keep it on the machine. The project records decision metadata locally and documents rollback. It has no measured cost-savings claim or tool-boundary enforcement.

## Review and maintenance

Reviewed on **2026-09-24** at [commit c31f1bc](https://github.com/suenot/codex-jev-router/tree/c31f1bcc9c792d526c5b6ca0bbbc2bad8bfdf695). The router, decider, installer behavior, README, and license were inspected for this listing. No live Jev call, Codex installation, or independent performance test was run as part of this catalog review.

Related: [Codex Jev Preflight](codex-jev-preflight.md), [jev-codex-router](jev-codex-router.md).
