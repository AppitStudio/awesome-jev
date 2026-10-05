# Code Quality (smixs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Advisory code-quality report and red-flag hooks for Claude Code, Codex, pi, omp, OpenCode and Grok, with an optional TypeSafe Jev classifier that asks calibrated yes/no questions about added test and source hunks (never blocks).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smixs/code-quality) |
| Maintainer | [smixs](https://github.com/smixs). Independently curated. |
| Format | Agent plugin / skill with Stop, UserPromptSubmit and PreToolUse hooks and a `.quality.toml` per repository |
| Requirements | Bun. Jev is optional: `TYPESAFE_API_KEY` (direct, pinned `jev-1.13.0`) or `OPENROUTER_API_KEY` (`typesafe/jev-1.13-20260917`), or a custom endpoint. |
| License | [MIT](https://github.com/smixs/code-quality/blob/0e160eadf7d1bfffb75a14bed88876d6f7bffbc7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Catch the "cheap way out" in agent changes — deleted or weakened tests, refreshed baselines, `--no-verify` — and report it to the agent on its next turn.
- Add a calibrated second opinion on test hunks that static rules miss (for example a test that only checks a file's text).
- Mismatch: this is advice, not a gate; if you need a hard CI block, wire your own CI rules — Jev answers are notes only.

## How it works

After the deterministic checks, `check`, `pre-commit` and the Stop adapter send each added test hunk (file name, added code) with fixed questions such as `textual_test` to Jev and compare the `noul` probability with a per-question threshold tuned on Jev 1.13 (hence the pinned model). Further packs cover untested changes, UX, agent and project questions. Provider `auto` picks TypeSafe, then OpenRouter, else prints `jev: not available` and asks nothing; errors are one line and never a verdict ([Jev reference](https://github.com/smixs/code-quality/blob/0e160eadf7d1bfffb75a14bed88876d6f7bffbc7/skills/code-quality/references/jev.md)).

## Get started

Install the plugin for your agent, wire a repository, and enable Jev in `.quality.toml` (live calls on each check):

```sh
claude plugin marketplace add smixs/code-quality
claude plugin install code-quality@code-quality
bun scripts/quality.ts install-hooks <repo>   # from the plugin root
# <repo>/.quality.toml:
# [review]
# jev = true            # TYPESAFE_API_KEY in the environment
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Jev reference](https://github.com/smixs/code-quality/blob/0e160eadf7d1bfffb75a14bed88876d6f7bffbc7/skills/code-quality/references/jev.md): providers, model pins, every question with its state shape and threshold, and curl examples for TypeSafe and OpenRouter.
- Install table in the README for Claude Code, Codex, Grok, pi, omp and OpenCode.

## Limits and data handling

With Jev on, added code hunks are sent to TypeSafe or OpenRouter. Thresholds were tuned by the maintainer on Jev 1.13; changing the model alias can shift them. Formerly published as `smixs/code-quality-skill` (GitHub redirects). Plugin hooks and Jev answers were not executed on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 0e160eadf7d1](https://github.com/smixs/code-quality/tree/0e160eadf7d1bfffb75a14bed88876d6f7bffbc7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
