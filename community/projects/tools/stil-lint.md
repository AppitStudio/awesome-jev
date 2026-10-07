# stil-lint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Style and quality linter for Norwegian (and English) text, delivered as a CLI and MCP server, that flags prose reading like unedited LLM output through several independent layers, with TypeSafe Jev as the optional judgment layer (directly or via OpenRouter); a style linter, not an authorship detector.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fredrsat/stil-lint) |
| Maintainer | [fredrsat](https://github.com/fredrsat). Independently curated. |
| Format | Python package with `stil-lint` CLI and stdio MCP server (install from source); optional PowerPoint checks |
| Requirements | Python with `pip install -e .` (`[pptx]` extra for decks); `TYPESAFE_API_KEY`, or an OpenRouter key with `TYPESAFE_BASE_URL`, only for `--mode full`. |
| License | [MIT](https://github.com/fredrsat/stil-lint/blob/6c04ffffe5d11c4c8f0368a71decd42d85a17a75/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Gate agent-written notifications, updates or homework messages in Norwegian or English before delivery.
- Run a personal style check on prose or a PowerPoint deck with findings per paragraph.
- Mismatch: it reports style findings, never "% AI-written"; layer 4 (Jev) is a paid API.

## How it works

Layers 0–3 (rules in [`src/stillint/rules.py`](https://github.com/fredrsat/stil-lint/blob/6c04ffffe5d11c4c8f0368a71decd42d85a17a75/src/stillint/rules.py), lexical and statistical checks) run locally. With `--mode full`, [`src/stillint/jev.py`](https://github.com/fredrsat/stil-lint/blob/6c04ffffe5d11c4c8f0368a71decd42d85a17a75/src/stillint/jev.py) asks Jev the questions defined in [`rules/jev.yaml`](https://github.com/fredrsat/stil-lint/blob/6c04ffffe5d11c4c8f0368a71decd42d85a17a75/rules/jev.yaml) and reports findings with probabilities. [`src/stillint/server.py`](https://github.com/fredrsat/stil-lint/blob/6c04ffffe5d11c4c8f0368a71decd42d85a17a75/src/stillint/server.py) exposes the same checks as MCP tools; a phrase bank remembers sent messages per agent.

## Get started

Local check first, then the Jev layer:

```sh
git clone https://github.com/fredrsat/stil-lint && cd stil-lint
pip install -e ".[pptx]"
stil-lint check text.md --genre sakprosa      # local, nothing leaves the machine
export TYPESAFE_API_KEY=...
stil-lint check text.md --mode full            # adds the Jev judgment layer
```

Local layers are free; `--mode full` sends text to TypeSafe (or OpenRouter) billed to your key.

## Examples and demos

- README *How an agent uses it* (check, read verdict, revise, remember) with a system-prompt snippet.
- Negative-control evaluation: [`bench/report_negative_control_jev.md`](https://github.com/fredrsat/stil-lint/blob/6c04ffffe5d11c4c8f0368a71decd42d85a17a75/bench/report_negative_control_jev.md).

## Limits and data handling

Text goes to TypeSafe/OpenRouter only in full mode. Research notes are in Norwegian. The NoReC corpus is used for offline evaluation only (CC BY-NC 4.0, not shipped). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 6c04ffffe5d1](https://github.com/fredrsat/stil-lint/tree/6c04ffffe5d11c4c8f0368a71decd42d85a17a75). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
