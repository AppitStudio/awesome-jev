# tdd-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI gates for dual-agent TDD: TypeSafe Jev judges requirement↔test coverage, failing-test blame routing, gaming, weakening, and drift—without generating code. Optional `tdd-gate run` orchestrates isolated worktrees.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bensheridan/tdd-gate) |
| Maintainer | [bensheridan](https://github.com/bensheridan). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI **`tdd-gate` 0.1.0** (private package layout; `npm run build` → `dist/cli.js`). Depends on `@typesafe-ai/sdk`. |
| Requirements | Node.js **≥ 20** (upstream `.nvmrc` notes 24); `TYPESAFE_API_KEY` for live gates. `--dry-run` coverage path needs no key. |
| License | [MIT](https://github.com/bensheridan/tdd-gate/blob/30e27f6400259389ee774f7dfc6c9e27a2996db9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `package.json`). Offline `npm test` and live dual-agent runs were **not** executed on the review host. Upstream live-run anecdotes are author-reported. |

## When to use

Use it when a test-writing agent and a code-writing agent must stay on one plan and you need **typed** coverage/blame/gaming/weakening/drift judgments before accepting a turn. Prefer [agent-evals](agent-evals.md) for broader CI judging harnesses.

## How it works

Each subcommand builds TypeSafe System One questions over requirements, tests, diffs, and/or JUnit results; code applies thresholds and prints JSON routes. `tdd-gate run` drives two agent CLIs in throwaway worktrees (code agent’s tree has tests deleted), runs gates before commits, and stops for humans on ambiguous blame. Gates never contact agents themselves.

## Get started

```sh
git clone https://github.com/bensheridan/tdd-gate.git
cd tdd-gate
git checkout 30e27f6400259389ee774f7dfc6c9e27a2996db9
npm install && npm run build
node dist/cli.js coverage --requirements examples/slugify/requirements.yml --tests examples/slugify/tests --dry-run
# Live (charges): export TYPESAFE_API_KEY=... && drop --dry-run
```

## Examples and demos

- `examples/slugify/` fixtures for coverage/blame/gaming/weakening/drift.
- Upstream README live dual-Claude-Code run notes (not reproduced here).
- `eval/cases/` harvested scenarios.

## Limits and data handling

Live gates send requirement/test/diff text to TypeSafe. Orchestrator isolation is by worktree deletion of tests—not a full sandbox. Assertion messages shown to the code agent can leak inputs/expected outputs; gaming gate is meant to catch that. No live Jev in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 30e27f6](https://github.com/bensheridan/tdd-gate/tree/30e27f6400259389ee774f7dfc6c9e27a2996db9) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, package metadata. No live TypeSafe spend.

Related: [agent-evals](agent-evals.md), [semantic-assert](semantic-assert.md), [Canny](canny.md).
