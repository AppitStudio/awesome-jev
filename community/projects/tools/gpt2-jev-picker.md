# Can a picker fix GPT-2's mistakes? by Shivam Mittal (experiment where Jev picks among GPT-2 XL's own candidate words and sentences)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment that hands GPT-2 XL's choice of next word or sentence to Jev, which only picks from GPT-2's own candidates and never writes. On 500 CounterFact fact prompts Jev raises accuracy from 9.8% to 23.0% (ceiling 28.4%); for word-by-word generation it does worse than a random control, and for sentence picks it is more coherent than random but loses on MAUVE. Each test has a random-pick control. Code, notebook, logs and per-run outputs included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CodeGeek04/jevgpt) |
| Maintainer | [Shivam Mittal](https://github.com/CodeGeek04) (CodeGeek04). Independently curated. |
| Format | Research write-up + Python script and notebook |
| Requirements | Python with PyTorch and a GPU for GPT-2 XL; a TypeSafe key to rerun the Jev picks. |
| License | [MIT](https://github.com/CodeGeek04/jevgpt/blob/3407974d32a96191870169d0e1029310b59dfe9a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_gpt2_experiment.py`](https://github.com/CodeGeek04/jevgpt/blob/3407974d32a96191870169d0e1029310b59dfe9a/jev_gpt2_experiment.py) at the pinned commit. |

## When to use

- Researchers curious whether a decision model can re-rank a small language model's candidates, including where it fails.
- Mismatch: a production decoding method; the author reports the word-level method does not work.

## How it works

`jev_gpt2_experiment.py` sends the text so far plus GPT-2's top candidates as one `choice` question to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and compares against greedy, nucleus, contrastive search and random-pick controls on the Su and Xu (2022) setup. Integration evidence: [`jev_gpt2_experiment.py`](https://github.com/CodeGeek04/jevgpt/blob/3407974d32a96191870169d0e1029310b59dfe9a/jev_gpt2_experiment.py).

## Get started

Read the results in the README, then rerun the experiment with your own key.

```sh
git clone https://github.com/CodeGeek04/jevgpt && cd jevgpt
export TYPESAFE_API_KEY=...
bash run_full.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Run logs: [github.com/CodeGeek04/jevgpt/tree/main/jev_gpt2_runs](https://github.com/CodeGeek04/jevgpt/tree/main/jev_gpt2_runs)
- Notebook: [github.com/CodeGeek04/jevgpt/blob/main/jev_gpt2_experiment.ipynb](https://github.com/CodeGeek04/jevgpt/blob/main/jev_gpt2_experiment.ipynb)

## Limits and data handling

Author's own single study on 100 WikiText-103 and 500 CounterFact prompts; prompts and candidates go to TypeSafe when rerun. A full rerun makes many billed Jev calls (about 136 per prompt for the word method).

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 3407974d32a9](https://github.com/CodeGeek04/jevgpt/tree/3407974d32a96191870169d0e1029310b59dfe9a). Inspected the README, LICENSE and `jev_gpt2_experiment.py` at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
