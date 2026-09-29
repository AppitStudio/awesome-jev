# jev-router (FrancoisChastel)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Route each coding-agent turn to the cheapest model that can finish it—Switchyard-style signals with TypeSafe Jev as judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FrancoisChastel/jev-router) |
| Maintainer | [FrancoisChastel](https://github.com/FrancoisChastel). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm CLI/relay (`@french-castle/jev-router`) with harness plugins. |
| Requirements | Node; OpenRouter or Vercel AI Gateway key (and/or `TYPESAFE_API_KEY`); Claude Code/Codex/OpenCode/Pi. |
| License | [MIT](https://github.com/FrancoisChastel/jev-router/blob/431fc64e5a349533aa125e9313ba994a2c459f0c/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [jev-router (gargpratyush)](jev-router.md), [JevRoute (suncirkles)](suncirkles-jev-router.md), and [jev-router (peptidehackers)](peptidehackers-jev-router.md). |

## When to use

Use when Claude Code/Codex/OpenCode/Pi should auto-pick cheaper models per turn with an honest cost ledger. Prefer other routers if you already pin a different policy stack.

## How it works

Sits between the harness and gateway; hard overrides, holds, tool signals, then a bounded Jev judge; policy maps answers to tier/effort. Fails open. Distinct from gargpratyush/jev-router and other jev-router owners. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/FrancoisChastel/jev-router.git
cd jev-router
git checkout 431fc64e5a349533aa125e9313ba994a2c459f0c
# or: npm install -g @french-castle/jev-router && jev-router setup
```

Pin revision `431fc64e5a349533aa125e9313ba994a2c459f0c` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live relay/judge traffic not run on the review host. Cost comparisons are local/log-based when configured. Distinct from other jev-router listings.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 431fc64](https://github.com/FrancoisChastel/jev-router/tree/431fc64e5a349533aa125e9313ba994a2c459f0c). AI-assisted README and LICENSE inspection; install/live paths not executed.
