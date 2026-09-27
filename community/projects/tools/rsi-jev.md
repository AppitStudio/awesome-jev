# RSI-Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Recursively self-improving research loop that trains Jev-style System One (noul/choice/score) models and serves them at `/v1/systemone`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Shanghua-Gao/RSI-Jev) |
| Maintainer | [Shanghua-Gao](https://github.com/Shanghua-Gao). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Research training system + Jev-compatible serve scripts. |
| Requirements | Python; GPU/training resources per upstream docs; optional TypeSafe for comparisons. |
| License | [MIT](https://github.com/Shanghua-Gao/RSI-Jev/blob/acf853be5ba9e6fec2de77e570259e3e585a78d8/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent research; not official Jev weights. |

## When to use

Use when studying self-improving typed-decision model training with a Jev-compatible serve path. Prefer hosted TypeSafe Jev for production judgments.

## How it works

Agents propose hypotheses and train typed-decision models; `scripts/serve.py` exposes `POST /v1/systemone` with Jev-shaped requests. Checkpoints follow base-model licenses; not affiliated with TypeSafe. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/Shanghua-Gao/RSI-Jev.git
cd RSI-Jev
git checkout acf853be5ba9e6fec2de77e570259e3e585a78d8
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `acf853be5ba9e6fec2de77e570259e3e585a78d8` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream). Independent research; not official Jev weights. Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit acf853be5ba9](https://github.com/Shanghua-Gao/RSI-Jev/tree/acf853be5ba9e6fec2de77e570259e3e585a78d8). AI-assisted README and LICENSE inspection; install/live paths not executed.
