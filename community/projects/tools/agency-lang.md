# Agency (agent language compiling to TypeScript with Jev decision models in typed llm() calls)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Agency is a language for building agents that compiles to TypeScript; typed `llm()` calls can route booleans, label choices and simple objects to TypeSafe Jev (or local Laya) decision models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/egonSchiele/agency-lang) |
| Maintainer | [egonSchiele](https://github.com/egonSchiele). Independently curated. |
| Format | Language + runtime (npm `agency-lang`, MIT in package) |
| Requirements | Node/pnpm, `pnpm install agency-lang`, and a TypeSafe or OpenRouter key for Jev. |
| License | [MIT (packages/agency-lang/LICENSE; no root license file)](https://github.com/egonSchiele/agency-lang/blob/5b2ff90a8499c922549777139c4f9329ef752d91/packages/agency-lang/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/agency-lang/lib/runtime/decision/dispatch.ts`](https://github.com/egonSchiele/agency-lang/blob/5b2ff90a8499c922549777139c4f9329ef752d91/packages/agency-lang/lib/runtime/decision/dispatch.ts) at the pinned commit. |

## When to use

- Get typed decisions from an agent language.
- Benchmark Jev against a text LLM on your labels.
- Mismatch: only booleans, labels and simple objects go to Jev.

## How it works

`decision/dispatch.ts` sets `DECISION_PROVIDER = "typesafe"` and dispatches typed decision calls over the System One protocol; `benchmarks/decision-models` compares Jev, Laya and a text model on an SMS spam set. Integration evidence: [`packages/agency-lang/lib/runtime/decision/dispatch.ts`](https://github.com/egonSchiele/agency-lang/blob/5b2ff90a8499c922549777139c4f9329ef752d91/packages/agency-lang/lib/runtime/decision/dispatch.ts).

## Get started

Install with `pnpm install agency-lang`, write a `.agency` file with a typed `llm()` call, and configure the Jev decision model per the docs guide.

```sh
pnpm install agency-lang
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision-model benchmark: [github.com/egonSchiele/agency-lang/blob/5b2ff90a8499c922549777139c4f9329ef752d91/packages/agency-lang/benchmarks/decision-models/README.md](https://github.com/egonSchiele/agency-lang/blob/5b2ff90a8499c922549777139c4f9329ef752d91/packages/agency-lang/benchmarks/decision-models/README.md)

## Limits and data handling

Inputs to decision calls are sent to TypeSafe/OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 5b2ff90a8499](https://github.com/egonSchiele/agency-lang/tree/5b2ff90a8499c922549777139c4f9329ef752d91). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
