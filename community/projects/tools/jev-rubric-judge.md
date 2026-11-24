# jev-rubric-judge by atoyangeor (experiment: Jev answers rubric questions first, a human expert answers only the uncertain ones, on InFoBench)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

On 1,115 yes/no quality questions about LLM-written texts from InFoBench, Jev answered first and an expert answered only the questions Jev was unsure about. The author reports the expert's work fell from 7.9 to 2.0 hours with accuracy 94.9% versus 93.3% for the expert alone, for 1.6 cents of Jev calls; a `gpt-6-luna` judge did about as well at higher cost and latency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atoyangeor/jev-rubric-judge) |
| Maintainer | [atoyangeor](https://github.com/atoyangeor). Independently curated. |
| Format | Python experiment (uv) with frozen data and reproduction scripts |
| Requirements | Python with uv; TypeSafe and OpenAI keys only to re-run model calls. |
| License | [MIT](https://github.com/atoyangeor/jev-rubric-judge/blob/19adc9c7788b47fbfbbe448487d8e4061b9c92f0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_rubric_judge/cli.py`](https://github.com/atoyangeor/jev-rubric-judge/blob/19adc9c7788b47fbfbbe448487d8e4061b9c92f0/src/jev_rubric_judge/cli.py) at the pinned commit. |

## When to use

- Estimate how much human review Jev can save on yes/no rubric grading, with thresholds tuned on your data.
- Mismatch: open-ended grading; the setup assumes yes/no rubric questions.

## How it works

`src/jev_rubric_judge/cli.py` sends each rubric question as a noul (few-shot variant) to `https://api.typesafe.ai/v1/systemone` and applies two probability thresholds to decide which questions go to a person. Integration evidence: [`src/jev_rubric_judge/cli.py`](https://github.com/atoyangeor/jev-rubric-judge/blob/19adc9c7788b47fbfbbe448487d8e4061b9c92f0/src/jev_rubric_judge/cli.py).

## Get started

Sync, run the offline tests, then the grading scripts.

```sh
git clone https://github.com/atoyangeor/jev-rubric-judge.git && cd jev-rubric-judge
uv sync && uv run pytest
uv run python runs/fair_yardstick.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results and method: [github.com/atoyangeor/jev-rubric-judge/blob/19adc9c7788b47fbfbbe448487d8e4061b9c92f0/README.md](https://github.com/atoyangeor/jev-rubric-judge/blob/19adc9c7788b47fbfbbe448487d8e4061b9c92f0/README.md)

## Limits and data handling

One dataset; costs use an assumed expert rate; the author lists caveats before trusting the result. Texts go to TypeSafe and OpenAI when re-run.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 19adc9c7788b](https://github.com/atoyangeor/jev-rubric-judge/tree/19adc9c7788b47fbfbbe448487d8e4061b9c92f0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
