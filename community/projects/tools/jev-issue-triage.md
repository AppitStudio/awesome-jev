# Jev Issue Triage (GitHub Action that labels and prioritizes new issues with Jev, with a local urgency dashboard)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that reads each new issue and labels it (`bug`, `enhancement`, `question`, `documentation`, `needs-repro`, `security`, `spam`, `severity: ...`). Jev answers small typed questions with probabilities; a short, tested decision table in code turns them into labels from a fixed list and comments from fixed templates. An optional local dashboard groups the backlog by urgency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/elcann7/jev-issue-triage) |
| Maintainer | [elcann7](https://github.com/elcann7). Independently curated. |
| Format | GitHub Action and Node CLI (JavaScript) |
| Requirements | A repository with issues enabled and a `TYPESAFE_API_KEY` repository secret; Node for the dashboard and eval scripts. |
| License | [MIT](https://github.com/elcann7/jev-issue-triage/blob/e92d9713957752b7cfa043f0fee89a199f375b5e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/elcann7/jev-issue-triage/blob/e92d9713957752b7cfa043f0fee89a199f375b5e/src/jev.mjs) at the pinned commit. |

## When to use

- Triage a busy repository's incoming issues cheaply, with labels chosen from a fixed list by readable code.
- Mismatch: English first, other languages mostly untested, and the maintainer calls severity a subjective call.

## How it works

`src/jev.mjs` sends the issue text and typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default); `src/decide.mjs` turns the probabilities into labels, and nothing the model returns is executed or posted. Integration evidence: [`src/jev.mjs`](https://github.com/elcann7/jev-issue-triage/blob/e92d9713957752b7cfa043f0fee89a199f375b5e/src/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
# .github/workflows/triage.yml, on: issues: types: [opened], permissions: issues: write
# add the repository secret TYPESAFE_API_KEY, then see the README's Quick start
npm run demo   # local dashboard sample
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the workflow, decision table and 16-issue evaluation: [github.com/elcann7/jev-issue-triage#readme](https://github.com/elcann7/jev-issue-triage#readme)

## Limits and data handling

Issue text goes to TypeSafe on your key; the Action needs only `issues: write` and labels or comments from fixed templates. The README describes it as an unofficial community project that targets an early-access API. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit e92d97139577](https://github.com/elcann7/jev-issue-triage/tree/e92d9713957752b7cfa043f0fee89a199f375b5e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
