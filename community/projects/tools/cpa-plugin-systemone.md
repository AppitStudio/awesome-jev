# Open Systemone (CLIProxyAPI plugin that routes System One decision requests like Jev to local or hosted nodes)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Plugin for CLIProxyAPI that adds System One decision nodes: a `{model, state, questions}` request goes to the node chosen by the model prefix and its answer comes back unchanged. Nodes can be local servers or hosted lanes (OpenCode, OpenRouter and others) with several keys, headers and per-node proxies; a management page checks latency and builds test decisions, and a Hugging Face tab lists models from the Jev Decision Index and downloads them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ducdao98z/cpa-plugin-systemone) |
| Maintainer | [ducdao98z](https://github.com/ducdao98z). Independently curated. |
| Format | Go plugin (c-shared library) |
| Requirements | CLIProxyAPI with plugin support and Go to build; keys for any hosted nodes. |
| License | [MIT](https://github.com/ducdao98z/cpa-plugin-systemone/blob/30e13067ea9e5327a9596a065307660368c361d6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`systemone.go`](https://github.com/ducdao98z/cpa-plugin-systemone/blob/30e13067ea9e5327a9596a065307660368c361d6/systemone.go) at the pinned commit. |

## When to use

- Put several decision-model providers behind one proxy with failover.
- Mismatch: only for CLIProxyAPI users.

## How it works

`systemone.go` forwards `/v1/systemone` requests to the configured node; `gguf.go` checks or patches GGUF metadata so llama.cpp can serve `/v1/systemone`. Integration evidence: [`systemone.go`](https://github.com/ducdao98z/cpa-plugin-systemone/blob/30e13067ea9e5327a9596a065307660368c361d6/systemone.go).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ducdao98z/cpa-plugin-systemone && cd cpa-plugin-systemone
go build -buildmode=c-shared -buildvcs=false -o systemone.so .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ducdao98z/cpa-plugin-systemone#readme](https://github.com/ducdao98z/cpa-plugin-systemone#readme)

## Limits and data handling

Decision requests go to whichever node you configure; local nodes keep them on your machine.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 30e13067ea9e](https://github.com/ducdao98z/cpa-plugin-systemone/tree/30e13067ea9e5327a9596a065307660368c361d6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
