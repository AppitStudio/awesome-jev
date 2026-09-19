# Supercov

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/supercorp-ai/supercov) |
| Maintainer | [Supercorp](https://github.com/supercorp-ai). Self-submission by the maintainer. Supercov is free and open source; Jev inference is billed by TypeSafe to the user's own key. |
| Format | Rust CLI, installed through `npx supercov`, `brew install supercorp-ai/tap/supercov`, `go run github.com/supercorp-ai/supercov/cmd/supercov@latest`, or crates.io. |
| Requirements | Node.js 22+ for the npm path. `TYPESAFE_API_KEY` for `quality`; coverage needs no account, config file, or custom reporter. Coverage supports JavaScript/TypeScript (Vitest including Browser Mode, Jest), Python, Ruby, Rust, Go, Java and Kotlin. |
| Jev's role | `quality` sends each source file with twelve Noul questions (god class, long method, deep nesting, complex conditional, long parameter list, duplicated logic, primitive obsession, dead code, feature envy, temporary field, message chains, magic values) to `jev-1.13.0`. `quality patch` asks them differentially and adds six change-only checks. Source-root detection asks Jev about paths no manifest explains. All scoring arithmetic is done by the CLI. |
| License | [MIT](https://github.com/supercorp-ai/supercov/blob/55f5ce93a239829c224b89e6749991310be91ea4/LICENSE). |
| Access and costs | Jev charges for input only, so the maintainer reports about one cent per megabyte of source; the CLI prints its estimate before sending anything and caches answers by content under `.supercov/quality/requests/`. |

## When to use

- Point a coding agent at a repository and have it pick the weakest file to refactor, with the properties that fired as the reason.
- Review a change in CI with `quality patch --annotate github`, which reports only files where something new appeared.
- Find untested lines and branches after a normal test run, and hand the agent small, targeted queries instead of a percentage.

It grades files, not people, and it is not a merge gate: the documentation positions the score as a way to find the code that is hardest to change, not as a pass or fail check.

## How it works

`quality` discovers source roots from package manifests, excludes tests, generated output and tool scripts (each with a stated reason), and sends one request per file with the file's text as state and twelve independent yes/no questions. Each question has a definition and a stated exception so two readers would agree. The CLI computes health as the mean of the twelve answers, weights larger files more when summarising a directory, and ranks files as good, fair or weak. Snapshots are saved locally and can be read and diffed without a key.

`quality patch` compares the old and new version of each changed file, asking whether the new version shows a property the old one did not, plus six checks that only make sense for a change: a credential written into source, untrusted input in a query, a change to authorisation, a test that checks less, a schema or data migration, and debugging left behind.

Coverage is separate and needs no model. `supercov -- <your test command>` runs the suite unchanged, records line, branch and MC/DC evidence, and answers questions such as which tests reach a file or which branches nothing exercises. See [Understanding quality](https://github.com/supercorp-ai/supercov/blob/55f5ce93a239829c224b89e6749991310be91ea4/docs/quality.md) and the [coverage model](https://github.com/supercorp-ai/supercov/blob/55f5ce93a239829c224b89e6749991310be91ea4/docs/coverage-model.md).

## Get started

Coverage first, because it needs no key. In any project with a test command:

```sh
npx supercov -- npm test
npx supercov runs latest
```

Quality, with a TypeSafe key. The environment variable is the only way to pass it; a key on the command line would land in shell history.

```sh
export TYPESAFE_API_KEY=...
npx supercov quality --dry-run   # prints every request, sends nothing
npx supercov quality             # live: sends source files to TypeSafe
npx supercov quality gaps        # only files something fired on
npx supercov quality patch       # what your uncommitted work introduced
```

`quality scope` lists which files would be sent and why the others were excluded, so check it before the first live run on proprietary code. Full options are in the [CLI reference](https://supercov.com/docs/cli).

## Examples and demos

- [Agent workflow](https://supercov.com/docs/agent-loop) walks through asking a coding agent to add a test, with a recorded session.
- [React verification example](https://github.com/supercorp-ai/supercov/tree/55f5ce93a239829c224b89e6749991310be91ea4/examples/react-verification) is a small Vitest project with a weak and a strong test for the same component; it is what this review ran.
- The README shows the `quality` summary and weakest-files output for a real repository.

## Limits and data handling

`quality` sends the full text of every in-scope source file to TypeSafe under your key; nothing is redacted. Check `quality scope` first and use `SUPERCOV_SOURCE_ROOTS` or a directory argument to narrow it. Cached requests and answers stay in `.supercov/` in the repository, so treat that directory as containing your source. Coverage never contacts a network.

The twelve properties are Fowler and Beck smells and CodeScene-style class smells; they say nothing about correctness, and the health number is the CLI's mean, not a model judgment. Scores are cached by file content, so a rename costs nothing but a one-character edit re-asks all twelve questions for that file.

## Review and maintenance

Reviewed on **2026-09-19** at commit [`55f5ce9`](https://github.com/supercorp-ai/supercov/commit/55f5ce93a239829c224b89e6749991310be91ea4), by the maintainer with AI assistance. Ran the published `supercov 1.0.1` through `npx` on the repository's `examples/react-verification` project: `quality scope` reported one included file and seven excluded with reasons; `quality --dry-run` without a key printed one request containing twelve `noul` questions for `jev-1.13.0` and sent nothing; `supercov -- npx vitest run` passed seven tests and `runs latest` reported line, branch and MC/DC coverage. No live Jev call was made during this review; the cost figures above are the maintainer's published measurements, not independent ones.

Related: [quality rubric](../../../examples/quality-rubric/README.md) for combining independent judgments in code.
