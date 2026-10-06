# Jeff (firelex)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jeff: an open 0.8B "System 1" decision model (MIT code, Apache-2.0 weights on Hugging Face) that uses the same request format as Jev, with swappable LoRA adapters (guard, triage, tools, grounding, spam…), GGUF files for llama.cpp, and Jeff-Code; independent and not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/firelex/jeff) |
| Product homepage | [jeffhub.ai](https://jeffhub.ai) |
| Maintainer | [firelex](https://github.com/firelex). Independently curated. |
| Format | Model weights + Python server/client (and TypeScript client) |
| Requirements | Python with `uv`; GPU recommended (CUDA or Apple silicon/MLX), CPU via llama.cpp GGUF. No TypeSafe account. |
| License | [MIT (code); Apache-2.0 weights](https://github.com/firelex/jeff/blob/5f7d0e0e3bd87d60c0df7cd22f760dd6769272fe/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Make fast routine decisions (guard, triage, tool choice, grounding) on your own hardware and defer only unsure cases to a large model.
- Prototype against the Jev request shape without sending data to a hosted service.
- Mismatch: this is not TypeSafe Jev; benchmarks are maintainer-reported.

## How it works

`jeff-serve` loads the base checkpoint and named adapters; each request names the adapter and asks typed questions, and the model reads option probabilities in one forward pass (one base, many LoRA adapters). Training began as a fork of the MIT [AutoJev](https://github.com/denis-pplx/autojev) recipe.

## Get started

Download the base and adapters, then serve locally:

```sh
git clone https://github.com/firelex/jeff && cd jeff
uv sync --no-default-groups --extra lora
uv run --no-default-groups hf download mstrasser/jeff-base --revision v1.3 --local-dir jeff-base-v1.3
JEFF_CHECKPOINT=jeff-base-v1.3 JEFF_ADAPTERS=adapters PORT=8765 uv run --no-default-groups --extra lora jeff-serve
```

No hosted calls; local compute only.

## Examples and demos

- [jeffhub.ai](https://jeffhub.ai) results and adapter pages (upstream).
- [Jeff-Code](https://github.com/firelex/jeff-code) coding agent and the [reference app](https://github.com/firelex/jeff-reference-app) for the 27B comparison.

## Limits and data handling

All accuracy, speed and memory figures (e.g. vs Qwen3.8-27B) are maintainer-reported; not reproduced. Independent project — same request format as Jev, not a validated substitute. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 5f7d0e0e3bd8](https://github.com/firelex/jeff/tree/5f7d0e0e3bd87d60c0df7cd22f760dd6769272fe). Inspected the upstream README and LICENSE at the pinned commit; found via a Hacker News comment by the maintainer. Model download, serving and benchmarks were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
