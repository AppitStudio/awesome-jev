# pi-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Add a TypeSafe Jev decision layer to the Pi coding agent: a pre-tool gate, a post-tool output judge, and a `jev_ask` tool for typed calibrated answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/y0usaf/pi-jev) |
| Maintainer | [y0usaf](https://github.com/y0usaf). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension published as npm `@y0usaf/pi-jev` (0.2.0 at review). |
| Requirements | Pi coding agent (`@earendil-works/pi-coding-agent`). Live judgments need a TypeSafe key (`TYPESAFE_API_KEY` or `apiKeyFile` in config). Without a key the extension loads, reports once, and stays out of the way. |
| License | [MIT](https://github.com/y0usaf/pi-jev/blob/1b493375ef52e6d8f59dfe83e84402b024536625/LICENSE). |

## When to use

Use it when you want Pi's `bash` / `write` / `edit` calls judged for destructiveness, exfiltration, scope, and impact before they run, and bash output judged for secret leaks and failure class afterward. Prefer simpler local deny-lists when you do not need calibrated probabilities.

**Shadow mode is the default:** flagged calls notify without blocking. Enforce mode can ask for confirmation; headless runs degrade to warnings unless `gate.blockWithoutUI` is set. Every error path fails open.

## How it works

The [client](https://github.com/y0usaf/pi-jev/blob/1b493375ef52e6d8f59dfe83e84402b024536625/src/client.ts) posts to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. The gate batches four questions (three Noul + one Score) in one request. The output judge asks two questions on `tool_result` for bash (secret leak + failure class) and appends advice from a local table when thresholds fire. `jev_ask` exposes the same primitives to the model as a tool. Identical inputs share a cache window (default 120s).

## Get started

```sh
pi install npm:@y0usaf/pi-jev
```

Configure `~/.pi/agent/pi-jev.json` or project `.pi/pi-jev.json` (project keys win). Live use needs a TypeSafe key and incurs usage charges. This listing did not install into a live Pi session.

Offline source checkout for inspection:

```sh
git clone https://github.com/y0usaf/pi-jev.git
cd pi-jev
git checkout 1b493375ef52e6d8f59dfe83e84402b024536625
```

## Examples and demos

Upstream README documents gate thresholds, output-judge classes, and `jev_ask` JSON shapes. No separate offline test suite was present in the reviewed tree; behavior claims below rest on source inspection.

## Limits and data handling

Tool arguments, redacted/capped projections as implemented, and bash output chunks are sent to TypeSafe when a key is present. Failures (missing key, timeout, 429, malformed response) produce no verdict and allow the tool call. Secret detection and thresholds are operational policy, not measured accuracy.

## Review and maintenance

Reviewed on **2026-09-19** at [commit 1b49337](https://github.com/y0usaf/pi-jev/tree/1b493375ef52e6d8f59dfe83e84402b024536625): package `@y0usaf/pi-jev` **0.2.0**, MIT. AI-assisted source review of `client.ts`, `gate.ts`, `output.ts`, `index.ts`, config defaults, and README. No offline automated tests were found or run; no live Pi install or TypeSafe calls were made.

Related: [pi-warden](pi-warden.md) also places Jev in front of Pi actions with local policy holds; [jev-use (shitianfang)](jev-use.md) routes no-text agent steps through MCP rather than a Pi extension.
