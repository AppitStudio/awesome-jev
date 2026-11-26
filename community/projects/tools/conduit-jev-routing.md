# conduit by Pedro Müller (local gateway for Claude Code and OpenCode with Anthropic → GLM → DeepSeek failover and an optional Jev mode that picks the model per call)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Loopback HTTP gateway for Claude Code and OpenCode in front of Anthropic, GLM via Z.ai and optionally DeepSeek: a circuit breaker fails over when the plan quota runs out and switches back later. In the optional `jev` routing mode, Jev reads a short summary of each request and picks the provider and model from the catalog, plus how long that pick should stick.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pmagnomuller/conduit) |
| Maintainer | [Pedro Müller](https://github.com/pmagnomuller). Independently curated. |
| Format | Go gateway, control CLI and web UI (macOS menu bar app included) |
| Requirements | Go toolchain to build, a Claude Code subscription and/or Z.ai key (DeepSeek optional); a TypeSafe key in `TYPESAFE_API_KEY` only for `jev` mode. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/route/client.go`](https://github.com/pmagnomuller/conduit/blob/27b94acc14ca29c61a6fb449693f0db8749b910e/internal/route/client.go) at the pinned commit. |

## When to use

- Claude Code or OpenCode users with a GLM or DeepSeek fallback who want each call routed by capability rather than a fixed order.
- Mismatch: teams that need a licensed, supported proxy; this is a personal project with no licence file.

## How it works

`internal/route/client.go` posts to the Jev base URL, which `internal/config/config.go` sets to `https://api.typesafe.ai/v1/systemone`, with a bounded dossier built in `internal/route/dossier.go` (last user message clipped to about 1,200 characters, step type, tool names and short result excerpts, requested model); the system prompt, tool schemas and other provider keys are not sent. A timeout, error or answer outside the catalog falls back to `auto` routing for that call. Integration evidence: [`internal/route/client.go`](https://github.com/pmagnomuller/conduit/blob/27b94acc14ca29c61a6fb449693f0db8749b910e/internal/route/client.go).

## Get started

Run the setup script (it builds the gateway, stores keys and points Claude Code at it), then switch routing to `jev`.

```sh
git clone https://github.com/pmagnomuller/conduit
cd conduit
./setup.sh                 # optional TypeSafe key prompt for Jev mode
conduitctl route jev       # let Jev pick per call
conduitctl decisions -n 5
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Writeup: [pedro-muller.com/ai/conduit/](https://pedro-muller.com/ai/conduit/)

## Limits and data handling

No licence file, so no reuse terms are granted. Jev sees a clipped summary of each request; your TypeSafe key is only sent to api.typesafe.ai. The breaker always overrides Jev (Anthropic models are removed from the choice while the plan quota is exhausted). Using a subscription through a local gateway is your own responsibility under each provider's terms.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 27b94acc14ca](https://github.com/pmagnomuller/conduit/tree/27b94acc14ca29c61a6fb449693f0db8749b910e). Inspected the README ("Routing modes"), `.env.example` and `internal/route/client.go` / `dossier.go` at the pinned commit; nothing was built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
