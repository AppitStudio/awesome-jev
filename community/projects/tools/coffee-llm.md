# Coffee LLM by Coffeebreak AI (personal model gateway for OpenCode, Cursor and Codex where Jev decides who leads each turn)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A personal Go gateway in front of many models, built for OpenCode first and reachable from Cursor and Codex through an OpenAI-compatible API, published as one model. A cheaper assistant gathers data, an expert judges and answers, and a deflator condenses long tool results, so the expensive model only sees what it needs. Models are data in `config/models.yaml`, and runtime settings change without a restart.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coffeebreak-ai/coffee-opencode-llm) |
| Maintainer | [coffeebreak-ai](https://github.com/coffeebreak-ai). Independently curated. |
| Format | Go service + CLI |
| Requirements | Go; an OpenCode inference URL and key; a Jev base URL and key (`JEV_BASE_URL`, `JEV_API_KEY`); SQLite or PostgreSQL. |
| License | [MIT](https://github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/jev.go`](https://github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/internal/jev/jev.go) at the pinned commit. |

## When to use

- Run one local endpoint for your coding tools that routes each turn between cheap and expensive models with Jev deciding.
- Mismatch: providers other than OpenCode inference; the gateway has one upstream.

## How it works

`internal/jev/jev.go` posts typed questions to `JEV_BASE_URL` + `/v1/systemone` with retries and limits from `config/gateway.yaml` (up to 4 questions and 32 calls per turn, 45% minimum confidence). Jev picks the access level and model for a turn and decides whether a long tool result should be compressed. Integration evidence: [`internal/jev/jev.go`](https://github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/internal/jev/jev.go).

## Get started

Export the four required variables and start the gateway, then point OpenCode, Cursor or Codex at it.

```sh
git clone https://github.com/coffeebreak-ai/coffee-opencode-llm && cd coffee-opencode-llm
export OPENCODE_INFERENCE_URL=... OPENCODE_API_KEY=... JEV_BASE_URL=https://api.typesafe.ai JEV_API_KEY=...
go run ./cmd/coffee-opencode-llm serve -config config/gateway.yaml -models config/models.yaml
curl http://127.0.0.1:8080/v1/models
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gateway limits: [github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/config/gateway.yaml](https://github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/config/gateway.yaml)
- API contract: [github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/api/openapi.yaml](https://github.com/coffeebreak-ai/coffee-opencode-llm/blob/08def9ab4bef4237175dd7c281630c538a8ceeb5/api/openapi.yaml)

## Limits and data handling

Conversation and tool-result text is sent to Jev for routing and compression decisions, and to OpenCode inference. Active work is on the `go` branch.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 08def9ab4bef](https://github.com/coffeebreak-ai/coffee-opencode-llm/tree/08def9ab4bef4237175dd7c281630c538a8ceeb5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
