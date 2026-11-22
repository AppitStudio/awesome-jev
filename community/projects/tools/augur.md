# Augur by JACKCOM (CLI that asks Jev or a local decision model typed questions and calibrates thresholds on your labels)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A normalized CLI for calibrated decision models, meant for agents and scripts: ask yes/no, choice or score questions about a text and get probabilities with no generated text, then `augur calibrate` measures the answers against examples you labelled so the threshold is something you measured. It informs and never blocks. Backends include TypeSafe's Jev, any `/v1/systemone` server such as Ollama 0.35+, Laya, or a command script.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JACK-COM/augur) |
| Maintainer | [JACK-COM](https://github.com/JACK-COM). Independently curated. |
| Format | Python CLI (Homebrew tap or uv) |
| Requirements | Python 3.11+ and numpy; a TypeSafe API key only for the hosted `jev` backend (macOS keychain or `TYPESAFE_API_KEY`); Ollama 0.35+ or Laya for local backends. |
| License | [MIT](https://github.com/JACK-COM/augur/blob/5d264a06ec3333d536c60fb1ec19176eeb00d0a0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/augur/augurlib/backends/systemone.py`](https://github.com/JACK-COM/augur/blob/5d264a06ec3333d536c60fb1ec19176eeb00d0a0/src/augur/augurlib/backends/systemone.py) at the pinned commit. |

## When to use

- Give an agent a measured, probability-based check for a rule it can phrase as a literal question, using Jev or a local model.
- Mismatch: hard enforcement gates; Augur reports and never blocks by design.

## How it works

`src/augur/augurlib/backends/systemone.py` speaks the System One HTTP API that both TypeSafe's Jev host and Ollama serve at `/v1/systemone`; keys are sent only to the host a person confirmed, over https, with no redirects, and every request and wait is bounded. Integration evidence: [`src/augur/augurlib/backends/systemone.py`](https://github.com/JACK-COM/augur/blob/5d264a06ec3333d536c60fb1ec19176eeb00d0a0/src/augur/augurlib/backends/systemone.py).

## Get started

Install from the JACK-COM Homebrew tap (or with uv) and let `augur configure backend` set up Jev or a local model.

```sh
brew tap jack-com/panoply
brew trust --formula jack-com/panoply/augur
brew install jack-com/panoply/augur
augur configure backend jev --store-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Augur guide: [github.com/JACK-COM/homebrew-panoply/blob/main/docs/augur/README.md](https://github.com/JACK-COM/homebrew-panoply/blob/main/docs/augur/README.md)
- README: [github.com/JACK-COM/augur/blob/5d264a06ec3333d536c60fb1ec19176eeb00d0a0/README.md](https://github.com/JACK-COM/augur/blob/5d264a06ec3333d536c60fb1ec19176eeb00d0a0/README.md)

## Limits and data handling

With the `jev` backend, question text is sent to TypeSafe; local backends keep it on the machine. Saving a backend that sends text off the machine needs a person to type `yes` at a terminal.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 5d264a06ec33](https://github.com/JACK-COM/augur/tree/5d264a06ec3333d536c60fb1ec19176eeb00d0a0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
