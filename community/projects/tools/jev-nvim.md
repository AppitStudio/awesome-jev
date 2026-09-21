# jev.nvim

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ask a Neovim buffer a plain-language question and get back a quickfix list ranked by Jev's per-function probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev.nvim) |
| Maintainer | [valentynkit](https://github.com/valentynkit). Self-submitted by the maintainer in [PR #7](https://github.com/AppitStudio/awesome-jev/pull/7), with no commercial relationship beyond authorship disclosed. |
| Format | Neovim plugin (Lua). |
| Requirements | Neovim 0.10+, `curl`, and a Treesitter parser for the language being queried (Lua, Python, Rust, Go, JavaScript, TypeScript, TSX at time of writing). A TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [Apache-2.0 query-file notice](https://github.com/valentynkit/jev.nvim/blob/a1577b0ec874208377e5f38496577d2b8797ab11/NOTICE), alongside [MIT](https://github.com/valentynkit/jev.nvim/blob/a1577b0ec874208377e5f38496577d2b8797ab11/LICENSE). |

## When to use

Use it for the searches `grep` cannot express because they describe a shape, not a string: "functions that swallow errors", "builds a SQL query by string concatenation", "a test that does not assert anything". It reads the current buffer, so it judges edits you have not saved yet, and results land in quickfix so `:cnext`/`:cdo` work immediately.

It judges each function in isolation. A question about how two functions interact together will not be answered correctly, because nothing in a single function's request tells Jev the other function exists.

## How it works

`vim.treesitter.query.get(lang, "jev")` splits the buffer (or each file matched by an optional glob argument) into functions. Each function becomes a payload of file, name, signature, doc, and source, trimmed to 3,450 characters, and gets one Jev question against the user's plain-language prompt. A session cache keyed on a hash of the question and the function source skips anything unchanged since the last run. Requests are packed under a 45,000-token budget with up to four in flight; a request rejected as over budget is bisected and retried. Responses append to quickfix as they arrive, including below-threshold results; virtual-text marks at function signatures are filtered by the configurable threshold (default 0.75). Use `:JevSort` to rank the list. Counting, sorting, thresholds, byte ranges, token estimation, and retries stay in Lua; Jev only answers the one question per function. Every error path (no key, no `curl`, no parser, a timeout, a 500) leaves the buffer untouched and reports one message.

## Get started

```lua
-- lazy.nvim
{ "valentynkit/jev.nvim", cmd = { "Jev", "JevSort", "JevClear" }, opts = {} }
```

Before launching Neovim, export `TYPESAFE_API_KEY` into its environment. Live queries send selected source text to TypeSafe and may incur charges. Inside a buffer with a supported Treesitter parser:

```vim
:Jev functions that swallow errors
:Jev builds a SQL query by string concatenation lua/**/*.lua
```

The plugin prints an estimated cost before sending anything (e.g. `jev: 48 functions, 1 request, about $0.0005`) and, above a configurable `confirm_above` function count, asks before spending.

## Examples and demos

The repository ships [demo instructions](https://github.com/valentynkit/jev.nvim/blob/a1577b0ec874208377e5f38496577d2b8797ab11/demo/README.md) and a [fixture corpus](https://github.com/valentynkit/jev.nvim/tree/a1577b0ec874208377e5f38496577d2b8797ab11/fixtures). The README states plainly that the demo clip is rendered against the plugin's test fake rather than a live endpoint, so the probabilities shown there are fixtures, not measurements; `demo/README.md` lists exactly what is staged. No live TypeSafe calls were made for this catalog review.

## Limits and data handling

Only the functions matched by the query and glob (trimmed source, signature, doc) go to TypeSafe's Jev endpoint under your own key, one question per function per request, batched under the token budget described above. Cost figures shown in the plugin are arithmetic over the token estimator, not a billed measurement, and do not establish the actual price of TypeSafe or an alternative endpoint configured via `JEV_BASE_URL`. The configured recipient receives the selected source content.

## Review and maintenance

Reviewed 2026-09-22 against commit [`a1577b0`](https://github.com/valentynkit/jev.nvim/commit/a1577b0ec874208377e5f38496577d2b8797ab11). Maintainer-side review inspected README, MIT license and Apache-2.0 notice, installation instructions, API client, quickfix/mark implementation and the test entry point. Neovim is not installed in the review environment, so no local plugin execution or live calls were performed. AI assistance was used for the submission and repair; demo outputs and cost estimates are not independent measurements.
