# ask-jev (Go CLI and MCP server)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Standard-library Go CLI and MCP stdio server for TypeSafe's System One API: ask choice, yes/no (noul) and score questions or a batch, get JSON back, and keep a local outcome log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hrubymar10/ask-jev) |
| Maintainer | [hrubymar10](https://github.com/hrubymar10). Independently curated. |
| Format | Go CLI and MCP stdio server |
| Requirements | Go toolchain, a TypeSafe API key in a local JSONC config. |
| License | [MIT](https://github.com/hrubymar10/ask-jev/blob/673f1912eaa58960ca822b64310e57fd60e47f6f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/hrubymar10/ask-jev/blob/673f1912eaa58960ca822b64310e57fd60e47f6f/internal/jev/client.go) at the pinned commit. |

## When to use

- Ask Jev a one-off routing or triage question from a shell script.
- Give an MCP-capable agent a small, dependency-free Jev tool.
- Mismatch: a thin client; thresholds and what to do with answers stay in your code.

## How it works

`internal/jev` builds the documented `{state, model, questions}` request and posts it to `https://api.typesafe.ai/v1/systemone`; the CLI requires HTTPS except for loopback test servers. Tests use mock HTTP servers and do not call TypeSafe. Integration evidence: [`internal/jev/client.go`](https://github.com/hrubymar10/ask-jev/blob/673f1912eaa58960ca822b64310e57fd60e47f6f/internal/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
cp config.example.jsonc config.jsonc && chmod 600 config.jsonc
bin/ask-jev choice --state '{"ticket":"My payment failed"}' \
  --question 'Which team should handle this?' \
  --option billing='Payments and refunds' --option technical='Bugs and outages'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Choice, noul, score and batch examples in the README.

## Limits and data handling

Questions and state go to TypeSafe on your key. Keep the key file outside the repository; `config.jsonc` is git-ignored.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 673f1912eaa5](https://github.com/hrubymar10/ask-jev/tree/673f1912eaa58960ca822b64310e57fd60e47f6f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
