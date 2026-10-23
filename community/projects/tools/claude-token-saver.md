# token-saver (pick the cheapest Claude model and effort with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI and library that routes each prompt to the cheapest Claude model and effort level that can handle it: one Jev call scores task type, difficulty and sensitivity, and transparent rules turn that into a model and effort pick.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/minBuild/token-saver) |
| Maintainer | [minBuild](https://github.com/minBuild). Independently curated. |
| Format | Python CLI and library |
| Requirements | Python 3.10+; a TypeSafe API key; an Anthropic key only to run the routed request. |
| License | [MIT](https://github.com/minBuild/token-saver/blob/b1aadb0cc384445aebde9778dd00dae91a10bd81/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/token_saver/classifiers/jev.py`](https://github.com/minBuild/token-saver/blob/b1aadb0cc384445aebde9778dd00dae91a10bd81/src/token_saver/classifiers/jev.py) at the pinned commit. |

## When to use

- Stop sending every request to the largest model at maximum effort.
- See why a prompt was routed where it was.
- Mismatch: Claude models only.

## How it works

`classifiers/jev.py` uses the official `typesafe_sdk` client to ask task-type, difficulty and reasoning questions in one call; a heuristic fallback runs without a key. Integration evidence: [`src/token_saver/classifiers/jev.py`](https://github.com/minBuild/token-saver/blob/b1aadb0cc384445aebde9778dd00dae91a10bd81/src/token_saver/classifiers/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install git+https://github.com/minBuild/token-saver.git
export TYPESAFE_API_KEY=...
token-saver route "Translate this sentence into English"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README with routing examples: [github.com/minBuild/token-saver#readme](https://github.com/minBuild/token-saver#readme)

## Limits and data handling

Prompts are sent to TypeSafe for routing. Main README is Korean with an English version.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit b1aadb0cc384](https://github.com/minBuild/token-saver/tree/b1aadb0cc384445aebde9778dd00dae91a10bd81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
