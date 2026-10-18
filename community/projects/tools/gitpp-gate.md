# gitpp-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Confidence-gated nudging for the git.pp fold: asks TypeSafe Jev before nudging, fails closed, and logs the decision so automation cannot push without a typed yes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SuperInstance/gitpp-gate) |
| Maintainer | [SuperInstance](https://github.com/SuperInstance). Independently curated. |
| Format | Small Node/JS gate scripts |
| Requirements | Node.js; TYPESAFE_API_KEY; git.pp / local fold context. |
| License | [MIT](https://github.com/SuperInstance/gitpp-gate/blob/67db87b7d2fab8b2de1b1a68ca6b2cafa9dfe34b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/SuperInstance/gitpp-gate/blob/67db87b7d2fab8b2de1b1a68ca6b2cafa9dfe34b/src/jev.mjs) at the pinned commit. |

## When to use

- Gate automated git nudges behind a Jev decision.
- Prefer fail-closed behavior with logged typed answers.
- Mismatch: thin gate for a specific fold workflow, not a general CI product.

## How it works

`src/jev.mjs` is a thin TypeSafe Jev client used by the gate before a nudge. Control stays in code; Jev only answers the typed question. Integration evidence: [`src/jev.mjs`](https://github.com/SuperInstance/gitpp-gate/blob/67db87b7d2fab8b2de1b1a68ca6b2cafa9dfe34b/src/jev.mjs).

## Get started

Clone, set TYPESAFE_API_KEY, and wire the gate into the git.pp nudge path per README.

```sh
git clone https://github.com/SuperInstance/gitpp-gate && cd gitpp-gate
# set TYPESAFE_API_KEY; see README for hook wiring
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README fail-closed gate description
- src/jev.mjs client

## Limits and data handling

Niche git.pp integration. Live calls require a TypeSafe key.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 67db87b7d2fa](https://github.com/SuperInstance/gitpp-gate/tree/67db87b7d2fab8b2de1b1a68ca6b2cafa9dfe34b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
