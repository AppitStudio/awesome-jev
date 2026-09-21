# Clean Code Review

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted (and source-built) pull-request reviewer: TypeSafe Jev judges each changed file against Uncle Bob-style Clean Code questions, then Luna writes evidence-first review prose; MCP endpoint for agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frostney/clean-code-review) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [clean-code-review.vercel.app](https://clean-code-review.vercel.app) — public web UI; MCP at the same deployment. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-21**. Hosted app uses operator AI Gateway budgets (documented ~$15/week project cap and per-session limits); self-host needs provider keys. Provider usage can incur charges. |
| Jev evidence | Inspected [agent/lib/judging/jev-model.ts](https://github.com/frostney/clean-code-review/blob/59e41b16af9210952471ffb59c9a69100f1f5679/agent/lib/judging/jev-model.ts) and [agent/lib/judging/questions.ts](https://github.com/frostney/clean-code-review/blob/59e41b16af9210952471ffb59c9a69100f1f5679/agent/lib/judging/questions.ts): Jev adapter for eve judging turns; Luna summarizes. Offline `bun test` mocks providers. Live PR review was not run. |
| Disclosure | Free source access does not include inference or hosted budgets. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [frostney](https://github.com/frostney) (Johannes Stein). |
| Format | Next.js / eve application with page UI and MCP server. |
| Platform and availability | Hosted web app and MCP; source build with Bun/Node. Public GitHub repositories only; up to 24 code files per review. |
| Jev's role | File-level Clean Code judgments (typed questions); Luna (separate model) drafts the human-readable review from those findings plus the PR description. |
| Requirements | For self-host: Bun/Node toolchain and AI Gateway / TypeSafe credentials as documented upstream. Hosted path uses the operator's budgets. |
| License | [MIT](https://github.com/frostney/clean-code-review/blob/59e41b16af9210952471ffb59c9a69100f1f5679/LICENSE). |

## When to use

Use it for a second opinion on public GitHub PRs when you want structured Clean Code checks before prose review, or an MCP tool agents can call. Prefer ordinary CI linters when you only need syntactic rules. Hosted reviews share the operator's spend caps.

## How it works

The app fetches a public PR, ranks changed files, and asks Jev the fixed question set per file. Findings feed Luna for a streamed review. Spend brakes and rate limits sit in the judging adapter and shared budgets. MCP exposes the same review path with its own limits.

## Get started

Hosted: open [clean-code-review.vercel.app](https://clean-code-review.vercel.app) and paste a public GitHub PR URL (subject to operator budgets).

Source:

```sh
git clone https://github.com/frostney/clean-code-review.git
cd clean-code-review
git checkout 59e41b16af9210952471ffb59c9a69100f1f5679
bun install
bun test
# configure env per upstream README, then bun run dev
```

Live reviews send PR file contents to model providers and may incur charges.

## Examples and demos

- Hosted product UI and MCP server card on the deployment.
- Offline tests under `agent/lib/**/*.test.ts` (judging, review, spend, rate limits).
- Architecture notes in upstream `docs/architecture.md`.

## Limits and data handling

Public GitHub PRs only; binaries/lockfiles/minified files skipped; prose files shown read-only. Hosted path enforces IP firewall limits and shared hourly/daily model budgets. PR text and code excerpts go to the configured providers. A full 24-file review is described upstream as about $0.02 in one measurement—treat as a single-run observation.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 59e41b1](https://github.com/frostney/clean-code-review/tree/59e41b16af9210952471ffb59c9a69100f1f5679): MIT. AI-assisted source review of README, LICENSE, Jev adapter, and question set. On Bun 1.4.2, **`bun test`: 70 passed**. No live TypeSafe or Luna calls; hosted UI not exercised end-to-end here.

Related: [Moongate](../tools/moongate.md) also evaluates PR diffs with TypeSafe Jev for CI annotations rather than Clean Code + Luna prose.
