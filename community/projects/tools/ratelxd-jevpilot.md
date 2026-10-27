# JevPilot by RatelXD (browser agent where Jev picks the next action and an LLM helps)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Research browser agent that takes a natural-language task, lets Jev choose the next action whenever the page state is clear, calls an OpenAI or Anthropic model only for input values, target selection, replanning and answer extraction, runs actions through browser-use and Playwright, and checks results against on-screen evidence; Korean documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RatelXD/JevPilot) |
| Maintainer | [RatelXD](https://github.com/RatelXD). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python with uv; a TypeSafe API key and an OpenAI or Anthropic key. |
| License | [MIT](https://github.com/RatelXD/JevPilot/blob/6cf7e89798372d25bae4673a48794add33009e7d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevpilot/engine/jev.py`](https://github.com/RatelXD/JevPilot/blob/6cf7e89798372d25bae4673a48794add33009e7d/src/jevpilot/engine/jev.py) at the pinned commit. |

## When to use

- Run browser tasks with most steps chosen by a fast decision model.
- Study a Jev-first, LLM-assisted agent design.
- Mismatch: research implementation with no claimed comparative advantage; distinct from the separately listed jevpilot by standardagents.

## How it works

`src/jevpilot/engine/jev.py` posts the indexed page state and candidate actions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); unclear states hand over to the configured LLM. Integration evidence: [`src/jevpilot/engine/jev.py`](https://github.com/RatelXD/JevPilot/blob/6cf7e89798372d25bae4673a48794add33009e7d/src/jevpilot/engine/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/RatelXD/JevPilot && cd JevPilot
uv sync --extra dev
uv run jevpilot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Korean): [github.com/RatelXD/JevPilot#readme](https://github.com/RatelXD/JevPilot#readme)

## Limits and data handling

Page content goes to TypeSafe and to the LLM provider. The README notes that subscription billing is unverified and API cost equivalents are not actual charges.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 6cf7e8979837](https://github.com/RatelXD/JevPilot/tree/6cf7e89798372d25bae4673a48794add33009e7d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
