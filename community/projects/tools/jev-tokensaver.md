# jev-tokensaver

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code and Cowork pre-reader: a local `jev` CLI, MCP server and skill that let TypeSafe Jev read long test logs, big files and candidate-file lists (`prune`, `find`, `rank`, `map`) and pass Claude only the relevant lines — lossless, fail-open, secrets scrubbed locally.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Dinesh-Sunny/jev-tokensaver) |
| Maintainer | [Dinesh-Sunny](https://github.com/Dinesh-Sunny). Independently curated. |
| Format | CLI + MCP server + Claude Code skill/hook (installer; `jev` 0.4.0 at review) |
| Requirements | macOS or Linux with uv (installer can install it); Claude Code and/or Claude Desktop (Cowork); a TypeSafe API key. |
| License | [MIT](https://github.com/Dinesh-Sunny/jev-tokensaver/blob/df4e7e01e9ae457e3237c6a27c98eb6379b7dfcb/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Pipe `npm test` output through `jev prune "which tests failed and why"` instead of loading thousands of lines.
- Find the relevant spots in a large file or rank candidate files before Claude opens them.
- Mismatch: no saving on small files or text Claude has already read (upstream FAQ).

## How it works

[`jev.py`](https://github.com/Dinesh-Sunny/jev-tokensaver/blob/df4e7e01e9ae457e3237c6a27c98eb6379b7dfcb/jev.py) applies deterministic filtering first (error lines, head/tail, skipping ignored and secret files), scrubs keys/tokens, then asks Jev typed questions and returns only relevant lines plus a verdict. Claude Code calls the CLI; Cowork uses `jev serve` (MCP); the [skill](https://github.com/Dinesh-Sunny/jev-tokensaver/blob/df4e7e01e9ae457e3237c6a27c98eb6379b7dfcb/skills/jev/SKILL.md) sets usage rules. Any failure prints `FALLBACK:` and Claude reads normally.

## Get started

Run the guided installer (review the script first):

```sh
curl -fsSL https://raw.githubusercontent.com/Dinesh-Sunny/jev-tokensaver/main/install.sh | bash
# then, for example:
npm test 2>&1 | jev prune "which tests failed and why"
```

Jev requests are billed by TypeSafe; default daily cap $0.20 (`JEV_DAILY_BUDGET_USD`).

## Examples and demos

- README *What it does* table (prune / find / rank / map) and *Is it accurate?* section (maintainer-reported).
- [docs/how-it-works.md](https://github.com/Dinesh-Sunny/jev-tokensaver/blob/df4e7e01e9ae457e3237c6a27c98eb6379b7dfcb/docs/how-it-works.md) and [SECURITY.md](https://github.com/Dinesh-Sunny/jev-tokensaver/blob/df4e7e01e9ae457e3237c6a27c98eb6379b7dfcb/SECURITY.md).

## Limits and data handling

Scrubbed excerpts and your question go to TypeSafe; `.jevoff` files and `jev off` exclude folders. Not affiliated with TypeSafe or Anthropic. Accuracy claims are upstream. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit df4e7e01e9ae](https://github.com/Dinesh-Sunny/jev-tokensaver/tree/df4e7e01e9ae457e3237c6a27c98eb6379b7dfcb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
