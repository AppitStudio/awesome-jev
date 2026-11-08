# Xum by Coder (coding-agent multiplexer desktop app with a TypeSafe provider and Jev auto model routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Coder's desktop app for isolated, parallel agentic development (formerly Mux); it includes a TypeSafe provider and uses `typesafe:jev-latest` as the default evaluation model for auto model routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coder/xum) |
| Maintainer | [coder](https://github.com/coder). Independently curated. |
| Format | Electron desktop app + CLI (AGPL-3.0) |
| Requirements | Xum desktop build, your model providers, and a TypeSafe API key for Jev routing. |
| License | [AGPL-3.0](https://github.com/coder/xum/blob/3d54449d064c480064985fbc47cd5a297bc68937/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/constants/autoModelRouting.ts`](https://github.com/coder/xum/blob/3d54449d064c480064985fbc47cd5a297bc68937/src/constants/autoModelRouting.ts) at the pinned commit. |

## When to use

- Let Jev pick which model handles each agent turn.
- Run many coding agents in parallel worktrees.
- Mismatch: routing quality depends on your configured models.

## How it works

`autoModelRouting.ts` sets `DEFAULT_AUTO_MODEL_ROUTING_EVALUATION_MODEL` to `typesafe:jev-latest`; the TypeSafe provider card in Settings stores the key and requests go to `/v1/systemone`. Integration evidence: [`src/constants/autoModelRouting.ts`](https://github.com/coder/xum/blob/3d54449d064c480064985fbc47cd5a297bc68937/src/constants/autoModelRouting.ts).

## Get started

Install Xum from the upstream releases/docs, add a TypeSafe key in Settings → Providers, and enable auto model routing.

```sh
git clone https://github.com/coder/xum.git && cd xum
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/coder/xum/blob/3d54449d064c480064985fbc47cd5a297bc68937/README.md](https://github.com/coder/xum/blob/3d54449d064c480064985fbc47cd5a297bc68937/README.md)

## Limits and data handling

Turn context for routing is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 3d54449d064c](https://github.com/coder/xum/tree/3d54449d064c480064985fbc47cd5a297bc68937). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
