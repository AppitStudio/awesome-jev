# unjangled-guardrails (local-first Jev-compatible guard for coding agent tool calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fork of the listed jev-guard: one hook-based guardrail that judges every tool call and result for Claude Code, Codex, Copilot CLI, Gemini CLI and Cursor using any Jev-compatible classifier, local by default, with TypeSafe and Vercel AI Gateway as cloud options and offline rules when the classifier is down.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/johnbuck/unjangled-guardrails) |
| Maintainer | [johnbuck](https://github.com/johnbuck). Independently curated. |
| Format | Agent hooks and CLI (Node.js) |
| Requirements | git and Node.js 20.3+; a local Jev-compatible endpoint, a TypeSafe key, or a Vercel AI Gateway key. |
| License | [MIT](https://github.com/johnbuck/unjangled-guardrails/blob/b27f6390ede776c3dd22eb8d3263277d06fa284c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/johnbuck/unjangled-guardrails/blob/b27f6390ede776c3dd22eb8d3263277d06fa284c/src/jev.js) at the pinned commit. |

## When to use

- Gate risky agent tool calls with a classifier you host yourself.
- Keep a rules floor when the classifier is unreachable instead of failing open.
- Mismatch: a guardrail, not a sandbox; keep your other controls.

## How it works

`src/jev.js` posts each call to `SYSTEMONE_URL` (a local `/v1/systemone` service) when set, otherwise to `https://api.typesafe.ai/v1/systemone` or Vercel AI Gateway (`typesafe-ai/jev`); a circuit breaker switches to vendored rules after repeated timeouts. Integration evidence: [`src/jev.js`](https://github.com/johnbuck/unjangled-guardrails/blob/b27f6390ede776c3dd22eb8d3263277d06fa284c/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/johnbuck/unjangled-guardrails && cd unjangled-guardrails
node src/cli.js install claude
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Changelog: [github.com/johnbuck/unjangled-guardrails/blob/main/CHANGELOG.md](https://github.com/johnbuck/unjangled-guardrails/blob/main/CHANGELOG.md)
- Upstream: [github.com/leepokai/jev-guard](https://github.com/leepokai/jev-guard)

## Limits and data handling

Tool calls and results go to the classifier endpoint you choose (local by default).

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit b27f6390ede7](https://github.com/johnbuck/unjangled-guardrails/tree/b27f6390ede776c3dd22eb8d3263277d06fa284c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
