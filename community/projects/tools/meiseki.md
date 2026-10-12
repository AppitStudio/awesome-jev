# meiseki

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent Skill / Claude Code and Codex plugin that rewrites AI-written Japanese documents for clarity; since v0.9.0 an optional TypeSafe Jev layer takes over the context judgments an LLM used to make (reported 23 s → 0.3 s on 20 questions).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bamboo-nova/meiseki) |
| Maintainer | [bamboo-nova](https://github.com/bamboo-nova). Independently curated. |
| Format | Agent Skill · Claude Code / Codex plugin |
| Requirements | Node.js; Claude Code or Codex; TypeSafe key optional (without it the LLM path runs as before). |
| License | [MIT](https://github.com/bamboo-nova/meiseki/blob/a6cac6e2cabe1d39a0c079a898749311c7fadbf5/LICENSE) |
| Jev evidence | [`experiments/jev-benchmark`](https://github.com/bamboo-nova/meiseki/tree/a6cac6e2cabe1d39a0c079a898749311c7fadbf5/experiments/jev-benchmark) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Make AI-generated Japanese docs readable in one pass, with cheap typed checks replacing slow LLM context calls.
- Mismatch: Japanese-only; Jev layer is optional and falls back to the LLM when unsure or keyless.

## How it works

Three layers: textlint-style rules flag spans, Jev decides context-dependent findings with high confidence, and uncertain cases go to the LLM; a send-blocking policy setting is included. Benchmarks with reproduction steps live in `experiments/jev-benchmark`. (Summarized from the upstream [README](https://github.com/bamboo-nova/meiseki/blob/a6cac6e2cabe1d39a0c079a898749311c7fadbf5/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): register the bundled `.claude-plugin/marketplace.json` as a marketplace, then install the plugin by name (see README.en.md).

## Limits and data handling

With a key set, document spans go to TypeSafe; a policy option can block sending. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit a6cac6e2cabe](https://github.com/bamboo-nova/meiseki/tree/a6cac6e2cabe1d39a0c079a898749311c7fadbf5). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
