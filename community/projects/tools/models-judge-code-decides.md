# Models Judge, Code Decides, Models Write by Jag Reehal (runnable support-reply example where Jev judges, TypeScript owns every decision and a second model only writes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small TypeScript example of a support workflow: Jev answers four yes/no questions about the customer message, a pure `decide()` function picks the action, code carries it out and states the outcome, another model writes the reply, and Jev checks the draft against the outcome before it is sent, falling back to the code's sentence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jagreehal/models-judge-code-decides-models-write) |
| Maintainer | [Jag Reehal](https://github.com/jagreehal). Independently curated. |
| Format | TypeScript example (AI SDK) |
| Requirements | Node.js 22.18+ and pnpm; a TypeSafe key (`JEV_API_KEY`) and an OpenCode key for the writer model. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/models.ts`](https://github.com/jagreehal/models-judge-code-decides-models-write/blob/ef6fa167c1bb739df3a2a6a8ef02f3017ff5b3e1/src/models.ts) at the pinned commit. |

## When to use

- Learn a pattern where model output can move numbers but never the business rule.
- Mismatch: if you need a production support bot; execution is simulated.

## How it works

`src/models.ts` creates Jev with `@ai-sdk/typesafe-ai` against `https://api.typesafe.ai/v1` (`jev-latest`) and the writer through OpenCode Go's OpenAI-compatible endpoint. Tests for the policy and failure paths run without any model. Integration evidence: [`src/models.ts`](https://github.com/jagreehal/models-judge-code-decides-models-write/blob/ef6fa167c1bb739df3a2a6a8ef02f3017ff5b3e1/src/models.ts).

## Get started

Install, add both keys, run the model-free tests, then the six-message run.

```sh
pnpm install
cp .env.example .env   # add JEV_API_KEY and OPENCODE_API_KEY
pnpm test
pnpm support
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Recorded run: [github.com/jagreehal/models-judge-code-decides-models-write/blob/ef6fa167c1bb739df3a2a6a8ef02f3017ff5b3e1/results/support-latest.txt](https://github.com/jagreehal/models-judge-code-decides-models-write/blob/ef6fa167c1bb739df3a2a6a8ef02f3017ff5b3e1/results/support-latest.txt)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Customer messages also go to OpenCode (a third-party host, non-TypeSafe writer model). The recorded run in `results/` is the author's own.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit ef6fa167c1bb](https://github.com/jagreehal/models-judge-code-decides-models-write/tree/ef6fa167c1bb739df3a2a6a8ef02f3017ff5b3e1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
