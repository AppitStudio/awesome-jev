# local-jev by Andrés Rubio del Saz (Jev-compatible typed decisions on your Mac with open Laya weights, over MCP, REST and a CLI)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local server for Apple Silicon that answers Jev-style `noul`, `choice` and `score` questions with the open Laya encoder models through laya-mlx. Agents reach it over MCP (`decide`, `decide_batch`, `status`), a `POST /v1/systemone` endpoint that existing Jev clients can point at, or a CLI; with the default backend the text stays on your Mac.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AndresRubio/jev-test) |
| Maintainer | [Andrés Rubio del Saz](https://github.com/AndresRubio). Independently curated. |
| Format | Python CLI, MCP server and REST API (uv tool) |
| Requirements | Apple Silicon Mac on macOS 14+, uv, about 1.5 GB of disk for the checkpoints and about 2.5 GB of memory with both loaded. |
| License | [Apache-2.0](https://github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/local_jev/api_rest.py`](https://github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/src/local_jev/api_rest.py) at the pinned commit. |

## When to use

- Give Claude Code or Codex fast, private yes/no, choice and score decisions without sending text to a cloud API.
- Mismatch: nuanced judgement; the README's own 60-item evaluation shows weak spots (negations, catch-all options) unless you fine-tune.

## How it works

`src/local_jev/api_rest.py` serves TypeSafe's documented `/v1/systemone` request shape on 127.0.0.1:7711 and `api_mcp.py` exposes the MCP tools; weights come from `convaiinnovations/laya` at a pinned revision with SHA-256 checks. An optional `remote` backend forwards to any Jev-compatible URL, such as an Unsloth-served model you trained from the exported decision log. This uses Laya, not TypeSafe's Jev. Integration evidence: [`src/local_jev/api_rest.py`](https://github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/src/local_jev/api_rest.py).

## Get started

Install the tool, pull the weights, then serve and connect an agent.

```sh
git clone https://github.com/AndresRubio/jev-test
cd jev-test
uv tool install --editable .
local-jev pull
local-jev serve
local-jev connect   # prints the claude mcp add command
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evaluation: [github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/eval/results.md](https://github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/eval/results.md)
- Benchmarks: [github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/docs/benchmarks.md](https://github.com/AndresRubio/jev-test/blob/1ece761c4552a547625a062f01e14a8bedf28105/docs/benchmarks.md)

## Limits and data handling

Not TypeSafe's Jev: answers come from Laya (322M to 421M parameters). On the author's 60 hand-labelled items it got 24 of 30 yes/no, 16 of 20 choice and 7 of 10 score questions right; confidences run high. Text in a state can steer answers, so do not use it as the only check on untrusted input. Apple Silicon only for the default backend.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 1ece761c4552](https://github.com/AndresRubio/jev-test/tree/1ece761c4552a547625a062f01e14a8bedf28105). Inspected the README, `eval/results.md` and the REST and MCP server code at the pinned commit; the server was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
