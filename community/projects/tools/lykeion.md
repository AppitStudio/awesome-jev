# Lykeion (self-hosted research lab where AI agents work studies across a four-stage board and Jev scores the work at stage gates)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted lab: each question becomes a study that moves through Grounding, Hypotheses, Experimentation and Validation, worked by Claude Code or Codex running sandboxed on your machine. A study advances only when server checks pass, and where a stage uses it Jev scores the work; every kept claim must cite a recorded source from OpenAlex, Europe PMC or arXiv. Adds scheduled agent work, shared notebooks and a LaTeX co-writing mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lykeion-tech/lykeion) |
| Maintainer | [lykeion-tech](https://github.com/lykeion-tech). Independently curated. |
| Format | Go server, Vue/Next.js web apps and a local agent daemon (`lyk`) |
| Requirements | PostgreSQL, the Go server and web apps, Claude Code or Codex signed in locally, and a sandbox (Seatbelt or bubblewrap); `TYPESAFE_API_KEY` turns on Jev scoring. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/internal/jev/jev.go`](https://github.com/lykeion-tech/lykeion/blob/4416ff82e0a6ff7143086a20c1846444b6d4758d/server/internal/jev/jev.go) at the pinned commit. |

## When to use

- Run agent-driven literature and experiment work with gates and source citations.
- Mismatch: a quick install; it is a multi-service self-hosted system.

## How it works

`server/internal/jev/jev.go` asks typed questions with model `jev-1.13.0` and refuses answers from any other model; `server/cmd/server/main.go` enables it against `https://api.typesafe.ai` only when `TYPESAFE_API_KEY` is set, keeping the key on the server. Integration evidence: [`server/internal/jev/jev.go`](https://github.com/lykeion-tech/lykeion/blob/4416ff82e0a6ff7143086a20c1846444b6d4758d/server/internal/jev/jev.go).

## Get started

Follow the README's "Run locally" section: set up the database roles, start the server and web apps, then the `lyk` daemon.

```sh
git clone https://github.com/lykeion-tech/lykeion && cd lykeion
# README → Run locally: database roles, server, web apps, lyk daemon
export TYPESAFE_API_KEY=...   # optional Jev scoring
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lykeion-tech/lykeion/blob/4416ff82e0a6ff7143086a20c1846444b6d4758d/README.md](https://github.com/lykeion-tech/lykeion/blob/4416ff82e0a6ff7143086a20c1846444b6d4758d/README.md)

## Limits and data handling

Study material scored by Jev is sent to TypeSafe on your key; agents use your own Claude Code or Codex sign-in. No license file (only third-party notices), so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 4416ff82e0a6](https://github.com/lykeion-tech/lykeion/tree/4416ff82e0a6ff7143086a20c1846444b6d4758d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
