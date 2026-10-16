# Decision Models Lab

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hands-on lab for decision models: send the same support ticket and typed questions to TypeSafe Jev and Microsoft Decision-1 through OpenRouter, compare answers and confidences, and learn when to hand a case to Claude for careful reasoning.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shashikantdev3/decision-models-lab) |
| Maintainer | [shashikantdev3](https://github.com/shashikantdev3). Independently curated. |
| Format | TypeScript examples and lab site (Node.js) |
| Requirements | Node.js 20.12+, an OpenRouter key with a little credit. |
| License | [MIT](https://github.com/shashikantdev3/decision-models-lab/blob/8680edc743aac34b6ad003bf48c3f39bdfff372f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/hello-world/hello.ts`](https://github.com/shashikantdev3/decision-models-lab/blob/8680edc743aac34b6ad003bf48c3f39bdfff372f/examples/hello-world/hello.ts) at the pinned commit. |

## When to use

- Get a first Jev call working in about five minutes and see typed answers with probabilities.
- Compare two decision models on identical questions before choosing one.
- Mismatch: learning material, not a production router.

## How it works

The hello-world example builds `OpenRouterDecisions` with model `typesafe/jev-1.14` by default (pass another ID such as Microsoft Decision-1 as an argument) and asks urgency, team and severity questions about a ticket. Integration evidence: [`examples/hello-world/hello.ts`](https://github.com/shashikantdev3/decision-models-lab/blob/8680edc743aac34b6ad003bf48c3f39bdfff372f/examples/hello-world/hello.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/shashikantdev3/decision-models-lab.git && cd decision-models-lab
npm install
cp .env.example .env   # set OPENROUTER_API_KEY
npm run hello
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample output for Jev 1.14 in the README.

## Limits and data handling

Ticket text goes to OpenRouter on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 8680edc743aa](https://github.com/shashikantdev3/decision-models-lab/tree/8680edc743aac34b6ad003bf48c3f39bdfff372f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
