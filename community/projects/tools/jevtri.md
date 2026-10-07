# jevtri (Jev Triage)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI for the first minutes of a Linux server incident: collects log lines around the incident time, masks secrets, and asks TypeSafe Jev how worth investigating each log is, so you know which log to read first; signed rpm/deb releases and English/Japanese/Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/takeshiue/jevtri) |
| Maintainer | [takeshiue](https://github.com/takeshiue). Independently curated. |
| Format | Go CLI with rpm/deb packages on GitHub Releases (v0.3.2 at review) or build from source |
| Requirements | Linux (AlmaLinux/Rocky/RHEL 8–10, Ubuntu 22.04/24.04, Debian 12 packages), a `TYPESAFE_API_KEY`, and configured log sources. |
| License | [MIT](https://github.com/takeshiue/jevtri/blob/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Decide where to start looking during an incident when a host has many logs.
- Audit exactly what would be sent (masking examples and a sent-log are documented).
- Mismatch: the score is an investigation priority, not the probability a log holds the cause; jevtri does not find causes, fix anything or monitor.

## How it works

[`internal/logread`](https://github.com/takeshiue/jevtri/tree/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9/internal/logread) collects lines in the incident window, [`internal/mask`](https://github.com/takeshiue/jevtri/tree/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9/internal/mask) masks passwords, tokens, keys, credentials in URLs, card numbers and more, and [`internal/jev/jev.go`](https://github.com/takeshiue/jevtri/blob/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9/internal/jev/jev.go) sends each log's masked lines with the symptom to `api.typesafe.ai/v1/systemone`. When every log scores low, it says so and suggests looking elsewhere.

## Get started

Install a release package (README *Install*; verify the signature first):

```sh
curl -fLO https://github.com/takeshiue/jevtri/releases/download/v0.3.2/jevtri_0.3.2_amd64.deb
sudo apt install ./jevtri_0.3.2_amd64.deb
sudo jevtri init   # stores the API key (root-only) and picks log sources
sudo jevtri -t 14:05 -i "The website returns 502"
```

Each run sends one request per log with lines in the window, billed to your TypeSafe key (budget limits configurable).

## Examples and demos

- Ranked test logs: [`guide/examples.md`](https://github.com/takeshiue/jevtri/blob/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9/guide/examples.md); masking before sending: [`guide/masking.md`](https://github.com/takeshiue/jevtri/blob/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9/guide/masking.md).

## Limits and data handling

Masked log lines, the incident time and your symptom text go to TypeSafe; nothing else is contacted (upstream). Masking is best-effort. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 51f4f2dac20f](https://github.com/takeshiue/jevtri/tree/51f4f2dac20f3f8e0d45cbf0617a137e71d612a9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
