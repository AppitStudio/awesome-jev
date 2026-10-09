# Jev Agent Control

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode V2 server plugin that uses TypeSafe Jev to route each request between Plan, Build, and your own primary agents, and to hand off unfinished work at completed execution boundaries while following each target agent's configured model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Krzysztof-Cieslak/jev-agent-control) |
| Maintainer | [Krzysztof-Cieslak](https://github.com/Krzysztof-Cieslak). Independently curated. |
| Format | OpenCode V2 plugin (npm `opencode-jev-agent-control`) |
| Requirements | OpenCode V2 (README: tested with 2.0.24); TypeSafe API key connected through OpenCode `/connect`. Local builds need Node.js 20+. |
| License | [MIT](https://github.com/Krzysztof-Cieslak/jev-agent-control/blob/43b26a54b0c76e8702347bbf5fc8c8cd78aff9b9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let Jev pick the right OpenCode primary agent for each request and continue work across agents automatically.
- Mismatch: OpenCode V2 only; every routed request is a hosted Jev call.

## How it works

The plugin asks Jev a typed choice over the configured primary agents for each request and, when `autoHandoff` is on, at completed execution boundaries. (Summarized from the upstream [README](https://github.com/Krzysztof-Cieslak/jev-agent-control/blob/43b26a54b0c76e8702347bbf5fc8c8cd78aff9b9/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Add `opencode-jev-agent-control` to the `plugins` list in `opencode.jsonc`, then run `opencode auth login typesafe --method key`.

## Limits and data handling

Request context is sent to TypeSafe for routing decisions under your account. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 43b26a54b0c7](https://github.com/Krzysztof-Cieslak/jev-agent-control/tree/43b26a54b0c76e8702347bbf5fc8c8cd78aff9b9). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
