# typia (`@typia/jev`)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

typia's `@typia/jev` package generates Jev noul/choice/score questions from TypeScript types — JSDoc comments become instructions and choice descriptions — and `evaluation.decode()` validates Jev's answers back into the declared type; works with `@typesafe-ai/sdk`, Vercel AI SDK and OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samchon/typia) |
| Product homepage | [typia.io](https://typia.io/docs/utilization/jev/) |
| Maintainer | [samchon](https://github.com/samchon). Independently curated. |
| Format | TypeScript compile-time library + adapter package (npm `@typia/jev` 15.1.0 at review) |
| Requirements | TypeScript with the `ttsc` transformer (typia setup), `@typesafe-ai/sdk` or Vercel AI SDK, and a TypeSafe/OpenRouter key. |
| License | [MIT](https://github.com/samchon/typia/blob/d9d3436b757060763fd75415b44fef59f84a618f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Define a triage interface (booleans, string-literal unions, tagged scores) and call Jev with questions generated from it.
- Decode Jev answers into a validated `IValidation<T>` and reuse the same type for OpenAI structured outputs.
- Mismatch: requires typia's compile-time transformer setup.

## How it works

`typia.llm.evaluation<T>()` emits neutral evaluation questions at compile time; [`packages/jev/src/index.ts`](https://github.com/samchon/typia/blob/d9d3436b757060763fd75415b44fef59f84a618f/packages/jev/src/index.ts) converts them to Jev's wire format (`boolean` → `noul`, choice/score unchanged) and `decode()` accepts Jev's native answers. Through Vercel AI SDK the questions go to `experimental_evaluate()` as-is.

## Get started

Install and generate questions from a type:

```sh
npm install @typia/jev typia @typesafe-ai/sdk
npm install -D ttsc typescript@rc
# const evaluation = typia.llm.evaluation<ITriage>();
# const { answers } = await new TypeSafeClient().systemOne({ state, questions: toJevQuestions(evaluation.questions) });
# const result = evaluation.decode(answers);
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [`@typia/jev` README](https://github.com/samchon/typia/blob/d9d3436b757060763fd75415b44fef59f84a618f/packages/jev/README.md) and the [Jev utilization guide](https://typia.io/docs/utilization/jev/).
- Blog post *Generate Jev Schemas from TypeScript Types* (typia.io, 2026-09-30), shared as Show HN.

## Limits and data handling

Listing covers the Jev integration in a general-purpose validation library. State is sent to the configured provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit d9d3436b7570](https://github.com/samchon/typia/tree/d9d3436b757060763fd75415b44fef59f84a618f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
