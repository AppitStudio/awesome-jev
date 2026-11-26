# wp-debuglog-triage by Hamza Ahmad Aslam (CLI that groups a WordPress debug.log, ties each group to core, a plugin or a theme, and ranks it by kind and urgency with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Command-line tool that turns a WordPress `debug.log` into a short ranked list of problems. Code groups repeated entries and attributes each group to core, a plugin or a theme from its file paths; Jev judges each group's kind (noise, deprecation, warning, fatal, security sign, performance) and urgency, and groups it is unsure about go to a review list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/wp-debuglog-triage) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). |
| License | [MIT](https://github.com/hamzaahmadaslam/wp-debuglog-triage/blob/12bf06b67a1832909c125b7347be1e429e14b54c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/wp-debuglog-triage/blob/12bf06b67a1832909c125b7347be1e429e14b54c/src/jev.mjs) at the pinned commit. |

## When to use

- WordPress developers and maintainers facing a large `debug.log` who want the one fatal error found among thousands of deprecation notices.
- Mismatch: knowing whether an error is still live or which plugin is active; the tool only sees the log.

## How it works

`src/jev.mjs` posts batches of grouped log messages to `https://api.typesafe.ai/v1/systemone` (model `jev-latest` unless `TYPESAFE_MODEL` is set) with a kind choice and an urgency score per group; anything below `--threshold` (0.8) goes to review. `--dry-run` prints the questions and a token estimate without sending anything. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/wp-debuglog-triage/blob/12bf06b67a1832909c125b7347be1e429e14b54c/src/jev.mjs).

## Get started

Install from npm, set your key and point it at a log file (or `-` for standard input).

```sh
npm install -g @hamzaahmadaslam/wp-debuglog-triage
export TYPESAFE_API_KEY=...
wp-debuglog-triage wp-content/debug.log --top 10
wp-debuglog-triage wp-content/debug.log --dry-run   # nothing sent
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample dry run: [github.com/hamzaahmadaslam/wp-debuglog-triage/blob/12bf06b67a1832909c125b7347be1e429e14b54c/examples/dry-run.txt](https://github.com/hamzaahmadaslam/wp-debuglog-triage/blob/12bf06b67a1832909c125b7347be1e429e14b54c/examples/dry-run.txt)

## Limits and data handling

Grouped log messages go to TypeSafe; log lines can contain attacker-written text (URLs, form values) that can move an answer, so check security-relevant groups yourself. Attribution comes from file paths only, grouping can merge two bugs that print the same message, and at most 20,000 distinct messages are grouped.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 12bf06b67a18](https://github.com/hamzaahmadaslam/wp-debuglog-triage/tree/12bf06b67a1832909c125b7347be1e429e14b54c). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
