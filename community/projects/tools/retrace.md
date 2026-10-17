# Retrace

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that keeps a ledger of every review thread on a pull request and, on each push, marks threads as likely fixed, partially fixed, still open or made worse using one Jev call per changed thread.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akbokha/retrace) |
| Maintainer | [akbokha](https://github.com/akbokha). Independently curated. |
| Format | GitHub Action (TypeScript) |
| Requirements | A GitHub repository with Actions, a `TYPESAFE_API_KEY` secret (or any Jev-compatible server); optional Anthropic key for the verifier cascade. |
| License | [MIT](https://github.com/akbokha/retrace/blob/931af48caeb7e167fd4ac54c611c6f75ed2f414e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/akbokha/retrace/blob/931af48caeb7e167fd4ac54c611c6f75ed2f414e/src/jev.ts) at the pinned commit. |

## When to use

- See which of many review comments a new push actually addressed, across several review rounds.
- Track threads from humans, Copilot or other review bots without adding another reviewer.
- Mismatch: it judges diffs near commented lines; it does not run tests or prove a fix.

## How it works

Threads on files the push did not touch are skipped without a model call. For changed files, a small state (nearby hunks, commit messages, up to four related files) goes to Jev through the TypeSafe SDK with three typed questions: addressed, touched, and an outcome choice. Low confidence is shown as unsure, and an optional LLM verifier must agree before a thread is marked fixed. The ledger lives in one sticky PR comment. Integration evidence: [`src/jev.ts`](https://github.com/akbokha/retrace/blob/931af48caeb7e167fd4ac54c611c6f75ed2f414e/src/jev.ts).

## Get started

From the upstream README (not run on the review host). Add the key as a repository secret, then:

```sh
# .github/workflows/retrace.yml
on:
  pull_request:
    types: [opened, synchronize, reopened]
permissions:
  contents: read
  pull-requests: write
jobs:
  retrace:
    runs-on: ubuntu-latest
    steps:
      - uses: akbokha/retrace@v0
        with:
          typesafe-api-key: ${{ secrets.TYPESAFE_API_KEY }}
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo PR: [github.com/akbokha/retrace/pull/1](https://github.com/akbokha/retrace/pull/1)
- One-page summary: `TLDR.md`; evaluation on MCR-bench in the README.

## Limits and data handling

Code hunks near review comments go to TypeSafe (or a self-hosted Kev server you configure) on your key. Needs `pull-requests: write` to update its comment.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 931af48caeb7](https://github.com/akbokha/retrace/tree/931af48caeb7e167fd4ac54c611c6f75ed2f414e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
