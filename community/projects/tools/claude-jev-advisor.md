# claude-jev-advisor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial Claude Code command hooks using TypeSafe Jev: a `context` helper that suggests `/compact` or `/clear` at natural stopping points, and (on Windows) an `rm` helper that asks before real files are deleted but lets Jev clear deletes of session-made or git-ignored files; README lists exactly what is sent to Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/delt96/claude-jev-advisor) |
| Maintainer | [delt96](https://github.com/delt96). Independently curated. |
| Format | npm CLI (`@delt/claude-jev-advisor`, 0.4.1 at review) that registers command hooks in `~/.claude/settings.json` |
| Requirements | Node.js 18+, Claude Code (bottom-row display uses early-access Claude Code mods), a `TYPESAFE_API_KEY`; the `rm` helper needs Windows PowerShell or PowerShell 7. |
| License | [MIT](https://github.com/delt96/claude-jev-advisor/blob/dddcbe2afa0c4adc184467fbd788c458be65e0d5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- See a hint to compact or clear when a long conversation reaches a stopping point.
- Have deletes of real files confirmed while temp, session-made or git-ignored targets pass.
- Mismatch: the `rm` helper is Windows-only; without a key it asks about every real file.

## How it works

[`src/context/judge.ts`](https://github.com/delt96/claude-jev-advisor/blob/dddcbe2afa0c4adc184467fbd788c458be65e0d5/src/context/judge.ts) sends the last three requests and Claude's last reply (truncated) to Jev at turn end; [`src/rm/judge.ts`](https://github.com/delt96/claude-jev-advisor/blob/dddcbe2afa0c4adc184467fbd788c458be65e0d5/src/rm/judge.ts) is consulted only for deletes it would otherwise ask about; [`src/jev.ts`](https://github.com/delt96/claude-jev-advisor/blob/dddcbe2afa0c4adc184467fbd788c458be65e0d5/src/jev.ts) is the API client. `install` backs up `settings.json` before changing it.

## Get started

Install and register the hooks:

```sh
npm i -g @delt/claude-jev-advisor
claude-jev-advisor install     # prompts for and verifies your TypeSafe key
```

The context helper makes one Jev call per turn; the rm helper calls Jev only for qualifying deletes. Billed to your TypeSafe key.

## Examples and demos

- README *Commands*, *The context helper*, *The rm helper* and *When Jev can lift the ask*.

## Limits and data handling

Truncated conversation excerpts and delete details go to TypeSafe as listed in the README. Not affiliated with Anthropic or TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit dddcbe2afa0c](https://github.com/delt96/claude-jev-advisor/tree/dddcbe2afa0c4adc184467fbd788c458be65e0d5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
