# CommandMate (phone-run AI coding team with a Jev issue-triage script)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local app for running Claude Code, Codex, Gemini CLI and other coding agents from your phone in Git worktree sessions; its orchestration includes a script that asks Jev to draft issue priority and which model should take each issue.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kewton/CommandMate) |
| Maintainer | [Kewton](https://github.com/Kewton). Independently curated. |
| Format | npm CLI and local web app (TypeScript, MIT) |
| Requirements | Node.js, the coding-agent CLIs you use, and `JEV_API_KEY` for the triage script. |
| License | [MIT](https://github.com/Kewton/CommandMate/blob/46c49efc2fd4a79b0153e25ba75e662c55a30866/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/orchestrate/jev-triage.mjs`](https://github.com/Kewton/CommandMate/blob/46c49efc2fd4a79b0153e25ba75e662c55a30866/scripts/orchestrate/jev-triage.mjs) at the pinned commit. |

## When to use

- Draft issue priority and agent assignment with typed answers.
- Run several coding agents from a phone.
- Mismatch: Jev is used in one maintainer triage script, not in the main app; the triage doc is in Japanese.

## How it works

`scripts/orchestrate/jev-triage.mjs` sends each issue's title, labels and body to `/v1/systemone` with four questions (model, impact, ready, urgent); `docs/jev-triage.md` says the result is a draft, not a ruling, and Jev only sees the issue body. Integration evidence: [`scripts/orchestrate/jev-triage.mjs`](https://github.com/Kewton/CommandMate/blob/46c49efc2fd4a79b0153e25ba75e662c55a30866/scripts/orchestrate/jev-triage.mjs).

## Get started

Install CommandMate, then run the triage script from a checkout with `JEV_API_KEY` in `.env` (see `docs/jev-triage.md`, Japanese).

```sh
npm install -g commandmate
node scripts/orchestrate/jev-triage.mjs --out jev-out.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Kewton/CommandMate/blob/46c49efc2fd4a79b0153e25ba75e662c55a30866/README.md](https://github.com/Kewton/CommandMate/blob/46c49efc2fd4a79b0153e25ba75e662c55a30866/README.md)

## Limits and data handling

Only public issue text is sent to TypeSafe per the doc; the coding agents use their own providers.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 46c49efc2fd4](https://github.com/Kewton/CommandMate/tree/46c49efc2fd4a79b0153e25ba75e662c55a30866). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
