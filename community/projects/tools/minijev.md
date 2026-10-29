# minijev (a Jev-style typed decision in about 50 lines from a small local LLM's next-token probabilities)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment and lightning talk (AI-driven development Osaka, 29 October 2026): reproduce Jev's request shape (state plus named noul, choice and score questions) by reading a small local LLM's next-token probabilities for lettered options, then compare it with the real Jev and Opus 5.5 on 300 public questions and operational metrics. Slides included; Japanese docs. Not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hisuzuya/minijev) |
| Maintainer | [hisuzuya](https://github.com/hisuzuya). Independently curated. |
| Format | Python scripts (MLX) with slides |
| Requirements | An Apple silicon Mac with mlx-lm; a TypeSafe API key only to evaluate the real Jev. |
| License | [MIT](https://github.com/hisuzuya/minijev/blob/9563ba03dc027da062220c4af7282a3f65c401e4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`eval.py`](https://github.com/hisuzuya/minijev/blob/9563ba03dc027da062220c4af7282a3f65c401e4/eval.py) at the pinned commit. |

## When to use

- Understand what a typed decision model does and where a 50-line imitation falls short.
- Mismatch: Japanese; a teaching experiment.

## How it works

`minijev.py` reads letter probabilities from a Qwen3 model; `eval.py` calls the real Jev at `https://api.typesafe.ai/v1/systemone` (`jev-latest`) for comparison. Integration evidence: [`eval.py`](https://github.com/hisuzuya/minijev/blob/9563ba03dc027da062220c4af7282a3f65c401e4/eval.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hisuzuya/minijev && cd minijev
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mlx-lm
.venv/bin/python minijev.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Slides: [speakerdeck.com/hisuzuya/jev-no-nakami-ha-50-kudari-de-saigen-dekiru-demo-honmono-tono-sa-ha-doko-ni-aru-no-ka](https://speakerdeck.com/hisuzuya/jev-no-nakami-ha-50-kudari-de-saigen-dekiru-demo-honmono-tono-sa-ha-doko-ni-aru-no-ka)
- README (Japanese): [github.com/hisuzuya/minijev#readme](https://github.com/hisuzuya/minijev#readme)

## Limits and data handling

Local runs stay on your Mac; evaluation questions go to TypeSafe only when comparing with the real Jev.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 9563ba03dc02](https://github.com/hisuzuya/minijev/tree/9563ba03dc027da062220c4af7282a3f65c401e4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
