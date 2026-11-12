# Morning AI Brief (You.com and Jev n8n workflow that posts cited AI news briefs to Slack)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

n8n workflow from You.com: every weekday it searches You.com for AI news per topic, asks Jev three questions about each article (a real new development, on topic, how material for your team), keeps only the confident and material ones, and has You.com Research write a short cited brief per topic for Slack.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/youdotcom-oss/n8n-ai-brief-workflow) |
| Maintainer | [youdotcom-oss](https://github.com/youdotcom-oss). Independently curated. |
| Format | n8n workflow template and `workflow.json` (MIT) |
| Requirements | n8n (Cloud or self-hosted) with the verified You.com and TypeSafe AI nodes, a You.com API key, a TypeSafe key (or Gateway credits on n8n Cloud), and a Slack app. |
| License | [MIT](https://github.com/youdotcom-oss/n8n-ai-brief-workflow/blob/fa0e1b6d387c695bc20c5a42c894dc09424c9cdf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered through n8n's announcement; the workflow is maintained by You.com. Discovered via X ([post](https://x.com/n8n_io/status/2120831738666500510)). |
| Jev evidence | [`workflow.json`](https://github.com/youdotcom-oss/n8n-ai-brief-workflow/blob/fa0e1b6d387c695bc20c5a42c894dc09424c9cdf/workflow.json) at the pinned commit. |

## When to use

- Get a daily Slack brief of real AI developments without roundups and explainers.
- Reuse the Jev filter pattern for any topic feed in n8n.
- Mismatch: needs paid You.com and TypeSafe usage; tuning numbers are the author's.

## How it works

`workflow.json` uses TypeSafe's official n8n node (`@typesafe-ai/n8n-nodes-typesafe-ai`) with `jev-latest`; thresholds (0.8 for the yes/no questions, 1.3 on a 0 to 2 materiality score) were tuned by the author on 674 articles, with evals in the repo. Integration evidence: [`workflow.json`](https://github.com/youdotcom-oss/n8n-ai-brief-workflow/blob/fa0e1b6d387c695bc20c5a42c894dc09424c9cdf/workflow.json).

## Get started

Import the template from the n8n library (or `workflow.json`), add the credentials and edit the Config node's topics and team description.

```sh
# n8n menu -> Import from File -> workflow.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- n8n template: [n8n.io/workflows/20558-send-weekday-ai-news-briefs-to-slack-with-youcom-and-typesafe-jev/](https://n8n.io/workflows/20558-send-weekday-ai-news-briefs-to-slack-with-youcom-and-typesafe-jev/)
- n8n blog spotlight: [blog.n8n.io/spotlight-you-com/](https://blog.n8n.io/spotlight-you-com/)

## Limits and data handling

Article titles and snippets go to TypeSafe; searches and briefs go to You.com; briefs post to your Slack.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit fa0e1b6d387c](https://github.com/youdotcom-oss/n8n-ai-brief-workflow/tree/fa0e1b6d387c695bc20c5a42c894dc09424c9cdf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
