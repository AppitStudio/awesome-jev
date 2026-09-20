# Graphlin

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Live architecture and activity diagrams for Claude Code or Codex while they explore and build a project, with optional TypeSafe Jev classification of graph evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royosherove/graphlin) |
| Maintainer | [royosherove](https://github.com/royosherove). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI/viewer (`npx graphlin`); Claude Code plugin and Codex hooks; local web viewer. |
| Requirements | macOS or Linux; Node.js 22.14+; Claude Code or Codex CLI. Local parsing needs no key. Optional AI classification uses `TYPESAFE_API_KEY` (masked prompt / private store). |
| License | [MIT](https://github.com/royosherove/graphlin/blob/942a8c3d261b6c3086f06ab2f503e80fc71ae441/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected. Live TypeSafe classification and live agent sessions were not run. |

## When to use

Use it when you want a live diagram of how an agent is reading and connecting code (Code, Blocks, C4, Changes, activity timeline) while you keep the host agent in another terminal. Prefer a static architecture doc or IDE diagram when you do not need agent-linked live updates. Local mode stays on-machine; source mode can send filtered excerpts and public agent messages to TypeSafe.

## How it works

Local collectors observe agent/file activity and build a graph. Optional classification goes through [`runtime/jev/provider.mjs`](https://github.com/royosherove/graphlin/blob/942a8c3d261b6c3086f06ab2f503e80fc71ae441/runtime/jev/provider.mjs) to `https://api.typesafe.ai/v1/systemone` (default model `jev-1.13.0`). Application code owns layout, privacy policy, and which evidence is offered. Metadata-only and local modes can run without a key; classification is optional.

## Get started

```sh
git clone https://github.com/royosherove/graphlin.git
cd graphlin
git checkout 942a8c3d261b6c3086f06ab2f503e80fc71ae441
npm ci
npm test
# Live viewer (may prompt for a TypeSafe key in source mode):
# npx --yes graphlin@latest
# Offline demo (no key):
# npx --yes graphlin@latest demo
```

## Examples and demos

- Upstream README preview image and `npx graphlin demo` offline walkthrough.
- Docs under [`docs/`](https://github.com/royosherove/graphlin/tree/942a8c3d261b6c3086f06ab2f503e80fc71ae441/docs) including Jev integration notes.

## Limits and data handling

In source mode, locally filtered source excerpts, user prompts, and public agent messages can leave the host for TypeSafe. Graphlin visualizes observable actions and code evidence; it does not capture private reasoning or prove runtime connectivity. Development preview.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 942a8c3](https://github.com/royosherove/graphlin/tree/942a8c3d261b6c3086f06ab2f503e80fc71ae441): MIT. AI-assisted source review of `runtime/jev/provider.mjs`, onboarding, README, and LICENSE. On Node.js 22.23.2, **`npm test`**: **1122 pass / 0 fail**. No live TypeSafe or live Claude/Codex sessions.

Related: [JevScope](jevscope.md), [Foreman](foreman.md).
