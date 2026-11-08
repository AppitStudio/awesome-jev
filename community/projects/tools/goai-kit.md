# goai-kit (Go LLM library with a TypeSafe Jev decisions package)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small no-magic Go library for OpenAI-compatible LLMs (structured JSON, text, tools) with a `jev` package for typed decisions via TypeSafe System One or OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mhrlife/goai-kit) |
| Maintainer | [mhrlife](https://github.com/mhrlife). Independently curated. |
| Format | Go module (no SPDX license file on the reviewed commit) |
| Requirements | Go and a TypeSafe or OpenRouter key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/client.go`](https://github.com/mhrlife/goai-kit/blob/2567499bb2d756195a5b5deb1eccacfd6118628c/jev/client.go) at the pinned commit. |

## When to use

- Mix LLM calls and Jev decisions in one Go library.
- Get typed answers without hand-writing HTTP.
- Mismatch: no OSI license on the reviewed commit.

## How it works

`jev/client.go` targets `https://api.typesafe.ai/v1/systemone` or `https://openrouter.ai/api/alpha/decisions`; `jev/types.go` models typed answers and usage. Integration evidence: [`jev/client.go`](https://github.com/mhrlife/goai-kit/blob/2567499bb2d756195a5b5deb1eccacfd6118628c/jev/client.go).

## Get started

Add the module with `go get` and use the `jev` package per README.

```sh
git clone https://github.com/mhrlife/goai-kit.git && cd goai-kit
export TYPESAFE_API_KEY=...
go test ./...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mhrlife/goai-kit/blob/2567499bb2d756195a5b5deb1eccacfd6118628c/README.md](https://github.com/mhrlife/goai-kit/blob/2567499bb2d756195a5b5deb1eccacfd6118628c/README.md)

## Limits and data handling

State and questions are sent to TypeSafe/OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 2567499bb2d7](https://github.com/mhrlife/goai-kit/tree/2567499bb2d756195a5b5deb1eccacfd6118628c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
