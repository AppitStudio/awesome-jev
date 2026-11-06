# jev-semantic-merge-gate (GitHub Action that enforces declared semantic merge policies with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that loads a declared semantic merge policy, diffs against a base ref, and asks TypeSafe Jev (`jev-1.13.0`) whether the change is safe enough to merge, with a configurable confidence threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-semantic-merge-gate) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | GitHub Action (Node.js, MIT) |
| Requirements | A GitHub Actions workflow, a policy file (default `.jev/policy.json`), and a `typesafe-api-key` input / `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/action.js`](https://github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/src/action.js) at the pinned commit. |

## When to use

- Block merges that violate declared semantic policies.
- Keep exact changed-line evidence next to the Jev verdict.
- Mismatch: policy quality determines usefulness; threshold defaults to 0.75.

## How it works

`src/action.js` maps the Action input into `TYPESAFE_API_KEY` and calls `run()` with model `jev-1.13.0` against the policy and diff. Integration evidence: [`src/action.js`](https://github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/src/action.js).

## Get started

From the upstream README (not run on the review host):

```sh
# workflow snippet (see upstream action.yml)
# uses: gbesse/jev-semantic-merge-gate@...
# with:
#   typesafe-api-key: ${{ secrets.TYPESAFE_API_KEY }}
#   policy: .jev/policy.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- action.yml: [github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/action.yml](https://github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/action.yml)
- README: [github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/README.md](https://github.com/gbesse/jev-semantic-merge-gate/blob/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1/README.md)

## Limits and data handling

Diff hunks and policy text are sent to TypeSafe on your key. Treat the gate as advisory automation under your branch rules.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit c39c4961dd84](https://github.com/gbesse/jev-semantic-merge-gate/tree/c39c4961dd843ac9b0a3eebe9e8d5b54cc53f6f1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
