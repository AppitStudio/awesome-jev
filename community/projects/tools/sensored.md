# sensored

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Streaming-first TypeScript PII redaction library (155 regex detectors, optional NER, Node/Bun/Deno/browser/edge) with opt-in Jev semantic confirmation (`semantic: { provider: "jev" }`) that asks TypeSafe Jev to confirm detected candidates before redacting.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atomicpages/sensored) |
| Product homepage | [atomicpages.github.io](https://atomicpages.github.io/sensored/) |
| Maintainer | [atomicpages](https://github.com/atomicpages). Independently curated. |
| Format | TypeScript library + CLI (npm `sensored`, 1.7.0 at review) |
| Requirements | Node.js 20+, Bun, Deno, browsers or edge runtimes; optional `@typesafe-ai/sdk` and `TYPESAFE_API_KEY` for semantic confirmation. |
| License | npm package metadata for `sensored` declares MIT, but the repository has **no LICENSE file** at the reviewed commit. Confirm terms with the maintainer before redistributing. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Redact PII from logs, LLM prompts or streams with deterministic detectors, and add a semantic second check only where regexes are ambiguous (person names).
- Keep sync `redact()` and `stream()` paths model-free while using `redactAsync()` with Jev for higher precision.
- Mismatch: only `person_name_lite` is opted into Jev confirmation at review; other detectors stay rule-based.

## How it works

Detectors find candidates; with `semantic.provider: "jev"` the async redactor asks Jev whether each `person_name_lite` candidate really is a person's name and records `semanticConfirmed` on the detection before redacting. Semantic code lives under [`packages/sensored/src/semantic`](https://github.com/atomicpages/sensored/tree/5d62a46bf415916a011ce5b3d04d2ad0cd55ca65/packages/sensored/src/semantic); the guide is [`docs/guide/semantic-confirmation.md`](https://github.com/atomicpages/sensored/blob/5d62a46bf415916a011ce5b3d04d2ad0cd55ca65/docs/guide/semantic-confirmation.md).

## Get started

Install the library (and the optional TypeSafe SDK for semantic confirmation):

```sh
npm install sensored @typesafe-ai/sdk
export TYPESAFE_API_KEY=...
# createRedactor({ rules: { person_name_lite: { action: "redact" } },
#                 semantic: { provider: "jev", apiKey: process.env.TYPESAFE_API_KEY } })
# await redactor.redactAsync("Contact John Smith today")
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Browser [playground](https://atomicpages.github.io/sensored/playground) with presets (processed locally; no Jev call).
- README *Semantic confirmation* snippet and the `eval/config-jev.json` evaluation config.

## Limits and data handling

The README's 100% precision/recall figure for `person_name_lite` with Jev is an upstream evaluation, not reproduced here. Candidate text is sent to TypeSafe when semantic confirmation is enabled. No LICENSE file in the repository (npm metadata says MIT). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 5d62a46bf415](https://github.com/atomicpages/sensored/tree/5d62a46bf415916a011ce5b3d04d2ad0cd55ca65). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
