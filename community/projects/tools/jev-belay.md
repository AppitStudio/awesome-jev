# Jev Belay

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Claude Code Stop hook that checks whether anything actually ran before it lets an unverified "done" stand.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev-belay) |
| Maintainer | [valentynkit](https://github.com/valentynkit). Self-submitted by the maintainer in [PR #7](https://github.com/AppitStudio/awesome-jev/pull/7), with no commercial relationship beyond authorship disclosed. |
| Format | Claude Code plugin / Stop hook, Node.js. |
| Requirements | Node 20+; Claude Code 2.1.196+ for its `prompt_id` field (older versions fall back to a session-keyed guard). A TypeSafe API key (`TYPESAFE_API_KEY`) is required for live use; without one the hook exits 0 and does nothing. |
| License | [MIT](https://github.com/valentynkit/jev-belay/blob/ef719db7eaadc56aa4def86c4da4ffff5bcbca35/LICENSE). |

## When to use

Use it if an agent session ends turns with an unverified "done" and you want that caught before you trust it, without adding a model call to every single stop. It is not a substitute for CI; it only judges the closing message of a turn where the transcript shows a file changed and nothing has since passed a test, build, or lint run.

A turn with no file edits never reaches the question at all, so a read-only "confirmed, tests pass" is not something this hook can catch. That gap is a direct consequence of the evidence gate that keeps everything else cheap.

## How it works

Two regex belts read the transcript slice since the user's last prompt: one for a test/build/lint runner named in a command, one for the runner's own summary in the output. If a check already passed since the last file change, the hook exits without calling Jev. Otherwise it sends one Jev request with four typed questions (wording adapted from `DevMortimer/pi-warden`'s `src/done.ts`) and reads the answer next to that transcript evidence. A block returns exit code 2 with the reason fed back into Claude's context; blocks are capped at one per prompt, none within 60 seconds of the previous one, three per session.

Every error path (missing key, API failure, timeout, already blocked this turn) exits 0 and lets the turn end, so a broken hook cannot get in the way.

## Get started

**Offline first:** from a source checkout, run `npm test`. The suite uses synthetic inputs and fake responses; it does not establish model quality. [Fake endpoint](https://github.com/valentynkit/jev-belay/blob/ef719db7eaadc56aa4def86c4da4ffff5bcbca35/tools/fake-jev.mjs) is available for isolated integration experiments.

**Live setup - sends a task/message projection and check summaries to TypeSafe and may incur charges:**

Inside Claude Code:

```sh
/plugin marketplace add valentynkit/jev-belay
/plugin install jev-belay@jev-belay
```

The current plugin declares configuration options for the key and settings; upstream documents configuration through Claude Code. For a manual Stop hook pointing at `belay.mjs`, export `TYPESAFE_API_KEY` in the shell before launching `claude`, or configure a supported environment block as shown in the [upstream installation guide](https://github.com/valentynkit/jev-belay/blob/ef719db7eaadc56aa4def86c4da4ffff5bcbca35/README.md#install). The hook does not load `.env` automatically. `JEV_BELAY_THRESHOLD` defaults to 0.70 and `JEV_BELAY_TIMEOUT_MS` to 20000. Plugin options take precedence over ordinary environment settings.

## Examples and demos

The [demo guide](https://github.com/valentynkit/jev-belay/blob/ef719db7eaadc56aa4def86c4da4ffff5bcbca35/demo/README.md) describes a Claude Code session where an unverified completion is blocked and a later check exposes a bug. Upstream reports that the current clip uses direct Jev responses; that recording and its model-quality claims were not independently reproduced. Rendering or re-recording the demo launches Claude Code and can require accounts and paid calls even when the Jev endpoint is faked. It is not the offline test command.

`node belay.mjs --replay demo/sample-decisions.jsonl` replays the supplied decision log without a live key.

## Limits and data handling

The transcript is read locally. [buildState()](https://github.com/valentynkit/jev-belay/blob/ef719db7eaadc56aa4def86c4da4ffff5bcbca35/belay.mjs#L470) sends capped, redacted task and final-message text, file-change counts, and check-command summaries when the evidence gate triggers. Redaction is heuristic, so inspect whether these inputs are appropriate to share. `JEV_BASE_URL` can change the recipient.

The hook stores local session guards. Optional `JEV_BELAY_LOG=1` writes decision records, including projected state, to `~/.claude/belay/decisions.jsonl`. Upstream cost, latency and calibration results are author-reported; this catalog did not reproduce them. A passing check or no file change normally avoids inference.

## Review and maintenance

Reviewed 2026-09-22 against commit [`ef719db`](https://github.com/valentynkit/jev-belay/commit/ef719db7eaadc56aa4def86c4da4ffff5bcbca35). Maintainer-side review inspected the README, license, plugin configuration, hook implementation and demo instructions. `npm test` passed 113 tests with 5 skipped using an isolated environment. No live TypeSafe calls or Claude Code installation were performed. AI assistance was used for the original submission and this repair; execution validates hook behavior against fixtures, not model accuracy.
