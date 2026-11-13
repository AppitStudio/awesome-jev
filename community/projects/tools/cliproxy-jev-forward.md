# cliproxy-embeddings-rerank-forward (CLIProxyAPI plugin that forwards Jev decision requests, embeddings and rerank to upstream providers)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Native Go plugin for CLIProxyAPI that adds management routes for OpenAI-style embeddings, Cohere-style rerank, Jev through OpenRouter's Decisions API and Jev through TypeSafe's System One API, with model aliases, several providers per route and key failover on 429 or 5xx.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KorenKrita/cliproxy-embeddings-rerank-forward) |
| Maintainer | [KorenKrita](https://github.com/KorenKrita). Independently curated. |
| Format | Go shared-library plugin for CLIProxyAPI (MIT) |
| Requirements | Go to build, a running CLIProxyAPI, and upstream keys (for example a TypeSafe key) entered in the plugin config. |
| License | [MIT](https://github.com/KorenKrita/cliproxy-embeddings-rerank-forward/blob/ffa556e5bcfa7816d2849701864c5a678705e0f5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`main.go`](https://github.com/KorenKrita/cliproxy-embeddings-rerank-forward/blob/ffa556e5bcfa7816d2849701864c5a678705e0f5/main.go) at the pinned commit. |

## When to use

- Put Jev, embeddings and rerank behind the same CLIProxyAPI gateway your tools already use.
- Fail over between several upstream keys or providers.
- Mismatch: if you don't run CLIProxyAPI.

## How it works

`main.go` registers `/v0/management/v1/systemone` (default upstream `https://api.typesafe.ai/v1/systemone`) and `/v0/management/decisions` and forwards request and response bodies unchanged after matching `body.model` to a provider. Upstream keys come from plugin configuration and are never taken from the inbound Authorization header, which carries the CLIProxyAPI management key. Integration evidence: [`main.go`](https://github.com/KorenKrita/cliproxy-embeddings-rerank-forward/blob/ffa556e5bcfa7816d2849701864c5a678705e0f5/main.go).

## Get started

Build the shared library, place it in your CLIProxyAPI plugins directory, then fill in the upstream URLs, keys and models in the management UI.

```sh
go build -buildmode=c-shared -o embeddings-forward.so .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with config reference: [github.com/KorenKrita/cliproxy-embeddings-rerank-forward/blob/ffa556e5bcfa7816d2849701864c5a678705e0f5/README.md](https://github.com/KorenKrita/cliproxy-embeddings-rerank-forward/blob/ffa556e5bcfa7816d2849701864c5a678705e0f5/README.md)

## Limits and data handling

Requests pass through your CLIProxyAPI host to the upstreams you configure; keys are stored in the plugin config on that host.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit ffa556e5bcfa](https://github.com/KorenKrita/cliproxy-embeddings-rerank-forward/tree/ffa556e5bcfa7816d2849701864c5a678705e0f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
