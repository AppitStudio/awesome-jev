# Attribute Engine (finds which content attributes correlate with performance; code counts, Jev labels, Claude proposes)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Python tool that breaks ad copy or other content into attributes, tests which line up with a metric such as conversion rate, and writes new content from what won: code measures countable things, Jev answers the judgment attributes you define in YAML, and Claude proposes new attributes blind.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/redavio/attribute-engine-ad-copy) |
| Maintainer | [redavio](https://github.com/redavio). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python, an OpenRouter or Vercel AI Gateway key for Jev, and an Anthropic (or Vercel) key for Claude; a CSV of content plus a metric. |
| License | [MIT](https://github.com/redavio/attribute-engine-ad-copy/blob/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/attribute_engine/tag.py`](https://github.com/redavio/attribute-engine-ad-copy/blob/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/src/attribute_engine/tag.py) at the pinned commit. |

## When to use

- Find which framing, tone or structure of your ads or emails lines up with performance.
- Mismatch: causal attribution or statistically rigorous A/B analysis; the author calls it an experiment.

## How it works

`src/attribute_engine/tag.py` sends each Jev attribute question through OpenRouter's decisions endpoint (`typesafe/jev-1.13`) or Vercel AI Gateway (`typesafe-ai/jev`), chosen by `jev_provider` in `attributes.yaml`; `compare.py` then tests which attributes correlate with the metric. The README frames results as correlations and hypotheses, not causes. Integration evidence: [`src/attribute_engine/tag.py`](https://github.com/redavio/attribute-engine-ad-copy/blob/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/src/attribute_engine/tag.py).

## Get started

Install from source, set your provider keys, and point it at a CSV of content with a metric column.

```sh
pip install -e .
attribute-engine --input my_content.csv
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/redavio/attribute-engine-ad-copy/blob/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/README.md](https://github.com/redavio/attribute-engine-ad-copy/blob/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/README.md)
- Walkthrough: [github.com/redavio/attribute-engine-ad-copy/tree/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/walkthrough](https://github.com/redavio/attribute-engine-ad-copy/tree/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc/walkthrough)

## Limits and data handling

Content text goes to OpenRouter or Vercel (for Jev) and Anthropic or Vercel (for Claude) on your keys. The maker also offers a free browser version at redavio.com that was not reviewed.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit ac099d0fbdc1](https://github.com/redavio/attribute-engine-ad-copy/tree/ac099d0fbdc1ed7b207cd89de04f32ea3f9fb7bc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
