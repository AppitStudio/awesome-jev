# Advocaat

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Ask several typed Jev questions about the same structured data in one request from TypeScript.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pithings/advocaat) |
| Maintainer | [pithings](https://github.com/pithings) / Pooya Parsa. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript library (`ask`) with an optional agent skill for question design. |
| Requirements | A TypeScript/Node project. Live calls need `TYPESAFE_API_KEY`, or `AI_GATEWAY_API_KEY` / `VERCEL_OIDC_TOKEN` for Vercel AI Gateway. Defaults: model `jev-latest` (direct) or `typesafe-ai/jev` (gateway). |
| License | [MIT](https://github.com/pithings/advocaat/blob/bc46287fc1102b95852a81d679c6e34a2c44f4a2/LICENSE). |

## When to use

Use it when an application needs closed-set Choice, Score, or yes/no (Noul) judgments over JSON-shaped state and wants a small typed client rather than hand-rolled HTTP. The [agent skill](https://github.com/pithings/advocaat/blob/bc46287fc1102b95852a81d679c6e34a2c44f4a2/skills/advocaat/SKILL.md) helps design questions; it does not replace application policy.

Prefer a language-native SDK if you are not on TypeScript. Your code still owns thresholds, retries, permissions, and downstream actions.

## How it works

`ask(state, questions)` maps tagged helpers (`ask.if`, `ask.choice`, `ask.score`, `ask.chance`, `ask.switch`) onto System One question objects and returns answers under the same keys. The [API client](https://github.com/pithings/advocaat/blob/bc46287fc1102b95852a81d679c6e34a2c44f4a2/src/api.ts) posts to TypeSafe `POST /v1/systemone` or the Vercel AI Gateway evaluation endpoint. Object interpolations become request state paths such as `` `input` `` rather than dumping large JSON into the question text. Requests are not retried; pass `signal` or a custom `fetch` for timeouts. Through the gateway, missing `confidence` is computed locally from `probabilities`.

## Get started

Install from npm (published version matched this review: **0.0.6**):

```sh
npx nypm i advocaat
```

Or from a pinned checkout without publishing:

```sh
git clone https://github.com/pithings/advocaat.git
cd advocaat
git checkout bc46287fc1102b95852a81d679c6e34a2c44f4a2
pnpm install --ignore-scripts
pnpm test
```

Expected: lint, typecheck, and **26** mocked Vitest tests pass. Live calls require a provider key and incur charges. Example:

```ts
import { ask } from "advocaat";

const issue = { title: "Checkout is down", body: "No one can pay." };
const { kind, security, severity } = await ask(issue, {
  kind: ask.choice`What kind of issue is this?`({ bug: "Something is broken", other: null }),
  security: ask.if`Does this issue describe a security vulnerability?`,
  severity: ask.score`How severe is this issue?`([
    "Cosmetic",
    "Workaround exists",
    "Blocks production",
  ]),
});
```

That snippet sends state and questions to the configured provider when awaited.

## Examples and demos

- [Unit tests](https://github.com/pithings/advocaat/tree/bc46287fc1102b95852a81d679c6e34a2c44f4a2/test): mocked request shaping and typed answers; optional live shape checks if `TYPESAFE_API_KEY` is set.
- [Playground triage sample](https://github.com/pithings/advocaat/blob/bc46287fc1102b95852a81d679c6e34a2c44f4a2/playground/triage.ts): illustrative usage; not executed for this listing.
- Install the skill with `npx skills add pithings/advocaat` when you want agent guidance for question design.

## Limits and data handling

State and questions go to TypeSafe or the configured gateway. No built-in retry or redaction. `ask.if` defaults to true only when chance is strictly above `0.5` (configurable). Package version is early (`0.0.x`); pin the reviewed commit for reproducible guides. Gateway confidence behavior can differ slightly from direct TypeSafe responses for longer score rubrics.

## Review and maintenance

Reviewed on **2026-09-19** at [commit bc46287](https://github.com/pithings/advocaat/tree/bc46287fc1102b95852a81d679c6e34a2c44f4a2): package version 0.0.6. AI-assisted source review covered README, license, client, ask helpers, skill, and tests. On Node.js 22.19.0 with pnpm 12.4.2, `pnpm test` passed (**26** tests). No live inference was performed.

Related: [TypeSafeAI.Net](typesafeai-net.md) and [Laravel AI](laravel-ai.md) provide similar typed-client roles in other languages.
