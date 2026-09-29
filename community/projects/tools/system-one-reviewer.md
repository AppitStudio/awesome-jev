# system-one-reviewer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local pull-request reviewer that keeps plumbing in code and asks TypeSafe Jev (or another System One model) for every judgment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/equationalapplications/system-one-reviewer) |
| Maintainer | [equationalapplications](https://github.com/equationalapplications). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI (`system-one-reviewer`) with evaluation harness. |
| Requirements | Python; git repo; TypeSafe (or local System One) credentials for live review. |
| License | [MIT](https://github.com/equationalapplications/system-one-reviewer/blob/9a73661dcd6a257501da10c73917df7eb69decae/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use for cheap local System One PR triage. Prefer full LLM agent reviewers when you need free-form patch suggestions.

## How it works

Clusters diff hunks, batches typed severity/true-positive/category questions to Jev or a local System One, and composes an advisory verdict in code. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/equationalapplications/system-one-reviewer.git
cd system-one-reviewer
git checkout 9a73661dcd6a257501da10c73917df7eb69decae
# follow upstream README for install and system-one-reviewer --repo ... --range ...
```

Pin revision `9a73661dcd6a257501da10c73917df7eb69decae` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Advisory only. Live review/eval not run on the review host. Diff text is sent to the configured provider when live.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 9a73661](https://github.com/equationalapplications/system-one-reviewer/tree/9a73661dcd6a257501da10c73917df7eb69decae). AI-assisted README and LICENSE inspection; install/live paths not executed.
