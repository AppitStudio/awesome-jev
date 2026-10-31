# Decision models demo (runnable talk demo comparing Jev, Microsoft-Decision-1 and OpenAI Decisions with a generative LLM)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small zero-dependency Node.js demo for a lightning talk on decision models: send state and typed questions, get a probability per option, and compare a decision model with a generative LLM on the same tasks. One adapter layer supports TypeSafe Jev, Microsoft-Decision-1 on Foundry and the OpenAI Decisions API, and a mock mode runs offline with no keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vibeprogrammer/decision-models-demo) |
| Maintainer | [vibeprogrammer](https://github.com/vibeprogrammer). Independently curated. |
| Format | Node.js 20+ scripts |
| Requirements | Node.js 20+; optional `TYPESAFE_API_KEY` (or Foundry / OpenAI keys); mock mode needs none. |
| License | [MIT](https://github.com/vibeprogrammer/decision-models-demo/blob/e0fb1db674f10f92f256ec0c077af8b49da36900/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/systemone.js`](https://github.com/vibeprogrammer/decision-models-demo/blob/e0fb1db674f10f92f256ec0c077af8b49da36900/src/providers/systemone.js) at the pinned commit. |

## When to use

- Show a team what decision models are with a demo that runs on a plane.
- Mismatch: teaching demo; mock latencies are simulated from published medians.

## How it works

`src/providers/systemone.js` builds the `{state, questions}` request for `POST https://api.typesafe.ai/v1/systemone` (default `jev-latest`); the same shape serves Microsoft-Decision-1, so scenarios never change between providers. Integration evidence: [`src/providers/systemone.js`](https://github.com/vibeprogrammer/decision-models-demo/blob/e0fb1db674f10f92f256ec0c077af8b49da36900/src/providers/systemone.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/vibeprogrammer/decision-models-demo.git && cd decision-models-demo
npm run demo
npm run compare
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vibeprogrammer/decision-models-demo#readme](https://github.com/vibeprogrammer/decision-models-demo#readme)

## Limits and data handling

Demo states go to the selected provider when not in mock mode. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit e0fb1db674f1](https://github.com/vibeprogrammer/decision-models-demo/tree/e0fb1db674f10f92f256ec0c077af8b49da36900). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
