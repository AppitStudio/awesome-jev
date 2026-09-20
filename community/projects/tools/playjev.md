# PlayJev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

PlayJev is an open 0.8B vision-language model fine-tuned to play ten browser games from the screen. It reproduces the typed-option decision shape on an open model; it does not run official Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/OmniJev/PlayJev) |
| Maintainer | [OmniJev](https://github.com/OmniJev). |
| Format | Python package (Playwright driver, collection, training, serving), ten vendored HTML5/JS games, a static browser demo, weights on Hugging Face. |
| Relationship to Jev | Independent model fine-tuned from Qwen3.5-0.8B-Base. No TypeSafe model, API, or endorsement. The bundled server answers in the OpenJev request shape. |
| Requirements | Python 3.12, one CUDA GPU (about 3 GB for inference, 17 GB for training at batch 64), Playwright Chromium. Weights download from Hugging Face on first run. |
| License | [Apache-2.0 code and weights](https://github.com/OmniJev/PlayJev/blob/2d7a0280841e3244a299c9c640efc8cefc46d476/LICENSE); the ten games keep their own licenses, vendored with each author's license file, and some game art is not the authors' to license. |
| Disclosure | Submitted by the maintainer. Listing is not an endorsement. |

## When to use

Use it to study a small model that decides from pixels instead of parsed state: one frame in, a probability over the moves the game lists, no text generated. It is also a working harness for turning a browser game into a training environment.

It is not an SDK, and it answers only the option list a game supplies.

## How it works

The prompt in [playjev/model.py](https://github.com/OmniJev/PlayJev/blob/2d7a0280841e3244a299c9c640efc8cefc46d476/playjev/model.py) holds one 448 px frame and the game's moves, each on a letter. The forward pass ends there and the letters' logits are normalized into a probability per move. The model never sees the game's name or its internal state, and the moves are shuffled in every training sample, so position carries nothing. Where velocity matters the vision tower also takes the previous frame as a separate image.

Each game is plain HTML5/JS with one hook, `window.pj` (`start`, `step`, `frame`, `score`, `done`, `actions`), described in [docs/HARNESS.md](https://github.com/OmniJev/PlayJev/blob/2d7a0280841e3244a299c9c640efc8cefc46d476/docs/HARNESS.md). The same page is the training environment and the demo tile.

Training is one cloning epoch over 863k teacher-labelled frames, then two DAgger rounds where the per-game search teachers relabel the frames the model itself visited.

## Get started

```sh
git clone https://github.com/OmniJev/PlayJev && cd PlayJev
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt && playwright install chromium
python -m playjev.play snake --policy local --ckpt OmniJev/PlayJev-0.8B --episodes 1
```

That opens Snake in headless Chromium and plays an episode. `python -m playjev.serve --ckpt <ckpt> --port 18732` exposes the checkpoint at `/v1/systemone`, and any demo tile switches to it with `?server=http://127.0.0.1:18732`. `bash scripts/reproduce.sh` rebuilds the model from the teachers up.

## Examples and demos

- [Browser demo](https://omnijev.github.io/PlayJev/): all ten games with recorded runs, the probability on every move, and the exact prompt.
- [Hugging Face Space](https://huggingface.co/spaces/OmniJev/PlayJev) and [weights](https://huggingface.co/OmniJev/PlayJev-0.8B).
- [docs/BASELINES.md](https://github.com/OmniJev/PlayJev/blob/2d7a0280841e3244a299c9c640efc8cefc46d476/docs/BASELINES.md): random play and each teacher on the same seeds.

## Limits and data handling

- Scores are the maintainer's own measurements: 16 held-out episodes per game, mean 0.53 of the teacher's score with random play at 0. Three games reach their teacher; 2048, Breakout and Floppy Bird stay well below it. No independent evaluation.
- Reading small digits at 448 px is a known failure: 2048 agrees with its teacher about half the time either way.
- Deciding one step late costs the reflex games most of their score, which is what running in real time buys.
- Inference is local. The weights download from Hugging Face, and the games are vendored in the repository, so a game session sends nothing to a third party.
- The games are other people's work under their own licenses, and three of them ship art the authors do not own.

## Review and maintenance

Reviewed **2026-09-20** at [`2d7a028`](https://github.com/OmniJev/PlayJev/tree/2d7a0280841e3244a299c9c640efc8cefc46d476). Maintainer submission: the prompt, harness contract, training scripts, license and third-party notes were checked against the code at that revision. Upstream scores are reported, not reproduced by this catalog.
