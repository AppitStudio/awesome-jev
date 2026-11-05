# jevlint by INDXDev (model-based linter that ranks which files to refactor first using AST metrics plus typed decision-model judgments)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Command-line linter that combines AST metrics (exact for TypeScript, JavaScript, Python, Go and Rust) with decision-model answers such as whether names carry meaning, then ranks files by mess, git churn and size and can hand the worst to Claude Code or Codex. Also reviews a PR or commit before and after, supports your own ast-grep-plus-question rules and runs with `--ast-only` without any API key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/INDXDev/jevlint) |
| Maintainer | [INDXDev](https://github.com/INDXDev). Independently curated. |
| Format | npm CLI `@indxjp/jevlint` (Node.js 24+) |
| Requirements | Node.js 24.22.1+ (or the listed 22/26 lines); a provider key for model-based scoring, none for `--ast-only`. |
| License | [MIT](https://github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision/providers.ts`](https://github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/src/decision/providers.ts) at the pinned commit. |

## When to use

- Decide where to spend a cleanup afternoon.
- Check what a change made worse with `jevlint pr`.
- Mismatch: not the same project as the already listed codegirl-007/jevlint; Jev is the model shown in the README but `docs/providers.md` also lists OpenAI Decisions, Vercel AI Gateway, Cloudflare, Microsoft Foundry and compatible endpoints.

## How it works

`src/decision/providers.ts` and `decide.ts` send typed score and yes/no questions to the configured decision model (the `typesafe` provider with `jev-latest` is the documented first option), with run-cost estimates (`audit --dry-run`). Integration evidence: [`src/decision/providers.ts`](https://github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/src/decision/providers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx @indxjp/jevlint --ast-only
npm install -g @indxjp/jevlint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with install and examples: [github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/README.md](https://github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/README.md)
- Provider setup: [github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/docs/providers.md](https://github.com/INDXDev/jevlint/blob/e5d06f43cbf2c77a453805d4517436fe21427301/docs/providers.md)

## Limits and data handling

Model-based scoring sends file contents to the configured provider on your key; the README's demo is a simulated run on a fictional project.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit e5d06f43cbf2](https://github.com/INDXDev/jevlint/tree/e5d06f43cbf2c77a453805d4517436fe21427301). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
