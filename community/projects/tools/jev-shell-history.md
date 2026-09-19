# jev-shell-history

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rank recent zsh commands with Jev and display an inline suggestion that the user can accept into the shell buffer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrnugget/jev-shell-history) |
| Maintainer | [mrnugget](https://github.com/mrnugget). |
| Format | zsh plugin and TypeScript CLI. |
| Jev's role | A Choice ranks history candidates; a Noul judges whether any candidate plausibly completes the typed input. |
| Requirements | zsh 5.9+, Node 22+ with native TypeScript execution, npm and `TYPESAFE_API_KEY`. |
| Access and costs | Source installation with a user-supplied TypeSafe account/key; provider calls can incur charges while typing. |
| License | `MIT` is declared in [package.json](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/package.json), but no project-level license text was found. A vendored skill's license does not establish the plugin's terms. |

## When to use

Use this experimental developer tool to recall commands by literal prefix,
abbreviation or a short description. It also illustrates a bounded semantic
selector: Jev ranks existing history entries, while application code preserves
the actual command strings and decides whether to display a suggestion.

It is not a command generator or a risk assessment system. A previously executed
command may still be inappropriate in the current directory or environment.

## How it works

The [history reader](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/src/history.ts)
reads the end of the history file and selects the latest 100 distinct commands
by default. Code excludes the already typed command and narrows to literal
prefix matches when present. One prefix candidate needs no provider request.

The [selector](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/src/suggest.ts)
uses `@typesafe-ai/sdk` (`^0.6.0`) and `systemOne`, with `jev-latest` as the
reported SDK default and an optional model override. A single request carries
Choice and Noul questions. Choice probabilities rank local candidate IDs;
returned command text always comes from the history, not generated output.

Prefix mode displays its top candidate regardless of score. Fuzzy mode defaults
to a top score of at least 0.3 and either a Noul of at least 0.5 or a top score
of at least 0.9. These are application thresholds, not validated calibration.

The [zsh integration](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/zsh/jev-shell-history.plugin.zsh)
starts a background CLI process on eligible buffer changes, cancels superseded
work and applies results only while the buffer still matches. Typing along an
existing prefix suggestion reuses it. Right arrow or Control-E accepts the
suggestion into the buffer; pressing Enter remains the execution step.

## Get started

These instructions were inspected, not executed. Install dependencies before
trying the CLI; the following step downloads npm packages but makes no Jev call.

```sh
git clone https://github.com/mrnugget/jev-shell-history.git
cd jev-shell-history
npm ci --ignore-scripts
node src/cli.ts --help
```

For an explicit live trial, configure `TYPESAFE_API_KEY` in your protected
environment and prepare a synthetic history file containing harmless commands.
The following command sends that file's selected entries and the supplied input
to TypeSafe and may incur charges:

```sh
node src/cli.ts --history /path/to/synthetic-history --buffer 'git ch' --json
```

The JSON reports ranked commands, scores, Noul, selected suggestion, model and
usage. Empty candidate sets and a single literal prefix candidate avoid model
calls, although the CLI still requires the key variable to be present.

To enable interactive suggestions, source
`zsh/jev-shell-history.plugin.zsh` from your checkout in an interactive zsh, as
shown in the [installation instructions](https://github.com/mrnugget/jev-shell-history#install).
This opt-in sends selected real history entries to TypeSafe as you type; review
that data flow before adding the source line permanently to `.zshrc`.

## Examples and demos

- The [recorded terminal demo](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/demo/demo.gif) uses fabricated history according to upstream. It is demonstration material, not a performance evaluation.
- [Mocked selector tests](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/src/suggest.test.ts) cover request shape, prefix selection, score ranking, no-call shortcuts and gate boundaries.
- The [PTY test](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/test/e2e.zsh) drives a real zsh with synthetic history and requires live credentials; it was not run during this review.

## Limits and data handling

Selected history strings and current typed input go to TypeSafe. There is no
secret-redaction pass: history may include credentials, internal paths or
private arguments. Model-facing command strings are truncated at 240 characters,
but acceptance restores the complete local command, including multiline content.
`JEV_DEBUG_LOG`, when enabled, records typed buffers, suggestion output and errors.

The CLI defaults to an eight-second timeout per attempt and leaves retry behavior
to its SDK configuration. Eligible buffer changes can cause repeated requests;
process cancellation does not establish that an already sent request is unbilled.
On API errors the CLI exits unsuccessfully; the plugin normally suppresses stderr
and displays no new suggestion. There is no lexical fallback after a failed
multi-candidate request. Missing candidate probabilities become zero, and the
plugin has no command-risk filter. Scores and selected fields are exposed, but
full raw typed responses are not retained.

## Review and maintenance

Reviewed on **2026-09-19** at commit
[`4b2b75d26c0ccf5726263904514a22a8e11659ea`](https://github.com/mrnugget/jev-shell-history/commit/4b2b75d26c0ccf5726263904514a22a8e11659ea).
Inspected README, package metadata, tracked license paths, history reader,
selector, CLI, zsh integration, mocked selector tests and live-test setup.
No dependencies were installed, tests executed, local shell history read or
provider requests sent. Live SDK compatibility, shell behavior and suggestion
quality remain unverified. See [catalog validation scope](../../../docs/validation.md#community-project-checks).

AI-assisted catalog review; contributor affiliation/commercial relationships
were not supplied. Listing is not an endorsement.
