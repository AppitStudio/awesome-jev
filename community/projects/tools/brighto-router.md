# BrighTO Router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted Rust LLM gateway with System One / Jev decision routes, load balancing, and team budgets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thusinh1969/BrighTO_Router) |
| Maintainer | [thusinh1969](https://github.com/thusinh1969). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust LLM gateway / router with Docker image and portal. |
| Requirements | Docker or Rust binary; PostgreSQL; upstream provider keys for configured routes. |
| License | [Apache-2.0](https://github.com/thusinh1969/BrighTO_Router/blob/0713d8129a6fcd9699b03fa91d235bd422171671/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when you want a self-hosted gateway that can route both LLM chat and System One / Jev-style decision traffic.

## How it works

Proxies chat/embeddings/media and System One decision endpoints; records usage metadata (not prompts) and supports model groups with fallback routing. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/thusinh1969/BrighTO_Router.git
cd BrighTO_Router
git checkout 0713d8129a6fcd9699b03fa91d235bd422171671
# follow upstream README / ./start.sh install; configure routes and keys as documented
```

Pin revision `0713d8129a6fcd9699b03fa91d235bd422171671` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Self-hosted traffic path; not a hosted agent platform. Live provider traffic not run on the review host.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 0713d81](https://github.com/thusinh1969/BrighTO_Router/tree/0713d8129a6fcd9699b03fa91d235bd422171671). AI-assisted README and LICENSE inspection; install/live paths not executed.
