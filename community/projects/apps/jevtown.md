# Jev Town

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser AI-town simulation where TypeSafe Jev makes each agent’s structured next-action choices and an LLM handles dialogue and memory

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NevaMind-AI/JevTown) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/NevaMind-AI/JevTown#readme) |
| Pricing and access | Free source build; no app purchase fee. LLM + TypeSafe Jev keys required for the Jev-driven demo (`JEV_API_KEY`, OpenAI-compatible LLM). Proxy caps runs at 2000 model calls. Checked 2026-09-29. |
| Jev evidence | Upstream README and feat-branch sources [`agent/decideJev.ts`](https://github.com/NevaMind-AI/JevTown/blob/52b19d76ac1aff102a3975a307cba4e652fd9986/agent/decideJev.ts), [`server/model/jev.ts`](https://github.com/NevaMind-AI/JevTown/blob/52b19d76ac1aff102a3975a307cba4e652fd9986/server/model/jev.ts). Main README documents `VITE_ACTION_DECIDER=jev`; the playable Jev demo currently lives on `feat/jev-demo-solarium` until merge. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Main tip and feat branch diverged at review time; live browser/Jev paths not run on the review host. Distinct from [Jev Lab](../tools/jev-lab.md) NPC-town labs. |
| Maintainer | [NevaMind-AI](https://github.com/NevaMind-AI). Independently curated. |
| Format | TypeScript · Vite browser simulation + local key proxy (MIT; based on a16z-infra/ai-town). |
| Platform and availability | Node.js 22 LTS; `npm run play:demo` → `http://localhost:5173/ai-town/`. MVP. |
| Jev's role | Jev chooses structured agent actions (seek/wander/wait, etc.); an LLM writes conversations and memory. Jev use is optional (`VITE_ACTION_DECIDER`). |
| Requirements | Node.js 22.22.1+; `JEV_API_KEY`; OpenAI-compatible LLM + embedding credentials in `.env.local`. |
| License | [MIT](https://github.com/NevaMind-AI/JevTown/blob/c954bf44c801ddd7a2d2299388dde3da670ee75a/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when exploring multi-agent simulations driven by System One decisions rather than scripted NPCs. Prefer [Jev Lab](../tools/jev-lab.md) for smaller Hundred NPC-town / Shogi labs.

## How it works

The engine enumerates legal options; Jev picks among them so illegal moves never occur. An LLM handles language. A local proxy holds keys so the browser never sees them.

## Get started

```sh
git clone https://github.com/NevaMind-AI/JevTown.git
cd JevTown
# Jev demo sources reviewed on feat/jev-demo-solarium:
git checkout 52b19d76ac1aff102a3975a307cba4e652fd9986
npm ci
# create .env.local with LLM_* and JEV_API_KEY; VITE_ACTION_DECIDER=jev
npm run play:demo
```

Pin revision `52b19d76ac1aff102a3975a307cba4e652fd9986` when reproducing this review. Upstream notes the demo may still live on that branch until merge to main.

## Examples and demos

README demo GIF and installation path at the pinned commits. No live simulation was run on the review host.

## Limits and data handling

Every decision and dialogue line is a model call; large casts cost more. Proxy stop after 2000 calls per run. Live TypeSafe/LLM paths were not executed on the review host.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) against main tip [c954bf4](https://github.com/NevaMind-AI/JevTown/tree/c954bf44c801ddd7a2d2299388dde3da670ee75a) (README/LICENSE) and feat tip [52b19d7](https://github.com/NevaMind-AI/JevTown/tree/52b19d76ac1aff102a3975a307cba4e652fd9986) (Jev integration files). AI-assisted inspection; install/live paths not executed.
