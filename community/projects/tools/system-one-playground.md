# System One Playground

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MIT toolkit for **SysOneScript** (`.sos` readable scripts + `sysone`/`sos` CLI), a **Go** TypeSafe System One client (`…/typesafe`), semantic lint (`semlint`), and **Studio** / VS Code extension—start offline, add live Jev judgments when needed. Distinct from standalone Go clients [jevgo](jevgo.md) and [TypeSafe Go](typesafe-go.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DonaldMurillo/system-one-playground) |
| Maintainer | [DonaldMurillo](https://github.com/DonaldMurillo). Independently curated; this entry is not an upstream submission or endorsement. Not affiliated with TypeSafe. |
| Format | Go module **`github.com/DonaldMurillo/system-one-playground`** — CLI installers, VS Code Marketplace extension **SysOneScript**, docs site, Studio. SOS **0.3** preview (README). |
| Requirements | Released CLI/extension: no Go install required. From source: Go (module declares **1.25**). Live Jev ops need `TYPESAFE_API_KEY` (or VS Code “Set Jev token”). Canonical scripts run offline without a key. |
| License | [MIT](https://github.com/DonaldMurillo/system-one-playground/blob/38444999c25e45dc6823cb91a58ff45f749be70f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected. Local `go test` / CLI installer not run on the review host. Live TypeSafe calls not made. |

## When to use

Use it when you want a **scripting language + editor** path for System One workflows, or a batteries-included Go client plus Studio, without cloning effect-heavy stacks. Prefer [jevgo](jevgo.md) / [TypeSafe Go](typesafe-go.md) for minimal Go-only clients; prefer official JS/Python SDKs for those languages.

## How it works

Offline: `sysone run` / `sos` execute SysOneScript without calling TypeSafe. Live: set `TYPESAFE_API_KEY` so model-backed Jev operations can post typed questions. The Go package [`typesafe`](https://github.com/DonaldMurillo/system-one-playground/blob/38444999c25e45dc6823cb91a58ff45f749be70f/typesafe/client.go) mirrors the JS SDK shape (`SystemOne`, `ListModels`, question constructors, retries) against `https://api.typesafe.ai`. Application/script code still owns thresholds and side effects. Docs cover the Go client, language, and editor services.

## Get started

```sh
# Standalone CLI (macOS/Linux example from README; verifies checksum)
curl -fsSL https://github.com/DonaldMurillo/system-one-playground/releases/download/vscode-v0.4.0/install.sh | sh
printf 'make message "Hello from System One Playground"\nshow message\n' > hello.sos
sysone run hello.sos
# Optional live judgments: export TYPESAFE_API_KEY=...
```

Or clone at [commit 3844499](https://github.com/DonaldMurillo/system-one-playground/tree/38444999c25e45dc6823cb91a58ff45f749be70f) and follow upstream docs. VS Code: search **SysOneScript** on the Marketplace. Live Jev steps incur TypeSafe charges; this listing did not run them.

## Examples and demos

- Offline `hello.sos` / `sysone build` path in the README.
- [`docs/go-client.md`](https://github.com/DonaldMurillo/system-one-playground/blob/38444999c25e45dc6823cb91a58ff45f749be70f/docs/go-client.md), language and editor guides under `docs/`.
- Docs site / Studio noted in README (`donaldmurillo.github.io/system-one-playground/`).

## Limits and data handling

Only model-backed Jev operations send state/questions to TypeSafe when a key is set. CLI installer downloads release binaries—review upstream checksums before piping install scripts. SOS is labeled preview; API/language drift is possible. No live TypeSafe calls on the review host.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 3844499](https://github.com/DonaldMurillo/system-one-playground/tree/38444999c25e45dc6823cb91a58ff45f749be70f): MIT; README cites SOS 0.3 preview and vscode-v0.4.0 installers. AI-assisted source review of README, `typesafe/client.go`, LICENSE, module path. No local Go build/test. No live TypeSafe calls. Marketplace/extension install not verified on the review host.

Related: [jevgo](jevgo.md), [TypeSafe Go](typesafe-go.md), [System One Harness](systemone-harness.md), [Discern](discern.md).
