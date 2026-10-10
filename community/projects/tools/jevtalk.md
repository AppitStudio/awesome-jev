# JevTalk

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment that gets Jev to answer questions in plain English by spelling answers one choice at a time, drafting in parallel and picking the best finished draft.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Promptable-Technologies/jevtalk) |
| Maintainer | [Promptable-Technologies](https://github.com/Promptable-Technologies). Independently curated. |
| Format | Python script |
| Requirements | Python 3; Jev access via OpenRouter or TypeSafe. |
| License | [MIT](https://github.com/Promptable-Technologies/jevtalk/blob/7b9f93bd7c2ca80e150ae8dfdafcec460569a144/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Explore how far a choice-only decision model can be pushed into short text generation.
- Mismatch: research toy; 30-150 Jev calls per answer and benchmark grading is done by Jev itself.

## How it works

Jev picks answer length, a key word, then the next word among candidates plus a done option, with grammar checks and a final polish pass. (Summarized from the upstream [README](https://github.com/Promptable-Technologies/jevtalk/blob/7b9f93bd7c2ca80e150ae8dfdafcec460569a144/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `python3 jevtalk.py "What color is grass?"` with your key configured.

## Limits and data handling

Questions are sent to the hosted Jev API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 7b9f93bd7c2c](https://github.com/Promptable-Technologies/jevtalk/tree/7b9f93bd7c2ca80e150ae8dfdafcec460569a144). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
