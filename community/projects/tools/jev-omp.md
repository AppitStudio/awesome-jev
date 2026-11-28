# jev-omp by Kaleb (oh-my-pi extensions: Jev picks the model for each subagent spawn and trims long tool output)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Two extensions for the oh-my-pi (OMP) coding agent. `jev-subagent-router` asks Jev closed questions about each subagent's task brief and picks a model from a pool you define, with confidence fallbacks, static escalations, an audit log and optional pacing across several coding subscriptions. `jev-context` scores blocks of long build, test and lint output before they enter history and keeps lossless originals for recall (opt-in, shadow mode by default).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/junkaleb-hash/jev-omp) |
| Maintainer | [Kaleb](https://github.com/junkaleb-hash) (junkaleb-hash). Independently curated. |
| Format | TypeScript extensions for oh-my-pi (Bun) |
| Requirements | oh-my-pi, Bun, and a TypeSafe key or another provider serving Jev. |
| License | [MIT](https://github.com/junkaleb-hash/jev-omp/blob/f758067e447559c2545f7aa9ce092cbb2068dcd4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev-subagent-router/router.ts`](https://github.com/junkaleb-hash/jev-omp/blob/f758067e447559c2545f7aa9ce092cbb2068dcd4/lib/jev-subagent-router/router.ts) at the pinned commit. |

## When to use

- oh-my-pi users who run many subagents across several models or subscriptions and want per-task model choice.
- Mismatch: other coding agents; these are native OMP extensions.

## How it works

`lib/jev-subagent-router/router.ts` resolves each pool's question tree with Jev (`jev-1.14.0` on `https://api.typesafe.ai/v1/systemone` by default, batched at 20 questions per request) and applies the chosen model in OMP's `before_subagent_spawn` hook; answers below `minConfidence` take the pool's fallback. Integration evidence: [`lib/jev-subagent-router/router.ts`](https://github.com/junkaleb-hash/jev-omp/blob/f758067e447559c2545f7aa9ce092cbb2068dcd4/lib/jev-subagent-router/router.ts).

## Get started

Clone the repo and link both extensions into `~/.omp/agent/`.

```sh
git clone https://github.com/junkaleb-hash/jev-omp && cd jev-omp
./bin/link
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pool config: [github.com/junkaleb-hash/jev-omp/blob/main/config/jev-subagent-pools.json](https://github.com/junkaleb-hash/jev-omp/blob/main/config/jev-subagent-pools.json)
- pstack for OMP: [github.com/junkaleb-hash/pstack-omp](https://github.com/junkaleb-hash/pstack-omp)

## Limits and data handling

Task briefs and (with `jev-context` on) tool-output blocks go to TypeSafe or your configured Jev provider. Quota balancing reads usage from `omp usage --json` and `agy`. Usage and cost figures are the author's own daily-use numbers.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit f758067e4475](https://github.com/junkaleb-hash/jev-omp/tree/f758067e447559c2545f7aa9ce092cbb2068dcd4). Inspected the README, LICENSE, the router and `jev-context` sources at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
