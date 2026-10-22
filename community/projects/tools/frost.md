# Frost (model router built on Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI from Haplab that takes a prompt or markdown task, has Jev assess it, then picks a model, harness and effort level locally from your own catalog, with explanations, alternatives and JSON output; decisions can be recorded and replayed offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marcus/frost) |
| Maintainer | [marcus](https://github.com/marcus). Independently curated. |
| Format | CLI (Go, Homebrew `marcus/tap/frost`) |
| Requirements | macOS or Linux; `TYPESAFE_API_KEY`; your model catalog and config. |
| License | [MIT](https://github.com/marcus/frost/blob/28ef2f739065bb9bb149b49701f869fe8b0dc9d2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/analyzer/typesafe/typesafe.go`](https://github.com/marcus/frost/blob/28ef2f739065bb9bb149b49701f869fe8b0dc9d2/internal/analyzer/typesafe/typesafe.go) at the pinned commit. |

## When to use

- Choose the cheapest model that meets a quality floor for each coding task.
- Feed routing recommendations to agents or scripts as JSON.
- Mismatch: it recommends what to run; it doesn't launch the model.

## How it works

`internal/analyzer/typesafe/typesafe.go` makes one analysis request to `https://api.typesafe.ai` per task; selection after that is deterministic Go code over your configured profiles. Integration evidence: [`internal/analyzer/typesafe/typesafe.go`](https://github.com/marcus/frost/blob/28ef2f739065bb9bb149b49701f869fe8b0dc9d2/internal/analyzer/typesafe/typesafe.go).

## Get started

From the upstream README (not run on the review host):

```sh
brew install marcus/tap/frost
export TYPESAFE_API_KEY=your-key
frost config check
frost route "Find why our retries sometimes duplicate a payment."
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configuration guide: [github.com/marcus/frost/blob/main/config/README.md](https://github.com/marcus/frost/blob/main/config/README.md)
- Capacity integration: [github.com/marcus/frost/blob/main/examples/capacity/README.md](https://github.com/marcus/frost/blob/main/examples/capacity/README.md)

## Limits and data handling

Task text is sent to TypeSafe. Starter profiles are examples, not a guarantee of model access.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 28ef2f739065](https://github.com/marcus/frost/tree/28ef2f739065bb9bb149b49701f869fe8b0dc9d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
