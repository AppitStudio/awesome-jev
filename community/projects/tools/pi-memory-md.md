# pi-memory-md (git-backed markdown memory for pi with TypeSafe Jev relevance checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Letta-like memory for the pi coding agent using git-backed markdown files; its tape-relevance step can use TypeSafe Jev (direct or via OpenRouter) to decide which memories are relevant to recall.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VandeeFeng/pi-memory-md) |
| Maintainer | [VandeeFeng](https://github.com/VandeeFeng). Independently curated. |
| Format | pi extension (TypeScript, MIT) |
| Requirements | pi, git, and optionally a TypeSafe or OpenRouter key. |
| License | [MIT](https://github.com/VandeeFeng/pi-memory-md/blob/3002f4e58a14c02876d1b343f4737465fc4abcb4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tape/tape-relevance.ts`](https://github.com/VandeeFeng/pi-memory-md/blob/3002f4e58a14c02876d1b343f4737465fc4abcb4/tape/tape-relevance.ts) at the pinned commit. |

## When to use

- Give pi persistent memory across sessions.
- Recall only relevant memories using Jev.
- Mismatch: Jev relevance is optional.

## How it works

`tape/tape-relevance.ts` defaults to `jev-latest` on TypeSafe or `typesafe/jev-1.13` on OpenRouter; tests cover both `systemone` endpoints. Integration evidence: [`tape/tape-relevance.ts`](https://github.com/VandeeFeng/pi-memory-md/blob/3002f4e58a14c02876d1b343f4737465fc4abcb4/tape/tape-relevance.ts).

## Get started

Install the extension into pi per README and optionally configure a Jev key for relevance.

```sh
git clone https://github.com/VandeeFeng/pi-memory-md.git && cd pi-memory-md
export TYPESAFE_API_KEY=...
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/VandeeFeng/pi-memory-md/blob/3002f4e58a14c02876d1b343f4737465fc4abcb4/README.md](https://github.com/VandeeFeng/pi-memory-md/blob/3002f4e58a14c02876d1b343f4737465fc4abcb4/README.md)

## Limits and data handling

Memory snippets checked for relevance are sent to TypeSafe/OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 3002f4e58a14](https://github.com/VandeeFeng/pi-memory-md/tree/3002f4e58a14c02876d1b343f4737465fc4abcb4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
