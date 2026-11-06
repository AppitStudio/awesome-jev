# Sael (AI request safety gateway with a TypeSafe Jev classifier and ops console)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go gateway that sits between clients and AI services to enforce configurable, auditable text-safety rules, with a web ops console and a first-class TypeSafe Jev integration for calibrated classification.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cipherTing/sael) |
| Maintainer | [cipherTing](https://github.com/cipherTing). Independently curated. |
| Format | Go gateway + web console + SDK (MIT) |
| Requirements | Go build/deploy environment and a TypeSafe key for Jev classification. |
| License | [MIT](https://github.com/cipherTing/sael/blob/ce62ac7653bf14f771988998b9871f5170a48e96/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gateway/internal/gateway/jev.go`](https://github.com/cipherTing/sael/blob/ce62ac7653bf14f771988998b9871f5170a48e96/gateway/internal/gateway/jev.go) at the pinned commit. |

## When to use

- Add a verifiable safety proxy in front of AI endpoints.
- Operate rules from a console with audit trails.
- Mismatch: Chinese-first docs; English README under docs/.

## How it works

`gateway/internal/gateway/jev.go` drives TypeSafe Jev classification for request screening; settings UI pins models such as `jev-latest`. Integration evidence: [`gateway/internal/gateway/jev.go`](https://github.com/cipherTing/sael/blob/ce62ac7653bf14f771988998b9871f5170a48e96/gateway/internal/gateway/jev.go).

## Get started

Follow the gateway quick start in the README / gateway docs with a TypeSafe key.

```sh
git clone https://github.com/cipherTing/sael.git && cd sael
export TYPESAFE_API_KEY=...
# see gateway/README.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cipherTing/sael/blob/ce62ac7653bf14f771988998b9871f5170a48e96/README.md](https://github.com/cipherTing/sael/blob/ce62ac7653bf14f771988998b9871f5170a48e96/README.md)

## Limits and data handling

Request text under review is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit ce62ac7653bf](https://github.com/cipherTing/sael/tree/ce62ac7653bf14f771988998b9871f5170a48e96). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
