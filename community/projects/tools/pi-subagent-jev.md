# pi-subagent-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

pi package that gates subagent dispatches through a Jev System One decision model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/G0-0000/pi-subagent-jev) |
| Maintainer | [G0-0000](https://github.com/G0-0000). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | pi coding-agent package + bundled skill. |
| Requirements | pi with pi-subagents; reachable System One / Jev endpoint and API key (`~/.config/jev-comp/env`). |
| License | [MIT](https://github.com/G0-0000/pi-subagent-jev/blob/3a4c31b8105ed7845e4f844faef7ff217c1f5dd5/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when pi subagent launches should pass a System One compliance gate before spawn.

## How it works

Hooks the pi-subagents `subagent` tool; blocked dispatches return violations without spawning. Also exposes general jev_ask/jev_models tools. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/G0-0000/pi-subagent-jev.git
cd pi-subagent-jev
git checkout 3a4c31b8105ed7845e4f844faef7ff217c1f5dd5
# or: pi install git:github.com/G0-0000/pi-subagent-jev
# configure ~/.config/jev-comp/env per upstream README
```

Pin revision `3a4c31b8105ed7845e4f844faef7ff217c1f5dd5` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Currently supports pi + pi-subagents only. Live endpoint paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 3a4c31b](https://github.com/G0-0000/pi-subagent-jev/tree/3a4c31b8105ed7845e4f844faef7ff217c1f5dd5). AI-assisted README and LICENSE inspection; install/live paths not executed.
