# jev by Happy Hacking Space (Go SDK, CLI and MCP server for TypeSafe's System One API and Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Go SDK, command-line tool, MCP server and agent skill for TypeSafe's System One API. The CLI asks noul (yes probability), choice, score and box questions from a string, file or stdin, and `noul --threshold` exits 0 or 1 so a judgment can gate a shell script. It follows the official SDKs' environment variables and retry defaults, and its README says it is not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HappyHackingSpace/jev) |
| Maintainer | [HappyHackingSpace](https://github.com/HappyHackingSpace). Independently curated. |
| Format | Go module, CLI binary, MCP server and agent skill |
| Requirements | Go (or a release binary) and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/HappyHackingSpace/jev/blob/bbe2f66668cdd12489c90823149e3f14032b4588/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.go`](https://github.com/HappyHackingSpace/jev/blob/bbe2f66668cdd12489c90823149e3f14032b4588/client.go) at the pinned commit. |

## When to use

- Call Jev from Go programs, shell scripts or an MCP client without writing the HTTP layer.
- Mismatch: it is a new, unofficial client written against the API reference, not TypeSafe's own SDK.

## How it works

`client.go` posts state and typed questions to `https://api.typesafe.ai` with `TYPESAFE_API_KEY`, `TYPESAFE_DEFAULT_MODEL` (`jev-latest`) and `TYPESAFE_BASE_URL` as settings, and returns typed answers; the CLI and `internal/mcpserver` wrap it. Integration evidence: [`client.go`](https://github.com/HappyHackingSpace/jev/blob/bbe2f66668cdd12489c90823149e3f14032b4588/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
go install github.com/happyhackingspace/jev/cmd/jev@latest
export TYPESAFE_API_KEY=...
jev noul "Is this message spam?" -s "WIN A FREE CRUISE NOW"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with CLI examples for noul, choice, score and box: [github.com/HappyHackingSpace/jev#readme](https://github.com/HappyHackingSpace/jev#readme)

## Limits and data handling

Every command sends the state you give it to TypeSafe on your key and incurs charges. The repository is hours old at review, and its behaviour was not run on the review host. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit bbe2f66668cd](https://github.com/HappyHackingSpace/jev/tree/bbe2f66668cdd12489c90823149e3f14032b4588). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
