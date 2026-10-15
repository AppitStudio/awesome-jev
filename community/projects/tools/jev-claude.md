# jev-claude

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python library, CLI and MCP server that sends code-facing decisions (decide/when/switch/rank) to TypeSafe Jev and human-facing text to an LLM you choose, with low-confidence answers routed to a person.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thiago-lage/jev-claude) |
| Maintainer | [thiago-lage](https://github.com/thiago-lage). Independently curated. |
| Format | Python library, CLI and MCP server (Portuguese docs) |
| Requirements | Python; TypeSafe API key for Jev; local Ollama or an OpenAI-compatible endpoint for `write`. |
| License | [MIT](https://github.com/thiago-lage/jev-claude/blob/bac9389f5eea202167b181adc1c889fe57f89dcf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_claude/backends/jev.py`](https://github.com/thiago-lage/jev-claude/blob/bac9389f5eea202167b181adc1c889fe57f89dcf/src/jev_claude/backends/jev.py) at the pinned commit. |

## When to use

- Replace JSON-parsing LLM calls for routing, filtering and ranking with typed Jev answers.
- Keep free-text generation on a local or OpenAI-compatible LLM.
- Mismatch: documentation is in Portuguese.

## How it works

`decide()` builds Choice/Noul/Score questions over your input and returns typed answers with an `uncertain` flag; `write()` calls a separate LLM. Rules, arithmetic and exact lookups stay in plain code. Integration evidence: [`src/jev_claude/backends/jev.py`](https://github.com/thiago-lage/jev-claude/blob/bac9389f5eea202167b181adc1c889fe57f89dcf/src/jev_claude/backends/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "jev-claude[jev] @ git+https://github.com/thiago-lage/jev-claude"
claude mcp add -s user jev-claude -- python -m jev_claude mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage examples in the upstream README (ticket routing).

## Limits and data handling

Decision inputs go to TypeSafe on your key; `write` inputs go to the LLM endpoint you configure.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit bac9389f5eea](https://github.com/thiago-lage/jev-claude/tree/bac9389f5eea202167b181adc1c889fe57f89dcf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
