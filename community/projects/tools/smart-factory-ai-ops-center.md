# smart-factory-ai-ops-center (simulated factory ops with TypeSafe Jev as the final judge)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research simulation of a virtual factory (virtual PLC/MQTT) where YOLO11n does first-pass inspection and TypeSafe Jev makes the final typed judgments for product inspection and line operations, with disturbance scenarios for paired comparisons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Imperfective/smart-factory-ai-ops-center) |
| Maintainer | [Imperfective](https://github.com/Imperfective). Independently curated. |
| Format | Python research simulation + TypeSafe adapter (MIT) |
| Requirements | Python environment for the simulation; a TypeSafe API key for live Jev judgments. |
| License | [MIT](https://github.com/Imperfective/smart-factory-ai-ops-center/blob/a642a6cef81179c306f14725e95b63f503e4cf2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sfaic2/adapters/typesafe_jev.py`](https://github.com/Imperfective/smart-factory-ai-ops-center/blob/a642a6cef81179c306f14725e95b63f503e4cf2e/sfaic2/adapters/typesafe_jev.py) at the pinned commit. |

## When to use

- Study closed-loop factory decisions with a typed System One final judge.
- Compare YOLO-first screening against Jev final calls under disturbances.
- Mismatch: simulation/research code; not a production MES.

## How it works

`sfaic2/adapters/typesafe_jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` and typed questions for the final factory judgments. Integration evidence: [`sfaic2/adapters/typesafe_jev.py`](https://github.com/Imperfective/smart-factory-ai-ops-center/blob/a642a6cef81179c306f14725e95b63f503e4cf2e/sfaic2/adapters/typesafe_jev.py).

## Get started

Clone, install per README, set TYPESAFE_API_KEY, and run the simulation scripts.

```sh
git clone https://github.com/Imperfective/smart-factory-ai-ops-center.git && cd smart-factory-ai-ops-center
export TYPESAFE_API_KEY=...
# follow README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Imperfective/smart-factory-ai-ops-center/blob/a642a6cef81179c306f14725e95b63f503e4cf2e/README.md](https://github.com/Imperfective/smart-factory-ai-ops-center/blob/a642a6cef81179c306f14725e95b63f503e4cf2e/README.md)

## Limits and data handling

Simulation state and inspection context are sent to TypeSafe on your key. Research-only; not production plant control.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit a642a6cef811](https://github.com/Imperfective/smart-factory-ai-ops-center/tree/a642a6cef81179c306f14725e95b63f503e4cf2e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
