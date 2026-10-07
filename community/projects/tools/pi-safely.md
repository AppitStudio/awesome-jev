# pi-safely

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi package that re-implements the core of Claude Code's auto mode for the Pi agent, gating every non-allowlisted tool call through a System One decision model — Jev (TypeSafe or OpenRouter), Cloudflare Clef or any `POST /v1/systemone` backend — that returns calibrated yes/no probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dcowsill/pi-safely) |
| Maintainer | [dcowsill](https://github.com/dcowsill). Independently curated. |
| Format | Pi package (`pi install` from Git, tagged refs such as v0.3.0) |
| Requirements | Pi agent; an OpenRouter key (default, provider must be allowed for TypeSafe/Cloudflare) or a TypeSafe key via Pi's `/login`. |
| License | [MIT](https://github.com/dcowsill/pi-safely/blob/b42c7525f1c380affc997b68db6dfd8e583a736c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give Pi a Claude Code-style auto mode without writing your own permission classifier.
- Reuse an existing Claude project allowlist (interoperability documented upstream).
- Mismatch: upstream lists known gaps versus the official Claude Code auto mode.

## How it works

[`extensions/safely.ts`](https://github.com/dcowsill/pi-safely/blob/b42c7525f1c380affc997b68db6dfd8e583a736c/extensions/safely.ts) intercepts tool calls; allowlisted ones pass, others go to [`src/system-one-classifier.ts`](https://github.com/dcowsill/pi-safely/blob/b42c7525f1c380affc997b68db6dfd8e583a736c/src/system-one-classifier.ts), which asks the configured backend yes/no questions and blocks or allows by threshold. Configuration example: [`safely.example.json`](https://github.com/dcowsill/pi-safely/blob/b42c7525f1c380affc997b68db6dfd8e583a736c/safely.example.json).

## Get started

Install into Pi:

```sh
pi install https://github.com/dcowsill/pi-safely.git
# then /login → TypeSafe AI (or use Pi's OpenRouter key)
```

Each gated tool call is a request billed to your OpenRouter, TypeSafe or Cloudflare account.

## Examples and demos

- README *Usage*, *UI additions* and *Configuration*.
- README *Known gaps vs official Claude Code auto mode*.

## Limits and data handling

Tool-call details are sent to the chosen classifier backend. The TypeSafe key is stored by Pi in `~/.pi/agent/auth.json` (0600, upstream). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b42c7525f1c3](https://github.com/dcowsill/pi-safely/tree/b42c7525f1c380affc997b68db6dfd8e583a736c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
