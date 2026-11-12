# Shot grouping with decision models (grouping film shots for color grading with Jev yes/no questions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and data for the write-up "Ask, Don't Embed": every pair of the 124 shots of Tears of Steel gets a yes/no question (same scene? same grade?) sent to Jev 1.14 and Cloudflare Clef, and the probabilities are clustered into scenes and grade groups, with saved answers, hand labels, costs and timings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JasonMakes801/shot-grouping-decision-models) |
| Maintainer | [JasonMakes801](https://github.com/JasonMakes801). Independently curated. |
| Format | Reproduction scripts and data (Python; code MIT, stills CC BY 3.0 Blender Foundation) |
| Requirements | Python and `requirements.txt`; scoring the saved answers needs no key, re-asking needs `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/JasonMakes801/shot-grouping-decision-models/blob/c6efa41e21f02da4619dbbe5311c52233bb9f755/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/JasonMakes801/shot-grouping-decision-models/blob/c6efa41e21f02da4619dbbe5311c52233bb9f755/jev.py) at the pinned commit. |

## When to use

- See a worked example of pairwise yes/no questions instead of embeddings.
- Reuse the pattern for grouping images or clips.
- Mismatch: one film, one experiment; OpenRouter's decisions endpoint is alpha.

## How it works

`jev.py` posts state and questions (with images) to OpenRouter's decisions endpoint with model `typesafe/jev-1.14`; `reproduce.sh` scores the saved answers against the hand labels, and `--run` asks Jev again. Integration evidence: [`jev.py`](https://github.com/JasonMakes801/shot-grouping-decision-models/blob/c6efa41e21f02da4619dbbe5311c52233bb9f755/jev.py).

## Get started

Install the requirements and score the saved answers offline.

```sh
pip install -r requirements.txt
./reproduce.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up: [fullstate.dev/work/decision-models/](https://fullstate.dev/work/decision-models/)

## Limits and data handling

Re-running sends the stills to OpenRouter/TypeSafe (and Cloudflare for Clef) on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit c6efa41e21f0](https://github.com/JasonMakes801/shot-grouping-decision-models/tree/c6efa41e21f02da4619dbbe5311c52233bb9f755). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
