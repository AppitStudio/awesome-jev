# AskGLP1 (paper code: GLP-1 patient-narrative knowledge graph with Jev post screening)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, prompts and evaluation questions for a paper that turns Reddit, WebMD and FAERS data about GLP-1 medications into a source-linked knowledge graph and a KG-grounded question-answering agent; Jev is the screening classifier that keeps posts reporting a drug, a personal experience and clinical detail before GPT extraction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZhaoqianXue/AskGLP1) |
| Maintainer | [ZhaoqianXue](https://github.com/ZhaoqianXue). Independently curated. |
| Format | Python pipeline, web app and evaluation materials |
| Requirements | Python, Neo4j and Node.js for the web app; a TypeSafe key for the screening step and an OpenAI key for extraction; a synthetic offline check runs without keys. |
| License | [MIT](https://github.com/ZhaoqianXue/AskGLP1/blob/9784c42be3d7b18e90d8c07adcb2ed35559bd186/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`results/jev-full-2026-09-29/scripts/full_run.py`](https://github.com/ZhaoqianXue/AskGLP1/blob/9784c42be3d7b18e90d8c07adcb2ed35559bd186/results/jev-full-2026-09-29/scripts/full_run.py) at the pinned commit. |

## When to use

- See how a decision model can pre-screen millions of social posts before an expensive extraction model.
- Reproduce or adapt the paper's pipeline and its 120 evaluation questions.
- Mismatch: research code; not medical advice and not a clinical tool.

## How it works

`results/jev-full-2026-09-29/scripts/full_run.py` sends each post with a `strict_keep` yes/no question to `https://api.typesafe.ai/v1/systemone` (pinned `jev-1.13.0`) and keeps posts whose probability is at least 0.5; a reconcile script records the configuration and prompt hash. Integration evidence: [`results/jev-full-2026-09-29/scripts/full_run.py`](https://github.com/ZhaoqianXue/AskGLP1/blob/9784c42be3d7b18e90d8c07adcb2ed35559bd186/results/jev-full-2026-09-29/scripts/full_run.py).

## Get started

From the upstream README (not run on the review host):

```sh
make install
make reproduce OUTPUT=.cache/synthetic-check   # synthetic offline check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ZhaoqianXue/AskGLP1#readme](https://github.com/ZhaoqianXue/AskGLP1#readme)
- Paper supplement: [github.com/ZhaoqianXue/AskGLP1/tree/main/paper-supplement](https://github.com/ZhaoqianXue/AskGLP1/tree/main/paper-supplement)

## Limits and data handling

Screening sends public post text to TypeSafe; extraction sends it to OpenAI. Results and figures are the authors'. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 9784c42be3d7](https://github.com/ZhaoqianXue/AskGLP1/tree/9784c42be3d7b18e90d8c07adcb2ed35559bd186). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
