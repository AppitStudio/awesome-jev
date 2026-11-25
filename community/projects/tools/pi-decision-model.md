# pi-decision-model by ahati (Pi coding-agent extension that adds Jev 1.14 and other decision models from OpenCode Go)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Extension for the Pi coding agent that registers OpenCode Go's decision models (`jev-1.14`, plus Google's `gemini-decision-1` and OpenAI's `gpt-6-luna-decision`) as classifier models, so Pi's code mode can ask typed yes/no, choice and score questions, and adds a `/decision-model` picker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ahati/pi-decision-model) |
| Maintainer | [ahati](https://github.com/ahati). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi 1.6+ and an OpenCode Go subscription (`opencode-go` credential or `OPENCODE_API_KEY`). |
| License | [MIT](https://github.com/ahati/pi-decision-model/blob/748417acab7c923d07e5205c32f5b03a6279fa99/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/index.ts`](https://github.com/ahati/pi-decision-model/blob/748417acab7c923d07e5205c32f5b03a6279fa99/extensions/index.ts) at the pinned commit. |

## When to use

- Use Jev for routing, triage or guardrails inside the Pi agent without a separate TypeSafe key.
- Mismatch: if you call TypeSafe directly; this goes through OpenCode Go.

## How it works

`extensions/index.ts` adds the models to the `opencode-go` provider with base URL `https://opencode.ai/inference/go/systemone/v1`; Pi's System One transport appends `/systemone`. Requests are billed to the OpenCode Go subscription. Integration evidence: [`extensions/index.ts`](https://github.com/ahati/pi-decision-model/blob/748417acab7c923d07e5205c32f5b03a6279fa99/extensions/index.ts).

## Get started

Install the extension into Pi and reload.

```sh
pi install git:github.com/ahati/pi-decision-model
# then /reload in pi and call models.classify(...) from codemode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README usage: [github.com/ahati/pi-decision-model/blob/748417acab7c923d07e5205c32f5b03a6279fa99/README.md](https://github.com/ahati/pi-decision-model/blob/748417acab7c923d07e5205c32f5b03a6279fa99/README.md)

## Limits and data handling

Jev is reached through OpenCode Go (a third-party host), not TypeSafe directly; the Gemini and OpenAI decision models are non-TypeSafe. Prices in the README are the author's snapshot.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 748417acab7c](https://github.com/ahati/pi-decision-model/tree/748417acab7c923d07e5205c32f5b03a6279fa99). Inspected the README and the extension code at the pinned commit; the extension was not installed on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
