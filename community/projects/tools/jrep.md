# jrep by Kieran (grep for what code does: Jev ranks functions by behaviour)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

A CLI for coding agents and developers: ask in plain words ("retries failed payments") and get back functions ranked by probability with exact `path:start-end` ranges. It chunks files by function with tree-sitter, skips lockfiles, binaries, docs and tests, packs several chunks and questions into each Jev request, and caches answers in SQLite so repeat searches cost nothing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/K1erans/Jrep) |
| Maintainer | [K1erans](https://github.com/K1erans). Independently curated. |
| Format | Go CLI + agent skill |
| Requirements | Go (to build); a TypeSafe API key (only when an answer is not cached). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cmd/jrep/main.go`](https://github.com/K1erans/Jrep/blob/d7f343afe1a562c4b9d4ba2860b484087ad2458e/cmd/jrep/main.go) at the pinned commit. |

## When to use

- Find where a behaviour lives in an unfamiliar codebase when you don't know the identifiers, from a terminal or a coding agent.
- Mismatch: exact strings or symbol names; use rg for those.

## How it works

`cmd/jrep/main.go` reads `TYPESAFE_API_KEY` and calls the System One API at `TYPESAFE_BASE_URL` (default `https://api.typesafe.ai`) through the author's jinter library; an adaptive limiter backs off on HTTP 429 and 529. `--refine` re-asks only the 300 best chunks from a previous question. Integration evidence: [`cmd/jrep/main.go`](https://github.com/K1erans/Jrep/blob/d7f343afe1a562c4b9d4ba2860b484087ad2458e/cmd/jrep/main.go).

## Get started

Build and install, then search a folder.

```sh
git clone https://github.com/K1erans/Jrep && cd Jrep
export TYPESAFE_API_KEY=...
make install
jrep "sends the password reset email" src/auth
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/K1erans/Jrep/blob/d7f343afe1a562c4b9d4ba2860b484087ad2458e/README.md](https://github.com/K1erans/Jrep/blob/d7f343afe1a562c4b9d4ba2860b484087ad2458e/README.md)
- Plan: [github.com/K1erans/Jrep/blob/d7f343afe1a562c4b9d4ba2860b484087ad2458e/PLAN.md](https://github.com/K1erans/Jrep/blob/d7f343afe1a562c4b9d4ba2860b484087ad2458e/PLAN.md)

## Limits and data handling

Code chunks are sent to TypeSafe; the cache is local. Speed and savings figures are the author's. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit d7f343afe1a5](https://github.com/K1erans/Jrep/tree/d7f343afe1a562c4b9d4ba2860b484087ad2458e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
