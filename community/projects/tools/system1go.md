# system1go (dependency-free Go SDK for System One and OpenAI Decisions)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go client with a `Jev` preset that defaults to `https://api.typesafe.ai` and `jev-latest`, plus an OpenAI Decisions preset, without pulling extra dependencies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/3inch-ai/system1go) |
| Maintainer | [3inch-ai](https://github.com/3inch-ai). Independently curated. |
| Format | Go SDK (MIT) |
| Requirements | Go toolchain and a TypeSafe or OpenAI Decisions key for live calls. |
| License | [MIT](https://github.com/3inch-ai/system1go/blob/55b5540e39d98e593cfcda857610ec14864c9ac6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`presets.go`](https://github.com/3inch-ai/system1go/blob/55b5540e39d98e593cfcda857610ec14864c9ac6/presets.go) at the pinned commit. |

## When to use

- Call TypeSafe Jev from Go with a tiny client.
- Share one API surface with OpenAI Decisions.
- Mismatch: SDK only; no agent runtime included.

## How it works

`presets.go` `Jev` sets protocol SystemOne, provider typesafe, default model `jev-latest` and base URL `https://api.typesafe.ai`. Integration evidence: [`presets.go`](https://github.com/3inch-ai/system1go/blob/55b5540e39d98e593cfcda857610ec14864c9ac6/presets.go).

## Get started

Clone, set TYPESAFE_API_KEY, and run the examples or tests in the README.

```sh
git clone https://github.com/3inch-ai/system1go.git && cd system1go
export TYPESAFE_API_KEY=...
go test ./...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/3inch-ai/system1go/blob/55b5540e39d98e593cfcda857610ec14864c9ac6/README.md](https://github.com/3inch-ai/system1go/blob/55b5540e39d98e593cfcda857610ec14864c9ac6/README.md)

## Limits and data handling

Requests you build are sent to TypeSafe or OpenAI on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 55b5540e39d9](https://github.com/3inch-ai/system1go/tree/55b5540e39d98e593cfcda857610ec14864c9ac6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
