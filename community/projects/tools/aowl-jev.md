# jev for aowl by aoughwl (Jev client library and small CLI for the aowl/Nimony language)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Client for TypeSafe's System One API written in aowl (the Nimony language), with errors returned as values, plus a headless CLI that asks one question and prints the probability for each option, a yes/no, or a score. Part of the aoughwl stack alongside its OpenAI and Anthropic clients.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aoughwl/jev) |
| Maintainer | [aoughwl](https://github.com/aoughwl). Independently curated. |
| Format | aowl library + CLI |
| Requirements | The aowlmony toolchain, the aoughwl `jsonref` and `requests` ports, and a TypeSafe API key. |
| License | [MIT](https://github.com/aoughwl/jev/blob/5436ad188e09afb1c6439fadb8c446e3b8015dff/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.aowl`](https://github.com/aoughwl/jev/blob/5436ad188e09afb1c6439fadb8c446e3b8015dff/src/jev.aowl) at the pinned commit. |

## When to use

- People writing aowl/Nimony code who want typed Jev answers.
- Mismatch: other languages; use the official Python or TypeScript SDKs.

## How it works

`src/jev.aowl` builds typed `choice`, `noul` and `score` questions and posts them to `https://api.typesafe.ai/v1/systemone`; the CLI exits 2 with no key and 3 on API errors. Integration evidence: [`src/jev.aowl`](https://github.com/aoughwl/jev/blob/5436ad188e09afb1c6439fadb8c446e3b8015dff/src/jev.aowl).

## Get started

Build with the included script, then ask a question.

```sh
git clone https://github.com/aoughwl/jev && cd jev
./build.sh
export TYPESAFE_API_KEY=...
bin/jev -q "Is this message a question?" --yes-no --state "Does the app work offline?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example program: [github.com/aoughwl/jev/blob/main/examples/ask.aowl](https://github.com/aoughwl/jev/blob/main/examples/ask.aowl)

## Limits and data handling

The state and questions go to TypeSafe. Niche toolchain; needs sibling aoughwl packages to build.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 5436ad188e09](https://github.com/aoughwl/jev/tree/5436ad188e09afb1c6439fadb8c446e3b8015dff). Inspected the README, LICENSE and `src/jev.aowl` at the pinned commit; nothing was built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
