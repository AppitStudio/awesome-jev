# Juggler (coding-agent workbench with Jev as its decision model)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Visual workbench for AI coding agents, with tree-shaped sessions and inspectable model calls; you can pick Jev as the decision model that answers yes/no, choice and score questions such as Auto-approve's review of a parked tool call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juggler-ai/juggler) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://juggler.studio) |
| Pricing and access | Free download (AGPL-3.0); bring your own provider subscriptions or keys and a TypeSafe key for Jev. Checked 2026-11-11. |
| Jev evidence | [`cmd/juggler/providers/jev/client.go`](https://github.com/juggler-ai/juggler/blob/497c2ffe943424790564301368dd844a200afd7e/cmd/juggler/providers/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [juggler-ai](https://github.com/juggler-ai). Independently curated. |
| Format | Desktop app and local server (Go/TypeScript, AGPL-3.0) |
| Platform and availability | macOS, Windows and Linux desktop app; server mode opens in a browser |
| Jev's role | Optional decision model for yes/no, choice and score checks such as auto-approve reviews of tool calls. |
| Requirements | The Juggler desktop app or server, the coding-agent providers you use, and a TypeSafe key for the `jev` provider. |
| License | [AGPL-3.0](https://github.com/juggler-ai/juggler/blob/497c2ffe943424790564301368dd844a200afd7e/LICENSE) |

## When to use

- Let a typed model review tool calls for auto-approve in a coding-agent UI.
- Inspect every model transaction of an agent session.
- Mismatch: Jev is optional and never used for chat; app code is AGPL-3.0 (extension SDK is Apache-2.0).

## How it works

`cmd/juggler/providers/jev/client.go` is a decision-only provider on `https://api.typesafe.ai/v1` (no chat models are offered from it); `cmd/juggler/core/decision_model.go` stores the chosen decision model in `~/.juggler/decision-model.json`, and when none is set that work falls back to the cheap chat model. Integration evidence: [`cmd/juggler/providers/jev/client.go`](https://github.com/juggler-ai/juggler/blob/497c2ffe943424790564301368dd844a200afd7e/cmd/juggler/providers/jev/client.go).

## Get started

Download a release, add TypeSafe as a provider, then choose Jev as the decision model in settings.

```sh
# download from https://github.com/juggler-ai/juggler/releases
juggler
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/juggler-ai/juggler/blob/497c2ffe943424790564301368dd844a200afd7e/README.md](https://github.com/juggler-ai/juggler/blob/497c2ffe943424790564301368dd844a200afd7e/README.md)

## Limits and data handling

Decision prompts (for example a parked tool call under review) go to TypeSafe on your key; chat traffic goes straight to the providers you chose.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 497c2ffe9434](https://github.com/juggler-ai/juggler/tree/497c2ffe943424790564301368dd844a200afd7e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
