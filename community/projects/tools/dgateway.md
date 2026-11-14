# dgateway (self-hosted gateway that puts Jev, OpenAI decisions, OpenRouter, Ollama and vLLM behind one classification, yes/no and score API)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted gateway with a web console: your app calls one API for categories, yes/no answers and scores, and you choose providers and models behind it (a TypeSafe provider for Jev is seeded but disabled until you add a key), with routing, provider health, request charts and cost tracking. Provider keys are stored encrypted.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BuddyLabsAI/dgateway) |
| Maintainer | [BuddyLabsAI](https://github.com/BuddyLabsAI). Independently curated. |
| Format | Docker image and Bun/TypeScript service with web console (MIT) |
| Requirements | Docker (or Bun), an admin token and gateway secret, and keys for the providers you enable (`TYPESAFE_API_KEY` for Jev). |
| License | [MIT](https://github.com/BuddyLabsAI/dgateway/blob/117163cba53c46c48d3671c4d19d1d6cd963b1ab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/modules/gateway/libs/management/functions/seed.ts`](https://github.com/BuddyLabsAI/dgateway/blob/117163cba53c46c48d3671c4d19d1d6cd963b1ab/src/modules/gateway/libs/management/functions/seed.ts) at the pinned commit. |

## When to use

- Switch decision-model providers (including Jev) without changing application code.
- Mismatch: a managed service; you run, secure and update the gateway yourself.

## How it works

`seed.ts` defines the seeded `typesafe` provider with base URL `https://api.typesafe.ai`, key from `TYPESAFE_API_KEY`, and the `jev-1.14` model with its input price; it starts disabled. Requests are forwarded to whichever provider a model route points to. Integration evidence: [`src/modules/gateway/libs/management/functions/seed.ts`](https://github.com/BuddyLabsAI/dgateway/blob/117163cba53c46c48d3671c4d19d1d6cd963b1ab/src/modules/gateway/libs/management/functions/seed.ts).

## Get started

Start the container bound to localhost, then add and test providers in the console.

```sh
docker run -d --name dgateway -p 127.0.0.1:8790:8790 -v dgateway-data:/data \
  -e ADMIN_TOKEN=replace-me -e GATEWAY_SECRET=replace-me-too \
  ghcr.io/buddylabsai/dgateway:latest
# open http://127.0.0.1:8790/ → Providers → typesafe → add key, Test, enable
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BuddyLabsAI/dgateway/blob/117163cba53c46c48d3671c4d19d1d6cd963b1ab/README.md](https://github.com/BuddyLabsAI/dgateway/blob/117163cba53c46c48d3671c4d19d1d6cd963b1ab/README.md)
- Container: [github.com/BuddyLabsAI/dgateway/pkgs/container/dgateway](https://github.com/BuddyLabsAI/dgateway/pkgs/container/dgateway)

## Limits and data handling

Prompts pass through your gateway to the providers you enable, on your keys. Replace the default admin token and secret before any non-local use, and keep `GATEWAY_SECRET` stable because it encrypts stored provider keys.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 117163cba53c](https://github.com/BuddyLabsAI/dgateway/tree/117163cba53c46c48d3671c4d19d1d6cd963b1ab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
