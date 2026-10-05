# MakerAi

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Native Delphi AI framework (agents, RAG, MCP, multi-provider chat) with `TAiJev` and eight Jev adapters for routing, tool/input guardrails, RAG reranking, eval scoring, bulk labeling and model routing — hosted Jev or Ollama `/v1/systemone` decision models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gustavoeenriquez/MakerAi) |
| Maintainer | [gustavoeenriquez](https://github.com/gustavoeenriquez). Independently curated. |
| Format | Framework / component library with demos |
| Requirements | Delphi 11 Alexandria or later for full support (10.4 limited). A TypeSafe key for hosted Jev, or a local Ollama 0.35+ serving decision models at `/v1/systemone`. |
| License | [MIT](https://github.com/gustavoeenriquez/MakerAi/blob/791d8c77946e16ade65a9d4827e55dd2adb768ef/LICENSE.txt). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add calibrated typed decisions (routing, guards, labels) to an existing Delphi application without a full LLM round-trip.
- Gate tool calls and user input in a Delphi agent with thresholds kept in code.
- Mismatch: outside Delphi/Object Pascal, use an SDK for your language instead.

## How it works

`TAiJev` (`Source/Tools/uMakerAi.Jev.pas`) sends typed questions and returns calibrated probabilities with a confidence your code thresholds. Adapters plug it into the framework: the agent-graph router writes `Blackboard['next_route']` and falls back on low confidence, the guardrail classifier blocks when P(risk) ≥ 0.5 and fails closed, the RAG reranker drops passages that try to instruct the model, and usage/cost is exposed per operation. Setting `Url` to Ollama's `/v1/` runs the same adapters on local decision models ([README](https://github.com/gustavoeenriquez/MakerAi/blob/791d8c77946e16ade65a9d4827e55dd2adb768ef/README.md)).

## Get started

Install the packages per the README, then configure `TAiJev` with a TypeSafe key or a local Ollama URL (live calls when a key is set):

```sh
git clone https://github.com/gustavoeenriquez/MakerAi.git
# add the Source/* library paths, then compile and install the packages (README → Installation)
# TAiJev: set your TypeSafe key per the README, or Url := 'http://localhost:11434/v1/' for Ollama
```

Hosted Jev calls are billed by TypeSafe; local Ollama decision models have no TypeSafe charge.

## Examples and demos

- README *Jev — calibrated decisions before spending an LLM*: maintainer-reported checks such as 15/15 dispatch decisions, 13 guardrail calibration cases, and a 126-entry accounting labeling run (92.9% for US$0.05). Not reproduced here.
- Demo `086-JevEvalsRag` (eval scorer + RAG reranker).

## Limits and data handling

Figures are small maintainer calibration sets. Input text (prompts, tool calls, passages) is sent to TypeSafe when hosted Jev is used. Delphi build and live inference were not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 791d8c77946e](https://github.com/gustavoeenriquez/MakerAi/tree/791d8c77946e16ade65a9d4827e55dd2adb768ef). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
