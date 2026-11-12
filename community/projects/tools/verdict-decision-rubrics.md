# Verdict (one rubric run on Jev and other decision models, side by side)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that turns a rubric of criteria, scales and levels into the typed questions each decision model takes, sends the same questions to Jev, Cloudflare Clef, OpenRouter, OpenAI's Decisions API and others, and shows where the models agree with your labels and with each other.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ustay-coder/verdict) |
| Maintainer | [Ustay-coder](https://github.com/Ustay-coder). Independently curated. |
| Format | CLI and core library on npm (TypeScript, MIT) |
| Requirements | Node 20+, `npm install -g @verdict-ai/cli`, and a key for each service you compare (`TYPESAFE_API_KEY` for Jev). A mock model runs without any key. |
| License | [MIT](https://github.com/Ustay-coder/verdict/blob/c6e33c3e6801c798a2b1dfc3b369124d017b12f6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/core/src/judges/decision/providers.ts`](https://github.com/Ustay-coder/verdict/blob/c6e33c3e6801c798a2b1dfc3b369124d017b12f6/packages/core/src/judges/decision/providers.ts) at the pinned commit. |

## When to use

- Check how Jev and other decision models answer your own cases before choosing one.
- Keep a rubric fixed and re-run it as model versions change.
- Mismatch: an evaluation tool; small case sets do not rank models.

## How it works

`providers.ts` defines a System One adapter that posts the rubric's questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) and the same request shape to OpenRouter's decisions endpoint; `verdict diff` compares any two kept runs case by case. Integration evidence: [`packages/core/src/judges/decision/providers.ts`](https://github.com/Ustay-coder/verdict/blob/c6e33c3e6801c798a2b1dfc3b369124d017b12f6/packages/core/src/judges/decision/providers.ts).

## Get started

Install the CLI, try the bundled Banking77 example with the mock model, then name the models you have keys for.

```sh
npm install -g @verdict-ai/cli
verdict run -r examples/banking77/intent.yaml -d examples/banking77/cases.jsonl --models mock
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Banking77 example: [github.com/Ustay-coder/verdict/tree/c6e33c3e6801c798a2b1dfc3b369124d017b12f6/examples/banking77](https://github.com/Ustay-coder/verdict/tree/c6e33c3e6801c798a2b1dfc3b369124d017b12f6/examples/banking77)
- Docs: [docs.verdict-ai.dev](https://docs.verdict-ai.dev)

## Limits and data handling

Your cases go to each provider you name, on your keys; runs are kept locally.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit c6e33c3e6801](https://github.com/Ustay-coder/verdict/tree/c6e33c3e6801c798a2b1dfc3b369124d017b12f6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
