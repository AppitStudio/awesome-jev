# Codex-Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VS Code Codex plugin that shortens noisy tool results with Jev-gated evidence selection before Codex reads them

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PhilippElhaus/Codex-Jev) |
| Maintainer | [PhilippElhaus](https://github.com/PhilippElhaus). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | VS Code Codex plugin / tooling. |
| Requirements | VS Code Codex; TypeSafe / provider keys per README. |
| License | [MIT](https://github.com/PhilippElhaus/Codex-Jev/blob/af025ccbce8d48fba8a7ac5811960a159b1bb354/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [codex-jev-router (suenot)](codex-jev-router-suenot.md) and [codex-jev-preflight](codex-jev-preflight.md). |

## When to use

Use when Codex tool dumps overwhelm context and you want Jev to keep selected evidence with a path back to the original. Prefer other Codex routers if you need model/effort routing instead of output gating.

## How it works

Gates/compacts tool output via Jev; uncertain results stay intact. Distinct from listed Codex-Jev routers/preflight tools. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/PhilippElhaus/Codex-Jev.git
cd Codex-Jev
git checkout af025ccbce8d48fba8a7ac5811960a159b1bb354
```

Pin revision `af025ccbce8d48fba8a7ac5811960a159b1bb354` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit af025cc](https://github.com/PhilippElhaus/Codex-Jev/tree/af025ccbce8d48fba8a7ac5811960a159b1bb354). AI-assisted README and LICENSE inspection; install/live paths not executed.
