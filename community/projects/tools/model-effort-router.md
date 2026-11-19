# model-effort-router by cmdaltctr (Claude Code mod where Jev picks the reasoning effort and subagent models for each task)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that asks Jev to rate each prompt, then sets the reasoning effort of the main conversation and the model and effort of each subagent when it starts, and shows what was sent (for example `Opus 5.5 / low`) in the prompt footer. Supports delegation to cheaper subagents, an effort ceiling, per-chat commands and naming a model or effort yourself. Installs from its own plugin marketplace with auto-update.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cmdaltctr/model-effort-router) |
| Maintainer | [cmdaltctr](https://github.com/cmdaltctr). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code, and either a TypeSafe API key (`typesafeApiKey`) or a Vercel AI Gateway key for Jev. |
| License | [MIT](https://github.com/cmdaltctr/model-effort-router/blob/0a921db1bbd43d6efc2f14c64934d51d5910caa1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/router.ts`](https://github.com/cmdaltctr/model-effort-router/blob/0a921db1bbd43d6efc2f14c64934d51d5910caa1/hooks/router.ts) at the pinned commit. |

## When to use

- Stop paying top-tier effort on simple Claude Code turns without switching models by hand.
- Mismatch: other coding agents; it targets Claude Code's mod and hook system.

## How it works

`hooks/router.ts` sends each prompt to Jev, preferring TypeSafe's own API (for its calibrated confidence) over the AI Gateway when both keys are set; `hooks/policy.ts` maps the answers to effort levels and subagent models. Integration evidence: [`hooks/router.ts`](https://github.com/cmdaltctr/model-effort-router/blob/0a921db1bbd43d6efc2f14c64934d51d5910caa1/hooks/router.ts).

## Get started

Install from the plugin marketplace, pick a scope and set a backend key in the plugin options.

```sh
claude plugin install model-effort-router --marketplace cmdaltctr/model-effort-router
# then set typesafeApiKey (or an AI Gateway key) in the plugin options
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cmdaltctr/model-effort-router/blob/0a921db1bbd43d6efc2f14c64934d51d5910caa1/README.md](https://github.com/cmdaltctr/model-effort-router/blob/0a921db1bbd43d6efc2f14c64934d51d5910caa1/README.md)

## Limits and data handling

Prompt text goes to TypeSafe or the AI Gateway on your key. Routing choices are advice applied by the mod; quality trade-offs are not measured here.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 0a921db1bbd4](https://github.com/cmdaltctr/model-effort-router/tree/0a921db1bbd43d6efc2f14c64934d51d5910caa1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
