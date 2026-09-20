# The Jev-enator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hooks that call TypeSafe Jev on the hot path: a PreToolUse danger gate, a PostToolUse failure notice, and a Stop completion check (log-only by default).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jakenbear/the-jev-enator) |
| Maintainer | [jakenbear](https://github.com/jakenbear). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python 3.10+ stdlib scripts + `install.sh` / `verify.sh` for Claude Code `settings.json` hooks. |
| Requirements | Claude Code; live hooks need `TYPESAFE_API_KEY` in the environment Claude inherits (install copies from `.env`). Missing key → hooks no-op. |
| License | [MIT](https://github.com/jakenbear/the-jev-enator/blob/d85b6229b7d5892fa406df90b465b186d0b75490/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline cassette fixtures inspected. Live TypeSafe calls were not run. Latency/cost badges are upstream claims, not remeasured here. |

## When to use

Use it when you want cheap typed judgments inside Claude Code tool/stop hooks rather than another LLM call. Prefer [Canny](canny.md) / [clear-head](clear-head.md) / [jev-guard](jev-guard.md) when you need their different evidence ledgers or multi-agent coverage.

## How it works

[`src/jev_gate.py`](https://github.com/jakenbear/the-jev-enator/blob/d85b6229b7d5892fa406df90b465b186d0b75490/src/jev_gate.py), [`jev_notice.py`](https://github.com/jakenbear/the-jev-enator/blob/d85b6229b7d5892fa406df90b465b186d0b75490/src/jev_notice.py), and [`jev_finish.py`](https://github.com/jakenbear/the-jev-enator/blob/d85b6229b7d5892fa406df90b465b186d0b75490/src/jev_finish.py) send typed questions to TypeSafe and map answers to allow/ask/deny or notices. Hook policy and Claude settings wiring live in install scripts; the completion check stays non-blocking unless you opt into enforce mode.

## Get started

```sh
git clone https://github.com/jakenbear/the-jev-enator.git
cd the-jev-enator
git checkout d85b6229b7d5892fa406df90b465b186d0b75490
export JEV_GATE_REPLAY=tests/cassette.json
python3 tests/test_jev_gate.py
python3 tests/test_jev_notice.py
python3 tests/test_jev_finish.py
```

Live install: copy `.env.example` → `.env`, run `./install.sh` and `./verify.sh`, then restart Claude Code. That path uses TypeSafe.

## Examples and demos

- Offline cassette suite (CI path): **26 + 19 + 12** fixture expectations at the reviewed revision.
- README tables for default enforce vs log-only behavior.

## Limits and data handling

Tool arguments, command output slices, and transcript excerpts used by hooks leave the host on live calls. Calibration is author-reported from limited stacks—treat false positives/negatives as expected and contribute cases upstream. Do not commit real keys.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d85b622](https://github.com/jakenbear/the-jev-enator/tree/d85b6229b7d5892fa406df90b465b186d0b75490): MIT. AI-assisted source review of hooks, install scripts, and README. Cassette replay: **gate 26/26**, **notice 19/19**, **finish 12/12**. No live TypeSafe calls.

Related: [Canny](canny.md), [clear-head](clear-head.md), [jev-guard](jev-guard.md), [toolgate](toolgate.md).
