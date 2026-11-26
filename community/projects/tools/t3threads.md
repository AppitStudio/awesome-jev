# t3threads by Jessica Black / Attune (CLI and MCP tools for T3 Code threads across machines, with Jev classifiers and watchers)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and MCP server that lists, searches, summarizes and coordinates your T3 Code agent threads on every linked machine, so agents can check for overlapping work, hand off tasks and wait for each other. Optional Jev features ask many threads the same typed questions at once (`classify`) and fire a watcher when Jev decides a condition you describe is true.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/attunehq/t3threads) |
| Maintainer | [Jessica Black](https://github.com/jssblck) / [Attune](https://github.com/attunehq). Independently curated. |
| Format | Node.js CLI, MCP server and agent skill (npm `t3threads`) |
| Requirements | Node.js, T3 Code with your existing sign-in; for Jev features a TypeSafe key in `TYPESAFE_API_KEY` or the macOS Keychain (`t3threads.typesafe`). |
| License | [MIT](https://github.com/attunehq/t3threads/blob/f3925b1a16ea83a0b5098ceb67611a6c9f421db1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/meow2149/status/2125890406709891192)). |
| Jev evidence | [`src/intelligence.ts`](https://github.com/attunehq/t3threads/blob/f3925b1a16ea83a0b5098ceb67611a6c9f421db1/src/intelligence.ts) at the pinned commit. |

## When to use

- People running many T3 Code threads across machines who want agents to find related work and get notified on described conditions.
- Mismatch: other agent hosts; it reads T3 Code's own data and sign-in.

## How it works

`src/intelligence.ts` sends selected thread text with named `noul`, `choice` and `score` questions to `https://api.typesafe.ai/v1/systemone` (default `jev-1.13.0`, `T3THREADS_JEV_MODEL` to change). `classify` returns probabilities per thread; a `jev` watcher fires once when the answer passes `--threshold` (default 0.9). Integration evidence: [`src/intelligence.ts`](https://github.com/attunehq/t3threads/blob/f3925b1a16ea83a0b5098ceb67611a6c9f421db1/src/intelligence.ts).

## Get started

Install from npm, link your machines, then try a Jev classifier across a project's threads.

```sh
npm install --global t3threads
export TYPESAFE_API_KEY=...
t3threads classify --project my-app --questions-json '{"overlap":{"type":"noul","instructions":"Does this work change billing webhooks?"}}'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev classifiers section: [github.com/attunehq/t3threads#jev-classifiers](https://github.com/attunehq/t3threads#jev-classifiers)

## Limits and data handling

Jev is opt-in and sends selected thread text to TypeSafe; summaries and `text` watchers use the model provider configured in T3. On macOS it reads T3 data and may trigger app-data and Keychain prompts, which the README explains. Results are cached by content and question.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit f3925b1a16ea](https://github.com/attunehq/t3threads/tree/f3925b1a16ea83a0b5098ceb67611a6c9f421db1). Inspected the README ("Jev classifiers", "Models and privacy"), LICENSE and `src/intelligence.ts` at the pinned commit; npm version 0.8.0 confirmed. Nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
