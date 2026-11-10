# OpenCompletion (multi-user LLM chatroom with a Jev classifier and Jev Battleship reasoner)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Flask multi-user chatroom playground for language models with an optional decision-endpoint classifier (TypeSafe Jev by default) for grading activities, plus a Jev Reasoner Battleship opponent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/russellballestrini/opencompletion) |
| Maintainer | [russellballestrini](https://github.com/russellballestrini). Independently curated. |
| Format | Flask + Socket.IO web app (Python, source only) |
| Requirements | Python, the chat-model endpoints you configure, and `MODEL_CLASSIFIER_ENDPOINT_0=https://api.typesafe.ai` with a TypeSafe key for the classifier. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`classifier.py`](https://github.com/russellballestrini/opencompletion/blob/745f9ae1c8efae28bf45c830034229b680774cce/classifier.py) at the pinned commit. |

## When to use

- Grade learner answers with typed decisions instead of parsing chat output.
- Play Battleship against a Jev-driven opponent.
- Mismatch: no license file, so source-available only; the hosted demo was not checked.

## How it works

`classifier.py` asks a decision endpoint for a choice/yes-no/score instead of parsing chat text (`jev-latest` default, auto/on/off switch); `jev_hunter.py` builds an exact placement-density grid for Battleship and lets Jev pick the shot. Integration evidence: [`classifier.py`](https://github.com/russellballestrini/opencompletion/blob/745f9ae1c8efae28bf45c830034229b680774cce/classifier.py).

## Get started

Set the classifier variables from the README and run `make classifier-check`.

```sh
git clone https://github.com/russellballestrini/opencompletion.git
export MODEL_CLASSIFIER_ENDPOINT_0=https://api.typesafe.ai
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/russellballestrini/opencompletion/blob/745f9ae1c8efae28bf45c830034229b680774cce/README.rst](https://github.com/russellballestrini/opencompletion/blob/745f9ae1c8efae28bf45c830034229b680774cce/README.rst)

## Limits and data handling

Messages being classified go to the configured decision endpoint on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 745f9ae1c8ef](https://github.com/russellballestrini/opencompletion/tree/745f9ae1c8efae28bf45c830034229b680774cce). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
