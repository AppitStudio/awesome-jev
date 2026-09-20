# Jev Lab

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local lab of Jev use cases: **Hundred** (100 NPCs in a tiny town) and **Jev Shogi** (human Sente, Jev/rules Gote). Engines keep legality; Jev only picks the next closed-set action when enabled.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jammaru/jev-lab) |
| Maintainer | [jammaru](https://github.com/jammaru). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | pnpm monorepo **jev-lab 0.2.0** (Vite web apps + Node servers); defaults to Rules mode without a key. |
| Requirements | Node.js / pnpm (Corepack); optional `TYPESAFE_API_KEY` or `JEV_API_KEY` for live Jev. Nix flake available. |
| License | [MIT](https://github.com/jammaru/jev-lab/blob/fcb8d0b19d023e70c49d23834899e12704d14666/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline Vitest inspected. Live Jev NPC/shogi sessions were not run. |

## When to use

Use it to study how application engines own world rules while Jev selects among legal next actions (society sim or shogi replies). Prefer production agent routers or SDKs when you need library integration rather than a demo lab.

## How it works

[`packages/decision-jev`](https://github.com/jammaru/jev-lab/tree/fcb8d0b19d023e70c49d23834899e12704d14666/packages/decision-jev) implements `JevProvider` with `@typesafe-ai/sdk` (`choice` questions, default model `jev-latest`). Hundred compact person/time state becomes request state; shogi uses a separate server path that only chooses among engine-legal USI moves. Without a key, products stay in **Rules** mode. Failures fall back to the rules provider.

## Get started

```sh
git clone https://github.com/jammaru/jev-lab.git
cd jev-lab
git checkout fcb8d0b19d023e70c49d23834899e12704d14666
pnpm install --frozen-lockfile
pnpm test
pnpm dev   # hub http://127.0.0.1:5173 — no key required for Rules mode
```

Optional live Jev: export `TYPESAFE_API_KEY` (or `JEV_API_KEY`) before enabling the Jev provider; usage incurs TypeSafe charges.

## Examples and demos

- Lab hub, Hundred, and Jev Shogi via `pnpm dev` / `pnpm dev:hundred` / `pnpm dev:shogi`.
- Recorded runs under `apps/hundred-server/runs/` (inspect locally).
- Offline Vitest suite (see Review).

## Limits and data handling

When Jev is enabled, compact NPC/board decision state leaves the host to TypeSafe. Jev never invents illegal shogi moves—the engine supplies candidates. This is a teaching/demo lab, not a hosted multiplayer service. E2E Playwright browser tests were not run on the review host.

## Review and maintenance

Reviewed on **2026-09-20** at [commit fcb8d0b](https://github.com/jammaru/jev-lab/tree/fcb8d0b19d023e70c49d23834899e12704d14666): **0.2.0**, MIT. AI-assisted source review of `packages/decision-jev`, shogi/hundred servers, README, and LICENSE. **`pnpm test`**: **54 passed** (17 files). No live TypeSafe calls.

Related: [TypeSafe Mario](typesafe-mario.md), [JevPilot](jevpilot.md), [jev-drone](jev-drone.md).
