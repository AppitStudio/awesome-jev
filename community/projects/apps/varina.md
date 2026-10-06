# Varina

[All projects](../README.md) · [Web apps](README.md#web-apps)

Chinese-language multi-seat AI design-exploration workbench (local web UI + CLI) where an optional TypeSafe Jev post-gate decides START or ASK — whether a finished answer merits deeper multi-seat exploration — before any extra model spend; Jev never writes answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deillusion/Aha-Engine) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/deillusion/Aha-Engine#readme) (Chinese; source-built local app, no separate website verified). |
| Pricing and access | No app purchase fee for the source build (Node.js 22, no third-party npm runtime dependencies). Real-model mode needs your own model provider keys; the Jev gate needs your own `TYPESAFE_API_KEY`. Usage is billed by those providers. Checked 2026-10-06. |
| Jev evidence | [`src/decision/jev_gateway.mjs`](https://github.com/deillusion/Aha-Engine/blob/a84506ebdf1057e19072d29905965e1f1c1ae0c4/src/decision/jev_gateway.mjs) sends one `choice` question (START / ASK) to `https://api.typesafe.ai` with `jev-latest`; README configuration notes say the key is used only for this gate. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [deillusion](https://github.com/deillusion). Independently curated. |
| Format | Local web workbench (`npm start`, served on `127.0.0.1:27333`) and CLI |
| Platform and availability | Any OS with Node.js 22+; runs locally in the browser. |
| Jev's role | Post-answer gate: after a normal answer completes, Jev chooses START (deeper Varina exploration has plausible value) or ASK (plainly irrelevant, e.g. a greeting); uncertainty defaults to START. |
| Requirements | Node.js 22+; model provider key(s) for real-model mode; optional `TYPESAFE_API_KEY` for the Jev gate. An offline demo mode needs no keys. |
| License | [Business Source License 1.1](https://github.com/deillusion/Aha-Engine/blob/a84506ebdf1057e19072d29905965e1f1c1ae0c4/LICENSE). |

## When to use

- Explore open-ended design problems (game mechanics, systems) with several AI "seats" and operators, but skip that extra spend when the question does not warrant it.
- See a small, concrete pattern: one Jev `choice` call as a cost gate in front of an expensive multi-agent step.
- Mismatch: the UI and docs are Chinese; for simple A-vs-B comparisons the README itself says you do not need Varina.

## How it works

Varina first answers normally (ReAct with tools, using your configured model). If the "Varina 探索" switch is on, `jev_gateway.mjs` posts the completed exchange as `state` with one `choice` question — START when there may be mechanisms, counterexamples, trade-offs or unresolved solution space to explore; ASK only when exploration is plainly irrelevant. ASK with enough probability skips exploration; anything uncertain or relevant becomes START, which runs operator assignment, viewpoint boards, a fact ledger and candidate solutions.

## Get started

Run the local workbench; configure models in 模型设置 and add `TYPESAFE_API_KEY` in `.env` for the Jev gate (live calls only when exploration is enabled):

```sh
git clone https://github.com/deillusion/Aha-Engine.git
cd Aha-Engine
cp .env.example .env      # model keys; optional TYPESAFE_API_KEY for the Jev gate
npm start                 # http://127.0.0.1:27333
# offline flow demo, no external model calls:
npm run demo -- --workspace ./my-project --prompt "设计一个合作机制"
```

Real-model mode calls your configured model providers and may be costly with multi-seat exploration; the Jev gate is one TypeSafe request per eligible answer.

## Examples and demos

- README walkthrough of a design exploration (operator assignment, viewpoint board, fact ledger, candidate solutions).
- `npm run demo` offline flow demonstration that calls no external model.

## Limits and data handling

Business Source License 1.1 — not an open-source license; production use is allowed under the stated revenue threshold, so read `LICENSE` before commercial use. Answers and exploration come from your general-purpose model, not Jev. Project writes require explicit requests and are backed up first. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit a84506ebdf10](https://github.com/deillusion/Aha-Engine/tree/a84506ebdf1057e19072d29905965e1f1c1ae0c4). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
