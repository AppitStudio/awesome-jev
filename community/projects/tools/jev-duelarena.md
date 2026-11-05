# jev-duelarena (criterion-by-criterion text duels and elimination brackets judged by Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Runs visible criterion-by-criterion text duels and progressive elimination brackets where Jev scores each criterion. Includes an opt-in live smoke against api.typesafe.ai that spends one paid request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-duelarena) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js tooling (MIT) |
| Requirements | Node.js and `TYPESAFE_API_KEY` for live runs (offline fixtures available). |
| License | [MIT](https://github.com/gbesse/jev-duelarena/blob/425e43e608b091bd3311730c83643a0760fe1198/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-client.mjs`](https://github.com/gbesse/jev-duelarena/blob/425e43e608b091bd3311730c83643a0760fe1198/src/jev-client.mjs) at the pinned commit. |

## When to use

- Compare two texts on explicit criteria with typed Jev scores.
- Run elimination brackets without inventing joint probabilities.
- Mismatch: live smoke is opt-in and costs a paid request.

## How it works

`src/jev-client.mjs` talks to TypeSafe; `scripts/live-smoke.mjs` refuses to run without `TYPESAFE_API_KEY` and is never meant for CI. Integration evidence: [`src/jev-client.mjs`](https://github.com/gbesse/jev-duelarena/blob/425e43e608b091bd3311730c83643a0760fe1198/src/jev-client.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
node bin/jev-duelarena.mjs --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-duelarena/blob/425e43e608b091bd3311730c83643a0760fe1198/README.md](https://github.com/gbesse/jev-duelarena/blob/425e43e608b091bd3311730c83643a0760fe1198/README.md)

## Limits and data handling

Duel texts are sent to TypeSafe on live runs. Do not enable live-smoke in CI.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 425e43e608b0](https://github.com/gbesse/jev-duelarena/tree/425e43e608b091bd3311730c83643a0760fe1198). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
