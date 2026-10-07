# px-triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Keyboard-driven CLI for triaging a GitHub repository's `triage`-labelled issues and PRs: TypeSafe Jev reads each item and proposes the next step (ask for info, bug + owner, schedule, review, close), you confirm with one key or override; GitHub changes run in the background, decisions are logged and traced to Arize Phoenix.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cephalization/px-triage) |
| Maintainer | [cephalization](https://github.com/cephalization). Independently curated. |
| Format | npm CLI `@cephalization/px-triage` (`pxt`), built with Effect and `@typesafe-ai/sdk` |
| Requirements | Node 22.12+, a TypeSafe API key, GitHub auth (`GITHUB_TOKEN` or `gh`); optional Phoenix for traces. |
| License | [MIT](https://github.com/cephalization/px-triage/blob/c7076723b3416f5ee8e6e6ee2ba14299a161ce1a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Work through a backlog of new issues and PRs quickly while keeping a human decision on each.
- Set up the `triage` label automatically with `pxt automate`.
- Mismatch: needs a `triage` label workflow on the repo.

## How it works

[`src/classify/Classifier.ts`](https://github.com/cephalization/px-triage/blob/c7076723b3416f5ee8e6e6ee2ba14299a161ce1a/src/classify/Classifier.ts) asks the questions in [`questions.ts`](https://github.com/cephalization/px-triage/blob/c7076723b3416f5ee8e6e6ee2ba14299a161ce1a/src/classify/questions.ts) about each item and proposes an action; [`src/github/GitHub.ts`](https://github.com/cephalization/px-triage/blob/c7076723b3416f5ee8e6e6ee2ba14299a161ce1a/src/github/GitHub.ts) applies confirmed changes.

## Get started

Install from npm and run inside a checkout (README *Quick start*; npm 0.4.0 checked 2026-10-08):

```sh
npm install -g @cephalization/px-triage
cd your/repo && pxt
```

Each triaged item sends Jev requests billed to your TypeSafe key.

## Examples and demos

- README *How a session works*.
- [Changelog](https://github.com/cephalization/px-triage/blob/c7076723b3416f5ee8e6e6ee2ba14299a161ce1a/CHANGELOG.md).

## Limits and data handling

Issue and PR text goes to TypeSafe (and traces to Phoenix if configured); GitHub writes use your token. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit c7076723b341](https://github.com/cephalization/px-triage/tree/c7076723b3416f5ee8e6e6ee2ba14299a161ce1a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
