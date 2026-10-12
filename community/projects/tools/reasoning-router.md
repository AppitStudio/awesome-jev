# reasoning-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Per-step reasoning effort for coding agents picked by a classifier (TypeSafe Jev by default in examples) without breaking the prompt cache; ships an OpenCode plugin, a Pi extension and a local proxy for Codex CLI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/robertn702/reasoning-router) |
| Maintainer | [robertn702](https://github.com/robertn702). Independently curated. |
| Format | OpenCode plugin · Pi extension · Codex proxy |
| Requirements | Node.js; classifier key (Jev via `REASONING_ROUTER_CLASSIFIER_API_KEY`). |
| License | [MIT](https://github.com/robertn702/reasoning-router/blob/f976d0194533806eb90b54716523c29cd9a19110/LICENSE) |
| Jev evidence | [`packages/classifiers/src`](https://github.com/robertn702/reasoning-router/tree/f976d0194533806eb90b54716523c29cd9a19110/packages/classifiers/src) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Cut output tokens on easy steps while keeping hard steps at high effort, without switching models.
- Mismatch: author SWE-bench numbers are self-reported; Clef and other classifiers are also supported.

## How it works

Before each step a classifier scores difficulty and the harness sets reasoning effort only, leaving model and cache stable; eval scripts live in `eval/`. (Summarized from the upstream [README](https://github.com/robertn702/reasoning-router/blob/f976d0194533806eb90b54716523c29cd9a19110/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): pick a harness section in the README and configure `"classifier": { "provider": "jev" }`.

## Limits and data handling

Step context goes to the chosen classifier provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit f976d0194533](https://github.com/robertn702/reasoning-router/tree/f976d0194533806eb90b54716523c29cd9a19110). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
