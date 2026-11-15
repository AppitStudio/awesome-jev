# Attest (tmux orchestration for real Claude Code and Codex roles in git worktrees, with Jev decision gates and a hash-chained audit ledger)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One command calls up an agent team: a plan is approved at a human gate, builder roles run as real Claude Code or Codex sessions in their own tmux windows and git worktrees, a reviewer role checks the branches, and only reviewed work is merged. Hosted Jev scores plan risk and clarity, role boundaries, result fidelity and merge risk; every decision goes into an append-only, hash-chained ledger with outcomes for calibration. Jev runs in shadow mode by default (recorded, not enforced); the README is a live run including a false positive it shows on purpose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NIRVANA-APOC/Attest) |
| Maintainer | [NIRVANA-APOC](https://github.com/NIRVANA-APOC). Independently curated. |
| Format | Node.js CLI and agent skill (TypeScript, MIT; build from source) |
| Requirements | Linux, macOS or WSL2, tmux, git, Node 20+, Claude Code and/or Codex CLI, and `ATTEST_JEV_API_KEY` for hosted Jev (an offline heuristic is used otherwise). |
| License | [MIT](https://github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/typesafe.ts`](https://github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/src/jev/typesafe.ts) at the pinned commit. |

## When to use

- Run parallel coding agents with human gates and an auditable record of Jev's risk calls.
- Mismatch: fully automatic merging; Attest is built around human approval.

## How it works

`src/jev/typesafe.ts` posts typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default; the README run used `jev-1.14.0`); `src/jev/report.ts` writes the audit report, and `tools/jev-live-check.mjs` sends one live check. Integration evidence: [`src/jev/typesafe.ts`](https://github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/src/jev/typesafe.ts).

## Get started

Build and link the CLI, install the workflow skill, then start a case from inside tmux.

```sh
git clone https://github.com/NIRVANA-APOC/Attest && cd Attest
npm ci && npm run build && npm link   # 0.1.0 is not on npm
attest setup
export ATTEST_JEV_API_KEY=$TYPESAFE_API_KEY
attest up -m my-case --orch claude
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (live run): [github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/README.md](https://github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/README.md)
- Jev audit guide: [github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/docs/jev-audit.md](https://github.com/NIRVANA-APOC/Attest/blob/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca/docs/jev-audit.md)

## Limits and data handling

Plan, role and result summaries are sent to TypeSafe on your key; coding runs use whatever providers your Claude Code and Codex are configured for. The maker presents Jev's answers as signals, not authority, and notes calibration needs more recorded outcomes.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit dcc42e93e212](https://github.com/NIRVANA-APOC/Attest/tree/dcc42e93e212a40fa21b4f3b2e793cd91fe6feca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
