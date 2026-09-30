# openclaw-jev-trigger

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenClaw plugin + CLI: write automation triggers in plain language; TypeSafe Jev (via `decisionModel`) judges each tick so the conversation model wakes only when it matters.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yousan/openclaw-jev-trigger) |
| Maintainer | [yousan](https://github.com/yousan). Independently curated. |
| Format | OpenClaw plugin (`jev_when`) + CLI that emits trigger scripts. |
| Requirements | OpenClaw ≥ 2026.9.6; Node 24.16+; `@openclaw/typesafe` + TypeSafe key (or local Kev/ONNX decisionModel). |
| License | [MIT](https://github.com/yousan/openclaw-jev-trigger/blob/01a92268a681ce4390d31b2f5d0c956c5e58464d/LICENSE). Hosted Jev usage may incur charges. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream benchmark on synthetic ticks is author-reported; not re-run here. Distinct from [openclaw-typesafe-ai](openclaw-typesafe-ai.md). Live OpenClaw/TypeSafe paths not run on the review host. |

## When to use

Use when OpenClaw automations need meaning-level wake conditions instead of brittle JavaScript. Prefer [openclaw-typesafe-ai](openclaw-typesafe-ai.md) for an explicit `typesafe_decide` tool without scheduler triggers.

## How it works

Each tick a script observes evidence and calls `jev_when` → OpenClaw `decisions.evaluate` (default hosted Jev). Returns `fire: false` to stay quiet or wakes the agent with a message when the condition edges true.

## Get started

```sh
git clone https://github.com/yousan/openclaw-jev-trigger.git
cd openclaw-jev-trigger
git checkout 01a92268a681ce4390d31b2f5d0c956c5e58464d
# follow upstream: openclaw plugins install @openclaw/typesafe; install this plugin; CLI examples
```

## Examples and demos

- Upstream demo GIF and CI-red / thread-finished examples in README.
- Author-reported synthetic benchmark tables (not re-run here).

## Limits and data handling

Hosted Jev receives observation evidence each tick. Catalog checks did not install OpenClaw or run live triggers.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 01a9226](https://github.com/yousan/openclaw-jev-trigger/tree/01a92268a681ce4390d31b2f5d0c956c5e58464d). AI-assisted README and license inspection; install/live paths not executed.
