# fish.career by P. Barrett Little (local-first job search MCP server and CLI where Jev scores each posting against your profile)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turns job-board feeds into a small ranked table with the reasons attached: Jev answers rubric questions per posting, deterministic code ranks, and the ranking is measured against your own judgment (17 labelled hard cases, pairwise accuracy 92.3% in the recorded run). Includes a LangGraph example with a human-review interrupt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pblittle/fish-career) |
| Maintainer | [P. Barrett Little](https://github.com/pblittle). Independently curated. |
| Format | Node.js MCP server and CLI (TypeScript; install from source) |
| Requirements | Node 20.12+ and a TypeSafe API key for live judging (the quality report runs offline). |
| License | [MIT](https://github.com/pblittle/fish-career/blob/4572362d2547aca129e2680f4b21bf6b3a5a92cc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`fish-career/src/adapters/judge/jev.ts`](https://github.com/pblittle/fish-career/blob/4572362d2547aca129e2680f4b21bf6b3a5a92cc/fish-career/src/adapters/judge/jev.ts) at the pinned commit. |

## When to use

- Rank job postings against your profile with explainable scores and a measurable fit to your judgment.
- Mismatch: bulk applying; it ranks and explains, you decide.

## How it works

`fish-career/src/adapters/judge/jev.ts` posts rubric questions to `https://api.typesafe.ai/v1/systemone`, retries on 429/5xx and validates every answer so a malformed one fails the posting instead of being clamped. Integration evidence: [`fish-career/src/adapters/judge/jev.ts`](https://github.com/pblittle/fish-career/blob/4572362d2547aca129e2680f4b21bf6b3a5a92cc/fish-career/src/adapters/judge/jev.ts).

## Get started

Build from source and run the offline quality report, then follow the first-ranked-table tutorial.

```sh
git clone https://github.com/pblittle/fish-career.git && cd fish-career
npm ci --prefix fish-career && npm run build --prefix fish-career
npm install -g ./fish-career
fish quality
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quality findings: [github.com/pblittle/fish-career/blob/4572362d2547aca129e2680f4b21bf6b3a5a92cc/specs/quality.md](https://github.com/pblittle/fish-career/blob/4572362d2547aca129e2680f4b21bf6b3a5a92cc/specs/quality.md)
- LangGraph example: [github.com/pblittle/fish-career/tree/4572362d2547aca129e2680f4b21bf6b3a5a92cc/examples/langgraph](https://github.com/pblittle/fish-career/tree/4572362d2547aca129e2680f4b21bf6b3a5a92cc/examples/langgraph)

## Limits and data handling

Posting text and your profile are sent to TypeSafe when judging live. The quality metrics come from the author's small labelled set.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 4572362d2547](https://github.com/pblittle/fish-career/tree/4572362d2547aca129e2680f4b21bf6b3a5a92cc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
