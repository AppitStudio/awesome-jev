# tinycomputer

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Rust Jev-based harness for desktop accessibility and browser automation (primitives, flows, and bounded tasks).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tinyhumansai/tinycomputer) |
| Maintainer | [tinyhumansai](https://github.com/tinyhumansai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust installable TinyBus module (`cdylib`) over vendored agent-desktop. |
| Requirements | Rust toolchain; host that loads TinyBus modules; TypeSafe Jev access for flows/tasks; desktop/browser permissions. |
| License | [GPL-3.0](https://github.com/tinyhumansai/tinycomputer/blob/60158ed864e6ab5aacb211e905f00f58cd82532f/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when an agent host needs Rust desktop+browser automation with Jev deciding small steps. Prefer lighter Playwright/MCP browser tools for web-only loops.

## How it works

Exposes typed desktop/browser primitives; Flows use TypeSafe Jev for live-screen decisions; Tasks run multi-step jobs with needs_input/approval/checkpoint stops (e.g. before payment). Facts stay local; Jev sees names not card data. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/tinyhumansai/tinycomputer.git
cd tinycomputer
git checkout 60158ed864e6ab5aacb211e905f00f58cd82532f
# follow upstream README / Cargo build for TinyBus host integration
```

Pin revision `60158ed864e6ab5aacb211e905f00f58cd82532f` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

GPL-3.0. Live desktop/browser/Jev paths not run on the review host. Tasks stop before payment; captchas need a human.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 60158ed](https://github.com/tinyhumansai/tinycomputer/tree/60158ed864e6ab5aacb211e905f00f58cd82532f). AI-assisted README and LICENSE inspection; install/live paths not executed.
