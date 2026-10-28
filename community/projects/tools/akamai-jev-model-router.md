# Jev Model Router by Akamai Developers (WebAssembly model router with Spin and TypeScript, Jev picking the model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Sample from Akamai's developer team: a single Spin WebAssembly component exposing `POST /ask` that asks Jev (via OpenRouter) which model should handle each prompt, forwards the prompt to that model on an Ollama instance and returns the answer. Accompanies the blog post "Build a Model Router with Jev, Spin & TypeScript".

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akamai-developers/jev-model-router) |
| Maintainer | [akamai-developers](https://github.com/akamai-developers). Independently curated. |
| Format | Spin WebAssembly component (TypeScript) |
| Requirements | Spin CLI v3+, Node.js 24+, an OpenRouter key and an Ollama instance. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision.ts`](https://github.com/akamai-developers/jev-model-router/blob/1e564a9c627dfeee60505e72b681ca2c8b917a69/src/decision.ts) at the pinned commit. |

## When to use

- Learn how to route prompts to local models with a decision model at the edge.
- Mismatch: a sample, not a product.

## How it works

`src/decision.ts` calls OpenRouter's Decisions API with `typesafe/jev-1.13` (set in `spin.toml`) and a Choice over the configured models. Integration evidence: [`src/decision.ts`](https://github.com/akamai-developers/jev-model-router/blob/1e564a9c627dfeee60505e72b681ca2c8b917a69/src/decision.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/akamai-developers/jev-model-router && cd jev-model-router
spin up --build --variable decition_model_api_key="$OPENROUTER_API_KEY" \
  --variable llm_endpoint="https://my-ollama:8080" --variable llm_api_key="$OLLAMA_KEY"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Blog post: [developers.akamai.com/blog/build-a-model-router-with-jev-spin-and-typescript/](https://developers.akamai.com/blog/build-a-model-router-with-jev-spin-and-typescript/)
- README: [github.com/akamai-developers/jev-model-router#readme](https://github.com/akamai-developers/jev-model-router#readme)

## Limits and data handling

Prompts go to OpenRouter for the routing decision and to your Ollama instance for the answer.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 1e564a9c627d](https://github.com/akamai-developers/jev-model-router/tree/1e564a9c627dfeee60505e72b681ca2c8b917a69). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
