# PetProject by Rectangular (finished browser house of LLM-run creatures, with nine rounds of Jev personality tests)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Finished simulation of a house of small creatures (hobs) in the browser, each run by a local LLM: they hatch, work, trade, fall out and die. Before reworking the personality system, the author tested it with Jev: about 121,000 decisions over eight rounds on character sheets and situations, then a ninth round on the hobs' own model. The write-up explains why traits that steered Jev's decisions changed nothing in the house.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Intranet-Explorer/PetProject) |
| Maintainer | [Rectangular](https://github.com/Intranet-Explorer) (Intranet-Explorer). Independently curated. |
| Format | Python engine + TypeScript/Pixi view + Jev experiment scripts |
| Requirements | An Apple Silicon Mac with room for a 27B model, Ollama, uv with Python 3.12+ and Node; an OpenRouter key for the Jev experiments. |
| License | [MIT](https://github.com/Intranet-Explorer/PetProject/blob/118a852da79447d26c58247d5740f1dfff4c5aeb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`experiments/jev/round6/run6.py`](https://github.com/Intranet-Explorer/PetProject/blob/118a852da79447d26c58247d5740f1dfff4c5aeb/experiments/jev/round6/run6.py) at the pinned commit. |

## When to use

- Game and simulation builders testing whether written character traits actually steer a model's choices.
- Mismatch: a maintained game; the project is finished and no longer developed.

## How it works

The scripts in `experiments/jev/` (for example `round6/run6.py`) post character sheets and situations to OpenRouter's decisions endpoint with `typesafe/jev-1.14` and record the probabilities; the house itself runs on a local Ollama model, not Jev. Integration evidence: [`experiments/jev/round6/run6.py`](https://github.com/Intranet-Explorer/PetProject/blob/118a852da79447d26c58247d5740f1dfff4c5aeb/experiments/jev/round6/run6.py).

## Get started

Run the house, or read the Jev rounds and their reports.

```sh
git clone https://github.com/Intranet-Explorer/PetProject && cd PetProject
./run.sh start live   # http://localhost:8000
# Jev experiments: export OPENROUTER_API_KEY=... (see experiments/jev/README.md; --mock runs offline)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- The Jev personality tests: [github.com/Intranet-Explorer/PetProject/blob/main/docs/JEV.md](https://github.com/Intranet-Explorer/PetProject/blob/main/docs/JEV.md)
- Lessons: [github.com/Intranet-Explorer/PetProject/blob/main/docs/LESSONS.md](https://github.com/Intranet-Explorer/PetProject/blob/main/docs/LESSONS.md)

## Limits and data handling

Jev is used only in the experiments; the live house uses a local model. The README puts the eight Jev rounds at a little under three dollars.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 118a852da794](https://github.com/Intranet-Explorer/PetProject/tree/118a852da79447d26c58247d5740f1dfff4c5aeb). Inspected the README, LICENSE, docs/JEV.md and `experiments/jev/round6/run6.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
