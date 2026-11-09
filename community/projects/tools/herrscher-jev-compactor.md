# herrscher-jev-compactor (Go compaction stage that asks TypeSafe Jev which tool calls to keep)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go plugin for the herrscher harness: before the backend summarises a session, Jev decides which tool calls the assistant still needs and the rest are pruned verbatim.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Herrscherd/herrscher-jev-compactor) |
| Maintainer | [Herrscherd](https://github.com/Herrscherd). Independently curated. |
| Format | Go library/plugin (MIT) |
| Requirements | Go, herrscher, and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Herrscherd/herrscher-jev-compactor/blob/6b7724f81cf63f0ea3656636bb54941697f134c9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.go`](https://github.com/Herrscherd/herrscher-jev-compactor/blob/6b7724f81cf63f0ea3656636bb54941697f134c9/client.go) at the pinned commit. |

## When to use

- Shrink agent histories without rewriting messages.
- Port the fast-jev-compaction idea to Go.
- Mismatch: only for herrscher users.

## How it works

`client.go` calls the System One API and `compactor.go` asks per tool call whether it is still needed; it is a Go port of fast-jev-compaction and runs via `compactStack: ["jev", "backend"]`. Integration evidence: [`client.go`](https://github.com/Herrscherd/herrscher-jev-compactor/blob/6b7724f81cf63f0ea3656636bb54941697f134c9/client.go).

## Get started

Import the package for its side effect in a herrscher build and set `compactStack` to include `jev`.

```sh
git clone https://github.com/Herrscherd/herrscher-jev-compactor.git && cd herrscher-jev-compactor
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Herrscherd/herrscher-jev-compactor/blob/6b7724f81cf63f0ea3656636bb54941697f134c9/README.md](https://github.com/Herrscherd/herrscher-jev-compactor/blob/6b7724f81cf63f0ea3656636bb54941697f134c9/README.md)

## Limits and data handling

Tool-call history is sent to TypeSafe for each compaction.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 6b7724f81cf6](https://github.com/Herrscherd/herrscher-jev-compactor/tree/6b7724f81cf63f0ea3656636bb54941697f134c9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
