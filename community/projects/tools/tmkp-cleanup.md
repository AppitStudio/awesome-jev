# tmkp-cleanup by cbizon (knowledge-graph cleaning for the Text Mining KP, with Jev judging each supporting sentence)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Code and validation for cleaning the Text Mining Knowledge Provider (TMKP) graph before it enters NCATS Translator. Many text-mined edges misread their sentence or map a mention to the wrong concept, so the pipeline asks Jev (`jev-1.13.0`) a typed question about each supporting sentence and turns the answers into fixed lists of edges to drop, sentences to prune and edges to repair. The lists are published for the translator-ingests pipeline, which applies them without calling any model. Validation labels were made by Claude instances working blind to Jev's answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cbizon/tmkp-cleanup) |
| Maintainer | [cbizon](https://github.com/cbizon). Independently curated. |
| Format | Python scripts using the TypeSafe SDK, run with uv (MIT) |
| Requirements | Python with uv, and `TYPESAFE_API_KEY` for the scripts that call Jev; the published lists need no key. |
| License | [MIT](https://github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/jev_client.py`](https://github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/pipeline/jev_client.py) at the pinned commit. |

## When to use

- See a worked example of using a typed-decision model to clean a large text-mined knowledge graph, with validation against blind labels.
- Mismatch: a reusable library; it is a research pipeline specific to TMKP edge types.

## How it works

`pipeline/jev_client.py` and `treats/prompt.py` send each supporting sentence and a multiple-choice question to Jev (`jev-1.13.0`) through `typesafe-sdk`; the question text is kept in `pipeline/prompts.py`. Integration evidence: [`pipeline/jev_client.py`](https://github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/pipeline/jev_client.py).

## Get started

Read each directory's README for method and results, then run the scoring scripts with your key from a secret store.

```sh
git clone https://github.com/cbizon/tmkp-cleanup && cd tmkp-cleanup
(cd treats && uv run pytest) && (cd pipeline && uv run pytest)
# live scoring (costs money): TYPESAFE_API_KEY=... uv run score_sentences.py ...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Treats README: [github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/treats/README.md](https://github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/treats/README.md)
- Pipeline README: [github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/pipeline/README.md](https://github.com/cbizon/tmkp-cleanup/blob/90f02804a86e65589622e71f2b03040dbdb369c5/pipeline/README.md)

## Limits and data handling

Sentences scored go to TypeSafe on your key. The full recorded answers are not published, only the subsets each validation needs, and the reported results are the authors' own.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 90f02804a86e](https://github.com/cbizon/tmkp-cleanup/tree/90f02804a86e65589622e71f2b03040dbdb369c5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
