# ELESSAR by David Jones-Gilardi (pixel-art checkers board of Bayesian nodes where Jev can supply the evidence for each record)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

A local demo that fuses differently shaped data sources into one view: pieces on a pixel-art checkers board are nodes in a Bayesian network. You connect sources, judge evidence, decide which records describe the same thing and crown the explanation you believe. An evidence toggle switches between hand-written rules and Jev, with Python and Rust engines side by side and scenario packs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SonicDMG/elessar) |
| Maintainer | [SonicDMG](https://github.com/SonicDMG). Independently curated. |
| Format | Python standard-library server and Rust engine with a web UI |
| Requirements | Python 3.9+ (no install); Rust optional; an OpenRouter API key for the Jev evidence engine (rules mode needs no key). |
| License | [MIT](https://github.com/SonicDMG/elessar/blob/ca3a0ef337c3c30d7660af60333d6bec0df0e938/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.py`](https://github.com/SonicDMG/elessar/blob/ca3a0ef337c3c30d7660af60333d6bec0df0e938/server/jev.py) at the pinned commit. |

## When to use

- Explore record linkage and Bayesian evidence visually, comparing rules with Jev.
- Mismatch: production entity resolution.

## How it works

`server/jev.py` asks Jev one yes/no question per signal about each candidate record through OpenRouter's `/api/v1/systemone` (default `jev-latest`) and uses the probability as evidence; answers are cached on disk so replays are free and deterministic. Integration evidence: [`server/jev.py`](https://github.com/SonicDMG/elessar/blob/ca3a0ef337c3c30d7660af60333d6bec0df0e938/server/jev.py).

## Get started

Run the Python server (rules mode works without a key).

```sh
git clone https://github.com/SonicDMG/elessar.git && cd elessar
./run.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/SonicDMG/elessar/blob/ca3a0ef337c3c30d7660af60333d6bec0df0e938/README.md](https://github.com/SonicDMG/elessar/blob/ca3a0ef337c3c30d7660af60333d6bec0df0e938/README.md)

## Limits and data handling

Record text is sent to OpenRouter and TypeSafe in Jev mode. Reaches Jev through OpenRouter.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit ca3a0ef337c3](https://github.com/SonicDMG/elessar/tree/ca3a0ef337c3c30d7660af60333d6bec0df0e938). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
