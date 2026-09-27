# jev-guard (yelkhanyergali-sys)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

PI Mono extension for prompt-cache-safe terminal pruning and surgical diff guards powered by Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yelkhanyergali-sys/jev-guard) |
| Maintainer | [yelkhanyergali-sys](https://github.com/yelkhanyergali-sys). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | JavaScript PI Mono extension with tests. |
| Requirements | Node.js ≥ 18; PI Mono; `TYPESAFE_API_KEY` for live Jev paths. |
| License | [MIT](https://github.com/yelkhanyergali-sys/jev-guard/blob/fee2b16565eb68bfd9e3b3c93bd1bfab826e2e1e/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when PI Mono sessions drown in build/test logs or need a pre-review diff risk check. Prefer other guards for Claude Code/OpenCode hosts.

## How it works

Hooks send terminal/diff context to TypeSafe Jev for keep/drop and risk judgments; application policy owns thresholds. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/yelkhanyergali-sys/jev-guard.git
cd jev-guard
git checkout fee2b16565eb68bfd9e3b3c93bd1bfab826e2e1e
# follow upstream README to install into PI Mono
```

Pin revision `fee2b16565eb68bfd9e3b3c93bd1bfab826e2e1e` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

PI Mono–specific; not a general LLM-app guardrails library (see rudra72r/jev-guard). Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit fee2b16](https://github.com/yelkhanyergali-sys/jev-guard/tree/fee2b16565eb68bfd9e3b3c93bd1bfab826e2e1e). AI-assisted README and LICENSE inspection; install/live paths not executed.
