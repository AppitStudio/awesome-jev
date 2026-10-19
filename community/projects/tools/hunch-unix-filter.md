# hunch (Unix filter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go command-line filter that sorts, filters and routes text by meaning: pipe in logs, tickets, reviews or diffs, ask a plain-English question, and Jev answers it for every line as yes/no, a category or a score with a confidence your next command can use.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yarolegovich/hunch) |
| Maintainer | [yarolegovich](https://github.com/yarolegovich). Independently curated. |
| Format | Command-line tool (Go; Homebrew tap, `go install`, release binaries) |
| Requirements | A key for TypeSafe, OpenRouter or OpenCode Zen (`hunch auth login`). |
| License | [Apache-2.0](https://github.com/yarolegovich/hunch/blob/ec7449caee5bed365d00b788285b7fddf1a71b9e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/provider/provider.go`](https://github.com/yarolegovich/hunch/blob/ec7449caee5bed365d00b788285b7fddf1a71b9e/internal/provider/provider.go) at the pinned commit. |

## When to use

- Filter `kubectl logs` or other streams for lines that match a meaning, not a regex.
- Label pull requests or tickets in CI and gate git hooks with exit codes.
- Mismatch: closed questions only; it does not summarise or write text.

## How it works

hunch sends each record and your question to Jev through the provider set up in `internal/provider/provider.go` (requests go to `/v1/systemone`; TypeSafe, OpenRouter and OpenCode Zen are supported). Answers come back with calibrated probabilities, so `--min` thresholds, sorting and routing work on the confidence. Input can be lines, JSONL or whole files, and output can be JSONL, TSV or the original lines. Integration evidence: [`internal/provider/provider.go`](https://github.com/yarolegovich/hunch/blob/ec7449caee5bed365d00b788285b7fddf1a71b9e/internal/provider/provider.go).

## Get started

From the upstream README: install with Homebrew or `go install`, then store a provider key.

```sh
brew tap yarolegovich/hunch https://github.com/yarolegovich/hunch
brew install hunch
hunch auth login
kubectl logs api | hunch "Is this an authentication failure?" --min 0.8 --raw
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/demo/run.sh
- [github.com/yarolegovich/hunch/releases](https://github.com/yarolegovich/hunch/releases)

## Limits and data handling

Every record you pipe in is sent to the chosen provider. Answers are model probabilities, not verified facts.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit ec7449caee5b](https://github.com/yarolegovich/hunch/tree/ec7449caee5bed365d00b788285b7fddf1a71b9e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
