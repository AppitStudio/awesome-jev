# XavierJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local decision layer for agent control flow—typed questions from one token's probabilities, measured against labelled sets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/liu-x27/XavierJev) |
| Maintainer | [liu-x27](https://github.com/liu-x27). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Local decision library + Claude Code permission hook + trainable judge. |
| Requirements | TypeScript/Node; local model runtime (e.g. Ollama) per upstream; no TypeSafe key required. |
| License | [MIT](https://github.com/liu-x27/XavierJev/blob/ed3e50d9158a88dec342407e58101f508c6eefe0/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent research; does not call hosted Jev API. |

## When to use

Use when studying local Jev-shaped gates without TypeSafe. Prefer hosted Jev when you need the official model.

## How it works

Answers yes/no, choice, and rubric questions from local logprobs with held-out measurements and a Claude Code permission hook. Independent: does not call the Jev API. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/liu-x27/XavierJev.git
cd XavierJev
git checkout ed3e50d9158a88dec342407e58101f508c6eefe0
# follow upstream README for local model + hook setup
```

Pin revision `ed3e50d9158a88dec342407e58101f508c6eefe0` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent research; does not call hosted Jev. Measurement claims are upstream-reported. Live local paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit ed3e50d](https://github.com/liu-x27/XavierJev/tree/ed3e50d9158a88dec342407e58101f508c6eefe0). AI-assisted README and LICENSE inspection; install/live paths not executed.
