# technique-guard (prompt-injection and jailbreak guard that judges the technique, with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Flags user input that tries to prompt-inject or jailbreak a downstream LLM before it reaches the model: it asks Jev a set of yes/no and multiple-choice questions about the technique, not the request, and combines the answers with a frozen logistic regression into allow, review or block, with a probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/j-pollack/technique-guard) |
| Maintainer | [j-pollack](https://github.com/j-pollack). Independently curated. |
| Format | Python library |
| Requirements | Python; a TypeSafe API key. |
| License | [MIT](https://github.com/j-pollack/technique-guard/blob/098fe9ae4a82d84210df444bd3443febb59b9523/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`technique_guard.py`](https://github.com/j-pollack/technique-guard/blob/098fe9ae4a82d84210df444bd3443febb59b9523/technique_guard.py) at the pinned commit. |

## When to use

- Screen inputs to an LLM app for hijack and jailbreak techniques.
- Mismatch: thresholds and weights were fitted by the author; re-check on your own traffic.

## How it works

`technique_guard.py` posts the text with its questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0` pinned) and applies the frozen regression to the probabilities. Integration evidence: [`technique_guard.py`](https://github.com/j-pollack/technique-guard/blob/098fe9ae4a82d84210df444bd3443febb59b9523/technique_guard.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/j-pollack/technique-guard && cd technique-guard
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/j-pollack/technique-guard#readme](https://github.com/j-pollack/technique-guard#readme)

## Limits and data handling

Each checked text goes to TypeSafe. Evaluation results are the author's.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 098fe9ae4a82](https://github.com/j-pollack/technique-guard/tree/098fe9ae4a82d84210df444bd3443febb59b9523). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
