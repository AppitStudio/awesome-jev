# When Accuracy Doesn't Move by David M. Woollard (research artifact showing Jev's probabilities shift under misleading bar charts while its answer stays correct)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research artifact for Experimental Note 01: Jev is asked which of two cities had the larger ridership increase, with the numbers fixing the answer and a bar column whose lengths are progressively distorted. Jev picked the correct city in every successful call, yet its probability fell from 1.00 to 0.72 in one arm, so accuracy alone hid the effect. Includes stimuli, prompts, frozen observations and a script that recomputes every number offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/woollard/note-001) |
| Maintainer | [Dave Woollard](https://github.com/woollard). Independently curated. |
| Format | Python research artifact (stdlib) |
| Requirements | Python 3 for the offline reproduction; a Vercel AI Gateway key only to re-run the paid experiment. |
| License | [Apache-2.0](https://github.com/woollard/note-001/blob/977b1494fa4dde338b09319da84b9e94b6901444/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`experiment/run_jev.py`](https://github.com/woollard/note-001/blob/977b1494fa4dde338b09319da84b9e94b6901444/experiment/run_jev.py) at the pinned commit. |

## When to use

- Anyone evaluating decision models who wants an example of measuring probability shifts, not just argmax accuracy.
- Mismatch: general Jev benchmarks; this is one narrow chart-distortion experiment.

## How it works

`experiment/run_jev.py` sends each manifest state as a two-option `choice` question to Jev (`typesafe-ai/jev` via Vercel AI Gateway) and records the returned distribution; `analysis/reproduce_note.py` recomputes the note from the frozen results. Integration evidence: [`experiment/run_jev.py`](https://github.com/woollard/note-001/blob/977b1494fa4dde338b09319da84b9e94b6901444/experiment/run_jev.py).

## Get started

Reproduce the reported numbers from the frozen data, with no model calls.

```sh
git clone https://github.com/woollard/note-001 && cd note-001
python3 analysis/reproduce_note.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Reproduction steps: [github.com/woollard/note-001#reproducing-the-reported-results](https://github.com/woollard/note-001#reproducing-the-reported-results)

## Limits and data handling

One task, two counterbalanced arms and a small number of calls collected on 2026-09-28; the live experiment has not been re-run since. Re-running it calls a paid third-party API.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 977b1494fa4d](https://github.com/woollard/note-001/tree/977b1494fa4dde338b09319da84b9e94b6901444). Inspected the README, LICENSE, `experiment/run_jev.py` and the reproduction script at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
