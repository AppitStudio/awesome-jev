# classifier.dev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-shot text classification over plain HTTP, a CLI, and MCP: a Cloudflare Worker packs inputs into TypeSafe Jev requests and returns a label with calibrated confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrmps/classifier-dev) |
| Product homepage | [classifier.dev](https://classifier.dev) |
| Maintainer | [mrmps](https://github.com/mrmps). Independently curated. |
| Format | Hosted HTTP API (classifier.dev), self-hostable Worker source, npm CLI, and MCP server |
| Requirements | None for anonymous hosted calls (per-IP rate limits). Paid workspace keys are required for the Fast/long-context paths (retail priced per million context tokens per upstream README). Self-hosting needs Cloudflare Workers and `TYPESAFE_API_KEY` (plus optional fallback provider keys). |
| License | [MIT](https://github.com/mrmps/classifier-dev/blob/b9211dd39ccbfea839a066dab4823b7151a6ac2f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Hosted service with free anonymous access and paid workspace tiers (see upstream README/site). |

## When to use

- Quick zero-shot labeling from shell scripts or agents without an account.
- Batch up to a thousand texts per request, or classify long documents through the paid workspace path.
- Mismatch: sensitive data should not go to a third-party hosted endpoint; self-host the Worker instead.

## How it works

The Worker validates input, packs texts and labels into Jev requests (`src/jev.ts`), and reads Jev's probabilities to return the top label and confidence. It includes an LLM fallback chain, per-IP rate limiting, and cost accounting.

## Get started

Try the hosted endpoint or install the CLI:

```sh
curl https://classifier.dev/spam,not+spam/Win+a+free+iPhone
npm i -g classifier-dev
classify bug,feature,praise < feedback.txt
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Hosted docs and benchmark page at [classifier.dev](https://classifier.dev); upstream `eval/` benchmarks (read `eval/README.md` before quoting numbers).

## Limits and data handling

Hosted calls send text to the classifier.dev operator and on to TypeSafe or a fallback model. Paid tiers apply to Fast and long-document paths; check current terms on the site. Confidence is calibrated by the model, not a correctness guarantee.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit b9211dd39ccb](https://github.com/mrmps/classifier-dev/tree/b9211dd39ccbfea839a066dab4823b7151a6ac2f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
