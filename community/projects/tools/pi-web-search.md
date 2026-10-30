# pi-web-search (Pi agent search tool with optional Jev ranking, prompt-injection filtering and coverage checks)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Extension for the Pi coding agent that gives it one search tool over Exa, Parallel, Jina Reader, grep.app and Sourcegraph, keyless by default. On thorough searches an optional classifier, Jev via TypeSafe, Vercel AI Gateway or OpenRouter, receives the query and candidate titles, URLs and excerpts and answers yes/no and choice questions to rank results, suppress likely prompt injection or phishing, and judge whether the evidence covers the query. Code applies the weights and thresholds. Part of the pi-extensions monorepo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GaganSD/pi-extensions) |
| Maintainer | [GaganSD](https://github.com/GaganSD). Independently curated. |
| Format | Pi extension (TypeScript, npm) |
| Requirements | Pi 0.99.0+; Jev access through an existing Pi login to TypeSafe, Vercel AI Gateway or OpenRouter (classifier off by default). |
| License | [MIT](https://github.com/GaganSD/pi-extensions/blob/a5fe18f053c26a696c4823bcd8c9ec188d55398c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pi-web-search/src/classifier/judge.ts`](https://github.com/GaganSD/pi-extensions/blob/a5fe18f053c26a696c4823bcd8c9ec188d55398c/pi-web-search/src/classifier/judge.ts) at the pinned commit. |

## When to use

- Have a coding agent rank and screen web results for relevance and injection before citing them.
- Mismatch: classification runs only on `thorough` searches; other Pi classifiers can replace Jev.

## How it works

`classifier/judge.ts` builds the state from the query and candidate excerpts with typed boolean and choice questions and calls Pi's `classify()` on the pinned model; ranking and filtering policy stays in code. Integration evidence: [`pi-web-search/src/classifier/judge.ts`](https://github.com/GaganSD/pi-extensions/blob/a5fe18f053c26a696c4823bcd8c9ec188d55398c/pi-web-search/src/classifier/judge.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:@gagansd/pi-web-search
/web-search classifier typesafe/jev-latest
/reload
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Classifier setup: [github.com/GaganSD/pi-extensions/tree/a5fe18f053c26a696c4823bcd8c9ec188d55398c/pi-web-search#classifier-api](https://github.com/GaganSD/pi-extensions/tree/a5fe18f053c26a696c4823bcd8c9ec188d55398c/pi-web-search#classifier-api)

## Limits and data handling

With the classifier on, the query and candidate titles, URLs and excerpts are sent to the chosen provider. Found via a third-party Jev project directory (typesafe-jev.com). Independent project; not affiliated with TypeSafe or Pi.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit a5fe18f053c2](https://github.com/GaganSD/pi-extensions/tree/a5fe18f053c26a696c4823bcd8c9ec188d55398c/pi-web-search). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
