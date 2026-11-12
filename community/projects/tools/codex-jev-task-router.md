# Task Router for Codex and Claude Code (skill that plans model, effort and workers, asking Jev only on unclear tasks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Skill for Codex and Claude Code plus a dependency-free Node.js helper that plans the model, thinking effort, skills and bounded worker use for a task; clear tasks route locally, and genuinely ambiguous public tasks can ask TypeSafe Jev for typed judgments that code then checks against explicit policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sir-ad/codex-jev-task-router) |
| Maintainer | [sir-ad](https://github.com/sir-ad). Independently curated. |
| Format | Agent skill with a Node.js helper (JavaScript, MIT) |
| Requirements | Git and Node.js 22+; Codex or Claude Code; optional `TYPESAFE_API_KEY` (or a macOS Keychain entry) for ambiguous tasks. |
| License | [MIT](https://github.com/sir-ad/codex-jev-task-router/blob/b246fb6125ff623ebc4dbb02001e4cf0d7b9062f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/route.mjs`](https://github.com/sir-ad/codex-jev-task-router/blob/b246fb6125ff623ebc4dbb02001e4cf0d7b9062f/scripts/route.mjs) at the pinned commit. |

## When to use

- Pick a cheaper model or lower effort for small tasks in Codex or Claude Code.
- Ask Jev only when a task is genuinely unclear, with policy checks in code.
- Mismatch: returns a plan; the agent still dispatches and verifies the work.

## How it works

`scripts/route.mjs` posts one request (`jev-latest`) to `https://api.typesafe.ai/v1/systemone` only when the task is marked uncertain, public and sanitized, caps it at one TypeSafe call, and records whether the plan came from local policy or from Jev plus policy; the helper returns a plan and never dispatches a worker itself. Integration evidence: [`scripts/route.mjs`](https://github.com/sir-ad/codex-jev-task-router/blob/b246fb6125ff623ebc4dbb02001e4cf0d7b9062f/scripts/route.mjs).

## Get started

Clone the tagged release into your Codex or Claude Code skills folder, then try the bundled examples, which need no key and make no network call.

```sh
git clone --branch v2.2.0 --depth 1 https://github.com/sir-ad/codex-jev-task-router.git "${CODEX_HOME:-$HOME/.codex}/skills/codex-task-router"
node scripts/route.mjs < examples/local-route.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Routing contract: [github.com/sir-ad/codex-jev-task-router/blob/b246fb6125ff623ebc4dbb02001e4cf0d7b9062f/references/routing-contract.md](https://github.com/sir-ad/codex-jev-task-router/blob/b246fb6125ff623ebc4dbb02001e4cf0d7b9062f/references/routing-contract.md)

## Limits and data handling

Only a reviewed, sanitized task summary is sent to TypeSafe, and only for tasks you mark as uncertain and public.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit b246fb6125ff](https://github.com/sir-ad/codex-jev-task-router/tree/b246fb6125ff623ebc4dbb02001e4cf0d7b9062f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
