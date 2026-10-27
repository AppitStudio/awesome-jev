# Jev-Codex-Router by Emirhan Yüksel (Codex CLI hook that trims context per prompt with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex CLI `UserPromptSubmit` hook that asks Jev which rule areas a new prompt actually needs, leaves the others out of context and resets context for greetings and simple replies, with a hard 200 ms timeout and a local heuristic engine when there is no key or network; Turkish documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/emirhanyuksel507-ai/jev-codex-router) |
| Maintainer | [emirhanyuksel507-ai](https://github.com/emirhanyuksel507-ai). Independently curated. |
| Format | Codex CLI hook (Python) |
| Requirements | Python; Codex CLI; a TypeSafe API key (optional, local heuristics without it). |
| License | [MIT](https://github.com/emirhanyuksel507-ai/jev-codex-router/blob/aa8847d7fc85c42a1136ba8c54a04e0a887aeebb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_codex_router/engine.py`](https://github.com/emirhanyuksel507-ai/jev-codex-router/blob/aa8847d7fc85c42a1136ba8c54a04e0a887aeebb/jev_codex_router/engine.py) at the pinned commit. |

## When to use

- Reduce context bloat in Codex CLI sessions.
- Mismatch: token-saving figures are the author's; distinct from the separately listed jev-codex-router by 0xNatoshi.

## How it works

`jev_codex_router/engine.py` uses the TypeSafe Python SDK with `jev-latest` against `https://api.typesafe.ai/v1` to classify the prompt with Choice, Noul and Score questions before Codex runs. Integration evidence: [`jev_codex_router/engine.py`](https://github.com/emirhanyuksel507-ai/jev-codex-router/blob/aa8847d7fc85c42a1136ba8c54a04e0a887aeebb/jev_codex_router/engine.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/emirhanyuksel507-ai/jev-codex-router && cd jev-codex-router
pip install -e .
python -m jev_codex_router.hook < tests/fixtures/sample_prompt.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Turkish): [github.com/emirhanyuksel507-ai/jev-codex-router#readme](https://github.com/emirhanyuksel507-ai/jev-codex-router#readme)

## Limits and data handling

Prompts go to TypeSafe when a key is set.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit aa8847d7fc85](https://github.com/emirhanyuksel507-ai/jev-codex-router/tree/aa8847d7fc85c42a1136ba8c54a04e0a887aeebb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
