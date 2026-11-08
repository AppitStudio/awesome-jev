# CyberStrikeAI (AI-native security operations platform with a TypeSafe Jev human-in-the-loop audit backend)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go platform for authorized security operations (Eino agents, MCP tools, workflows, attack-chain analysis) whose HITL audit agent can use TypeSafe Jev to allow or block tool calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AIPentest/CyberStrikeAI) |
| Maintainer | [AIPentest](https://github.com/AIPentest). Independently curated. |
| Format | Go server + web UI (Apache-2.0) |
| Requirements | Go/Docker deployment per README, a chat model, and optionally a TypeSafe API key for the Jev audit backend. |
| License | [Apache-2.0](https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/hitl/jev.go`](https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/internal/hitl/jev.go) at the pinned commit. |

## When to use

- Gate risky agent tool calls in authorized security testing.
- Use structured Jev allow/block instead of prompt-JSON audits.
- Mismatch: only use on systems you own or are authorized to test.

## How it works

Setting `hitl.audit_backend: typesafe` routes HITL approval decisions to TypeSafe Jev (`internal/typesafe/client.go`, default `jev-latest` on `https://api.typesafe.ai`); the audit prompt becomes a Jev `operatorPolicy` overlay. The default backend is an OpenAI-compatible chat model. Integration evidence: [`internal/hitl/jev.go`](https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/internal/hitl/jev.go).

## Get started

Deploy per README quick start, then set `hitl.audit_backend: typesafe` and the audit model key in `config.yaml` (see `docs/en-US/hitl-best-practices.md`).

```sh
git clone https://github.com/AIPentest/CyberStrikeAI.git && cd CyberStrikeAI
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/README.md](https://github.com/AIPentest/CyberStrikeAI/blob/b43bdb991c3bee4f433cd1a0a370a90c4e24241e/README.md)

## Limits and data handling

Tool-call context and operator policy are sent to TypeSafe when the Jev backend is enabled. High-risk tooling (WebShell/C2) needs the upstream hardening guide.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit b43bdb991c3b](https://github.com/AIPentest/CyberStrikeAI/tree/b43bdb991c3bee4f433cd1a0a370a90c4e24241e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
