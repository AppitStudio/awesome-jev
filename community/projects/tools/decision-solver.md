# decision-solver (combine Jev preferences with finite constraints and verifiable search)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Combines separate Jev option preferences with finite constraints and exact bounded search, without claiming a joint probability. Uses model `jev-1.13.0` in its Jev client pack.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/decision-solver) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js library/CLI (MIT) |
| Requirements | Node.js and `TYPESAFE_API_KEY` for live preference queries. |
| License | [MIT](https://github.com/gbesse/decision-solver/blob/7136222cb1359b6a0a87bd7215d38f2a674bf3d8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/gbesse/decision-solver/blob/7136222cb1359b6a0a87bd7215d38f2a674bf3d8/src/jev.mjs) at the pinned commit. |

## When to use

- Rank constrained options with typed Jev preferences.
- Keep search exact and preferences separate from feasibility.
- Mismatch: not a single joint probabilistic model over the full plan.

## How it works

`src/jev.mjs` builds preference packs pinned to `jev-1.13.0` and queries TypeSafe; the solver combines those preferences with finite constraints. Integration evidence: [`src/jev.mjs`](https://github.com/gbesse/decision-solver/blob/7136222cb1359b6a0a87bd7215d38f2a674bf3d8/src/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
# see README for solving a constrained preference problem
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/decision-solver/blob/7136222cb1359b6a0a87bd7215d38f2a674bf3d8/README.md](https://github.com/gbesse/decision-solver/blob/7136222cb1359b6a0a87bd7215d38f2a674bf3d8/README.md)

## Limits and data handling

Preference queries send option text to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 7136222cb135](https://github.com/gbesse/decision-solver/tree/7136222cb1359b6a0a87bd7215d38f2a674bf3d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
