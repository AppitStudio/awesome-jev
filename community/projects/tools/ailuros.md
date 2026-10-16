# Ailuros

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ingress decision service for proxies: Envoy (`ext_proc`, `ext_authz`), NGINX `auth_request`, Traefik `ForwardAuth` and Envoy Gateway on Kubernetes send each request to Ailuros, which asks TypeSafe Jev or an OpenAI-compatible model, including local models, for an allow or block decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0x4272616e646f6e/ailuros) |
| Maintainer | [0x4272616e646f6e](https://github.com/0x4272616e646f6e). Independently curated. |
| Format | Go service (Docker image) |
| Requirements | Docker; a TypeSafe API key for the Jev backend, or an OpenAI-compatible endpoint. |
| License | [Apache-2.0](https://github.com/0x4272616e646f6e/ailuros/blob/b61daa74096fc989ae47bb106ebed995052a506e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/classifier/jev/jev.go`](https://github.com/0x4272616e646f6e/ailuros/blob/b61daa74096fc989ae47bb106ebed995052a506e/internal/classifier/jev/jev.go) at the pinned commit. |

## When to use

- Put a model-based allow/block check in front of an API behind Envoy, NGINX or Traefik.
- Mismatch: early development; size the deployment for Jev's rate limits and per-request latency.

## How it works

The Jev classifier posts each request summary to `/v1/systemone` and maps the answer to allow or block; the proxy frontends turn that into the native response for each proxy. Integration evidence: [`internal/classifier/jev/jev.go`](https://github.com/0x4272616e646f6e/ailuros/blob/b61daa74096fc989ae47bb106ebed995052a506e/internal/classifier/jev/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/0x4272616e646f6e/ailuros.git && cd ailuros
docker build -t ailuros .
# see README and docs/ for the Jev backend settings and proxy frontends
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Kubernetes setup: `docs/kubernetes.md`.

## Limits and data handling

Request data you forward goes to TypeSafe (or your chosen model) on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit b61daa74096f](https://github.com/0x4272616e646f6e/ailuros/tree/b61daa74096fc989ae47bb106ebed995052a506e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
