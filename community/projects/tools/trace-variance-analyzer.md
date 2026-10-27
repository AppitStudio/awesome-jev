# Trace Variance Analyzer (flag likely failed agent runs from one run, with one Jev read)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Scores AI agent runs you already have, with no answer key: Jev reads the task, the visible steps and the final answer once and returns the probability the answer is right; an optional pairing step uses an LLM judge to compare two runs of the same task. Includes the author's measurements on four frontier models and an evaluate command to check the scores on your own labelled sample.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BeakrHub/TraceVarianceAnalyzer) |
| Maintainer | [BeakrHub](https://github.com/BeakrHub). Independently curated. |
| Format | Python CLI (standard library) |
| Requirements | Python 3.9+; a TypeSafe API key for scoring, and an OpenAI key only for the optional pairing step. |
| License | [MIT](https://github.com/BeakrHub/TraceVarianceAnalyzer/blob/05d988c39b7293dee062d126fbf8cf810c266538/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`onerun/jev.py`](https://github.com/BeakrHub/TraceVarianceAnalyzer/blob/05d988c39b7293dee062d126fbf8cf810c266538/onerun/jev.py) at the pinned commit. |

## When to use

- Triage which agent runs to review first when you have no reference answers.
- Check whether a single-run risk score works on your own tasks before relying on it.
- Mismatch: AUROC figures (0.64 to 0.72) are the author's, on their benchmarks.

## How it works

`onerun/jev.py` posts the task and run history to TypeSafe's System One API (`TYPESAFE_BASE_URL`, default `https://api.typesafe.ai/v1`) and turns the answer into `risk = 1 - P(correct)`. Integration evidence: [`onerun/jev.py`](https://github.com/BeakrHub/TraceVarianceAnalyzer/blob/05d988c39b7293dee062d126fbf8cf810c266538/onerun/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/BeakrHub/TraceVarianceAnalyzer && cd TraceVarianceAnalyzer
python3 -m pip install -e .
onerun --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with findings: [github.com/BeakrHub/TraceVarianceAnalyzer#readme](https://github.com/BeakrHub/TraceVarianceAnalyzer#readme)

## Limits and data handling

Task text and the visible agent history go to TypeSafe for each scored run. Jev never sees hidden reasoning or an answer key.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 05d988c39b72](https://github.com/BeakrHub/TraceVarianceAnalyzer/tree/05d988c39b7293dee062d126fbf8cf810c266538). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
