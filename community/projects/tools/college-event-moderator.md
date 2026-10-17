# College Event Moderator

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark and local playground that screens college chapter event proposals with Jev or a local s1ced or Vega model: five shared questions per event, expected answers, and a report of accuracy, confidence, latency and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Saiguru2554/college-event-moderator) |
| Maintainer | [Saiguru2554](https://github.com/Saiguru2554). Independently curated. |
| Format | Python package with CLI, benchmark runner and local dashboard (uv) |
| Requirements | Python 3.10+ and uv; a TypeSafe API key only for the Jev runs (local models need no key). |
| License | [Apache-2.0](https://github.com/Saiguru2554/college-event-moderator/blob/d4482093ba00a1fb8bf53da3e4bfbcc758ef1e08/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/event_moderator/benchmark.py`](https://github.com/Saiguru2554/college-event-moderator/blob/d4482093ba00a1fb8bf53da3e4bfbcc758ef1e08/src/event_moderator/benchmark.py) at the pinned commit. |

## When to use

- Compare hosted Jev with small local decision models on the same labelled proposals before choosing one for a screening job.
- Use the playground to see each verdict with its probability and whether it matched the expected answer.
- Mismatch: 12 sample events written for this project; a first filter with human fallback, not a policy engine.

## How it works

Each event is a state plus five screening questions (safe, action, team, risk, budget) sent in the System One request shape `{model, state, questions}`; the same contract is used for Jev and the local models, so answers, probabilities, uncertainty and usage line up. `benchmark.py` runs the models side by side and writes the comparison. Integration evidence: [`src/event_moderator/benchmark.py`](https://github.com/Saiguru2554/college-event-moderator/blob/d4482093ba00a1fb8bf53da3e4bfbcc758ef1e08/src/event_moderator/benchmark.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Saiguru2554/college-event-moderator.git
cd college-event-moderator
uv sync
export TYPESAFE_API_KEY=...   # optional, Jev only
uv run event-moderator run hookah_dorm_party --model jev-latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Dashboard screenshot and the 12 events with expected answers in the README.
- `uv run event-moderator-server` opens the local playground on port 8781.

## Limits and data handling

Proposal text goes to TypeSafe only when you pick the Jev model; local models download from Hugging Face and run offline. The README notes the local s1ced model is right about 83% of the time on its own training distribution.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit d4482093ba00](https://github.com/Saiguru2554/college-event-moderator/tree/d4482093ba00a1fb8bf53da3e4bfbcc758ef1e08). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
