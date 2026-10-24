# JevBench by NavdeeepSinghh (live speed, cost and accuracy race of Jev vs Claude)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Next.js app and CLI that asks Jev and Claude the same typed questions, times each call on the server, prices it at list rates and grades both on 104 hand-labelled inputs, with an arena, a benchmark runner, a cost-at-scale view and shareable result cards.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NavdeeepSinghh/JEV-working-) |
| Maintainer | [NavdeeepSinghh](https://github.com/NavdeeepSinghh). Independently curated. |
| Format | Web app and CLI (Next.js, TypeScript) |
| Requirements | Node.js; TypeSafe and Anthropic keys for live runs (simulated mode without keys). |
| License | [MIT](https://github.com/NavdeeepSinghh/JEV-working-/blob/d03a6e661517c3c51560bf8c23d1b7fd4c0deb12/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/server/jev.ts`](https://github.com/NavdeeepSinghh/JEV-working-/blob/d03a6e661517c3c51560bf8c23d1b7fd4c0deb12/lib/server/jev.ts) at the pinned commit. |

## When to use

- Check launch speed and cost claims against your own workload.
- Show a team how a decision model compares with a small LLM.
- Mismatch: simulated mode uses illustrative numbers and is stamped as such.

## How it works

`lib/server/jev.ts` uses `@typesafe-ai/sdk` (`choice`, `score`, `noul`) with `jev-latest`; the same scenario spec becomes a JSON-schema prompt for Claude, and only provider time is measured. Integration evidence: [`lib/server/jev.ts`](https://github.com/NavdeeepSinghh/JEV-working-/blob/d03a6e661517c3c51560bf8c23d1b7fd4c0deb12/lib/server/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/NavdeeepSinghh/JEV-working-.git
cd JEV-working- && npm install
npm run dev
npm run bench
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with method: [github.com/NavdeeepSinghh/JEV-working-#readme](https://github.com/NavdeeepSinghh/JEV-working-#readme)

## Limits and data handling

Benchmark inputs go to TypeSafe and Anthropic. Any numbers are the user's own runs.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit d03a6e661517](https://github.com/NavdeeepSinghh/JEV-working-/tree/d03a6e661517c3c51560bf8c23d1b7fd4c0deb12). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
