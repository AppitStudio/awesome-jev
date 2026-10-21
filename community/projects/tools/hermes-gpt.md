# Hermes GPT (Jev decision bridge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP connector that gives ChatGPT controlled access to a Hermes Agent machine, now with an optional Jev bridge: three typed tools for yes/no, choose and score judgments, plus an advisory Jev review score for dispatched work.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asimons81/hermes-gpt) |
| Maintainer | [asimons81](https://github.com/asimons81). Independently curated. |
| Format | MCP server (Python, PyPI `hermes-gpt`) |
| Requirements | Python 3 with pip; a Hermes Agent setup; Node.js and a TypeSafe key for the optional Jev bridge (`HERMES_GPT_ENABLE_JEV=1`). |
| License | [MIT](https://github.com/asimons81/hermes-gpt/blob/9cfd71e3b0c0384e06103563781002fd9d041fd6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/tonysimons/status/2112930360900427854)). |
| Jev evidence | [`jev_bridge.py`](https://github.com/asimons81/hermes-gpt/blob/9cfd71e3b0c0384e06103563781002fd9d041fd6/jev_bridge.py) at the pinned commit. |

## When to use

- Get a fast second opinion from Jev in ChatGPT before running with an idea on your Hermes machine.
- Add an advisory Jev score to Work Contract reviews without giving it approval authority.
- Mismatch: the Jev tools are off by default and need separate key setup.

## How it works

With the gate on, `jev_bridge.py` starts the pinned community `jev-mcp` adapter over local stdio and exposes `hermes_jev_yes_no`, `hermes_jev_choose` and `hermes_jev_score`; Jev judges only the text supplied and grants no authority (see `docs/jev.md`). Integration evidence: [`jev_bridge.py`](https://github.com/asimons81/hermes-gpt/blob/9cfd71e3b0c0384e06103563781002fd9d041fd6/jev_bridge.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pip install hermes-gpt
export HERMES_GPT_ENABLE_JEV=1
# provision the TypeSafe key as described in docs/jev.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev bridge guide: [github.com/asimons81/hermes-gpt/blob/master/docs/jev.md](https://github.com/asimons81/hermes-gpt/blob/master/docs/jev.md)
- Review assist: [github.com/asimons81/hermes-gpt/blob/master/docs/review-assist.md](https://github.com/asimons81/hermes-gpt/blob/master/docs/review-assist.md)

## Limits and data handling

Text passed to the Jev tools is sent to TypeSafe. The connector itself can act on your machine; read the operator and security docs first. Community project, not affiliated with TypeSafe or OpenAI.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 9cfd71e3b0c0](https://github.com/asimons81/hermes-gpt/tree/9cfd71e3b0c0384e06103563781002fd9d041fd6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
