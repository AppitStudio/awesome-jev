# Pad

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first project management (CLI, web UI, agent skill) for developers and coding agents; an optional TypeSafe decision provider asks Jev whether items need a human or are blocked and matches playbooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PerpetualSoftware/pad) |
| Product homepage | [getpad.dev](https://getpad.dev) |
| Maintainer | [PerpetualSoftware](https://github.com/PerpetualSoftware). Independently curated. |
| Format | Self-hosted binary / Docker image; optional hosted Pad Cloud |
| Requirements | Homebrew or Docker. Decision provider: `PAD_DECISION_PROVIDER=typesafe`, `PAD_TYPESAFE_API_KEY`, optional `PAD_DECISION_MODEL` (default `jev-1.13.0`). |
| License | [Apache-2.0](https://github.com/PerpetualSoftware/pad/blob/be5457595442f2e1b54d0ee2c7de8499f737ca81/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Pad Cloud (app.getpad.dev) is a hosted option; pricing was not verified for this listing. |

## When to use

- Surface which agent-created items actually need a human decision on the dashboard.
- Route a free-text request to the right playbook from an agent via MCP.
- Mismatch: leave the provider off if item content must not leave your machine; Pad works fully without it.

## How it works

With the provider enabled, item create/update/comment events queue asynchronous jobs; a server tick asks Jev typed questions over the item (title, collection, fields, body clipped to 16,000 characters, last 10 comments) and stores answers used by the dashboard `attention` list and playbook matching. With no provider, nothing is queued or sent ([README: Decision provider](https://github.com/PerpetualSoftware/pad/blob/be5457595442f2e1b54d0ee2c7de8499f737ca81/README.md#decision-provider-optional)).

## Get started

Install Pad, then enable the optional provider (live Jev calls):

```sh
brew install PerpetualSoftware/tap/pad
export PAD_DECISION_PROVIDER=typesafe
export PAD_TYPESAFE_API_KEY=...
export PAD_DECISION_MODEL=jev-1.13.0
pad playbook match -- "triage the failing deploy"
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Docs at [getpad.dev/docs](https://getpad.dev/docs); `GET /workspaces/{ws}/items/{slug}/decisions` lists an item's latest answers.

## Limits and data handling

Enabling the provider sends item content to `api.typesafe.ai` and incurs TypeSafe charges. Off is the default and not a degraded mode.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit be5457595442](https://github.com/PerpetualSoftware/pad/tree/be5457595442f2e1b54d0ee2c7de8499f737ca81). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
