# opencode-inference (OpenCode plugin giving agents decide, generate and models tools, with Jev as the default decision model)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

OpenCode V2 plugin that adds an `inference` Code Mode namespace: `decide` asks trained decision models (OpenRouter, Tinfoil) questions about some state and returns native probabilities, `generate` runs a one-turn tool-free sub-call on any registered model, and `models` lists what each supports so agents avoid failed calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rndmcnlly/opencode-inference) |
| Maintainer | [rndmcnlly](https://github.com/rndmcnlly). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode V2; an OpenRouter key for Jev (Tinfoil optional). |
| License | [MIT](https://github.com/rndmcnlly/opencode-inference/blob/eda465e70023f46bae48746db8ffc536f14e2eae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.ts`](https://github.com/rndmcnlly/opencode-inference/blob/eda465e70023f46bae48746db8ffc536f14e2eae/index.ts) at the pinned commit. |

## When to use

- Let an OpenCode agent get calibrated yes/no or choice answers mid-task.
- Mismatch: Jev is the default, not the only decision model.

## How it works

`index.ts` defaults `decide` to `openrouter/typesafe/jev-1.13` via OpenRouter's Decisions API (`https://openrouter.ai/api/alpha/decisions`). Integration evidence: [`index.ts`](https://github.com/rndmcnlly/opencode-inference/blob/eda465e70023f46bae48746db8ffc536f14e2eae/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/rndmcnlly/opencode-inference
# register the plugin in your OpenCode config (see README)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/rndmcnlly/opencode-inference#readme](https://github.com/rndmcnlly/opencode-inference#readme)

## Limits and data handling

State passed to `decide` goes to OpenRouter (and the model provider).

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit eda465e70023](https://github.com/rndmcnlly/opencode-inference/tree/eda465e70023f46bae48746db8ffc536f14e2eae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
