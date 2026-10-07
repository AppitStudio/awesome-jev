# Decider.jl

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Julia front end for decision models: ask Choice, YesNo and Score questions about some state and get calibrated probabilities keyed by your own `@enum` or `Symbol`s, with backends for TypeSafe Jev, OpenRouter decision models and the OpenAI Decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/farrellm/Decider.jl) |
| Maintainer | [farrellm](https://github.com/farrellm). Independently curated. |
| Format | Julia package (install from GitHub URL) |
| Requirements | Julia and a `TYPESAFE_API_KEY` (or `OPENROUTER_API_KEY` / `OPENAI_API_KEY` for other backends). |
| License | [MIT](https://github.com/farrellm/Decider.jl/blob/0d85fa8108a3975758fdadf9a75cc1a3f7601e58/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route, classify or score text from Julia data pipelines with Jev.
- Swap between Jev, OpenRouter and OpenAI Decisions without changing question code.
- Mismatch: young package; check the README for current install instructions.

## How it works

[`src/backends.jl`](https://github.com/farrellm/Decider.jl/blob/0d85fa8108a3975758fdadf9a75cc1a3f7601e58/src/backends.jl) defines `TypeSafe()`, `OpenRouter()` and `OpenAIDecisions()`; [`src/codecs/systemone.jl`](https://github.com/farrellm/Decider.jl/blob/0d85fa8108a3975758fdadf9a75cc1a3f7601e58/src/codecs/systemone.jl) encodes questions for the System One API. `ask`, `probabilities` and `decide` share one signature.

## Get started

Add the package by its GitHub URL with Julia Pkg (the README shows usage, not install), then ask a question (README *Usage*):

```sh
julia -e 'using Pkg; Pkg.add(url="https://github.com/farrellm/Decider.jl")'
# using Decider; @enum Dept billing technical sales
# decide(TypeSafe(), Choice(Dept, "Which team should handle this?"), "I was charged twice.")
```

Each `ask` / `decide` call is a request billed by the chosen provider.

## Examples and demos

- README *Usage* and *Questions*.
- Design notes: [`DESIGN.md`](https://github.com/farrellm/Decider.jl/blob/0d85fa8108a3975758fdadf9a75cc1a3f7601e58/DESIGN.md).

## Limits and data handling

State you pass goes to the selected provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 0d85fa8108a3](https://github.com/farrellm/Decider.jl/tree/0d85fa8108a3975758fdadf9a75cc1a3f7601e58). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
