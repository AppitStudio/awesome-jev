# Jev Belay

[All projects](../README.md) · [Developer tools](../README.md#developer-tools)

A Claude Code Stop hook that checks whether anything actually ran before it lets an unverified "done" stand.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev-belay) |
| Maintainer | [valentynkit](https://github.com/valentynkit). I am the maintainer, submitting my own project; no commercial relationship beyond authorship. |
| Format | Claude Code plugin / Stop hook, Node.js. |
| Requirements | Node 20+; Claude Code 2.1.196+ for its `prompt_id` field (older versions fall back to a session-keyed guard). A TypeSafe API key (`TYPESAFE_API_KEY`) is required for live use; without one the hook exits 0 and does nothing. |
| License | [MIT](https://github.com/valentynkit/jev-belay/blob/98f39e04492068e39b48962183acf43b4337da32/LICENSE). |

## When to use

Use it if an agent session ends turns with an unverified "done" and you want that caught before you trust it, without adding a model call to every single stop. It is not a substitute for CI; it only judges the closing message of a turn where the transcript shows a file changed and nothing has since passed a test, build, or lint run.

A turn with no file edits never reaches the question at all, so a read-only "confirmed, tests pass" is not something this hook can catch. That gap is a direct consequence of the evidence gate that keeps everything else cheap.

## How it works

Two regex belts read the transcript slice since the user's last prompt: one for a test/build/lint runner named in a command, one for the runner's own summary in the output. If a check already passed since the last file change, the hook exits without calling Jev. Otherwise it sends one Jev request with four typed questions (wording adapted from `DevMortimer/pi-warden`'s `src/done.ts`) and reads the answer next to that transcript evidence. A block returns exit code 2 with the reason fed back into Claude's context; blocks are capped at one per prompt, none within 60 seconds of the previous one, three per session.

Every error path (missing key, API failure, timeout, already blocked this turn) exits 0 and lets the turn end, so a broken hook cannot get in the way.

## Get started

**Offline first:** `tools/fake-jev.mjs` in the repository stands in for the API, and the repo's demo clip and `demo/README.md` say plainly that its four probabilities came from that fake rather than a live call.

**Live setup - sends transcript text to TypeSafe and may incur charges:**

```sh
/plugin marketplace add valentynkit/jev-belay
/plugin install jev-belay@jev-belay
```

or by hand in `~/.claude/settings.json`, pointing a `Stop` hook at `belay.mjs`. Then `cp .env.example .env` and set `TYPESAFE_API_KEY`. `JEV_BELAY_THRESHOLD` (default 0.75) and `JEV_BELAY_TIMEOUT_MS` (default 20000) are the two settings worth reading before turning it on for a real session.

## Examples and demos

The repository's own [demo](https://github.com/valentynkit/jev-belay/blob/98f39e04492068e39b48962183acf43b4337da32/demo/README.md) walks through one real session: Claude claims "Done" without running anything, gets blocked, runs the suite itself, and finds a bug the rename exposed. `node belay.mjs watch` and `node belay.mjs --replay demo/sample-decisions.jsonl` replay recorded decisions without a live key.

## Limits and data handling

The transcript slice since the last prompt, plus the four question texts, goes to TypeSafe's Jev endpoint under your own key when the evidence gate triggers. Nothing is sent on the far more common path where a check already passed or nothing changed. The author reports (self-reported, not independently reproduced) that in one 2,491-stop corpus the question was reached on 16.6% of stops, at roughly $0.000017 per call it does reach. Detection quality against that corpus is not independently established here; the README cites a related published calibration finding (a similar "don't say done" rule scoring AUROC 0.50 on a different project's corpus) as the reason the evidence-first design exists, not as a result for this project itself.

## Review and maintenance

Reviewed 2026-09-19 against commit [`98f39e0`](https://github.com/valentynkit/jev-belay/commit/98f39e04492068e39b48962183acf43b4337da32). This page was prepared with AI assistance from the project's own README, CHANGELOG, and source layout; I did not run a live TypeSafe key against it as part of this submission, and the corpus/cost figures above are the author's self-reported numbers, not independently re-measured here.
