# agent-reflex

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Coding-agent plugin that uses a System One decision model (Jev, or a local model served by llama.cpp, Ollama or LM Studio) for a shell guardrail, post-edit checks, task complexity classification and a confidence check across OpenCode, Claude Code, Codex, Hermes, Qwen Code, Antigravity and Pi.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/psygreg/agent-reflex) |
| Maintainer | [psygreg](https://github.com/psygreg). Independently curated. |
| Format | Agent plugin set and skill with an install script |
| Requirements | One of the supported agents; a System One endpoint (TypeSafe, OpenRouter, Vercel AI Gateway, OpenCode Zen, or a local server). |
| License | [Apache-2.0](https://github.com/psygreg/agent-reflex/blob/618ca2e4b027eb814e4036c85e593e593fcdfd53/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/hermes/classifier.py`](https://github.com/psygreg/agent-reflex/blob/618ca2e4b027eb814e4036c85e593e593fcdfd53/plugins/hermes/classifier.py) at the pinned commit. |

## When to use

- Block dangerous shell commands before your coding agent runs them.
- Pick reasoning effort per request (OpenCode and Pi) and save tokens.
- Mismatch: features differ by host; dynamic effort and history pruning are OpenCode or Pi only.

## How it works

Each host plugin sends the command, edit or request to the configured classifier (`https://api.typesafe.ai/v1` for TypeSafe, or a local `<baseURL>/systemone`) and acts on the typed answer: block, warn, classify complexity or flag low confidence. Integration evidence: [`plugins/hermes/classifier.py`](https://github.com/psygreg/agent-reflex/blob/618ca2e4b027eb814e4036c85e593e593fcdfd53/plugins/hermes/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add psygreg/agent-reflex   # then ask your agent to install it
# or:
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Per-host notes under `plugins/`.

## Limits and data handling

Commands and edit context go to the classifier you configure; with a local server nothing leaves your machine.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 618ca2e4b027](https://github.com/psygreg/agent-reflex/tree/618ca2e4b027eb814e4036c85e593e593fcdfd53). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
