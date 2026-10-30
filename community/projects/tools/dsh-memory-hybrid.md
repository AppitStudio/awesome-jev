# dsh-memory-hybrid (long-term memory plugin for DeepSeek Harness with forgetting curves and optional Jev grading)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Long-term memory plugin for DeepSeek Harness that treats memories as having weight and cost: an authoritative key-value layer, a derived vector index, Ebbinghaus-style decay with revival, and mood modulation, on an embedded SQLite engine with no external services. Extraction and grading are rule-based by default; filling in a Jev endpoint and key lets Jev take over the grading choices. Docs in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dolou12388/dsh-memory-hybrid) |
| Maintainer | [dolou12388](https://github.com/dolou12388). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript, embedded SQLite) |
| Requirements | DeepSeek Harness; an embedding endpoint; optionally a TypeSafe endpoint and key (`jev-1.14.0` default model) for Jev grading. |
| License | [MIT](https://github.com/dolou12388/dsh-memory-hybrid/blob/47105148fc67670051d03d39353882a7f4d2b227/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugin/src/pipeline/pipeline.js`](https://github.com/dolou12388/dsh-memory-hybrid/blob/47105148fc67670051d03d39353882a7f4d2b227/plugin/src/pipeline/pipeline.js) at the pinned commit. |

## When to use

- Give a coding agent memory that fades unimportant items instead of recalling everything equally.
- Mismatch: Jev is optional and off until both endpoint and key are set; rules handle grading otherwise.

## How it works

`pipeline.js` calls Jev only when `jevEndpoint` and `jevApiKey` are both configured, then lets Jev's classification set each extracted candidate's kind, tier and importance before writing; otherwise the rule extractor decides. Integration evidence: [`plugin/src/pipeline/pipeline.js`](https://github.com/dolou12388/dsh-memory-hybrid/blob/47105148fc67670051d03d39353882a7f4d2b227/plugin/src/pipeline/pipeline.js).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile <your-profile> add "link:<this-dir>/plugin"
# Settings -> Memory: set jevEndpoint to https://api.typesafe.ai/v1/systemone and jevApiKey
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install and design notes (Chinese): [github.com/dolou12388/dsh-memory-hybrid/blob/47105148fc67670051d03d39353882a7f4d2b227/plugin/README.md](https://github.com/dolou12388/dsh-memory-hybrid/blob/47105148fc67670051d03d39353882a7f4d2b227/plugin/README.md)

## Limits and data handling

With Jev enabled, conversation snippets being graded are sent to TypeSafe. Keys are stored write-only in settings. Not affiliated with TypeSafe or DeepSeek.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 47105148fc67](https://github.com/dolou12388/dsh-memory-hybrid/tree/47105148fc67670051d03d39353882a7f4d2b227). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
