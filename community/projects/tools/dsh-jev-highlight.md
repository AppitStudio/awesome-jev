# Jev Highlight for DeepSeek Harness (highlight the parts of long AI answers worth reading)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Web plugin for DeepSeek Harness that leaves AI answers unchanged but highlights what to read first: it splits an answer into units, asks a decision model four yes/no questions about each (conclusion, action, risk, relevance) and shades them by priority; StartLux-Decision is the default model and TypeSafe Jev is a supported option. Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Zorien-ai/dsh-jev-highlight) |
| Maintainer | [Zorien-ai](https://github.com/Zorien-ai). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript) |
| Requirements | DeepSeek Harness; an API key for StartLux (via Bamboo Relay) or TypeSafe Jev. |
| License | [MIT](https://github.com/Zorien-ai/dsh-jev-highlight/blob/ef18c9be67754fc39841773751be0a79e10a7c2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/index.js`](https://github.com/Zorien-ai/dsh-jev-highlight/blob/ef18c9be67754fc39841773751be0a79e10a7c2e/lib/index.js) at the pinned commit. |

## When to use

- Skim long agent reports by reading the highlighted conclusions and risks first.
- Mismatch: Jev is optional, not the default model; DeepSeek Harness only.

## How it works

`lib/index.js` defines the provider settings; with Jev selected it posts Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0` in the shipped configs) and weights the probabilities into a priority. Integration evidence: [`lib/index.js`](https://github.com/Zorien-ai/dsh-jev-highlight/blob/ef18c9be67754fc39841773751be0a79e10a7c2e/lib/index.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Zorien-ai/dsh-jev-highlight.git && cd dsh-jev-highlight
dsh plugin --profile <profile> add .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/Zorien-ai/dsh-jev-highlight#readme](https://github.com/Zorien-ai/dsh-jev-highlight#readme)

## Limits and data handling

Answer text goes to the selected decision provider. The plugin does not change the AI's output.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit ef18c9be6775](https://github.com/Zorien-ai/dsh-jev-highlight/tree/ef18c9be67754fc39841773751be0a79e10a7c2e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
