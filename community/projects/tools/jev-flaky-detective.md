# JEV Flaky Detective

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action: TypeSafe Jev classifies failing tests as regression, flaky, environment, or unknown—results are never masked or auto-rerun.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JevForge/jev-flaky-detective) |
| Maintainer | [JevForge](https://github.com/JevForge). Independently curated. |
| Format | GitHub Action (TypeScript) + CI workflow. |
| Requirements | GitHub Actions; TypeSafe/Jev access as documented (Vercel AI Gateway path mentioned upstream); test history inputs per README. |
| License | [MIT](https://github.com/JevForge/jev-flaky-detective/blob/ebfd5b80ad6581799b0900b101d26665a5f9a682/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use on red builds when you need a **typed failure class** for humans/CI policy without auto-greenwashing flaky tests.

## How it works

Collects current results and history, asks Jev for a class, and emits structured outputs; explicitly does not mask or auto-rerun failures.

## Get started

```sh
# Add the Action from https://github.com/JevForge/jev-flaky-detective
# Pin commit ebfd5b80ad6581799b0900b101d26665a5f9a682 in your workflow per upstream docs
```

## Examples and demos

- README CI badge and release tags.
- Upstream action inputs/outputs.

## Limits and data handling

Failure logs/metadata go to the configured Jev provider. Classification is advisory—do not drop required checks based on “flaky” alone without your own policy.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit ebfd5b8](https://github.com/JevForge/jev-flaky-detective/tree/ebfd5b80ad6581799b0900b101d26665a5f9a682). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [jev-pr-profiler](jev-pr-profiler.md).
