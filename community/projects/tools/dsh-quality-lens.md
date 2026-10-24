# Model Quality Radar (DeepSeek Harness plugin with optional Jev scoring)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin that shows a quality and topic-coverage score on every answer, with an evidence-backed report and copy-ready prompt fixes; optional Jev mode scores five dimensions and checks coverage in one request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lishinho/dsh-quality-lens) |
| Maintainer | [lishinho](https://github.com/lishinho). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript) |
| Requirements | DeepSeek Harness (dsh); optional TypeSafe or OpenRouter key for Jev mode. |
| License | [MIT](https://github.com/lishinho/dsh-quality-lens/blob/ab36c4a50e7fa3b256aac4435859ae4712b8b264/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.js`](https://github.com/lishinho/dsh-quality-lens/blob/ab36c4a50e7fa3b256aac4435859ae4712b8b264/lib/jev.js) at the pinned commit. |

## When to use

- See at a glance which answers were incomplete or overconfident.
- Get suggestions for how to ask better next time.
- Mismatch: observes only; it does not rewrite answers.

## How it works

`lib/jev.js` posts the question and answer to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) or OpenRouter's Decisions endpoint; on failure it falls back to local label scoring. Jev mode is off by default. Integration evidence: [`lib/jev.js`](https://github.com/lishinho/dsh-quality-lens/blob/ab36c4a50e7fa3b256aac4435859ae4712b8b264/lib/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile web add github:lishinho/dsh-quality-lens
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/lishinho/dsh-quality-lens#readme](https://github.com/lishinho/dsh-quality-lens#readme)

## Limits and data handling

Only the current question and answer are sent, and only in Jev mode.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit ab36c4a50e7f](https://github.com/lishinho/dsh-quality-lens/tree/ab36c4a50e7fa3b256aac4435859ae4712b8b264). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
