# gbrain-evals

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Benchmark suite for the gbrain agent-memory system, including a matched-pair System One report on where TypeSafe Jev (`jev-1.13.0`) helps or hurts nine memory decision slots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/garrytan/gbrain-evals) |
| Maintainer | [garrytan](https://github.com/garrytan). Independently curated. |
| Format | Evaluation repository (BrainBench runners, receipts, reports) |
| Requirements | Bun. Offline checks need no key; replaying Jev slots needs a gbrain checkout of the `feat/system-one-v1` branch and a TypeSafe key. Some other categories call paid model APIs. |
| License | [MIT](https://github.com/garrytan/gbrain-evals/blob/c40123c52b3f2873418f974e22f7db90d8b89e9a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Decide whether a small decision model is worth wiring into an agent-memory pipeline, using a published negative-and-positive result rather than a single headline.
- Replay a Jev slot against your own gbrain checkout before enabling it.
- Mismatch: this is an evaluation repo; the Jev slots themselves live on gbrain's `feat/system-one-v1` branch, not on gbrain master.

## How it works

gbrain's System One work adds nine slots where Jev can replace a fixed rule or larger LLM (triage, rerank, evidence trimming, abstention, intent, recall-needed, grounding, injection, contradiction). The report compares matched pairs on September 30, 2026; gbrain's branch turns on only triage (S7) and contradiction (S9) via `gbrain decide enable --recommended`, and only when a key is present ([System One report](https://github.com/garrytan/gbrain-evals/blob/c40123c52b3f2873418f974e22f7db90d8b89e9a/docs/benchmarks/2026-09-30-system-one-jev.md)).

## Get started

Run the free offline checks from the repository root, then verify the System One record (no model API):

```sh
git clone https://github.com/garrytan/gbrain-evals && cd gbrain-evals
bun install --frozen-lockfile
bun run eval:query:validate
bun eval/runner/system-one-jev.ts verify   # offline check of the Sept 30 record
```

The offline commands make no API calls; `system-one-jev.ts run` replays against a gbrain checkout and needs a TypeSafe key (billed usage).

## Examples and demos

- [System One report](https://github.com/garrytan/gbrain-evals/blob/c40123c52b3f2873418f974e22f7db90d8b89e9a/docs/benchmarks/2026-09-30-system-one-jev.md): per-slot verdicts, e.g. triage missed 0/18 buried decisions vs 10/18 but sent more routine chats to the writer; contradiction sweep found 94/97 updated facts. Maintainer-measured.
- [eval/README.md](https://github.com/garrytan/gbrain-evals/blob/c40123c52b3f2873418f974e22f7db90d8b89e9a/eval/README.md) for every runner and its cost profile.

## Limits and data handling

All Jev numbers are maintainer-reported from one evaluation; labels come from generators, benchmark annotations or an LLM, not people. The repository documents its own corrections of earlier figures. Jev slots are off without a key and live on a gbrain branch, not a release.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit c40123c52b3f](https://github.com/garrytan/gbrain-evals/tree/c40123c52b3f2873418f974e22f7db90d8b89e9a). Inspected the README, the System One report and eval/README at the pinned commit; no benchmark, install, or live inference was run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
