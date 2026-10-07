# system-one-parsers

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Lab building a domain-free Universal Dependencies parser out of many small Jev questions — one Choice per word for part of speech, then head and relation choices — decoded into a tree in plain code, with offline oracle/dry clients, recorded runs and a rules-only floor; work in progress.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Engid/system-one-parsers) |
| Maintainer | [Engid](https://github.com/Engid). Independently curated. |
| Format | Bun/TypeScript research repo: parser strategies, Jev clients (live, mock, oracle, recording) and eval harness |
| Requirements | Bun; `bun run fetch-ud` downloads UD English EWT (CC BY-SA 4.0, not redistributed); `TYPESAFE_API_KEY` in `.env` for live evals. |
| License | [MIT](https://github.com/Engid/system-one-parsers/blob/7f73050ef895910bba96beaec5b8f1b8bbb43efe/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Explore decomposing a structured NLP task into many typed Jev questions and decoding the answers in code.
- Reuse the live/mock/oracle/recording client pattern for replayable Jev experiments.
- Mismatch: work in progress; one 125-sentence dev sample so far, and long sentences cost ~76k input tokens each.

## How it works

Tokenization is code; [`src/strategies/head-selection/questions.ts`](https://github.com/Engid/system-one-parsers/blob/7f73050ef895910bba96beaec5b8f1b8bbb43efe/src/strategies/head-selection/questions.ts) asks a Choice over the 17 UPOS tags per word and then head/relation questions; [`src/decode/cle.ts`](https://github.com/Engid/system-one-parsers/blob/7f73050ef895910bba96beaec5b8f1b8bbb43efe/src/decode/cle.ts) builds a maximum spanning tree. Clients in [`src/jev/`](https://github.com/Engid/system-one-parsers/tree/7f73050ef895910bba96beaec5b8f1b8bbb43efe/src/jev) switch between live API, mock, gold-tree oracle and recorded replay, and [`eval/run.ts`](https://github.com/Engid/system-one-parsers/blob/7f73050ef895910bba96beaec5b8f1b8bbb43efe/eval/run.ts) scores UPOS/UAS/LAS.

## Get started

Offline first (no API calls):

```sh
git clone https://github.com/Engid/system-one-parsers.git && cd system-one-parsers
bun install
bun run fetch-ud
bun test
bun run eval --client oracle   # plumbing check, should be 100%
bun run eval --client dry      # shows questions and request size, no network
```

Offline clients are free; live evals send sentences to TypeSafe and are billed to your key (input-token heavy).

## Examples and demos

- README *First Jev sample* (2026-10-06, jev-1.13.0): head-selection UPOS 92.0%, UAS 51.3%, LAS 40.0% on 125 dev sentences vs a rules floor — maintainer-reported.
- Error analysis script: [`eval/analyze.ts`](https://github.com/Engid/system-one-parsers/blob/7f73050ef895910bba96beaec5b8f1b8bbb43efe/eval/analyze.ts).

## Limits and data handling

Numbers come from one recorded maintainer run; the README quotes only recorded results. Live mode sends treebank sentences to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 7f73050ef895](https://github.com/Engid/system-one-parsers/tree/7f73050ef895910bba96beaec5b8f1b8bbb43efe). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
