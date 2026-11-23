# loop-engineering-on-product by David Tseng (overnight Claude Code product loop with optional Jev fast-reject pre-checks in front of its LLM gates)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An autonomous product-improvement loop for Claude Code: each round researches one idea, has it judged for value before any code, writes a PRD, builds it, has a different agent validate it and pushes to an isolated branch for a human to merge. Optional Jev pre-checks can only reject (fabricated signals, a repeat of the same tactic, a label that does not match behaviour, a repeated failure), never approve, and are rolled out off → shadow → prefilter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/InjayTseng/loop-engineering-on-product) |
| Maintainer | [InjayTseng](https://github.com/InjayTseng). Independently curated. |
| Format | Claude Code framework (shell driver, prompts, Node.js scripts, dashboard) |
| Requirements | A product that builds, an `origin` remote, the `claude` CLI and Node.js 18+; a TypeSafe, OpenRouter or AI Gateway key only for the optional Jev pre-checks. |
| License | [MIT](https://github.com/InjayTseng/loop-engineering-on-product/blob/e46ab9af2dabc332b78593321ef7c085f27b74d1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev/jev.mjs`](https://github.com/InjayTseng/loop-engineering-on-product/blob/e46ab9af2dabc332b78593321ef7c085f27b74d1/scripts/jev/jev.mjs) at the pinned commit. |

## When to use

- Run an agent product loop where cheap Jev checks may skip obviously bad rounds but never approve work.
- Mismatch: proven savings; the author marks the Jev layer N=0 (wired and tested, not yet shown worthwhile on a real run).

## How it works

`scripts/jev/jev.mjs` uses the `jev-use` package with `TYPESAFE_API_KEY`, `OPENROUTER_API_KEY` or `AI_GATEWAY_API_KEY`, prints one `JEV:` result line and always exits 0; a pass, timeout or missing key means the LLM gate runs as if Jev were absent. `JEV_MODE` defaults to `off`. Integration evidence: [`scripts/jev/jev.mjs`](https://github.com/InjayTseng/loop-engineering-on-product/blob/e46ab9af2dabc332b78593321ef7c085f27b74d1/scripts/jev/jev.mjs).

## Get started

Install the framework into your repository on a separate branch, then follow the Jev rollout order in docs/09-jev.md.

```sh
scripts/loop-kit.sh install <your-repo>
cd <your-repo> && git checkout -b loop
(cd scripts/jev && npm ci) && export TYPESAFE_API_KEY=...
JEV_MODE=prefilter node scripts/jev/eval-backlog.mjs   # offline eval on a past run
JEV_MODE=shadow scripts/run-loop.sh 20
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev pre-check design: [github.com/InjayTseng/loop-engineering-on-product/blob/e46ab9af2dabc332b78593321ef7c085f27b74d1/docs/09-jev.md](https://github.com/InjayTseng/loop-engineering-on-product/blob/e46ab9af2dabc332b78593321ef7c085f27b74d1/docs/09-jev.md)
- Real run logs: [github.com/InjayTseng/loop-engineering-on-product/tree/e46ab9af2dabc332b78593321ef7c085f27b74d1/examples](https://github.com/InjayTseng/loop-engineering-on-product/tree/e46ab9af2dabc332b78593321ef7c085f27b74d1/examples)

## Limits and data handling

The loop runs Claude Code unattended on your repository (on a separate branch); review every commit before merging. Jev pre-checks send idea text, git log lines and gate records to the configured provider.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit e46ab9af2dab](https://github.com/InjayTseng/loop-engineering-on-product/tree/e46ab9af2dabc332b78593321ef7c085f27b74d1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
