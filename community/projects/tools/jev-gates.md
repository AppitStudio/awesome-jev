# jev-gates

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Composable three-valued semantic logic circuits: small TypeSafe Jev (or LocalJev) judgments become explicit TRUE/FALSE/UNKNOWN signals, combined with exact rules and optional second-layer semantic nodes, producing an auditable decision plus trace. Distinct from [typesafe-agent-gates](typesafe-agent-gates.md) (LangChain middleware for shell/triage) and [toolgate](toolgate.md) (coding-agent tool firewall).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/carlchou0dailyfresh/jev-gates) |
| Maintainer | [carlchou0dailyfresh](https://github.com/carlchou0dailyfresh). Independently curated; this entry is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | TypeScript library + CLI **jev-gates 0.1.0** (Node.js ≥ 22; zero runtime dependencies; local `dist/` build). |
| Requirements | Node.js 22+; `npm install` / build. Live TypeSafe runs need `TYPESAFE_API_KEY` and `--provider typesafe`. Offline demo/tests use `--mock` hand-written answers. |
| License | [MIT](https://github.com/carlchou0dailyfresh/jev-gates/blob/ee60004e949763c127ead40d38804aa52e5f805a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source, offline `npm test`, and mock demo inspected. Live TypeSafe and LocalJev providers were not called. |

## When to use

Use it when you want stacked, inspectable semantic+exact decisions (for example support triage) as JSON circuits rather than a single opaque prompt. Prefer [typesafe-agent-gates](typesafe-agent-gates.md) inside LangChain agents; prefer [SemDecide](semdecide.md) for one-shot CLI predicates.

## How it works

Circuit JSON wires exact comparisons and semantic nodes. The TypeSafe adapter in [`src/providers/http.ts`](https://github.com/carlchou0dailyfresh/jev-gates/blob/ee60004e949763c127ead40d38804aa52e5f805a/src/providers/http.ts) posts to `https://api.typesafe.ai/v1/systemone` (default model `jev-1.13.0`). Threshold policies map probabilities to three-valued signals; three-valued logic combines them; optional layers can read prior signals. The CLI refuses to silently switch from mock to network—you must pass `--mock` or `--provider`.

## Get started

```sh
git clone https://github.com/carlchou0dailyfresh/jev-gates.git
cd jev-gates
git checkout ee60004e949763c127ead40d38804aa52e5f805a
npm install
npm test
npm run demo
# Live (charges): TYPESAFE_API_KEY=... node dist/cli.js run examples/support-triage.json \
#   --input examples/support-input.json --provider typesafe --model jev-1.13.0
```

## Examples and demos

- Offline mock demo (`npm run demo`) and `examples/` support-triage / layered-review circuits.
- Review host: **`npm test`**: **49 passed**. Mock demo exercised; no live provider.

## Limits and data handling

Observed inputs and semantic question text leave the host toward TypeSafe or your LocalJev server when a network provider is selected. LocalJev probabilities come from whatever model that bridge uses—calibrate separately. Circuit output does not by itself send messages or change queues; your controller owns side effects.

## Review and maintenance

Reviewed on **2026-09-21** at [commit ee60004](https://github.com/carlchou0dailyfresh/jev-gates/tree/ee60004e949763c127ead40d38804aa52e5f805a): **0.1.0**, MIT. AI-assisted source review of README, `src/providers/http.ts`, CLI, examples, and LICENSE. Offline tests: **49 passed**. No live TypeSafe/LocalJev calls.

Related: [typesafe-agent-gates](typesafe-agent-gates.md), [toolgate](toolgate.md), [SemDecide](semdecide.md), [daf-jev](daf-jev.md).
