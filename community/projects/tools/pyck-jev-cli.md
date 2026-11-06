# jev-cli (Unix CLI and MCP server exposing 15 TypeSafe Jev System One tools)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI and MCP server that wraps OpenRouter System One decision models (default TypeSafe Jev) as fifteen tools—score, verify, ask and related framings of noul/choice/score—usable from a shell or any MCP client such as OpenCode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pyck-ai/jev-cli) |
| Maintainer | [pyck-ai](https://github.com/pyck-ai). Independently curated. |
| Format | Go CLI + MCP server (MIT) |
| Requirements | Go build or release binary, and an OpenRouter key (default model `~typesafe/jev-latest`). |
| License | [MIT](https://github.com/pyck-ai/jev-cli/blob/e9fe55497dbd1910a7ddfec8a2a285e6063be971/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cmd/jev/main.go`](https://github.com/pyck-ai/jev-cli/blob/e9fe55497dbd1910a7ddfec8a2a285e6063be971/cmd/jev/main.go) at the pinned commit. |

## When to use

- Call Jev primitives from scripts without embedding an SDK.
- Expose the same tools to an MCP harness.
- Mismatch: defaults to OpenRouter; bring your own key and spend policy.

## How it works

`cmd/jev/main.go` registers the tool set once for both CLI and MCP modes against OpenRouter System One. Integration evidence: [`cmd/jev/main.go`](https://github.com/pyck-ai/jev-cli/blob/e9fe55497dbd1910a7ddfec8a2a285e6063be971/cmd/jev/main.go).

## Get started

Install the binary per the README and run `jev score` or start the MCP server.

```sh
git clone https://github.com/pyck-ai/jev-cli.git && cd jev-cli
# build per README
export OPENROUTER_API_KEY=...
jev score --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/pyck-ai/jev-cli/blob/e9fe55497dbd1910a7ddfec8a2a285e6063be971/README.md](https://github.com/pyck-ai/jev-cli/blob/e9fe55497dbd1910a7ddfec8a2a285e6063be971/README.md)

## Limits and data handling

Prompt/state for each tool call is sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit e9fe55497dbd](https://github.com/pyck-ai/jev-cli/tree/e9fe55497dbd1910a7ddfec8a2a285e6063be971). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
