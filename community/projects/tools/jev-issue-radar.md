# jev-issue-radar

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local, read-only GitHub duplicate-issue triage dashboard: lexical retrieval picks candidates; TypeSafe Jev (via OpenRouter Decisions) chooses relationship and evidence line IDs; maintainers inspect original passages before acting. Distinct from [Metis](metis.md) (label/missing-detail Action on new issues).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Patrick-SCH03/jev-issue-radar) |
| Maintainer | [Patrick-SCH03](https://github.com/Patrick-SCH03). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js **0.1.1** loopback HTTP server + static dashboard (no production npm dependencies). |
| Requirements | Node.js **≥ 22**. Live comparisons need `OPENROUTER_API_KEY` on the server. GitHub REST is read-only. |
| License | [MIT](https://github.com/Patrick-SCH03/jev-issue-radar/blob/5878ba97d70d8aed10a2a628f224a8612d4e870b/LICENSE). OpenRouter/Jev usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected; live OpenRouter/GitHub scans were not run. Experimental MVP per upstream. |

## When to use

Use it when you want **evidence-linked duplicate/related judgments** on public issues without auto-closing or labeling. Prefer [Metis](metis.md) for automated category labels and missing-detail comments on new issues.

## How it works

[`lib/jev.mjs`](https://github.com/Patrick-SCH03/jev-issue-radar/blob/5878ba97d70d8aed10a2a628f224a8612d4e870b/lib/jev.mjs) posts Choice questions for `typesafe/jev-1.13` to `https://openrouter.ai/api/alpha/decisions`. Application code validates chosen evidence IDs, confidence (≥ 0.8 for strong duplicate display), and reason consistency before showing passages. Retrieval is title-weighted lexical overlap only—not a duplicate probability.

## Get started

```sh
git clone https://github.com/Patrick-SCH03/jev-issue-radar.git
cd jev-issue-radar
git checkout 5878ba97d70d8aed10a2a628f224a8612d4e870b
npm test
npm start   # open the local dashboard; no-key demo available
# Set OPENROUTER_API_KEY on the server before paid comparisons.
```

Live runs send issue text to OpenRouter/Jev and can incur charges; this listing ran offline tests only.

## Examples and demos

- Offline `npm test` — **48 passed** on the review host.
- Upstream no-key demo UI and `docs/VALIDATION.md` (synthetic smoke; quality on real repos not established).

## Limits and data handling

Issue bodies/titles leave the host on live comparisons. The tool never mutates GitHub. Cross-language or differently worded duplicates may never reach Jev if retrieval misses them. Upstream cost/latency figures were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 5878ba9](https://github.com/Patrick-SCH03/jev-issue-radar/tree/5878ba97d70d8aed10a2a628f224a8612d4e870b): **0.1.1**, MIT. AI-assisted source review of README, LICENSE, `lib/jev.mjs`, `server.mjs`, and `package.json`. Ran `npm test` (48 pass). No live OpenRouter or GitHub API calls.

Related: [Metis](metis.md), [jev-pr-judge](jev-pr-judge.md), [Moongate](moongate.md).
