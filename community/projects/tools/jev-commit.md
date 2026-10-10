# jev-commit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

pre-commit hook that makes one Jev call per commit to judge whether the commit message matches the staged diff, and flags filler messages, debug leftovers, unmentioned work and secret-shaped lines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valentynkit/jev-commit) |
| Maintainer | [valentynkit](https://github.com/valentynkit). Independently curated. |
| Format | pre-commit `commit-msg` hook |
| Requirements | pre-commit; TypeSafe API key. |
| License | [MIT](https://github.com/valentynkit/jev-commit/blob/e2bd64adfb820d5a11ea23ea71a2e7e243c305fb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch agent-written commit messages that do not match the code.
- Mismatch: warns rather than blocks, except for credential-shaped added lines; the staged diff is sent to a hosted API.

## How it works

The message and staged diff are sent together as five Jev questions in one request; high scores are reported as findings. (Summarized from the upstream [README](https://github.com/valentynkit/jev-commit/blob/e2bd64adfb820d5a11ea23ea71a2e7e243c305fb/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Add the repo to `.pre-commit-config.yaml` and run `pre-commit install --hook-type commit-msg`.

## Limits and data handling

Commit message and staged diff are sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit e2bd64adfb82](https://github.com/valentynkit/jev-commit/tree/e2bd64adfb820d5a11ea23ea71a2e7e243c305fb). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
