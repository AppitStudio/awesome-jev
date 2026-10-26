# Axiomaton (tell your model what changed since its training cutoff; Jev resolves contradictions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go command-line tool from Canonical that keeps append-only logs of dated facts about languages, tools and libraries and renders those newer than a model's knowledge cutoff as Markdown for its context; logs for Go, Python, Rust, Zig and Canonical's craft tools ship with it, and a decision model (default `typesafe/jev-1.13` via OpenRouter) resolves contradictions between facts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/canonical/axiomaton) |
| Maintainer | [canonical](https://github.com/canonical). Independently curated. |
| Format | Go command-line tool (`ax`) |
| Requirements | Go 1.27+; an OpenRouter key (or any OpenAI-compatible endpoint) for summaries, embeddings and the decision role; podman or LXD for `ax update`. |
| License | [GPL-3.0](https://github.com/canonical/axiomaton/blob/27267defdd2b4f50cf253984bf0478f207125c07/COPYING) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/models/openrouter/client.go`](https://github.com/canonical/axiomaton/blob/27267defdd2b4f50cf253984bf0478f207125c07/internal/models/openrouter/client.go) at the pinned commit. |

## When to use

- Give a coding model an accurate list of changes since its cutoff for the stack you use.
- Maintain project-specific fact logs with sandboxed agents that verify release notes.
- Mismatch: querying shipped logs needs no model; Jev is used only for the decision role.

## How it works

`ax setup` writes a decision role that defaults to `typesafe/jev-1.13`; `internal/models/openrouter/client.go` sends those decisions to the OpenRouter Decisions API, and results are cached; without a decision model, contradictions are not resolved. Integration evidence: [`internal/models/openrouter/client.go`](https://github.com/canonical/axiomaton/blob/27267defdd2b4f50cf253984bf0478f207125c07/internal/models/openrouter/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
go install github.com/canonical/axiomaton/cmd/ax@latest
export OPENROUTER_API_KEY=sk-or-...
ax setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/canonical/axiomaton#readme](https://github.com/canonical/axiomaton#readme)

## Limits and data handling

Fact text sent for decisions goes to OpenRouter and on to TypeSafe; Jev is reached through OpenRouter, not called directly. Independently listed; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 27267defdd2b](https://github.com/canonical/axiomaton/tree/27267defdd2b4f50cf253984bf0478f207125c07). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
