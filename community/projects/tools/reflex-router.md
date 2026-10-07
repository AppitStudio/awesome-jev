# reflex-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Alpha loopback proxy for Claude Code: at the start of each piece of work a decision model (TypeSafe Jev by default, local Laya or TypeLLM) judges how much reasoning the task needs; in opt-in route mode cheap work goes to a cheaper model when it will not break the prompt cache, and every decision is recorded with signals of whether it looked wrong afterwards (`reflex report`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ziyacivan/reflex-router) |
| Product homepage | [www.npmjs.com](https://www.npmjs.com/package/reflex-router) |
| Maintainer | [ziyacivan](https://github.com/ziyacivan). Independently curated. |
| Format | npm package `reflex-router` (0.10.0 at review; `reflex` command) and GitHub release tarballs |
| Requirements | Node.js 20+, Claude Code with your own Anthropic credentials, and a `TYPESAFE_API_KEY` (or Laya/TypeLLM backend). |
| License | [MIT](https://github.com/ziyacivan/reflex-router/blob/cbab9b8a5e3584915d507036c361b85a80e7f42a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure in shadow mode what a Jev-based router would have done before letting it route.
- Collect correction, test-failure and undo signals per decision to judge routing later.
- Mismatch: alpha; upstream states no threshold is calibrated and reasoning-effort routing's quality impact is unmeasured.

## How it works

Claude Code talks to a local front door; only positively identified starts of work are sent (redacted, capped) to the backend in [`src/backend/jev.ts`](https://github.com/ziyacivan/reflex-router/blob/cbab9b8a5e3584915d507036c361b85a80e7f42a/src/backend/jev.ts); [`src/worker/router.ts`](https://github.com/ziyacivan/reflex-router/blob/cbab9b8a5e3584915d507036c361b85a80e7f42a/src/worker/router.ts) forwards byte for byte in `shadow` mode or rewrites the model in `route` mode. Data handling: [`docs/privacy.md`](https://github.com/ziyacivan/reflex-router/blob/cbab9b8a5e3584915d507036c361b85a80e7f42a/docs/privacy.md).

## Get started

Install and check the setup (README *Quick start*):

```sh
npm install -g reflex-router
export TYPESAFE_API_KEY=...
reflex doctor
# then start Claude Code through reflex as described in the README
```

One Jev request per start of work, billed to your TypeSafe key; Anthropic usage as usual.

## Examples and demos

- README *How it works* diagram and *Delegation hint (opt-in experiment)*.

## Limits and data handling

Redacted task text goes to the decision backend; requests to Anthropic carry your own credentials. Records stay in `~/.reflex/`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit cbab9b8a5e35](https://github.com/ziyacivan/reflex-router/tree/cbab9b8a5e3584915d507036c361b85a80e7f42a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
