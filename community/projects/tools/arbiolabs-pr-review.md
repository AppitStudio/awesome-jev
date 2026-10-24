# pr-review by Arbio (evidence-backed PR reviewer with a Jev risk triage)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pull request reviewer that reports only findings it can back with code evidence and resumes after crashes; Jev scores the risk of each change during triage and can raise the review depth, never lower it. Runs as a CLI, a GitHub App service, a terminal UI or a macOS app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arbiolabs/pr-reviewer-agent) |
| Maintainer | [arbiolabs](https://github.com/arbiolabs). Independently curated. |
| Format | CLI, GitHub App service and macOS app (TypeScript, Rust) |
| Requirements | Node 22.19+, pnpm, git; a Rust toolchain for the TUI and desktop app; a review model; optional TypeSafe key. |
| License | [MIT](https://github.com/arbiolabs/pr-reviewer-agent/blob/075a1cd5c8d7a9559fa1d9483c2119b2f980bb8e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/decision.ts`](https://github.com/arbiolabs/pr-reviewer-agent/blob/075a1cd5c8d7a9559fa1d9483c2119b2f980bb8e/src/jev/decision.ts) at the pinned commit. |

## When to use

- Run automated PR reviews that stay quiet unless they have evidence.
- Send auth, payments or migration changes to a deeper review automatically.
- Mismatch: human review is still required.

## How it works

`src/jev/decision.ts` uses the `jev-systemone` client to ask a category choice, a risk score and a sensitivity yes/no about the diff. With a TypeSafe key it calls TypeSafe's API; with no key on public repositories it uses the free OpenCode Zen tier (a third-party gateway), and on private repositories without a key Jev is skipped. Integration evidence: [`src/jev/decision.ts`](https://github.com/arbiolabs/pr-reviewer-agent/blob/075a1cd5c8d7a9559fa1d9483c2119b2f980bb8e/src/jev/decision.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
export TYPESAFE_API_KEY=...
node bin/pr-review.mjs review https://github.com/owner/repo/pull/2 --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/arbiolabs/pr-reviewer-agent#readme](https://github.com/arbiolabs/pr-reviewer-agent#readme)

## Limits and data handling

Disclosure: without a key, public-repo diffs go to the third-party OpenCode Zen free tier by default (documented upstream). Diffs also go to your chosen review model.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 075a1cd5c8d7](https://github.com/arbiolabs/pr-reviewer-agent/tree/075a1cd5c8d7a9559fa1d9483c2119b2f980bb8e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
