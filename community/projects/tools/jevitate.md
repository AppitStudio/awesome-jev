# Jevitate

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Autonomous browser testing that explores your web app, reports only failures the browser can prove (HTTP 5xx, uncaught exceptions, hangs, failed checks) and turns each one into a replayable recording and deterministic regression test; Jev handles its judgment questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/matt-cochran/jevitate) |
| Maintainer | [matt-cochran](https://github.com/matt-cochran). Independently curated. |
| Format | Node.js CLI (`@jevitate/cli`) with MCP server and agent skills |
| Requirements | Node.js 22+, a locally running web app, `OPENROUTER_API_KEY` for generation and Jev judgment (or `TYPESAFE_API_KEY` for Jev). |
| License | [MIT](https://github.com/matt-cochran/jevitate/blob/9c262eaec5dc624da416932a7311748a2fa5b327/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/ai-core/src/jev-sdk-adapter.ts`](https://github.com/matt-cochran/jevitate/blob/9c262eaec5dc624da416932a7311748a2fa5b327/packages/ai-core/src/jev-sdk-adapter.ts) at the pinned commit. |

## When to use

- Find failures nobody wrote a test for, then commit them as regressions for CI.
- Verify a fix by replaying the recording that reproduced the bug.
- Mismatch: a model only suggests what to try; pass or fail is decided by code-level oracles, so Jev is one part of the loop.

## How it works

An adapter translates Jevitate's judgment questions and answers to `@typesafe-ai/sdk`; exploration may be model-guided, but detection uses code-decided oracles and every defect is reproduced in fresh contexts before it is reported. Integration evidence: [`packages/ai-core/src/jev-sdk-adapter.ts`](https://github.com/matt-cochran/jevitate/blob/9c262eaec5dc624da416932a7311748a2fa5b327/packages/ai-core/src/jev-sdk-adapter.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g @jevitate/cli
jevitate install-browser
jevitate init
jevitate explore --strategy adversarial --url http://localhost:3000/settings --fake-ai
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Two-minute no-key demo: `docs/demo.md`.
- Website: [jevitate.com](https://jevitate.com)

## Limits and data handling

Page content used for judgments goes to OpenRouter or TypeSafe on your key; recordings and regressions stay in `.jevitate/` in your repo.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 9c262eaec5dc](https://github.com/matt-cochran/jevitate/tree/9c262eaec5dc624da416932a7311748a2fa5b327). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
