# guardrails-md

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Berget AI plugin for opencode, pi and Claude Code (plus a git pre-commit hook) that scores every bash command with a System One decision model against your repo's `guardrails.md` before it runs; defaults to Berget's `berget/bev` model, and any `/v1/systemone`-compatible endpoint (TypeSafe settings as fallback) can be used.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/berget-ai/guardrails-md) |
| Maintainer | [berget-ai](https://github.com/berget-ai). Independently curated. |
| Format | Coding-agent plugin + pre-commit hook |
| Requirements | opencode, pi or Claude Code; `BERGET_API_KEY` (or Berget seat login) for the default model, or `BERGET_BASE_URL`/`TYPESAFE_*` settings for another System One endpoint. |
| License | [MIT](https://github.com/berget-ai/guardrails-md/blob/533aaa5a00717f143733f4907dc694dee1d3cf29/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Maintained by Berget AI, whose hosted model is the default backend; no affiliation with the reviewer. |

## When to use

- Put written team rules (`guardrails.md`) in front of agent bash commands.
- Use the same gate in a git pre-commit hook.
- Mismatch: default backend is Berget's model, not TypeSafe Jev; fail-closed by default.

## How it works

[`core.ts`](https://github.com/berget-ai/guardrails-md/blob/533aaa5a00717f143733f4907dc694dee1d3cf29/core.ts) sends the command (first 2,000 characters) plus your rules as System One questions (destructive, credentials, rule violation…) to the configured endpoint; scores above thresholds block the call. Adapters for opencode and pi live in [`adapters/`](https://github.com/berget-ai/guardrails-md/tree/533aaa5a00717f143733f4907dc694dee1d3cf29/adapters).

## Get started

Add `guardrails.md` to your repo, then enable the opencode plugin:

```sh
# opencode.json
# { "plugin": ["@bergetai/opencode-guardrails-md"] }
export BERGET_API_KEY=...       # or point BERGET_BASE_URL at another /v1/systemone endpoint
```

Each command is one request to Berget (or your configured endpoint), billed by that provider.

## Examples and demos

- `guardrails.example.md` and the README accuracy table (upstream, Berget model).

## Limits and data handling

Commercial vendor's own model by default; accuracy tables are upstream. Commands and rules are sent to the endpoint. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 533aaa5a0071](https://github.com/berget-ai/guardrails-md/tree/533aaa5a00717f143733f4907dc694dee1d3cf29). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
