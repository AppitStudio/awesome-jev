# jev-controller

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fail-open advisory workflow controller for OMP that asks Jev what to do after each tool result.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ac-kurniawan/jev-controller) |
| Maintainer | [ac-kurniawan](https://github.com/ac-kurniawan). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript library + OMP hook (`hooks/post/jev-controller.ts`). |
| Requirements | OMP coding agent; `TYPESAFE_API_KEY`; Node/TypeScript toolchain per upstream. |
| License | [MIT](https://github.com/ac-kurniawan/jev-controller/blob/5070ccdc860fa5439a3f8c291af95f3d73b22b85/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when an OMP agent needs a cheap fail-open nudge after tools. Prefer host-native routers for other agents.

## How it works

Builds a tool-result summary, calls `POST /v1/systemone` for a Choice verdict, and appends a directive only on actionable answers. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ac-kurniawan/jev-controller.git
cd jev-controller
git checkout 5070ccdc860fa5439a3f8c291af95f3d73b22b85
# install OMP hook per upstream README; export TYPESAFE_API_KEY=…
```

Pin revision `5070ccdc860fa5439a3f8c291af95f3d73b22b85` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

OMP adapter only in-repo; Hermes/OpenCode/Codex adapters not shipped. Live Jev calls not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 5070ccd](https://github.com/ac-kurniawan/jev-controller/tree/5070ccdc860fa5439a3f8c291af95f3d73b22b85). AI-assisted README and LICENSE inspection; install/live paths not executed.
