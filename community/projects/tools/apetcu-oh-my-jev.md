# oh-my-jev (apetcu)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-powered tool-call gate, model router, and latency telemetry for the oh-my-pi coding agent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/apetcu/oh-my-jev) |
| Maintainer | [apetcu](https://github.com/apetcu). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | oh-my-pi / omp plugin. |
| Requirements | oh-my-pi (omp); Bun; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/apetcu/oh-my-jev/blob/7bdecf93a0ff40258de33afdfe0573bdef005aa6/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from MassiveLabsNet/oh-my-jev. |

## When to use

Use when oh-my-pi should gate ambiguous tool calls with TypeSafe Jev while keeping deterministic allow/ask paths.

## How it works

Gate triages tool calls with deterministic fast paths plus Jev risk scoring for the ambiguous middle; optional router and JSONL telemetry. Distinct from MassiveLabsNet/oh-my-jev. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/apetcu/oh-my-jev.git
cd oh-my-jev
git checkout 7bdecf93a0ff40258de33afdfe0573bdef005aa6
# or: omp install github:apetcu/oh-my-jev
# export TYPESAFE_API_KEY; follow upstream README
```

Pin revision `7bdecf93a0ff40258de33afdfe0573bdef005aa6` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Designed for omp yolo approval mode. Live paths not run on the review host. Distinct from MassiveLabsNet/oh-my-jev.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 7bdecf9](https://github.com/apetcu/oh-my-jev/tree/7bdecf93a0ff40258de33afdfe0573bdef005aa6). AI-assisted README and LICENSE inspection; install/live paths not executed.
