# jevx (muthuishere)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Give your coding agent a fast, typed gut feeling—yes/no, pick-one, and rating answers from a System One model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muthuishere/jevx) |
| Maintainer | [muthuishere](https://github.com/muthuishere). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go CLI, npm package, and agent skill for Claude Code/Codex. |
| Requirements | Go/npm per install path; System One endpoint credentials in environment variables. |
| License | [MIT](https://github.com/muthuishere/jevx/blob/67ed9a6277fae8f4211ba358064b606174f3cd58/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from hawkyre/jevx (browser extension). |

## When to use

Use when Claude Code/Codex should offload small typed judgments to System One via a skill/CLI.

## How it works

Skill + CLI ask named typed questions with exit-code contracts; optional hook plugins start in shadow mode. Distinct from hawkyre/jevx (X draft extension). Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/muthuishere/jevx.git
cd jevx
git checkout 67ed9a6277fae8f4211ba358064b606174f3cd58
# or: npm i -g @muthuishere/jevx
# follow https://muthuishere.github.io/jevx/ for skill install
```

Pin revision `67ed9a6277fae8f4211ba358064b606174f3cd58` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live System One paths not run on the review host. Distinct from hawkyre/jevx browser extension.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 67ed9a6](https://github.com/muthuishere/jevx/tree/67ed9a6277fae8f4211ba358064b606174f3cd58). AI-assisted README and LICENSE inspection; install/live paths not executed.
