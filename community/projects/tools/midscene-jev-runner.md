# Midscene JEV Runner

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Community Playwright/Midscene Test runner that lets TypeSafe Jev (via OpenRouter Decisions) pick browser operations and targets on a caller-owned page—independent of the Midscene core repo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KiritoKing/midscene-jev-runner) |
| Maintainer | [KiritoKing](https://github.com/KiritoKing) / package scope `@chlrc`. Independently curated; this entry is not an upstream submission or endorsement. Not an official Midscene package. |
| Format | TypeScript npm package **`@chlrc/midscene-jev-runner` 0.1.2** (`runJev`, `createJevNodes`). |
| Requirements | Node.js `^20.19.0 \|\| ^22.12.0 \|\| >=24`; peer `@midscene/test` + Playwright. `OPENROUTER_API_KEY` (or `MIDSCENE_JEV_API_KEY`); optional `MIDSCENE_JEV_BASE_URL` / `MIDSCENE_JEV_MODEL_NAME`. TYPE_TEXT needs a separate text-model key/base/model. |
| License | [MIT](https://github.com/KiritoKing/midscene-jev-runner/blob/d2aee4ad4ac16367d49f456fcf723b8968872ca7/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `src/runner.ts`, `src/decision.ts`, `src/constants.ts`). Offline install and live browser/Jev were **not** executed on the review host. |

## When to use

Use it when you already drive Playwright (or Midscene Test YAML) and want Jev to choose each browser action from an accessibility-oriented observation, with optional completion verification. Prefer [jev-dom](jev-dom.md) for a DOM action-space research package without Midscene; prefer [Jev Ultrafast](jev-ultrafast.md) for the broader Python agent. The runner does **not** create, navigate, route, or close the supplied `Page`.

## How it works

[`runJev`](https://github.com/KiritoKing/midscene-jev-runner/blob/d2aee4ad4ac16367d49f456fcf723b8968872ca7/src/runner.ts) observes the page, builds a decision request ([`decision.ts`](https://github.com/KiritoKing/midscene-jev-runner/blob/d2aee4ad4ac16367d49f456fcf723b8968872ca7/src/decision.ts)), and posts to OpenRouter Decisions at `https://openrouter.ai/api/alpha` with model `~typesafe/jev-latest` by default ([`constants.ts`](https://github.com/KiritoKing/midscene-jev-runner/blob/d2aee4ad4ac16367d49f456fcf723b8968872ca7/src/constants.ts)). Code executes the chosen operation, can re-check `verifyCompletion` after actions and before the next decision, and emits structured observer events. Password/file inputs are excluded; query strings are stripped from URLs in observations.

## Get started

```sh
pnpm add @chlrc/midscene-jev-runner @midscene/test playwright
export OPENROUTER_API_KEY=...
# See upstream example/ for Midscene Test project setup
```

Pin for review: [commit d2aee4a](https://github.com/KiritoKing/midscene-jev-runner/tree/d2aee4ad4ac16367d49f456fcf723b8968872ca7). Live runs send page observations to the configured Decisions endpoint and can incur charges.

## Examples and demos

- Upstream [`example/`](https://github.com/KiritoKing/midscene-jev-runner/tree/d2aee4ad4ac16367d49f456fcf723b8968872ca7/example) Midscene Test config + YAML `jevAct` step.
- Direct `runJev(page, { goal, verifyCompletion })` API in the README.

## Limits and data handling

Caller owns browser lifecycle. Without `verifyCompletion`, `DONE` is a model judgment, not business proof. Observations and goals leave the machine to OpenRouter/TypeSafe-compatible gateways. This listing did not run Playwright or live Decisions.

## Review and maintenance

Reviewed on **2026-09-23** at [commit d2aee4a](https://github.com/KiritoKing/midscene-jev-runner/tree/d2aee4ad4ac16367d49f456fcf723b8968872ca7) (`@chlrc/midscene-jev-runner` **0.1.2**, MIT). AI-assisted source review of README, LICENSE, runner/decision/constants. No live TypeSafe/OpenRouter spend.

Related: [jev-dom](jev-dom.md), [Jev Ultrafast](jev-ultrafast.md), [Jev Browser (tontoko)](jev-browser-tontoko.md).
