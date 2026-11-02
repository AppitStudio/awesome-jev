# ModelRoute (DeepSeek Harness plugin where a Jev judge routes each turn to haiku, sonnet or opus)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin that registers one `auto` model: a small judge call per turn decides whether the turn needs the haiku, sonnet or opus tier and forwards it to the model you mapped there, with a settings panel and a cost monitor. Jev (System One) or StartLux can be the judge; README in English and Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ochprince/model-route) |
| Maintainer | [ochprince](https://github.com/ochprince). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript packages) |
| Requirements | DeepSeek Harness, Node.js, a Jev key (or StartLux); keys for the models you map to each tier. |
| License | [Apache-2.0](https://github.com/ochprince/model-route/blob/8b7676ade25a7b6ae4f4dc5f47c9cf45afd4cc86/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/dsh-llm-model-route/lib/jev.js`](https://github.com/ochprince/model-route/blob/8b7676ade25a7b6ae4f4dc5f47c9cf45afd4cc86/packages/dsh-llm-model-route/lib/jev.js) at the pinned commit. |

## When to use

- Stop paying top-model prices for routine coding turns.
- Mismatch: savings depend on your tier mapping; without a judge key every turn runs on the default.

## How it works

`packages/dsh-llm-model-route/lib/jev.js` speaks TypeSafe's `POST /v1/systemone` and returns the tier choice; `lib/judges.js` switches between the Jev and StartLux judges. Integration evidence: [`packages/dsh-llm-model-route/lib/jev.js`](https://github.com/ochprince/model-route/blob/8b7676ade25a7b6ae4f4dc5f47c9cf45afd4cc86/packages/dsh-llm-model-route/lib/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ochprince/model-route.git
npm run test   # decision core, no Harness needed
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Chinese README: [github.com/ochprince/model-route/blob/main/README.zh.md](https://github.com/ochprince/model-route/blob/main/README.zh.md)

## Limits and data handling

Each turn's request text is sent to the judge provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 8b7676ade25a](https://github.com/ochprince/model-route/tree/8b7676ade25a7b6ae4f4dc5f47c9cf45afd4cc86). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
