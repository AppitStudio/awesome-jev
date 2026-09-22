# jevyoumean

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic “Did you mean?” CLI wrapper (`jym`): when a subcommand is unknown, TypeSafe Jev picks among documented options by intent (from help text), not edit distance.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/syumai/jevyoumean) |
| Maintainer | [syumai](https://github.com/syumai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go module **`github.com/syumai/jevyoumean`** (CLI bins `jym`, plus eval/help helpers). |
| Requirements | Go toolchain to install; `TYPESAFE_API_KEY` for live suggestions. |
| License | [MIT](https://github.com/syumai/jevyoumean/blob/93172f463aa1b6f4a4ddafbdd020a89cb901ab3d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `go test` inspected; live TypeSafe suggestions not run on the review host. Upstream marks the project experimental. |

## When to use

Use it when you want **intent-aware CLI typo correction** (for example `git remove` → `git rm`) via Jev Choice over help-derived criteria. Prefer plain shell aliases when you already know the exact command. Do not treat suggestions as guaranteed correct.

## How it works

`jym` resolves the wrapped binary, captures help text, and posts Choice questions to `https://api.typesafe.ai/v1/systemone`. Code validates answers against criteria (including a `__none__` escape hatch), then prompts to run the suggestion, keep the typed command, or cancel. Shell/mise integration helpers avoid recursive wrapping.

## Get started

```sh
git clone https://github.com/syumai/jevyoumean.git
cd jevyoumean
git checkout 93172f463aa1b6f4a4ddafbdd020a89cb901ab3d
go test ./...
go install ./cmd/jym@93172f463aa1b6f4a4ddafbdd020a89cb901ab3d
# Live: export TYPESAFE_API_KEY=... then: jym -- git remove foo.txt
```

Live suggestions send help-derived command names/descriptions to TypeSafe and may incur charges. This listing did not call TypeSafe.

## Examples and demos

- Offline on the review host: `go test ./...` → **7 packages ok** (including mocked `internal/jev` System One client tests).
- Upstream README demo GIF and mise/`--shell-integration` snippets.

## Limits and data handling

Help text and typed tokens for unknown subcommands leave the host on live suggestions. Suggestions can be wrong; the interface may change. Failures should leave an explicit cancel/run-as-typed path—inspect upstream for exact UX.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 93172f4](https://github.com/syumai/jevyoumean/tree/93172f463aa1b6f4a4ddafbdd020a89cb901ab3d): MIT. AI-assisted source review of README, LICENSE, `internal/jev/`. Offline Go tests 7 packages ok. No live TypeSafe on the review host.

Related: [jev-shell-history](jev-shell-history.md), [jsort](jsort.md).
