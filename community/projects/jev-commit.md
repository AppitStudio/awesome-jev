# Jev Commit

[All projects](../README.md) · [Developer tools](../README.md#developer-tools)

A pre-commit hook where one Jev call checks whether the commit message actually matches the staged diff.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev-commit) |
| Maintainer | [valentynkit](https://github.com/valentynkit). I am the maintainer, submitting my own project; no commercial relationship beyond authorship. |
| Format | Python CLI, usable as a [pre-commit](https://pre-commit.com/) `commit-msg` hook or a plain git hook. |
| Requirements | Python (packaged via `pipx`/`pyproject.toml`); a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/valentynkit/jev-commit/blob/311e163b8abb9c333132155bc2e0bbfac4f36283/LICENSE). |

## When to use

Use it when commits (especially agent-written ones) claim more or less than the diff shows: filler messages, a message that names one change while the diff also carries an unrelated one, debug leftovers (`print`, commented-out code, a hardcoded localhost, a skipped test), or unmentioned files. It also runs a credential check on every added line, which is the one finding it blocks on by default; everything else warns and lets the commit through.

If your repository never has agents or unfamiliar contributors writing commit messages, a simpler commit-message linter may be enough; this is aimed specifically at the message-versus-diff mismatch that a template or regex cannot catch.

## How it works

The staged diff is read with two `git` calls run under a locked-down environment (no hooks path, no textconv, no external diff, no inherited `GIT_*`, no API key in the child process). An amend against a clean index is compared to `HEAD^` and never blocks. Added lines pass through a credential belt (thirteen high-precision patterns that block, two high-recall ones that only report) before anything reaches the model. Hunks are packed into one or more Jev requests under a 24k-token budget, with lockfiles, generated directories, and binaries collapsed to a row of counts. Each request asks five Nouls (filler message, contradicts the diff, debug leftovers, unmentioned work, secret-shaped) pinned to `jev-1.13.0`; findings across chunks combine by taking the worst answer. Every error path (timeout past 8 seconds, API error, missing key, Ctrl-C) exits 0 and lets the commit through.

## Get started

```sh
pipx install git+https://github.com/valentynkit/jev-commit
```

As a pre-commit hook:

```yaml
repos:
  - repo: https://github.com/valentynkit/jev-commit
    rev: v0.1.0
    hooks:
      - id: jev-commit
```

```sh
pre-commit install --hook-type commit-msg
```

or as a plain git hook pointed at `jev-commit "$1"`. Then `cp .env.example .env` and set `TYPESAFE_API_KEY`. `jev-commit --strict .git/COMMIT_EDITMSG` blocks on any finding past threshold rather than only a credential; a line ending `# jev-commit: allow` is skipped by the credential belt.

## Examples and demos

The repository's [README](https://github.com/valentynkit/jev-commit/blob/311e163b8abb9c333132155bc2e0bbfac4f36283/README.md) and `demo.gif`/`demo.mp4` show a commit whose message claims a null check while the diff also adds an endpoint and a debug print, then a second commit blocked for staging a private key. I have not re-run these against a live key as part of this submission; the repository's own `make measure` target is what regenerates detection-rate numbers against recorded answers, and the README says that figure is not published yet.

## Limits and data handling

The staged diff (packed and truncated as described above) and the commit message go to TypeSafe's Jev endpoint under your own key on every commit that reaches a check. The author reports (self-reported, not independently reproduced) a median cost of $0.000044 per commit and about four cents per thousand commits, and a median 1,048 input tokens over a 152-case corpus. Everything except the credential check is advisory; a warning does not block the commit.

## Review and maintenance

Reviewed 2026-09-19 against commit [`311e163`](https://github.com/valentynkit/jev-commit/commit/311e163b8abb9c333132155bc2e0bbfac4f36283). This page was prepared with AI assistance from the project's own README, CHANGELOG, and source layout; I did not run a live TypeSafe key against it as part of this submission, and the cost/token figures above are the author's self-reported numbers over their own corpus, not independently re-measured here.
