# Jev review gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Actions gate: local rules + TypeSafe Jev questions on the diff; exits 0/1 (does not merge).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RomanXSad/jev-review-gate) |
| Maintainer | [RomanXSad](https://github.com/RomanXSad). Independently curated. |
| Format | GitHub Action that asks TypeSafe Jev over a diff/rule pack and exits 0/1. |
| Requirements | GitHub Actions; TypeSafe API key as secret; rule pack in repo. |
| License | [MIT](https://github.com/RomanXSad/jev-review-gate/blob/0d066d49ff8328e3e551d08d06e711e802774a0c/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use to block deploy jobs until Jev/rule-pack checks pass. Prefer human review for large/sensitive diffs (upstream notes limits).

## How it works

Action posts typed questions to api.typesafe.ai/v1/systemone (jev-latest). Jev does not merge or push.

## Get started

```sh
git clone https://github.com/RomanXSad/jev-review-gate.git
cd jev-review-gate
git checkout 0d066d49ff8328e3e551d08d06e711e802774a0c
# add Action + TYPESAFE_API_KEY secret per upstream
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 0d066d4](https://github.com/RomanXSad/jev-review-gate/tree/0d066d49ff8328e3e551d08d06e711e802774a0c). AI-assisted README and license inspection; install/live paths not executed.
