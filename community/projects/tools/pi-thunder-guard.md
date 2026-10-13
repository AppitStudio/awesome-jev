# pi-thunder-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Safety guard for Pi: before each bash call (and writes outside the repo) TypeSafe Jev must be at least 85% sure the call keeps to a short restriction list, or it is blocked with guidance.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mandalorian007/pi-thunder-guard) |
| Maintainer | [Mandalorian007](https://github.com/Mandalorian007). Independently curated. |
| Format | Pi extension |
| Requirements | Pi; TypeSafe key (`typesafe` in Pi auth or `TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/Mandalorian007/pi-thunder-guard/blob/9eaecc16862223bac257bc8b316d19281646c188/LICENSE) |
| Jev evidence | [`index.ts`](https://github.com/Mandalorian007/pi-thunder-guard/blob/9eaecc16862223bac257bc8b316d19281646c188/index.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Stop agent mistakes from deleting files or touching paths outside the workspace.
- Mismatch: guards against mistakes, not a determined adversarial agent.

## How it works

Each bash command (and outside-workspace write/edit) is sent to Jev with the restriction list; below threshold the call is blocked and the model is told which restriction was in doubt. (Summarized from the upstream [README](https://github.com/Mandalorian007/pi-thunder-guard/blob/9eaecc16862223bac257bc8b316d19281646c188/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `pi install git:github.com/Mandalorian007/pi-thunder-guard` (pin `@v0.2.2`).

## Limits and data handling

Commands and file paths go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 9eaecc168622](https://github.com/Mandalorian007/pi-thunder-guard/tree/9eaecc16862223bac257bc8b316d19281646c188). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
