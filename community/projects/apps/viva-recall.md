# Viva Recall (flashcards you answer in your own words, marked by Jev, with an appeal agent you can argue with)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

A desktop flashcard app for open-ended recall. You write a question and the answer you expect, an LLM turns that answer into small yes/no checks, and at review time Jev answers every check in one request; plain code turns the probabilities into a verdict and FSRS schedules the next review. If you dispute a mark, an appeal agent can fix the checks, but only if your previously settled answers still pass.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jacquescogal/viva-recall) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jacquescogal/viva-recall#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build: run it with `npm run dev` using your own TypeSafe key and LLM key. No packaged release and no license file, so reuse terms are not granted. Checked 2026-11-22. |
| Jev evidence | [`src/main/marker/jev.ts`](https://github.com/jacquescogal/viva-recall/blob/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1/src/main/marker/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jacquescogal](https://github.com/jacquescogal). Independently curated. |
| Format | Electron + React desktop app |
| Platform and availability | Electron desktop app (tested on macOS, Apple Silicon); local SQLite. |
| Jev's role | Marks each review: one `noul` question per check, sent with only the question and your answer as state; code bands the probabilities (yes / no / unsure) and applies the card's rule. |
| Requirements | Node 20+, a TypeSafe API key for Jev and an LLM key (OpenAI-compatible or Anthropic) for writing checks and appeals; Laya can be tried locally as an experimental marker. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Study material where the answer is a sentence or two in your own words, not a single fact you can type exactly.
- Mismatch: Windows or Linux users who need a packaged build; only an unpacked macOS build (`npm run dist:mac`) is documented.

## How it works

`src/main/marker/jev.ts` posts to `https://api.typesafe.ai/v1/systemone` with the pinned model version from the Electron main process (keys stay out of the renderer and are encrypted with the OS keychain); the verdict rules are in `src/main/domain/decide.ts`. A bundled set of 60 labelled answers is run once as a health check of the marker. Integration evidence: [`src/main/marker/jev.ts`](https://github.com/jacquescogal/viva-recall/blob/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1/src/main/marker/jev.ts).

## Get started

Install and start the dev build; the setup wizard asks for your keys, tests the connection and runs the calibration health check.

```sh
git clone https://github.com/jacquescogal/viva-recall && cd viva-recall
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshots: [github.com/jacquescogal/viva-recall/blob/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1/docs/screenshots/library.png](https://github.com/jacquescogal/viva-recall/blob/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1/docs/screenshots/library.png)
- Specs (openspec): [github.com/jacquescogal/viva-recall/tree/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1/openspec/specs](https://github.com/jacquescogal/viva-recall/tree/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1/openspec/specs)

## Limits and data handling

Each review sends the question and your answer to TypeSafe; card generation and appeals go to the LLM you configure. Laya support is marked experimental. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 6c5b59bfdf2c](https://github.com/jacquescogal/viva-recall/tree/6c5b59bfdf2c648047746d24c42be3e0c62f4ae1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
