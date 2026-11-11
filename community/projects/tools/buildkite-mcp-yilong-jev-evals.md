# Buildkite MCP server evals (Yilong grader that uses Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Eval suite in Buildkite's official MCP server repository whose Yilong grader sends complete eval evidence to Jev and reads its grading probabilities, with a long-context fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/buildkite/buildkite-mcp-server) |
| Maintainer | [buildkite](https://github.com/buildkite). Independently curated. |
| Format | Eval scripts (Shell/Python) in a Go MCP server repo, MIT |
| Requirements | A checkout, the eval tooling in `evals/README.md`, and a TypeSafe key for Yilong (`YILONG_MODEL`, default `jev-1.14.0`). |
| License | [MIT](https://github.com/buildkite/buildkite-mcp-server/blob/2d83bff0aa69d4766a0c47be1be44cd8a33c946f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`evals/scripts/yilong.sh`](https://github.com/buildkite/buildkite-mcp-server/blob/2d83bff0aa69d4766a0c47be1be44cd8a33c946f/evals/scripts/yilong.sh) at the pinned commit. |

## When to use

- Grade MCP tool-use evals with a typed model.
- See how a vendor repo handles Jev's body limits and rejections.
- Mismatch: Jev is only in the eval harness; the MCP server itself does not use it.

## How it works

`evals/scripts/yilong.sh` posts evidence to `/v1/systemone`; per `evals/README.md`, oversize evidence is summarized and retried in long-context mode, and Jev rejections become `undetermined`. Integration evidence: [`evals/scripts/yilong.sh`](https://github.com/buildkite/buildkite-mcp-server/blob/2d83bff0aa69d4766a0c47be1be44cd8a33c946f/evals/scripts/yilong.sh).

## Get started

Read `evals/README.md`, set the TypeSafe key, then run the eval scripts against your MCP server build.

```sh
git clone https://github.com/buildkite/buildkite-mcp-server.git && cd buildkite-mcp-server/evals
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evals README: [github.com/buildkite/buildkite-mcp-server/blob/2d83bff0aa69d4766a0c47be1be44cd8a33c946f/evals/README.md](https://github.com/buildkite/buildkite-mcp-server/blob/2d83bff0aa69d4766a0c47be1be44cd8a33c946f/evals/README.md)

## Limits and data handling

Eval evidence (tool calls and outputs) goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 2d83bff0aa69](https://github.com/buildkite/buildkite-mcp-server/tree/2d83bff0aa69d4766a0c47be1be44cd8a33c946f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
