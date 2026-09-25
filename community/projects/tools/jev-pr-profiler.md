# jev-pr-profiler

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that profiles pull-request risk with TypeSafe Jev (plus a deterministic risk floor) and emits review-depth / recommended-check outputs for downstream CI—never merges on its own.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JevForge/jev-pr-profiler) |
| Maintainer | [JevForge](https://github.com/JevForge). Independently curated. |
| Format | GitHub Action ([Marketplace](https://github.com/marketplace/actions/jev-pull-request-profiler)). |
| Requirements | Workflow permissions for the PR; `AI_GATEWAY_API_KEY`, `TYPESAFE_API_KEY`, or `JEV_CUSTOM_API_KEY`. |
| License | [MIT](https://github.com/JevForge/jev-pr-profiler/blob/482b916c7f2c5fb78b9c4e8e7b53e432f00c73de/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Action run against a private PR not executed on the review host. |

## When to use

Use to **standardize PR review depth signals** in CI from metadata and compact diff summaries. Prefer full PR review apps when you need prose findings rather than risk enums.

## How it works

Collectors gather PR metadata and optional security/coverage/incident JSON → deterministic floor → Jev typed evaluation → schema/allowlist validation → outputs / optional comment, labels, check run, or reviewer request (per README). Free-form explanation is display-only.

## Get started

```yaml
- id: profile
  uses: JevForge/jev-pr-profiler@v0.1.0
  env:
    AI_GATEWAY_API_KEY: ${{ secrets.AI_GATEWAY_API_KEY }}
  with:
    create_check_run: true
    low_confidence_policy: request-review
```

Pin review tip: `482b916c7f2c5fb78b9c4e8e7b53e432f00c73de`.

## Examples and demos

- README demo walkthrough for an auth-cookie hardening PR.
- Upstream CI badge on the repository.

## Limits and data handling

Sends compact PR metadata (not full patch hunks) to the configured Jev provider. Never auto-approves or blocks merge; downstream jobs decide.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 482b916](https://github.com/JevForge/jev-pr-profiler/tree/482b916c7f2c5fb78b9c4e8e7b53e432f00c73de). AI-assisted README and LICENSE inspection; Marketplace Action not executed here.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Replace LLM decision calls with a Jev gate in Python](../../knowledge-base/articles/jev-decision-gate.md) — Independently suggested by JevList; not an endorsement by Hanako. Use a GitHub Action for pull-request risk signals instead of writing your own Python gate.
<!-- knowledge:backlinks:end -->
