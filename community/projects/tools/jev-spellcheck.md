# jev-spellcheck (finding misspellings and wrong real words in recipes with Jev, against dictionaries, RoBERTa and Claude)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment that uses Jev to find spelling mistakes and real-word mix-ups ("flower" for "flour") in English recipe steps down to the word, compared with a dictionary, LanguageTool, a dictionary plus RoBERTa, and Claude Haiku 4.5 and Sonnet 5.5 on 1,000 test sentences. The author reports F1 0.94 for the best Jev setup at about $0.08 per 1,000 sentences. Japanese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/haruto-kamijo/jev-spellcheck) |
| Maintainer | [haruto-kamijo](https://github.com/haruto-kamijo). Independently curated. |
| Format | Python scripts and datasets |
| Requirements | Python; a TypeSafe API key to rerun the Jev probes (dry-run mode estimates cost first). |
| License | [MIT](https://github.com/haruto-kamijo/jev-spellcheck/blob/8fb549a87f823f11a58e1c146d9e2688e7ddba7e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`probe.py`](https://github.com/haruto-kamijo/jev-spellcheck/blob/8fb549a87f823f11a58e1c146d9e2688e7ddba7e/probe.py) at the pinned commit. |

## When to use

- See how a decision model compares with LLMs and classic spellcheckers on a concrete task.
- Mismatch: one domain; results are the author's.

## How it works

`probe.py` posts each sentence to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0` and asks where an error is; it defaults to a dry run that only counts and estimates. Integration evidence: [`probe.py`](https://github.com/haruto-kamijo/jev-spellcheck/blob/8fb549a87f823f11a58e1c146d9e2688e7ddba7e/probe.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/haruto-kamijo/jev-spellcheck && cd jev-spellcheck
# see the README (Japanese) for the dry-run and probe commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/haruto-kamijo/jev-spellcheck#readme](https://github.com/haruto-kamijo/jev-spellcheck#readme)
- Summary: [github.com/haruto-kamijo/jev-spellcheck/blob/main/results/v2test/summary.md](https://github.com/haruto-kamijo/jev-spellcheck/blob/main/results/v2test/summary.md)

## Limits and data handling

Recipe sentences go to TypeSafe in live runs. Code is MIT; the data is CC BY-SA 4.0.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 8fb549a87f82](https://github.com/haruto-kamijo/jev-spellcheck/tree/8fb549a87f823f11a58e1c146d9e2688e7ddba7e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
