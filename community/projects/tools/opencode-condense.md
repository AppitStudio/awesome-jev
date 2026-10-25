# opencode-condense (opencode context pruning by a scorer model, local or Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

opencode plugin that keeps long sessions alive without summaries: a scorer model decides which old tool calls and results can be dropped or truncated while user and assistant text stays verbatim; designed for a small local GGUF scorer, with TypeSafe Jev as the built-in default endpoint.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/condottab/opencode-condense) |
| Maintainer | [condottab](https://github.com/condottab). Independently curated. |
| Format | opencode plugin (TypeScript) |
| Requirements | Node 18+ and opencode 1.18.31+; a local OpenAI-compatible scorer, or a TypeSafe key for Jev. |
| License | [MIT](https://github.com/condottab/opencode-condense/blob/a1e9036a51a7c4372042adec0bbad07a3006619c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/request.ts`](https://github.com/condottab/opencode-condense/blob/a1e9036a51a7c4372042adec0bbad07a3006619c/src/request.ts) at the pinned commit. |

## When to use

- Keep a long opencode session past its context window without losing paths and errors.
- Run the scorer locally so the transcript never leaves the machine.
- Mismatch: the author's design point is a local scorer; Jev is the default only when no base URL is set.

## How it works

`src/request.ts` targets `https://api.typesafe.ai/v1/systemone` (`jev-latest`) unless `baseUrl` points at your own server; passes run in the background after 60% occupancy with cooldowns. Integration evidence: [`src/request.ts`](https://github.com/condottab/opencode-condense/blob/a1e9036a51a7c4372042adec0bbad07a3006619c/src/request.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/condottab/opencode-condense
# add opencode/entry.ts to "plugin" in opencode.json with { "baseUrl": ..., "model": ... }
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/condottab/opencode-condense#readme](https://github.com/condottab/opencode-condense#readme)

## Limits and data handling

With Jev, old tool calls and results from the session go to TypeSafe; with a local scorer nothing leaves the machine.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit a1e9036a51a7](https://github.com/condottab/opencode-condense/tree/a1e9036a51a7c4372042adec0bbad07a3006619c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
