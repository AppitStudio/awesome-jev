# mu

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Early-stage coding agent built on pi (CLI + desktop app) with a judgment kernel: Jev answers typed questions at decision points such as tool approval, constraint checks, context admission and test-log trimming, each switchable active/shadow/off and logged to a verdict ledger.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qybaihe/mu) |
| Maintainer | [qybaihe](https://github.com/qybaihe). Independently curated. |
| Format | Coding-agent CLI and desktop app (macOS, Windows, Linux builds on GitHub Releases) |
| Requirements | Node.js 22.19+ for the CLI (`npm i -g mu-agent`) or a desktop release; a model sign-in or API key for the main model. Jev via `TYPESAFE_API_KEY` or OpenRouter, Vercel AI Gateway, OpenCode Zen or Cloudflare keys. |
| License | [MIT](https://github.com/qybaihe/mu/blob/7335d774c998bb5d935ba14581a8f4be1a5f311e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let a small judge gate tool approvals and constraint crossings while the large model does the work.
- Trim long test logs and stale tool output by goal-aware Jev questions instead of summaries.
- Mismatch: pre-release; names, settings and formats may change. Use `MU_JUDGE=off` or Laya if nothing may leave the machine.

## How it works

Each decision point (`input.preflight`, `tool.approval`, `tool.constraint`, `tool.admission`, `context.forget`, `memory.capture`, `review.triage` and more) asks a bounded yes/no, choice or score question and records the verdict with its probability. Points can be `active`, `shadow` (asked and logged, no effect) or `off`, and each can name its own judge or cascade such as `laya,jev` ([README](https://github.com/qybaihe/mu/blob/7335d774c998bb5d935ba14581a8f4be1a5f311e/README.md)).

## Get started

Install the CLI and check the judges, then run a session (live judge calls):

```sh
npm i -g mu-agent
export TYPESAFE_API_KEY=...   # optional; see the note on the no-key default below
mu doctor
mu
mu ledger 5   # what the judge decided in the last 5 sessions
```

Important: with no judge key set, mu uses Jev 1.13 on OpenCode Zen (free for a limited time per upstream), so judged fields go to OpenCode; set your own key, choose Laya, or set `MU_JUDGE=off`. TypeSafe and other providers bill their own usage.

## Examples and demos

- README *Measured* section: maintainer study where Jev trimmed 40.2% of tuned-goal test logs with 0/72 required lines lost (282 live requests ≈ $0.017). Upstream-reported on synthetic projects; not reproduced here.
- `node kyrn/spikes/judge-bench/test-log-replay.ts` replays the non-Jev arms offline.

## Limits and data handling

Early development (0.1.x). The judge sees only the fields each question needs; verdicts are logged locally. Jev measurements come from the authors' own sessions and synthetic projects. Main-model costs depend on your provider or subscription.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 7335d774c998](https://github.com/qybaihe/mu/tree/7335d774c998bb5d935ba14581a8f4be1a5f311e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
