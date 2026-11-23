# Building a model router by Rhys Lindmark (AI Engineer workshop: route prompts with Jev judgments and a truth table in code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A hands-on workshop with slides, a local router page and an eval. Level 1 asks Jev one Choice ("which model should I use?"); level 2 breaks the decision into judgments a person could answer from the prompt and picks the model with a table in code; level 3 scores every router on 168 graded prompts against fixed, perfect and random routing and helps you build an eval for your own project.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rhys-Lindmark/model-router-workshop) |
| Maintainer | [Rhys-Lindmark](https://github.com/Rhys-Lindmark). Independently curated. |
| Format | Node.js workshop repo (no dependencies) + slides |
| Requirements | Git and Node.js 22+; a TypeSafe key to route your own prompts and an OpenRouter key to have real models answer (the app and scoring work offline on saved Jev answers). |
| License | [MIT](https://github.com/Rhys-Lindmark/model-router-workshop/blob/24350136ba0cdd2fd05bba3578d7f84163ab5b04/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/Rhys-Lindmark/model-router-workshop/blob/24350136ba0cdd2fd05bba3578d7f84163ab5b04/src/jev.js) at the pinned commit. |

## When to use

- Learn, or teach in 15 or 45 minutes, how to turn a routing decision into Jev judgments plus a policy you can test.
- Mismatch: a production gateway; this is a teaching repo with a reference router.

## How it works

`src/jev.js` posts typed questions to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`; `scripts/ask.js` asks your questions about all 168 prompts and caches the answers so `npm run score` can compare routers offline. `npm run my-eval` runs every option on your own prompts with a $1 cap. Integration evidence: [`src/jev.js`](https://github.com/Rhys-Lindmark/model-router-workshop/blob/24350136ba0cdd2fd05bba3578d7f84163ab5b04/src/jev.js).

## Get started

Run the doctor and the router page offline, then add keys to route your own prompts.

```sh
git clone https://github.com/Rhys-Lindmark/model-router-workshop.git && cd model-router-workshop
npm run doctor
npm run app        # http://localhost:3401
npm run score      # scores every router on the 168 test prompts
cp .env.example .env   # TYPESAFE_API_KEY, OPENROUTER_API_KEY
npm run doctor -- --live
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Slides: [rhys-lindmark.github.io/model-router-workshop/slides/](https://rhys-lindmark.github.io/model-router-workshop/slides/)
- Live reference router: [ai.rhyslindmark.com/jev/model-router](https://ai.rhyslindmark.com/jev/model-router)
- Workshop guide: [github.com/Rhys-Lindmark/model-router-workshop/blob/24350136ba0cdd2fd05bba3578d7f84163ab5b04/docs/WORKSHOP.md](https://github.com/Rhys-Lindmark/model-router-workshop/blob/24350136ba0cdd2fd05bba3578d7f84163ab5b04/docs/WORKSHOP.md)

## Limits and data handling

The headline figures (for example Router v2 passing 91.1% at $3.20 per 1,000 prompts) are the author's own eval on his 168 prompts. Live mode sends prompts to TypeSafe and OpenRouter.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 24350136ba0c](https://github.com/Rhys-Lindmark/model-router-workshop/tree/24350136ba0cdd2fd05bba3578d7f84163ab5b04). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
