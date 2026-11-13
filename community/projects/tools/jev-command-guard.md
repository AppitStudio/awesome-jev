# jev-command-guard (Claude Code PreToolUse hook where Jev rates each shell command's risk before it runs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hook that sends every Bash or PowerShell command to Jev before it runs, asks six typed questions (category, 0–3 risk score, deletes data, sends data out, touches secrets, runs remote code) and stops for your confirmation when the command looks dangerous; it only adds friction, never auto-approves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/renrai/jev-pre-tool-use) |
| Maintainer | [renrai](https://github.com/renrai). Independently curated. |
| Format | Claude Code PreToolUse hook (TypeScript on Node.js 22.18+, MIT) |
| Requirements | Node.js 22.18+, Claude Code and a TypeSafe key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/renrai/jev-pre-tool-use/blob/7be91a9b198defcfe2f45c34ba3f286a0074aad1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classify.ts`](https://github.com/renrai/jev-pre-tool-use/blob/7be91a9b198defcfe2f45c34ba3f286a0074aad1/src/classify.ts) at the pinned commit. |

## When to use

- Get a confirmation prompt before an agent runs destructive or data-leaking commands.
- Mismatch: a security boundary; it is a learning project and only adds prompts.

## How it works

`src/classify.ts` uses the official `@typesafe-ai/sdk` client with the questions in `src/questions.ts` (`choice`, `score` and four `noul` flags) and the reported model `jev-1.14.0`; `src/policy.ts` turns the answers into ask-or-allow. One call takes about 100 ms per the author. Integration evidence: [`src/classify.ts`](https://github.com/renrai/jev-pre-tool-use/blob/7be91a9b198defcfe2f45c34ba3f286a0074aad1/src/classify.ts).

## Get started

Install, add your key to `.env`, try a command by hand, then enable the hook in Claude Code as the README shows.

```sh
npm install
cp .env.example .env   # add TYPESAFE_API_KEY
npm run try -- "git push --force origin main"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/renrai/jev-pre-tool-use/blob/7be91a9b198defcfe2f45c34ba3f286a0074aad1/README.md](https://github.com/renrai/jev-pre-tool-use/blob/7be91a9b198defcfe2f45c34ba3f286a0074aad1/README.md)

## Limits and data handling

Each shell command Claude Code wants to run goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 7be91a9b198d](https://github.com/renrai/jev-pre-tool-use/tree/7be91a9b198defcfe2f45c34ba3f286a0074aad1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
