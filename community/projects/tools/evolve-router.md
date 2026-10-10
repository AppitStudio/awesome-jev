# EvolveRoute

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first LLM routing gateway (single Rust binary) that sits between your coding agents and LLM providers and routes each request to the most suitable model, judged per request by TypeSafe Jev plus a heuristic second opinion, with a feedback flywheel and an auditable JSONL decision log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/holny/evolve-router) |
| Maintainer | [holny](https://github.com/holny). Independently curated. |
| Format | Rust binary gateway (OpenAI/Anthropic-compatible) with a local dashboard |
| Requirements | Rust toolchain to build; your LLM provider keys; TypeSafe API key for Jev routing (heuristic fallback without it). |
| License | [MIT](https://github.com/holny/evolve-router/blob/cc664e71b164e9778ad66c862e2ec5461bede2ac/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Route agent traffic across several providers and subscription plans with traceable per-request decisions.
- Mismatch: young project; routing quality claims come from the maintainer, not verified here.

## How it works

Jev judges each request's task profile against provider capabilities and quotas; a heuristic takes the conservative side and takes over when Jev is unavailable, so routing never blocks. (Summarized from the upstream [README](https://github.com/holny/evolve-router/blob/cc664e71b164e9778ad66c862e2ec5461bede2ac/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Build the binary per the README, point your agent's base URL at the gateway, and configure providers.

## Limits and data handling

README states user data stays on the host apart from calls to your configured providers and TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit cc664e71b164](https://github.com/holny/evolve-router/tree/cc664e71b164e9778ad66c862e2ec5461bede2ac). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
