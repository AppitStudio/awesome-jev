# Jev Review Action

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Configurable GitHub Action that reviews catalog-style submissions or pull-request diffs with TypeSafe Jev only—no text-generation model—then updates one PR comment from a fixed template.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fatwang2/jev-review-action) |
| Maintainer | [fatwang2](https://github.com/fatwang2). Independently curated; this entry is not an upstream submission or endorsement. Not an official TypeSafe product. |
| Format | GitHub Action (`action.yml`) + Node.js ≥ 22 review engine (`jev-review-action` 0.2.0). |
| Requirements | Workflow permissions for contents/pull-requests as documented; `TYPESAFE_API_KEY` (or Vercel/Cloudflare Jev provider inputs). Policy JSON on the default branch. |
| License | [MIT](https://github.com/fatwang2/jev-review-action/blob/929b99227431f0a35752d4860e9ba7c36abe5bda/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `node --test` inspected. Live TypeSafe and live GitHub Action runs were not executed. Distinct from [Jev Review](jev-review.md) (MCP) and [jev-pr-judge](jev-pr-judge.md). |

## When to use

Use it when you want policy-driven catalog or PR classification comments powered only by typed Jev judgments. Prefer [jev-pr-judge](jev-pr-judge.md) for its Next.js UI + sticky-comment product shape, or [Jev Review](jev-review.md) for an MCP coding-agent loop.

## How it works

[`src/typesafe.mjs`](https://github.com/fatwang2/jev-review-action/blob/929b99227431f0a35752d4860e9ba7c36abe5bda/src/typesafe.mjs) posts to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with provider fallback order configurable in `action.yml`. Policies under `examples/` define categories/questions; application code owns discovery of README/source evidence, decision mapping, and the single PR comment update.

## Get started

```sh
git clone https://github.com/fatwang2/jev-review-action.git
cd jev-review-action
git checkout 929b99227431f0a35752d4860e9ba7c36abe5bda
npm test
```

Live wiring: copy an example policy to `.github/jev-review.json`, set `TYPESAFE_API_KEY`, and add the upstream workflow (pin the action to a full commit SHA for production). That path calls TypeSafe and GitHub APIs.

## Examples and demos

- [`examples/catalog.json`](https://github.com/fatwang2/jev-review-action/blob/929b99227431f0a35752d4860e9ba7c36abe5bda/examples/catalog.json) and [`examples/pull-request.json`](https://github.com/fatwang2/jev-review-action/blob/929b99227431f0a35752d4860e9ba7c36abe5bda/examples/pull-request.json).
- Offline tests under `test/` with fake fetch (52 tests at reviewed revision).

## Limits and data handling

PR metadata, patches, and fetched repository file contents used as evidence leave GitHub runners toward the configured Jev provider. Comments are template-rendered—not model-written prose. Pin action revisions; do not embed secrets in policies.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 929b992](https://github.com/fatwang2/jev-review-action/tree/929b99227431f0a35752d4860e9ba7c36abe5bda): MIT, package 0.2.0. AI-assisted source review of `action.yml`, core modules, and README. **`npm test` / `node --test`**: **52 passed**. No live TypeSafe or Actions runs.

Related: [jev-pr-judge](jev-pr-judge.md), [Jev Review](jev-review.md), [Jev Review (Dev Agrawal)](jev-review-devagrawal.md).
