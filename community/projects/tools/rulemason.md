# rulemason (shared rules and checkpoints for AI coding tools, with an optional Jev judge that checks plans against your written rules; Chinese)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shared rules and checkpoints for Claude Code, OpenCode, Cursor and Codex: one place keeps the coding rules, each project gets read-only copies, and checkpoints run after a plan, before code and after code. The optional judge uses Jev to decide whether a plan breaks a rule you wrote, returning pass, review or block. Documentation is in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rulemason/rulemason) |
| Maintainer | [rulemason](https://github.com/rulemason). Independently curated. |
| Format | Python CLI (PyPI package `rulemason`) with skills and lint configs |
| Requirements | uv; optionally `TYPESAFE_API_KEY` for the Jev judge (`rulemason key`); OpenSpec for the full flow. |
| License | [Apache-2.0](https://github.com/rulemason/rulemason/blob/16ee77d7288ba0bb86a3dba736f4aedf7ac3e449/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/rulemason/judge/judge.py`](https://github.com/rulemason/rulemason/blob/16ee77d7288ba0bb86a3dba736f4aedf7ac3e449/src/rulemason/judge/judge.py) at the pinned commit. |

## When to use

- Keep AI coding tools to the same written rules across projects and gate plans before code is written.
- Mismatch: the docs are in Chinese; Jev only judges plans against rules, and without a key a person answers the questions.

## How it works

`src/rulemason/judge/judge.py` picks `jev` or `manual` as the judge, builds typed `Noul` and `Score` questions with `typesafe_sdk` and reuses one connection per run, with the model pinned to `jev-1.14.0`; it errors rather than silently degrading when `JUDGE_PROVIDER=jev` has no key. Integration evidence: [`src/rulemason/judge/judge.py`](https://github.com/rulemason/rulemason/blob/16ee77d7288ba0bb86a3dba736f4aedf7ac3e449/src/rulemason/judge/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install rulemason
rulemason --version
rulemason init   # in your project root
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese) with commands and the daily flow: [github.com/rulemason/rulemason#readme](https://github.com/rulemason/rulemason#readme)

## Limits and data handling

With the Jev judge on, plan text and the rules go to TypeSafe on your key, which is stored in `~/.config/rulemason/env` with mode 600. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 16ee77d7288b](https://github.com/rulemason/rulemason/tree/16ee77d7288ba0bb86a3dba736f4aedf7ac3e449). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
