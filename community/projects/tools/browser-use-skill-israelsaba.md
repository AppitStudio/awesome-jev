# browser-use skill by israelsaba (agent skill for local browser automation with Gemini or Jev Ultrafast, keys from macOS Keychain)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Agent Skill for OpenCode, Claude Code, Codex, Hermes and other SKILL.md agents that runs local browser automation with two backends: a Gemini Flash Playwright agent, or browser-use's Jev Ultrafast agent driving Chrome over CDP; API keys are read from the macOS Keychain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/israelsaba/browser-use-skill) |
| Maintainer | [israelsaba](https://github.com/israelsaba). Independently curated. |
| Format | Agent skill (`SKILL.md` + Python `run.py`, MIT) |
| Requirements | macOS (Keychain), Python with `uv`, Chrome, and a Google or TypeSafe key; the Jev backend needs `browser-use/jev-ultrafast` and `browser-harness` installed. |
| License | [MIT](https://github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run.py`](https://github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/run.py) at the pinned commit. |

## When to use

- Give a coding agent a fast local browser via Jev Ultrafast without putting keys in config files.
- Mismatch: Linux or Windows; key handling is built around the macOS Keychain.

## How it works

`run.py` runs the `jev` backend through [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast), reading the TypeSafe key from the Keychain service `typesafe_ai_api` (or an environment fallback); the skill itself does not call TypeSafe directly. Integration evidence: [`run.py`](https://github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/run.py).

## Get started

Review `SKILL.md` and `run.py`, copy both into your agent's skills folder, store your key in the Keychain and install the Jev Ultrafast backend.

```sh
mkdir -p ~/.config/opencode/skills/browser-use
cp SKILL.md run.py ~/.config/opencode/skills/browser-use/
uv pip install "git+https://github.com/browser-use/jev-ultrafast.git" "browser-harness==0.1.13"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/README.md](https://github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/README.md)
- Skill definition: [github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/SKILL.md](https://github.com/israelsaba/browser-use-skill/blob/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd/SKILL.md)

## Limits and data handling

Page state goes to TypeSafe (Jev backend) or Google (Gemini backend) on your keys; the browser runs with your local permissions.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit bfce6b0e7166](https://github.com/israelsaba/browser-use-skill/tree/bfce6b0e71661b6a6ddc6ccaa1b22172d6bf35dd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
