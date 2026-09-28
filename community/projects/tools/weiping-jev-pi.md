# jev-pi (weiping)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev for pi: TypeSafe System One judgments in the agent loop—permission gate, output ladder, conditional context, agent router.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/weiping/jev-pi) |
| Maintainer | [weiping](https://github.com/weiping). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | pi package (extensions + skills + prompts); npm `jev-pi`. |
| Requirements | pi; `TYPESAFE_API_KEY` (jev-1.13.0); TypeScript loaded via jiti. |
| License | [MIT](https://github.com/weiping/jev-pi/blob/6e39a421e770d65ebd301cb4381a3815ca195d37/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Pi port of weiping/jev-claude-code; distinct from other pi-jev-* routers. |

## When to use

Use when a pi coding agent should get the same Jev loop controls as weiping's Claude Code plugin.

## How it works

Pi port of weiping/jev-claude-code: extension hooks for bash permission/output, context injection, dispatch_agent routing, plus `/jev:*` commands and `jev_ask`. Shadow mode default. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/weiping/jev-pi.git
cd jev-pi
git checkout 6e39a421e770d65ebd301cb4381a3815ca195d37
# or: pi install npm:jev-pi
# pi -e npm:jev-pi for a one-off trial
```

Pin revision `6e39a421e770d65ebd301cb4381a3815ca195d37` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live pi/TypeSafe paths not run on the review host. Shadow mode default. Related to weiping/jev-claude-code.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 6e39a42](https://github.com/weiping/jev-pi/tree/6e39a421e770d65ebd301cb4381a3815ca195d37). AI-assisted README and LICENSE inspection; install/live paths not executed.
