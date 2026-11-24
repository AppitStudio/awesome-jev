# Releval (self-hosted search relevance evaluation with AI judges that grade results with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted tool for search engineers to evaluate and track search relevance (NDCG, MRR) against Elasticsearch, OpenSearch, Vespa or any search API. Since 1.2.0 its AI judges can grade each result with Jev, recording a probability for every grade so you can see where the judge hesitated and which judgments to sample; 1.3.0 adds OpenAI's Decisions API under a common decision-model type.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://releval.co) |
| Tags | `Closed source` · `Freemium` · `Commercial` · `BYOK` |
| Product homepage | [Product homepage](https://releval.co) |
| Pricing and access | [Pricing](https://releval.co/pricing): free Individual tier (1 user, 1 search endpoint, 1 App Client, unlimited evaluations); Team and Enterprise tiers are paid via a license file (prices not listed publicly). Self-hosted. Jev and other AI judges use your own provider keys, billed separately. Checked 2026-11-24. |
| Jev evidence | [`blog/jev-ai-judges/`](https://releval.co/blog/jev-ai-judges/) at the pinned release. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Closed source: the implementation could not be inspected; Jev support is vendor-reported (release notes), not checked hands-on. Commercial product: free Individual tier, paid Team and Enterprise licenses; check current pricing. No relationship with the vendor. Discovered via X ([post](https://x.com/releval_co/status/2125230203555528898)). |
| Maintainer | Releval (founder Russ Cam, [releval.co](https://releval.co)). Independently curated. |
| Format | Self-hosted web app (closed source) |
| Platform and availability | Self-hosted server with a web UI (downloadable from releval.co). |
| Jev's role | A decision judge sends Jev the query, the result's title and mapped fields, and one description per grade on the evaluation's scale; Jev returns a probability per grade and Releval records the grade from them. |
| Requirements | Your own infrastructure, a search endpoint to evaluate, and a TypeSafe (or OpenAI) key for decision judges. |
| License | [Proprietary self-hosted license (Releval License Agreement)](https://releval.co/pricing) |

## When to use

- Widen relevance-judgment coverage cheaply and know which AI judgments are worth checking by hand.
- Mismatch: if you need open-source tooling; Releval is closed source with paid team tiers.

## How it works

Per the vendor's 1.2.0 release notes, a Jev judge is set up like any other AI judge (provider, model, template) and asks one Score-style question per result; judgments keep the full probability distribution. Integration evidence: [`blog/jev-ai-judges/`](https://releval.co/blog/jev-ai-judges/).

## Get started

Download Releval, follow the getting-started docs, then add an AI judge with the decision-model type and Jev as the model.

```sh
# see https://releval.co/docs for install and configuration
# then: AI Judges → new judge → model type: decision model → Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Judging relevance with Jev (1.2.0): [releval.co/blog/jev-ai-judges/](https://releval.co/blog/jev-ai-judges/)
- Decision models and a UI glow up (1.3.0): [releval.co/blog/decision-models-and-a-ui-glow-up/](https://releval.co/blog/decision-models-and-a-ui-glow-up/)
- Docs: [releval.co/docs/](https://releval.co/docs/)

## Limits and data handling

Closed source, so data handling could not be verified; the vendor says Releval is self-hosted and no data leaves your environment, but queries and results sent to Jev go to TypeSafe. Team and Enterprise prices are not public.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [Releval 1.3.0 release notes](https://releval.co/blog/decision-models-and-a-ui-glow-up/). Closed source: the implementation could not be inspected. Read the vendor's 1.2.0 and 1.3.0 release notes, docs index and pricing page; Jev support is vendor-reported, not checked hands-on. The app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
