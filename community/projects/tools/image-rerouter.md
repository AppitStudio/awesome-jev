# image-rerouter (splits diffusion steps between SDXL and SSD-1B to cut cost, with Jev classifying each prompt to pick the handoff)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research project measuring how much cheaper an image gets when a big model (SDXL) and a smaller one (SSD-1B) split the 30 denoising steps: on a 60-prompt pilot the authors report a 12/18 handoff about 20% cheaper with no clear quality loss. Because the best handoff depends on the prompt type, the router asks Jev about each prompt (composition, text, density) and picks the handoff.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aaronh-e/image-rerouter) |
| Maintainer | [aaronh-e](https://github.com/aaronh-e). Independently curated. |
| Format | Python research code with notebooks, benchmarks and a results site (no license file) |
| Requirements | Python with a GPU (or the CPU requirements), the SDXL and SSD-1B weights, and a TypeSafe key for the Jev router (a heuristic provider runs offline). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`rerouter/decider.py`](https://github.com/aaronh-e/image-rerouter/blob/76e04a77e8679c51df7453224b1e0b67058510f5/rerouter/decider.py) at the pinned commit. |

## When to use

- Route generation requests between a large and a small image model by prompt type.
- Mismatch: production serving; results come from a 60-prompt pilot.

## How it works

`rerouter/decider.py` sends one request per prompt to `https://api.typesafe.ai/v1/systemone` with `jev-latest` (set in `config.yaml` under `decider`); AIML API's mirror and an offline keyword heuristic are optional providers. `bench/decider_eval.py` evaluates the router. Integration evidence: [`rerouter/decider.py`](https://github.com/aaronh-e/image-rerouter/blob/76e04a77e8679c51df7453224b1e0b67058510f5/rerouter/decider.py).

## Get started

Install the requirements and run the Jev router evaluation.

```sh
git clone https://github.com/aaronh-e/image-rerouter && cd image-rerouter
bash setup.sh
TYPESAFE_API_KEY=... python bench/decider_eval.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results site: [aaronh-e.github.io/image-rerouter/](https://aaronh-e.github.io/image-rerouter/)
- README: [github.com/aaronh-e/image-rerouter/blob/76e04a77e8679c51df7453224b1e0b67058510f5/README.md](https://github.com/aaronh-e/image-rerouter/blob/76e04a77e8679c51df7453224b1e0b67058510f5/README.md)
- Research plan: [github.com/aaronh-e/image-rerouter/blob/76e04a77e8679c51df7453224b1e0b67058510f5/RESEARCH_PLAN.md](https://github.com/aaronh-e/image-rerouter/blob/76e04a77e8679c51df7453224b1e0b67058510f5/RESEARCH_PLAN.md)

## Limits and data handling

Image prompts go to TypeSafe on your key when the Jev provider is on; generation runs on your own GPU.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 76e04a77e867](https://github.com/aaronh-e/image-rerouter/tree/76e04a77e8679c51df7453224b1e0b67058510f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
