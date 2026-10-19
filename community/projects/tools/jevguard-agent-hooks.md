# jevguard (agent hook guard)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prompt-injection guard that runs from coding agents' own hooks in Claude Code, Grok Build and Codex CLI (adapters for Copilot CLI, Cursor and Hermes too): Jev scores web pages, search results, MCP responses and fetched files before the model reads them, and withholds results that look like injections.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Dehumanizer77/jevguard) |
| Maintainer | [Dehumanizer77](https://github.com/Dehumanizer77). Independently curated. |
| Format | Agent hook scripts (Python 3.11+, no pip installs) |
| Requirements | Python 3.11+, git, a supported coding agent and a TypeSafe API key stored by the owner in `~/.config/jevguard/typesafe.key`. |
| License | [MIT](https://github.com/Dehumanizer77/jevguard/blob/a0072db955b0c4e679650f0d4377c28ce2cb34e9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevguard/core/jev_detector.py`](https://github.com/Dehumanizer77/jevguard/blob/a0072db955b0c4e679650f0d4377c28ce2cb34e9/jevguard/core/jev_detector.py) at the pinned commit. |

## When to use

- Add an injection check on outside content that reaches a coding agent.
- Gate risky agent actions after untrusted content has been read.
- Mismatch: one layer, not a security boundary; untested against adaptive attackers.

## How it works

Hooks send the text of each outside tool result to `https://api.typesafe.ai/v1/systemone` with two fixed questions; the detector in `jevguard/core/jev_detector.py` reuses the questions, chunking and thresholds from jooray/hermes-firewall (MIT). The engine tracks where each result came from, and per-agent adapters replace withheld results in each tool's own shape and gate risky actions. Integration evidence: [`jevguard/core/jev_detector.py`](https://github.com/Dehumanizer77/jevguard/blob/a0072db955b0c4e679650f0d4377c28ce2cb34e9/jevguard/core/jev_detector.py).

## Get started

From the upstream README: clone into `~/.local/share/jevguard`, link the CLI, have the owner paste the key, then install the hooks per agent.

```sh
git clone https://github.com/Dehumanizer77/jevguard ~/.local/share/jevguard
mkdir -p ~/.local/bin && ln -s ~/.local/share/jevguard/bin/jevguard ~/.local/bin/jevguard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/REFERENCE.md
- [juraj.bednar.io/en/blog-en/2026/09/28/a-prompt-injection-gate-for-my-ai-agent-what-worked-what-didnt-and-the-benchmark/](https://juraj.bednar.io/en/blog-en/2026/09/28/a-prompt-injection-gate-for-my-ai-agent-what-worked-what-didnt-and-the-benchmark/)

## Limits and data handling

Outside content is sent to TypeSafe for scoring. Detectors miss some attacks; keep agent permissions tight. macOS untested; Windows needs WSL.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit a0072db955b0](https://github.com/Dehumanizer77/jevguard/tree/a0072db955b0c4e679650f0d4377c28ce2cb34e9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
