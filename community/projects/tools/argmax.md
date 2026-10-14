# argmax

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Unity swarm-programming RTS where four commanders, including TypeSafe Jev answering typed battlefield questions, emit the same decision type.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WalterGropius/argmax) |
| Maintainer | [WalterGropius](https://github.com/WalterGropius). Independently curated. |
| Format | Unity 6 game + SpacetimeDB server (C#) |
| Requirements | Unity 6; TypeSafe key for the Jev commander. |
| License | [MIT](https://github.com/WalterGropius/argmax/blob/a1fe742b5617bd092c19f8c8234dec2395e32ef1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`shared/Argmax.Sim/Runtime/JevBrief.cs`](https://github.com/WalterGropius/argmax/blob/a1fe742b5617bd092c19f8c8234dec2395e32ef1/shared/Argmax.Sim/Runtime/JevBrief.cs) at the pinned commit. |

## When to use

- Pit Jev against Argot metaprograms, an ML-Agents policy or humans.
- Mismatch: movement uses a local Jev-style softmax, not live Jev calls.

## How it works

The simulation summarizes battlefield state; the Jev commander answers typed questions that map to a `MetaDecision`. Arena tools run tournaments and Jev-vs-AI matches. Integration evidence: [`shared/Argmax.Sim/Runtime/JevBrief.cs`](https://github.com/WalterGropius/argmax/blob/a1fe742b5617bd092c19f8c8234dec2395e32ef1/shared/Argmax.Sim/Runtime/JevBrief.cs).

## Get started

From the upstream README (not run on the review host):

```sh
# open client/ in Unity 6; see README for server setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Arena CLI: `tools/Arena/`.
- Docs: `docs/`.

## Limits and data handling

Battle summaries go to TypeSafe for the Jev commander.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit a1fe742b5617](https://github.com/WalterGropius/argmax/tree/a1fe742b5617bd092c19f8c8234dec2395e32ef1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
