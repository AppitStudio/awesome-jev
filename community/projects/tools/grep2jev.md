# grep2jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that lets a coding agent hand file triage to Jev: pipe in candidate files, Jev scores each against the request in parallel (Python sent as AST skeletons), and the agent reads only files that pass.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mars7100/grep2jev) |
| Maintainer | [mars7100](https://github.com/mars7100). Independently curated. |
| Format | Node.js CLI (no dependencies) |
| Requirements | Node 24+; a TypeSafe key in the shell, `.env` or `~/.jev_key`. |
| License | [MIT](https://github.com/mars7100/grep2jev/blob/1406eecedd22bc87aecd2ab84839d7c6839a17ff/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`grep2jev.ts`](https://github.com/mars7100/grep2jev/blob/1406eecedd22bc87aecd2ab84839d7c6839a17ff/grep2jev.ts) at the pinned commit. |

## When to use

- Cut agent context by letting Jev pick relevant files from a grep hit list.
- Ask bug, change or owner questions per file.
- Mismatch: client core is copied from ten-levels-of-jev; this repo adds the triage CLI.

## How it works

`grep2jev.ts` expands files, directories and globs, sends each file (or its Python AST skeleton) with one Noul question chosen by `--task`, and prints files above `--threshold`. `core/` and `lib/` are copied from disler/ten-levels-of-jev under MIT. Integration evidence: [`grep2jev.ts`](https://github.com/mars7100/grep2jev/blob/1406eecedd22bc87aecd2ab84839d7c6839a17ff/grep2jev.ts).

## Get started

From the upstream README: set a key, then pipe `rg -l` output into the CLI.

```sh
rg -l proration | node grep2jev.ts "the proration test fails because of rounding"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README task modes (bug, change, owner)

## Limits and data handling

File contents go to TypeSafe. Scores can miss callers; check results before skipping files.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 1406eecedd22](https://github.com/mars7100/grep2jev/tree/1406eecedd22bc87aecd2ab84839d7c6839a17ff). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
