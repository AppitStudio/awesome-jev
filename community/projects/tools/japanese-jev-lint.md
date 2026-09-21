# japanese-jev-lint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI/library (`jjl`) that lints Japanese prose with TypeSafe Jev: per-sentence Noul probabilities for typos, subject–predicate twist, long sentences, and repeated phrases—plus regex rules for です/ます mixing—without generating rewrite suggestions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pankona/japanese-jev-lint) |
| Maintainer | [pankona](https://github.com/pankona). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go module **github.com/pankona/japanese-jev-lint** with CLI `jjl` (`go install .../cmd/jjl@latest`). |
| Requirements | Go **1.25+** (per `go.mod`); live Jev checks need `TYPESAFE_API_KEY`. `-dry-run` lists sentences that would be sent. |
| License | [MIT](https://github.com/pankona/japanese-jev-lint/blob/a2372ac92a7c0e3ffae8253b0e96be58bc46ee07/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `go test ./...`: **ok** (all packages). Live TypeSafe calls were not run. Distinct from [jev-lint](jev-lint.md) / [JevLint](jevlint.md) (English/code semantic lint). |

## When to use

Use it as a **pre-review pass** on Japanese Markdown/posts when you want calibrated “looks suspicious” flags for humans or reviewdog—not auto-rewrites. Prefer English/code linters ([jev-lint](jev-lint.md), [JevLint](jevlint.md)) for those languages.

## How it works

[`jev.go`](https://github.com/pankona/japanese-jev-lint/blob/a2372ac92a7c0e3ffae8253b0e96be58bc46ee07/jev.go) posts sentence `state` and typed questions to `https://api.typesafe.ai/v1/systemone`. The linter thresholds Jev probabilities and emits diagnostics in `text`, `rdjsonl`, `textlint`, or `json` formats. Without a key, only local regex checks run. Upstream warns that **manuscript text is sent to api.typesafe.ai**.

## Get started

```sh
go install github.com/pankona/japanese-jev-lint/cmd/jjl@latest
export TYPESAFE_API_KEY=...   # do not paste secrets into chat
jjl -dry-run content/posts/*/index.md
jjl content/posts/*/index.md
```

From the reviewed tip:

```sh
git clone https://github.com/pankona/japanese-jev-lint.git
cd japanese-jev-lint
git checkout a2372ac92a7c0e3ffae8253b0e96be58bc46ee07
go test ./...
```

Live linting sends sentence text to TypeSafe and can incur charges.

## Examples and demos

- Upstream README shows reviewdog / textlint-shaped output.
- This listing: `go test ./...` → all packages **ok**. No live TypeSafe call.

## Limits and data handling

Full sentence text leaves the host on live Jev checks—use only on content you are allowed to send. The tool does not invent corrections. Exit codes: 0 none, 1 findings (unless `-fail-on none`), 2 errors. Confirm TypeSafe billing separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit a2372ac](https://github.com/pankona/japanese-jev-lint/tree/a2372ac92a7c0e3ffae8253b0e96be58bc46ee07): MIT. AI-assisted source review of README, LICENSE, `jev.go`, linter packages, and offline `go test ./...`. No live provider calls.

Related: [jev-lint](jev-lint.md), [JevLint](jevlint.md), [patdown](patdown.md).
