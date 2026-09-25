# jev-playwright (arthurfiorette)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Playwright reporter/plugin: TypeSafe Jev selects which E2E tests to run from changed files; skipped tests stay visible and a green run can still mean zero tests executed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arthurfiorette/jev-playwright) |
| Maintainer | [arthurfiorette](https://github.com/arthurfiorette). Independently curated. |
| Format | TypeScript Playwright integration / reporter. |
| Requirements | Node.js; Playwright project; TypeSafe API key for live selection; CI-aware `enabled` flag recommended. |
| License | [MIT](https://github.com/arthurfiorette/jev-playwright/blob/96bdcc6bdf2dd0a9194c302e84eb6c87abb4f398/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **shrink Playwright suites in CI** by letting Jev pick tests related to the diff—distinct from other `jev-playwright` owners.

## How it works

Reporter inspects included changes, asks Jev which tests to run, and skips the rest. Docs warn that selecting zero tests can still exit successfully.

## Get started

```sh
git clone https://github.com/arthurfiorette/jev-playwright.git
cd jev-playwright
git checkout 96bdcc6bdf2dd0a9194c302e84eb6c87abb4f398
# Wire the reporter into playwright.config per README; set TYPESAFE_API_KEY
```

## Examples and demos

- README notes on CI `enabled` gating and “Selected 0/N tests” pitfalls.

## Limits and data handling

Diff/test metadata go to TypeSafe. Do not treat an empty selection as a full-suite pass without comparing to full runs.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 96bdcc6](https://github.com/arthurfiorette/jev-playwright/tree/96bdcc6bdf2dd0a9194c302e84eb6c87abb4f398). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [JevForge jev-pr-profiler](jev-pr-profiler.md), [jev-flaky-detective](jev-flaky-detective.md).
