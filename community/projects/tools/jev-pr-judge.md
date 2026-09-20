# jev-pr-judge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed pull-request verdicts with TypeSafe System One: one parallel Jev call, policy weights in TypeScript, plus a local Next.js UI and a GitHub Action that posts a sticky comment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juanegido/jev-pr-judge) |
| Maintainer | [juanegido](https://github.com/juanegido). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript / Next.js app **0.1.0** with bundled GitHub Action (`juanegido/jev-pr-judge`, `action.yml` → `dist/action`). |
| Requirements | Node.js for the app/tests; live judging needs `TYPESAFE_API_KEY` (and optional `GITHUB_TOKEN` for private PRs / higher rate limits). Action needs the TypeSafe key as a repository secret. |
| License | [MIT](https://github.com/juanegido/jev-pr-judge/blob/c7ec7b2ea089863514292d6e6100214213720935/LICENSE). |

## When to use

Use it to get a cheap, code-owned approve/send-back/human-review style signal on whether a PR matches its claim. Prefer [Moongate](moongate.md) when you already encode many repo-specific JSON semantic rules for CI annotations; prefer [Jev Review](jev-review.md) MCP variants for agent-in-the-loop review. Profiles (`balanced`, `hotfix`, `refactor`, `docs`) change policy weights—not the model prompt chain.

## How it works

Judge code under [`src/lib/judge/`](https://github.com/juanegido/jev-pr-judge/tree/c7ec7b2ea089863514292d6e6100214213720935/src/lib/judge) builds bounded PR state and posts parallel System One questions via `@typesafe-ai/sdk`; [`policy.ts`](https://github.com/juanegido/jev-pr-judge/blob/c7ec7b2ea089863514292d6e6100214213720935/src/lib/judge/policy.ts) applies thresholds in application code. The Action reads the PR through the GitHub API (no checkout required for the default flow) and can fail the job based on `fail-on`.

## Get started

```sh
git clone https://github.com/juanegido/jev-pr-judge.git
cd jev-pr-judge
git checkout c7ec7b2ea089863514292d6e6100214213720935
npm install
cp env.example .env.local   # TYPESAFE_API_KEY=…
npm test                    # offline policy/state unit tests
# Live UI: npm run dev  → http://localhost:3000
# Action: uses: juanegido/jev-pr-judge@v1 with typesafe-api-key secret (see README)
```

Live judging sends PR title/body/diff-derived evidence to TypeSafe. This listing did not call the API or run the Action.

## Examples and demos

- README GitHub Action workflow snippet and profile inputs.
- Offline tests via `npm test` (policy, state, code-facts, render).
- Evaluation helpers under `evaluation/` and `scripts/` (optional live).

## Limits and data handling

PR text and selected diff evidence leave CI/dev machines for TypeSafe. Action comments are sticky updates when enabled. Upstream frames the project as a demo of System One primitives—treat verdict quality as unbenchmarked here. Pin an Action ref (`@v1` / commit SHA) in production workflows.

## Review and maintenance

Reviewed on **2026-09-20** at [commit c7ec7b2](https://github.com/juanegido/jev-pr-judge/tree/c7ec7b2ea089863514292d6e6100214213720935): **0.1.0**, MIT. AI-assisted source review of README, `action.yml`, judge policy module, `package.json`, and license. No `npm test` / live TypeSafe or GitHub Action run on the review host.

Related: [Moongate](moongate.md), [Jev Review](jev-review.md), [patdown](patdown.md).
