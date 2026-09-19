# jev.nvim

[All projects](../README.md) · [Developer tools](../README.md#developer-tools)

Ask a Neovim buffer a plain-language question and get back a quickfix list ranked by Jev's per-function probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev.nvim) |
| Maintainer | [valentynkit](https://github.com/valentynkit). I am the maintainer, submitting my own project; no commercial relationship beyond authorship. |
| Format | Neovim plugin (Lua). |
| Requirements | Neovim 0.10+, `curl`, and a Treesitter parser for the language being queried (Lua, Python, Rust, Go, JavaScript, TypeScript, TSX at time of writing). A TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/valentynkit/jev.nvim/blob/a1577b0ec874208377e5f38496577d2b8797ab11/LICENSE). |

## When to use

Use it for the searches `grep` cannot express because they describe a shape, not a string: "functions that swallow errors", "builds a SQL query by string concatenation", "a test that does not assert anything". It reads the current buffer, so it judges edits you have not saved yet, and results land in quickfix so `:cnext`/`:cdo` work immediately.

It judges each function in isolation. A question about how two functions interact together will not be answered correctly, because nothing in a single function's request tells Jev the other function exists.

## How it works

`vim.treesitter.query.get(lang, "jev")` splits the buffer (or each file matched by an optional glob argument) into functions. Each function becomes a payload of file, name, signature, doc, and source, trimmed to 3,450 characters, and gets one Jev question against the user's plain-language prompt. A session cache keyed on a hash of the question and the function source skips anything unchanged since the last run. Requests are packed under a 45,000-token budget with up to four in flight; a request rejected as over budget is bisected and retried. Responses append to quickfix as they arrive and get a probability shown as virtual text at the end of each matched function's signature line, filtered by a configurable threshold (default 0.75). Counting, sorting, thresholds, byte ranges, token estimation, and retries stay in Lua; Jev only answers the one question per function. Every error path (no key, no `curl`, no parser, a timeout, a 500) leaves the buffer untouched and reports one message.

## Get started

```lua
-- lazy.nvim
{ "valentynkit/jev.nvim", cmd = { "Jev", "JevSort", "JevClear" }, opts = {} }
```

Then `export TYPESAFE_API_KEY=...` and, inside a buffer with a supported Treesitter parser:

```vim
:Jev functions that swallow errors
:Jev builds a SQL query by string concatenation lua/**/*.lua
```

The plugin prints an estimated cost before sending anything (e.g. `jev: 48 functions, 1 request, about $0.0005`) and, above a configurable `confirm_above` function count, asks before spending.

## Examples and demos

The repository ships `demo.gif`/`demo.tape` and a fixture corpus under `fixtures/`. The README states plainly that the demo clip is rendered against the plugin's test fake rather than a live endpoint, so the probabilities shown there are fixtures, not measurements; `demo/README.md` lists exactly what is staged. I have not run the plugin against a live TypeSafe key as part of this submission.

## Limits and data handling

Only the functions matched by the query and glob (trimmed source, signature, doc) go to TypeSafe's Jev endpoint under your own key, one question per function per request, batched under the token budget described above. Cost figures shown in the plugin are arithmetic over the token estimator, not a billed measurement, so the repository notes they hold for whatever endpoint is configured via `JEV_BASE_URL`.

## Review and maintenance

Reviewed 2026-09-19 against commit [`a1577b0`](https://github.com/valentynkit/jev.nvim/commit/a1577b0ec874208377e5f38496577d2b8797ab11). This page was prepared with AI assistance from the project's own README, CHANGELOG, and source layout; I did not run a live TypeSafe key against it as part of this submission, and the cost estimate above is the author's own arithmetic over the fixture corpus, not an independently billed measurement.
