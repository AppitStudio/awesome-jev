# laya-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Port of gargpratyush/jev-router (listed) that takes per-turn model routing decisions from Laya — the open, Jev-compatible System One model — instead of TypeSafe Jev: `laya-claude` and `laya-codex` launch the real Claude Code / Codex CLIs behind a local proxy that sends simple turns to the fast tier and hard ones to the strong tier, running Laya locally with no API key or against your own `LAYA_URL` server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bussolabs/laya-router) |
| Maintainer | [bussolabs](https://github.com/bussolabs). Independently curated. |
| Format | npm CLI (`laya-claude`, `laya-codex`, `laya-explain`) |
| Requirements | Node; existing `claude login` / `codex login`; local Laya (downloaded on first use) or `LAYA_URL`. |
| License | [MIT](https://github.com/bussolabs/laya-router/blob/697cf58283028a597b5beb7fa113c95fb9926dff/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Cut cost on routine turns while keeping each CLI's native UX.
- Self-host the routing decision.
- Mismatch: only fresh user turns are routed.

## How it works

[`src/router.mjs`](https://github.com/bussolabs/laya-router/blob/697cf58283028a597b5beb7fa113c95fb9926dff/src/router.mjs) asks Laya at `/v1/systemone`; [`src/policy.mjs`](https://github.com/bussolabs/laya-router/blob/697cf58283028a597b5beb7fa113c95fb9926dff/src/policy.mjs) maps answers to tiers; [`src/proxy.mjs`](https://github.com/bussolabs/laya-router/blob/697cf58283028a597b5beb7fa113c95fb9926dff/src/proxy.mjs) rewrites the model per turn.

## Get started

Install globally (README):

```sh
npm install -g @bussolabs/laya-router
laya-claude
```

No routing API charges with local Laya; the routed models bill your existing accounts.

## Examples and demos

- npm: [`@bussolabs/laya-router`](https://www.npmjs.com/package/@bussolabs/laya-router).
- Architecture: [`docs/laya-claude-architecture.md`](https://github.com/bussolabs/laya-router/blob/697cf58283028a597b5beb7fa113c95fb9926dff/docs/laya-claude-architecture.md).

## Limits and data handling

Turn text goes to your Laya server. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 697cf5828302](https://github.com/bussolabs/laya-router/tree/697cf58283028a597b5beb7fa113c95fb9926dff). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
