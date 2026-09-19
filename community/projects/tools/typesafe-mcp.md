# TypeSafe MCP

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeSafe MCP exposes Jev judgments to coding agents through a Go stdio MCP server, with an additional pi extension.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/itsmostafa/typesafe-mcp) |
| Maintainer | [Mostafa / itsmostafa](https://github.com/itsmostafa). |
| Format | Go `evaluate` executable, MCP tool, and pi extension. |
| Platform | Installer targets macOS and Linux on amd64/arm64; source-build access is also documented. |
| Jev's role | Evaluates supplied state against typed questions and returns the provider response to the agent. |
| Requirements | A compatible MCP client or pi; TypeSafe or OpenRouter account/key; source build declares Go 1.27.1 in `go.mod`. |
| License | [MIT](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/LICENSE). Inference and client access costs are separate. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use this when an agent needs a reusable tool for classification, routing, or rubric scoring, without embedding a TypeSafe client into each agent workflow.

It is also a compact example of exposing raw Jev responses over MCP. It does not implement your routing policy, uncertainty thresholds, or downstream actions.

## How it works

The [`evaluate` tool](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/tools.go) accepts `state`, a map of `questions`, and an optional `model`. It documents Noul, Choice, and Score questions, checks selected criteria shapes locally, and returns the response body as MCP text content.

The [route selection](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/main.go) uses:

- `TYPESAFE_API_KEY`: `https://api.typesafe.ai/v1/systemone`, default model `jev-latest`.
- Otherwise `OPENROUTER_API_KEY`: `https://openrouter.ai/api/alpha/decisions`, default model `~typesafe/jev-latest`.

TypeSafe takes precedence when both keys exist. An explicit model passes through unchanged. The OpenRouter route uses an alpha endpoint; continued compatibility was not live-tested. Consult the [TypeSafe API reference](https://docs.typesafe.ai/api) for current provider semantics.

Server guidance encourages independent questions, complete instructions, raw evidence, and a no-match option. Those are instructions for the calling agent, not enforced decision policy.

## Get started

The [upstream quickstart](https://github.com/itsmostafa/typesafe-mcp#quickstart) documents its release installer and Go installation. To build the reviewed source instead, with the declared Go toolchain available:

```sh
git clone https://github.com/itsmostafa/typesafe-mcp.git
cd typesafe-mcp
git checkout 0c9f35d9b1859189fc7e7d01947061f311ca6dde
go build -o evaluate ./cmd/evaluate
./evaluate version
```

Building may download Go dependencies. These commands were inspected, not executed during this review.

Configure an MCP client to launch the absolute path to this binary with argument `mcp`, supplying one provider key through its environment. The [manual configuration notes](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/CLAUDE.md#manual-client-config) explain this path.

Alternatively, after privately setting the provider key in your shell:

```sh
./evaluate setup mcp
```

This detects Claude Code, Codex, and Claude Desktop and writes their configuration. It copies every `TYPESAFE_*` variable and `OPENROUTER_API_KEY` into client configuration. It replaces the `evaluate` entry and removes a legacy entry named `jev`, including an unrelated entry using that name. Review the [setup implementation](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/setup.go) before choosing automatic registration.

For pi, `./evaluate setup pi` writes an extension into pi's configuration directory; reload pi afterward. That extension inherits keys from pi's environment rather than embedding them in the generated file.

A tool call sends the supplied state and questions to the selected provider and may incur inference charges. Registration alone is not a model-quality check. Ask the client to make one call using the upstream synthetic ticket example; expect the provider JSON returned under matching question IDs.

## Examples and demos

- [Quickstart ticket example](https://github.com/itsmostafa/typesafe-mcp#quickstart): urgency and department judgments over synthetic text; executing it requires live credentials.
- [Tool reference](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/CLAUDE.md#tool-reference): criteria shapes, Score indexing, and manual configuration.
- [Tests](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/evaluate_test.go): local HTTP fixtures and in-memory MCP calls covering errors, routing, setup, and validation. These are synthetic fixtures, not recorded Jev responses.

No separate hosted demo was identified in the inspected documentation.

## Limits and data handling

- All supplied state and questions leave the machine for TypeSafe or OpenRouter. Returned content also enters the calling agent's context; that client controls its storage and further use.
- HTTP 429 and 529 responses receive up to three retries with exponential backoff. Other HTTP errors and transport failures become tool errors. The HTTP client has a 60-second timeout per attempt, not a 60-second total retry budget.
- Responses are read through a 16 MiB limit. The client does not detect truncation or validate successful response JSON, required answers, probabilities, or types. Consumers must handle missing, malformed, or uncertain results.
- Input checks are partial: unknown question types pass through, and the server does not establish that question instructions are semantically complete.
- Raw answers are preserved, but no uncertainty fallback or action authorization is enforced. The tool's read-only annotation does not prevent downstream client actions.
- Agent setup writes local configuration and keys; inference costs and client subscriptions are separate from the MIT source license. Prices were not verified.

## Review and maintenance

Reviewed on **2026-09-19** at [`0c9f35d9b1859189fc7e7d01947061f311ca6dde`](https://github.com/itsmostafa/typesafe-mcp/tree/0c9f35d9b1859189fc7e7d01947061f311ca6dde).

Inspected the public repository, README, MIT license, `go.mod`, installer, task definitions, routing, HTTP client, tool schema/validation, registration, pi bridge, and representative tests. Confirmed the public repository was reachable and recorded the checkout with `git rev-parse HEAD`.

This was a source review only: no dependency installation, build, tests, client registration, binary update, provider requests, or performance/quality evaluation was executed. The inspected tests cover selected mocked behavior; no passing test result is claimed.

Related: [TypeSafeAI.Net](typesafeai-net.md) for a .NET client, or the catalog's [offline examples](../../../examples/README.md) for deterministic teaching workflows.
