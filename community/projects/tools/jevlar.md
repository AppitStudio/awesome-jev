# Jevlar by amscotti (self-hosted gateway for System One decision APIs with key failover, routing and per-caller usage)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small Go gateway between your apps and decision-model APIs that speak the System One wire format. Callers authenticate once against Jevlar; it picks a healthy provider and key, retries elsewhere on failure, keeps rate-limited or revoked keys off the hot path, routes a model name across targets by priority or speed, and records what each caller consumed, with Prometheus metrics and SIGHUP reloads. Everything is one TOML file: no database, no UI. Providers include TypeSafe Jev, Google AI Studio's Gemini Decisions, Upstage Solar Decide, Ollama, OpenRouter and self-hosted Kev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amscotti/jevlar) |
| Maintainer | [amscotti](https://github.com/amscotti). Independently curated. |
| Format | Self-hosted HTTP gateway (Go, Apache-2.0) |
| Requirements | Go (pinned through mise) or a container; provider keys such as `TYPESAFE_API_KEY` in the TOML config. |
| License | [Apache-2.0](https://github.com/amscotti/jevlar/blob/f858951917a5fd82000c55368436c912c5e11f90/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`configs/example.toml`](https://github.com/amscotti/jevlar/blob/f858951917a5fd82000c55368436c912c5e11f90/configs/example.toml) at the pinned commit. |

## When to use

- Share TypeSafe and other decision-model keys across services with failover and per-caller cost tracking.
- Mismatch: chat or completion APIs; it speaks only the System One wire format (plus Gemini Decisions).

## How it works

`configs/example.toml` defines the `typesafe` provider at `https://api.typesafe.ai` + `/v1/systemone` with `jev-latest`, `jev-1.13.0` and `jev-1.14`, and routes `jev-latest` across targets; `scripts/sdk-compat.sh` checks the official SDKs against the gateway. Integration evidence: [`configs/example.toml`](https://github.com/amscotti/jevlar/blob/f858951917a5fd82000c55368436c912c5e11f90/configs/example.toml).

## Get started

Start with the minimal config, then add providers and client keys.

```sh
git clone https://github.com/amscotti/jevlar && cd jevlar
mise install && mise run check
go run ./cmd/jevlar --config configs/minimal.toml
curl http://127.0.0.1:8080/healthz
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/amscotti/jevlar/blob/f858951917a5fd82000c55368436c912c5e11f90/README.md](https://github.com/amscotti/jevlar/blob/f858951917a5fd82000c55368436c912c5e11f90/README.md)

## Limits and data handling

Requests pass through your gateway to the configured providers; client tokens are stored only as hashes. Early project.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit f858951917a5](https://github.com/amscotti/jevlar/tree/f858951917a5fd82000c55368436c912c5e11f90). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
