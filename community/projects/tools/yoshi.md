# Yoshi

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental local context-pruning proxy for Claude Code and Codex: TypeSafe Jev (via Vercel AI Gateway `typesafe-ai/jev`) judges which historical spans can be omitted while preserving protocol bytes. Honest POC with measured benchmarks; production pruning is intended to move into CompozyOS.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/compozy/yoshi) |
| Maintainer | [compozy](https://github.com/compozy). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Bun/TypeScript loopback proxy **0.1.0** (experimental POC). |
| Requirements | Bun; `AI_GATEWAY_API_KEY` for Jev judging (without it, Yoshi forwards unchanged); Claude Code / Codex pointed at the local listener. |
| License | [MIT](https://github.com/compozy/yoshi/blob/55c719718e5039f2276fbad804211682ae012f1e/LICENSE). Gateway/TypeSafe and upstream Anthropic/OpenAI usage have separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; offline `bun test` run. Live Claude Code/Codex sessions and live Gateway Jev calls were not run. Upstream warns both v12 trials were slower than baseline. |

## When to use

Use it when you want a local, inspectable request-path pruning proxy that asks Jev whether omitting a span would lose a required fact or binding constraint. Prefer [fast-jev-compaction](fast-jev-compaction.md), [jev-pruner](jev-pruner.md), or [winnow](winnow.md) for different compaction/hook shapes. If you want the longer-term product direction, follow [CompozyOS](https://github.com/compozy/compozy)—Yoshi itself is labeled a POC.

## How it works

Yoshi sits on `127.0.0.1` and accepts Anthropic Messages (Claude Code) and OpenAI Responses (Codex). Above a size gate it splits eligible completed tool args/results/reports into spans and asks Jev via [`src/judge.ts`](https://github.com/compozy/yoshi/blob/55c719718e5039f2276fbad804211682ae012f1e/src/judge.ts) (`createGateway(...).evaluationModel("typesafe-ai/jev")`). Only validated omissions become explicit markers; failed/timed-out judgments keep spans. Sticky decisions can persist across turns. Benchmarks and privacy notes are in upstream `docs/BENCHMARKS.md` / README.

## Get started

```sh
git clone https://github.com/compozy/yoshi.git
cd yoshi
git checkout 55c719718e5039f2276fbad804211682ae012f1e
bun install --frozen-lockfile
bun test
bun run check
# Live proxy (not run here): set AI_GATEWAY_API_KEY, then bun start / follow upstream README for Claude Code or Codex wiring.
```

## Examples and demos

- Measured v12 study tables/figures in upstream README and `docs/BENCHMARKS.md` (not re-run).
- Offline `bun test`: **43 passed** on the review host.
- Without a Gateway key, requests forward unchanged (safe dry path for wiring checks).

## Limits and data handling

Candidate spans (including source from Write/Edit/Bash args) go to TypeSafe through the Vercel AI Gateway when judging is enabled; upstream notes no zero-data-retention option. Jev outages can delay requests up to the evaluation deadline. Do not treat README input-reduction figures as a guaranteed savings percentage for your workload.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 55c7197](https://github.com/compozy/yoshi/tree/55c719718e5039f2276fbad804211682ae012f1e): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/judge.ts`, and server/proxy modules. Ran `bun install --frozen-lockfile` and `bun test`: **43 passed / 0 failed**. Live Gateway/Claude/Codex paths not executed.

Related: [fast-jev-compaction](fast-jev-compaction.md), [jev-pruner](jev-pruner.md), [winnow](winnow.md), [clear-head](clear-head.md).
