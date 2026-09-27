# jev-switch

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local-first gateway for aggregating and routing TypeSafe Jev–compatible model endpoints.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ARCJ137442/jev-switch) |
| Maintainer | [ARCJ137442](https://github.com/ARCJ137442). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust daemon + React console + optional Tauri desktop shell. |
| Requirements | Rust toolchain / Docker for the daemon; Node for the UI; upstream provider credentials stay in the daemon. |
| License | [Apache-2.0](https://github.com/ARCJ137442/jev-switch/blob/6b01d0a1baffdd8a40d5db59a0720191fac8317f/LICENSE-APACHE). Dual-licensed; Apache-2.0 SPDX on GitHub (`LICENSE-APACHE` / `LICENSE-MIT`). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to front multiple System One–compatible upstreams behind one local `/v1/systemone` with inspectable routing. Prefer direct SDK calls for a single hosted endpoint.

## How it works

Gateway accepts Jev-shaped requests, plans a route DAG, and translates to upstream dialects; it does not load model weights. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ARCJ137442/jev-switch.git
cd jev-switch
git checkout 6b01d0a1baffdd8a40d5db59a0720191fac8317f
# follow upstream README / Docker Compose
```

Pin revision `6b01d0a1baffdd8a40d5db59a0720191fac8317f` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

v0.1 lacks native TypeSafe and OpenRouter adapters (roadmap). Dual license files. Install/live paths not run on the review host. Distinct from jev-switchboard.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 6b01d0a](https://github.com/ARCJ137442/jev-switch/tree/6b01d0a1baffdd8a40d5db59a0720191fac8317f). AI-assisted README and LICENSE inspection; install/live paths not executed.
