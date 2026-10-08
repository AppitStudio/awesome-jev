# model-router (muhx)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that picks the model and reasoning effort for each task with Jev — subagent model at spawn, main-loop effort per turn, and (on by default in this fork) main-loop model — using TypeSafe's `/v1/systemone` (`jev-latest`) or the Vercel AI Gateway, with a risky-task `noul`, confidence-aware policy and a built-in fallback classifier. A derivative of claude-code-templates' `jev-model-router` (also listed) under MIT.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muhx/model-router) |
| Maintainer | [muhx](https://github.com/muhx). Independently curated. |
| Format | Claude Code plugin (`/plugin install model-router --marketplace muhx/model-router`) |
| Requirements | Claude Code with mods; `TYPESAFE_API_KEY` or a Vercel AI Gateway key (otherwise built-in classifier). |
| License | [MIT](https://github.com/muhx/model-router/blob/faa16112607ae66c18975393fc2c59bc96601981/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route cheap tasks to fast models and hard ones to stronger models automatically.
- Mismatch: main-loop model switching invalidates prompt cache; this fork enables it by default.

## How it works

[`hooks/model-router.ts`](https://github.com/muhx/model-router/blob/faa16112607ae66c18975393fc2c59bc96601981/hooks/model-router.ts) asks Jev for tier, effort and risk; [`hooks/policy.ts`](https://github.com/muhx/model-router/blob/faa16112607ae66c18975393fc2c59bc96601981/hooks/policy.ts) applies confidence thresholds before changing anything.

## Get started

Install as a plugin (README *Install*):

```sh
/plugin install model-router --marketplace muhx/model-router
```

One Jev request per routed turn/spawn on your key.

## Examples and demos

- README sample log lines (`jev: tier fast (0.87) · effort 0.4 → low`).

## Limits and data handling

Task text goes to TypeSafe or Vercel. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit faa16112607a](https://github.com/muhx/model-router/tree/faa16112607ae66c18975393fc2c59bc96601981). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
