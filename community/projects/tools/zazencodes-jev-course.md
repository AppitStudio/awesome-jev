# ZazenCodes Jev course resources

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Free MIT companion code for ZazenCodes' *Jev: Introduction to System 1 AI* course: notebooks on Jev's Noul/Choice/Score primitives with a latency and cost benchmark against large LLMs, a use-case catalog, use-case implementations and a custom Pi model router in TypeScript.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zazencodes/system-one-ai-with-jev-course) |
| Product homepage | [zazencodes.com](https://zazencodes.com) |
| Maintainer | [zazencodes](https://github.com/zazencodes). Independently curated. |
| Format | Course repository: Jupyter notebooks (uv) per lesson + TypeScript solution for a Pi model router |
| Requirements | uv, a TypeSafe API key; the Lesson 03 benchmark also needs OpenAI and Anthropic keys. |
| License | [MIT](https://github.com/zazencodes/system-one-ai-with-jev-course/blob/7f9ca47e4560458f22b5bfde088383ef0a6e704b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. The course videos are a paid ZazenCodes product (Skool membership or one-time purchase); this listing covers the free MIT companion repository only. |

## When to use

- Learn when to use Jev for routing, guardrails and intent classification next to a System 2 LLM.
- Reuse the lesson notebooks as starting points without buying the course.
- Mismatch: the lessons themselves (videos) are paid; the repo is supporting material.

## How it works

Each folder maps to a lesson: [`03-three-primitives`](https://github.com/zazencodes/system-one-ai-with-jev-course/tree/7f9ca47e4560458f22b5bfde088383ef0a6e704b/03-three-primitives) (primitives + benchmark notebook), [`04-jev-use-cases`](https://github.com/zazencodes/system-one-ai-with-jev-course/tree/7f9ca47e4560458f22b5bfde088383ef0a6e704b/04-jev-use-cases), [`05-implementing-use-cases`](https://github.com/zazencodes/system-one-ai-with-jev-course/tree/7f9ca47e4560458f22b5bfde088383ef0a6e704b/05-implementing-use-cases) and [`06-custom-pi-model-router`](https://github.com/zazencodes/system-one-ai-with-jev-course/tree/7f9ca47e4560458f22b5bfde088383ef0a6e704b/06-custom-pi-model-router) with a [`jev-model-router.ts`](https://github.com/zazencodes/system-one-ai-with-jev-course/blob/7f9ca47e4560458f22b5bfde088383ef0a6e704b/06-custom-pi-model-router/solution/jev-model-router.ts) solution.

## Get started

Clone and install (README *Setup*):

```sh
git clone https://github.com/zazencodes/system-one-ai-with-jev-course.git && cd system-one-ai-with-jev-course
uv sync
cp .env.example .env    # add TYPESAFE_API_KEY (and OpenAI/Anthropic keys for the benchmark)
```

Notebook cells call TypeSafe (and OpenAI/Anthropic for the benchmark) on your keys.

## Examples and demos

- README *Course Roadmap & Repository Layout*.

## Limits and data handling

Benchmark figures are the course author's. Course access is sold separately by ZazenCodes. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 7f9ca47e4560](https://github.com/zazencodes/system-one-ai-with-jev-course/tree/7f9ca47e4560458f22b5bfde088383ef0a6e704b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
