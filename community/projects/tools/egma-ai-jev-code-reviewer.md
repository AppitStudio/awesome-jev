# Jev Code Reviewer (egma-ai)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local PR review stack: TypeSafe Jev prioritizes change units (P0/P1/P2); OpenAI explains diffs in natural language; Chrome extension overlays GitHub Files changed—posts nothing to GitHub.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/egma-ai/jev-code-reviewer) |
| Maintainer | [egma-ai](https://github.com/egma-ai). Independently curated. |
| Format | Node CLI (`jev-reviewer`) + local server + Chrome extension + optional agent skill. |
| Requirements | Node.js 22+; GitHub CLI; TypeSafe + OpenAI keys; Chrome for the extension. Optional `graphifyy` for code graphs. |
| License | [MIT](https://github.com/egma-ai/jev-code-reviewer/blob/d1966f537a09efacd96408b364c885f9ae424282/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use when agent PRs are huge and you want **attention triage plus NL explanations** without uploading reviews to GitHub.

## How it works

`analyze` sends change units to Jev for priority and OpenAI for explanations; the extension talks only to `127.0.0.1:4731`. Coverage capped (default 12 units).

## Get started

```sh
git clone https://github.com/egma-ai/jev-code-reviewer.git
cd jev-code-reviewer
git checkout d1966f537a09efacd96408b364c885f9ae424282
npm install
npm run demo   # offline replay at http://127.0.0.1:4731/demo
```

## Examples and demos

- Bundled demo recording and demonstration PR linked from README.
- `jev-reviewer doctor` / `serve` / `analyze --pr …`.

## Limits and data handling

Changed code leaves the machine to TypeSafe and OpenAI. Keys stored in `~/.config/jev-reviewer/credentials.json` (owner-only, not encrypted). New GitHub `/changes` UI unsupported.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit d1966f5](https://github.com/egma-ai/jev-code-reviewer/tree/d1966f537a09efacd96408b364c885f9ae424282). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [Clean Code Review](../apps/clean-code-review.md), [jev-pr-profiler](jev-pr-profiler.md).
