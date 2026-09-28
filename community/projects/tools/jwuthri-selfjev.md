# SelfJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open decisions model with a Jev-shaped typed API (yes/no, choice, score, multi) from forward-pass probabilities — Qwen3.5-4B + LoRA, one GPU; independent of hosted Jev

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jwuthri/SelfJev) |
| Maintainer | [Jwuthri](https://github.com/Jwuthri). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python · open decision model (Apache-2.0). |
| Requirements | Python/GPU per README; optional selfjev.dev for demos. |
| License | [Apache-2.0](https://github.com/Jwuthri/SelfJev/blob/2c4d2e0058e47d8ffbfe34d03a22dadd48ff384c/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when researching open System One–style decision models. Not an official Jev substitute; separate from hosted TypeSafe Jev.

## How it works

Model returns typed answer probabilities without text generation. Homepage: <\1>selfjev.dev. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/Jwuthri/SelfJev.git
cd SelfJev
git checkout 2c4d2e0058e47d8ffbfe34d03a22dadd48ff384c
```

Pin revision `2c4d2e0058e47d8ffbfe34d03a22dadd48ff384c` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 2c4d2e0](https://github.com/Jwuthri/SelfJev/tree/2c4d2e0058e47d8ffbfe34d03a22dadd48ff384c). AI-assisted README and LICENSE inspection; install/live paths not executed.
