# LLM Gateway by sxueck (self-hosted LLM gateway with a web UI whose tiered router uses a Jev choice to send each request to a low, medium or high model tier; Chinese and English)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Self-hosted LLM gateway with a web UI for managing providers, virtual keys, routing and models. Its tiered (formerly expert) router asks Jev one `choice` question to sort each request into a low, medium or high difficulty tier, each with its own ordered candidate models. The response carries headers naming the routed model, tier and route source (`jev`, `session`, `fallback`, `fail_open`, `manual` or `cache`). The README is in Chinese with an English copy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sxueck/llm-gateway) |
| Maintainer | [sxueck](https://github.com/sxueck). Independently curated. |
| Format | Bun and TypeScript service with a web UI (Docker image) |
| Requirements | Bun, a database as described in the README, and server-side `JEV_API_URL`, `JEV_API_KEY` and `JEV_MODEL` settings for Jev routing. |
| License | [MIT](https://github.com/sxueck/llm-gateway/blob/cc9a8b0ea602f8d17a403ef188a3ccb10f4d7422/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/backend/src/services/expert-router/jev-client.ts`](https://github.com/sxueck/llm-gateway/blob/cc9a8b0ea602f8d17a403ef188a3ccb10f4d7422/packages/backend/src/services/expert-router/jev-client.ts) at the pinned commit. |

## When to use

- Send easy requests to cheap models and hard ones to strong models through a gateway you host.
- Mismatch: Jev routing is one optional feature of a larger gateway, and it must be enabled with at least one candidate model.

## How it works

`packages/backend/src/services/expert-router/jev-client.ts` calls the configured System One URL (`https://api.typesafe.ai/v1/systemone` or OpenRouter) with an 800 ms default timeout and a circuit breaker that opens after three failures; failures and missing candidates follow the fail-open chain. Integration evidence: [`packages/backend/src/services/expert-router/jev-client.ts`](https://github.com/sxueck/llm-gateway/blob/cc9a8b0ea602f8d17a403ef188a3ccb10f4d7422/packages/backend/src/services/expert-router/jev-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sxueck/llm-gateway.git
cd llm-gateway
bun install
bun run dev:all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese) with the tiered-router section: [github.com/sxueck/llm-gateway#readme](https://github.com/sxueck/llm-gateway#readme)
- English README: [github.com/sxueck/llm-gateway/blob/cc9a8b0ea602f8d17a403ef188a3ccb10f4d7422/README_EN.md](https://github.com/sxueck/llm-gateway/blob/cc9a8b0ea602f8d17a403ef188a3ccb10f4d7422/README_EN.md)

## Limits and data handling

Request text sent to the classifier goes to TypeSafe or OpenRouter with the server-side key; keep the key out of the frontend. The README's token-volume claim is the author's own. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit cc9a8b0ea602](https://github.com/sxueck/llm-gateway/tree/cc9a8b0ea602f8d17a403ef188a3ccb10f4d7422). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
