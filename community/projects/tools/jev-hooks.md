# jev-hooks

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code commit-reviewer plugins driven by typed `/v1/systemone` decisions (self-hosted rizzo-flow or TypeSafe Jev) with a measured question bench.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/7hemas7er/jev-hooks) |
| Maintainer | [7hemas7er](https://github.com/7hemas7er). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code hook plugins + question bench. |
| Requirements | Claude Code; rizzo-flow or TypeSafe Jev endpoint/key. |
| License | [MIT](https://github.com/7hemas7er/jev-hooks/blob/aaf2839834dc8f19cda078027aea2617bbeb3795/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when Claude Code commits should get a typed-decision safety net. Prefer lighter linters for purely syntactic checks.

## How it works

PreToolUse Bash hook reviews the pending commit diff via `POST /v1/systemone`, then denies, asks, or adds context per policy; fail-open when the backend is down. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/7hemas7er/jev-hooks.git
cd jev-hooks
git checkout aaf2839834dc8f19cda078027aea2617bbeb3795
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `aaf2839834dc8f19cda078027aea2617bbeb3795` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit aaf2839834dc](https://github.com/7hemas7er/jev-hooks/tree/aaf2839834dc8f19cda078027aea2617bbeb3795). AI-assisted README and LICENSE inspection; install/live paths not executed.
