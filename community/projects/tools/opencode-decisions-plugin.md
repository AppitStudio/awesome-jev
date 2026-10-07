# OpenCode Decisions plugin

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode V2 plugin exposing a `decisions_evaluate` tool so an agent can ask typed questions of Jev (text, through OpenCode Console's Jev models) or OpenAI Decisions (text and images); the agent keeps the taxonomy and interprets the probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/matthewpetela/opencode-decisions-plugin) |
| Maintainer | [matthewpetela](https://github.com/matthewpetela). Independently curated. |
| Format | OpenCode V2 plugin installed from GitHub (`opencode plugin add`), single `index.js` |
| Requirements | OpenCode v2.0.0+; an OpenCode Console API key for Jev (`jev-1.13`, or the limited-time `jev-1.13-free`) or an OpenAI API key for Decisions. |
| License | [MIT](https://github.com/matthewpetela/opencode-decisions-plugin/blob/d8ace9f189e2412ed3b28df13acf11fdcbea5fe3/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give an OpenCode agent a cheap typed judgment (choice, noul, score) instead of free-text classification.
- Switch to OpenAI Decisions when the input includes images.
- Mismatch: Jev is reached through OpenCode Console's hosted models, not TypeSafe's API directly; the legacy `jev_jev_evaluate` tool id is kept for older agents.

## How it works

[`index.js`](https://github.com/matthewpetela/opencode-decisions-plugin/blob/d8ace9f189e2412ed3b28df13acf11fdcbea5fe3/index.js) registers the tool and forwards provider-native questions to OpenCode Console's Jev endpoint or OpenAI `/v1/decisions`, returning answers and probabilities to the agent. Multi-label behaviour and options are documented in the README.

## Get started

Install with OpenCode's plugin manager (README *Install*):

```sh
opencode plugin add github:matthewpetela/opencode-decisions-plugin
opencode plugin list
```

Upstream lists `jev-1.13` at $0.042 per million input tokens (output free) and a limited-time free `jev-1.13-free` via OpenCode Console; OpenAI Decisions is billed by OpenAI. Pricing may change.

## Examples and demos

- README *Usage: Decisions tool* (Jev text default, OpenAI text or image, multiple choice, noul and score).
- README *Models and cost*.

## Limits and data handling

Content the agent passes to the tool goes to OpenCode Console (Jev) or OpenAI. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit d8ace9f189e2](https://github.com/matthewpetela/opencode-decisions-plugin/tree/d8ace9f189e2412ed3b28df13acf11fdcbea5fe3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
