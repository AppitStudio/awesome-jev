# jev-browser by dennisonbertram (TypeScript browser agent where Jev picks each action from a numbered table of real page controls)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

TypeScript library that reads a page into a numbered table of its real controls, has Jev choose which control to use at each step, and acts with real mouse and keyboard input; a small text model only writes field values and plans multi-step tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dennisonbertram/jev-browser) |
| Maintainer | [dennisonbertram](https://github.com/dennisonbertram). Independently curated. |
| Format | npm library on Playwright (TypeScript, MIT) |
| Requirements | Node 22+, Playwright Chromium, a TypeSafe key (`TYPESAFE_API_KEY`) and, for tasks that type or plan, an OpenAI-compatible text-model key (`TEXT_MODEL_API_KEY`). |
| License | [MIT](https://github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decide.ts`](https://github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/src/decide.ts) at the pinned commit. |

## When to use

- Automate short, well-defined web journeys quickly and cheaply with a classifier choosing each click.
- Keep an agent from inventing selectors or actions: it can only pick from controls the library observed.
- Mismatch: open-ended research browsing; the author reports a lower success rate than an LLM-driven control.

## How it works

`src/decide.ts` sends one `POST https://api.typesafe.ai/v1/systemone` request per step with an operation head plus a target choice over the observed control table; the library re-checks the chosen element before sending input, so the model can only return an index, never a selector or code. The author's own benchmark (9 journeys x 3) reports 25/27 tasks done with a 1.3 s median versus 21/27 and 14.5 s for an LLM tool-calling loop; these are author-reported figures. Integration evidence: [`src/decide.ts`](https://github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/src/decide.ts).

## Get started

Install the package and Chromium, load the two keys into your shell, then call `run(context, { goal })` from your own script.

```sh
npm install @dennisonbertram/jev-browser
npx playwright install chromium
export TYPESAFE_API_KEY="your-key"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and benchmark table: [github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/README.md](https://github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/README.md)
- Progress notes and figures: [github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/PROGRESS.md](https://github.com/dennisonbertram/jev-browser/blob/a98a61d6af0afa1982950143e813a9e304145162/PROGRESS.md)

## Limits and data handling

Page control tables (with password and one-time-code values masked to a character count) go to TypeSafe on your key; field text generation goes to the text-model provider you configure. It drives a real browser with your permissions.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit a98a61d6af0a](https://github.com/dennisonbertram/jev-browser/tree/a98a61d6af0afa1982950143e813a9e304145162). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
