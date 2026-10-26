# Séance collusion detection (hard-negative benchmark for LLM collusion monitors, with Jev as one monitor)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Proposed benchmark of hard negatives for LLM collusion monitors, built for an Apart Research sprint: four LLM players play a guessing game where a secret pair may pass information through ordinary talk, and monitors, including Jev asked plainly and with a plus-factor briefing, must say which pair colludes or none; an explorer shows every game.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jvargas2/seance-collusion-detection) |
| Maintainer | [jvargas2](https://github.com/jvargas2). Independently curated. |
| Format | Python research code with game records and an explorer |
| Requirements | Python with uv; keys only for new monitor or player runs (TypeSafe for the Jev monitor); scoring reruns from committed predictions. |
| License | [MIT](https://github.com/jvargas2/seance-collusion-detection/blob/98c19d4659741c8b622f9f2e93e603dbf62e4b78/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/seance/jev.py`](https://github.com/jvargas2/seance-collusion-detection/blob/98c19d4659741c8b622f9f2e93e603dbf62e4b78/src/seance/jev.py) at the pinned commit. |

## When to use

- Measure whether your collusion monitor wrongly accuses honest, cooperative tables.
- Compare a decision model against LLM monitors on the same frozen test set.
- Mismatch: one game and a sprint-sized study; results are the author's.

## How it works

`src/seance/jev.py` sends the public game record with a Choice over the six pairs plus none to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, resolved to `jev-1.14.0` in the logs) and stores the probabilities as monitor predictions. Integration evidence: [`src/seance/jev.py`](https://github.com/jvargas2/seance-collusion-detection/blob/98c19d4659741c8b622f9f2e93e603dbf62e4b78/src/seance/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv run --group report python -m seance.final --run runs/final --monitor "My monitor=my_monitor.jsonl" --out my_scores
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Explorer: [jvargas2.github.io/seance-collusion-detection/explorer/](https://jvargas2.github.io/seance-collusion-detection/explorer/)
- README: [github.com/jvargas2/seance-collusion-detection#readme](https://github.com/jvargas2/seance-collusion-detection#readme)

## Limits and data handling

New Jev runs send game transcripts to TypeSafe. Code is MIT; game data and predictions are CC BY 4.0 (`LICENSE-DATA`). Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 98c19d465974](https://github.com/jvargas2/seance-collusion-detection/tree/98c19d4659741c8b622f9f2e93e603dbf62e4b78). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
