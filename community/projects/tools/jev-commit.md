# Jev Commit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A pre-commit hook where one Jev call checks whether the commit message actually matches the staged diff.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev-commit) |
| Maintainer | [valentynkit](https://github.com/valentynkit). Self-submitted by the maintainer in [PR #7](https://github.com/AppitStudio/awesome-jev/pull/7), with no commercial relationship beyond authorship disclosed. |
| Format | Python CLI, usable as a [pre-commit](https://pre-commit.com/) `commit-msg` hook or a plain git hook. |
| Requirements | Python 3.10+ (packaged via `pipx`/`pyproject.toml`); a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/valentynkit/jev-commit/blob/311e163b8abb9c333132155bc2e0bbfac4f36283/LICENSE). |

**Review blocker:** at the reviewed upstream revision, the hook still calls Jev after a blocking credential match and may upload the detected credential before refusing the commit. Do not enable live inference for sensitive repositories at this revision. An offline-tested maintainer patch is prepared, but has not landed upstream; this listing is pending that fix.

## When to use

Use it when commits (especially agent-written ones) claim more or less than the diff shows: filler messages, a message that names one change while the diff also carries an unrelated one, debug leftovers (`print`, commented-out code, a hardcoded localhost, a skipped test), or unmentioned files. It also runs a credential check on every added line, which is the one finding it blocks on by default; everything else warns and lets the commit through.

If your repository never has agents or unfamiliar contributors writing commit messages, a simpler commit-message linter may be enough; this is aimed specifically at the message-versus-diff mismatch that a template or regex cannot catch.

## How it works

The staged diff is read with two `git` calls run under a locked-down environment (no hooks path, no textconv, no external diff, no inherited `GIT_*`, no API key in the child process). An amend against a clean index is compared to `HEAD^` and never blocks. Added lines pass through a credential belt (thirteen high-precision patterns that block, two high-recall checks that only report). In this revision the scan does not prevent a model upload; the blocking verdict is applied afterward. Hunks are packed into one or more Jev requests under a 24k-token budget, with lockfiles, generated directories, and binaries collapsed to a row of counts. Each request asks five Nouls (filler message, contradicts the diff, debug leftovers, unmentioned work, secret-shaped) pinned to `jev-1.13.0`; findings across chunks combine by taking the worst answer. API failures and missing keys do not block by themselves, but the local credential check still blocks ordinary commits without a successful response. Clean-index amends remain allowed. Unexpected exceptions and Ctrl-C are caught by the entry point and return 0.

## Get started

Start with offline source review and tests; live hook installation is pending the upload fix:

```sh
git clone https://github.com/valentynkit/jev-commit
cd jev-commit
git checkout 311e163b8abb9c333132155bc2e0bbfac4f36283
make test
```

`make test` uses `uv` to obtain pytest, then runs tests against a local fake without a TypeSafe key. Dependency installation can contact the package registry.

For eventual pre-commit installation, the configuration filename is `.pre-commit-config.yaml` and the installation command is `pre-commit install --hook-type commit-msg`. The submitted `v0.1.0` tag does not exist; use a real reviewed commit containing the upload fix once available. The current SHA above is suitable for reproducing the review, not a fixed release.

The installed hook reads its process environment and does not load `.env`. After the fix lands, export `TYPESAFE_API_KEY` before launching Git or a Git GUI that inherits that environment. This works without a source checkout in the active directory. Live calls send selected diff content and the message to the configured endpoint and may incur charges.

`--strict` blocks on findings past its thresholds. `--exclude` and `# jev-commit: allow` bypass parts of the credential scan; they are not redaction controls.

## Examples and demos

The [demo guide](https://github.com/valentynkit/jev-commit/blob/311e163b8abb9c333132155bc2e0bbfac4f36283/demo/README.md) shows a message/diff mismatch and a staged private-key-shaped fixture. Probabilities, latency and costs in the clip are simulated or placeholders from its local fake. `make measure` replays recorded answers; detection-rate results are not established by running the mock suite.

## Limits and data handling

The packed diff and commit message go to TypeSafe by default, or another recipient through `JEV_BASE_URL`. At the reviewed revision, blocking scanner matches do not stop that upload. The local scanner is not comprehensive secret detection: it examines added lines and permits exclusions and placeholder heuristics.

Cost estimates are arithmetic over the author’s corpus and assumed token prices, not billed measurements. The default model findings are advisory; `--strict` changes the blocking policy.

## Review and maintenance

Reviewed 2026-09-22 against upstream commit [`311e163`](https://github.com/valentynkit/jev-commit/commit/311e163b8abb9c333132155bc2e0bbfac4f36283). Maintainer-side inspection covered source, license, installation and demo instructions. Four new regression cases reproduced a request after a blocking match on the unchanged source. A local patch skips inference on blocking scanner matches while preserving allowed amends; its full offline suite passed 105 tests with 1 skipped. That patch is not part of the linked upstream commit and does not make the upstream release fixed. No live provider calls were made. AI assistance was used for the submission, review and patch.
