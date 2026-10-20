# System One for Delphi

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Single-unit Delphi client for System One models: ask choice, score and noul questions about a text and get typed answers with every option's probability, against TypeSafe's Jev API, a local Ollama model, or any OpenAI-compatible chat model through an adapter with the same interface.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danieleteti/systemone-delphi) |
| Maintainer | [danieleteti](https://github.com/danieleteti). Independently curated. |
| Format | Delphi unit (RTL only; Delphi 12 and 13) |
| Requirements | Delphi 12 or 13; a TypeSafe key for Jev, or Ollama 0.35.1+ with a local System One model. |
| License | [Apache-2.0](https://github.com/danieleteti/systemone-delphi/blob/e2a7fd8b287d0cdab0f643428ecb0905450cbc84/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sources/SystemOne.Client.pas`](https://github.com/danieleteti/systemone-delphi/blob/e2a7fd8b287d0cdab0f643428ecb0905450cbc84/sources/SystemOne.Client.pas) at the pinned commit. |

## When to use

- Route tickets, e-mails or notes in a Delphi backend with a probability instead of parsing LLM prose.
- Develop against a local model and switch to hosted Jev by changing the constructor.
- Mismatch: client library only; you choose the questions and thresholds.

## How it works

`ISystemOneClient.Ask` is implemented by `TSystemOneClient` in `sources/SystemOne.Client.pas`, which posts to `/v1/systemone` (for example `https://api.typesafe.ai` with `jev-latest`), and by `TSystemOneLLMAdapter`, which asks the same questions of a chat model. Answers carry the label, probabilities, confidence and token usage. Integration evidence: [`sources/SystemOne.Client.pas`](https://github.com/danieleteti/systemone-delphi/blob/e2a7fd8b287d0cdab0f643428ecb0905450cbc84/sources/SystemOne.Client.pas).

## Get started

From the upstream README (not run on the review host):

```sh
// copy sources\SystemOne.Client.pas into your project, then:
Client := TSystemOneClient.Create('https://api.typesafe.ai',
  GetEnvironmentVariable('TYPESAFE_API_KEY'), 'jev-latest');
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Full docs: [www.danieleteti.it/systemone-delphi/](https://www.danieleteti.it/systemone-delphi/)
- sample/Triage.dpr and tests/ (36 offline, 15 live checks)

## Limits and data handling

Text goes to TypeSafe when pointed at the Jev API; stays local with Ollama.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit e2a7fd8b287d](https://github.com/danieleteti/systemone-delphi/tree/e2a7fd8b287d0cdab0f643428ecb0905450cbc84). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
