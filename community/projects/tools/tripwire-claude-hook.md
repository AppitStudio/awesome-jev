# Tripwire (Claude Code PreToolUse hook that gates tool calls with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hook that asks Jev seven yes/no questions about each pending tool call and allows, asks or blocks it; README compares Jev with Claude Haiku and Sonnet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sraavan/tripwire) |
| Maintainer | [Sraavan](https://github.com/Sraavan). Independently curated. |
| Format | Python hook (stdlib, MIT) |
| Requirements | Python 3.11+, Claude Code v2.1.295+, and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Sraavan/tripwire/blob/c44e68aad345df0a449969070e9200056a3878e6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tripwire/jev.py`](https://github.com/Sraavan/tripwire/blob/c44e68aad345df0a449969070e9200056a3878e6/tripwire/jev.py) at the pinned commit. |

## When to use

- Gate destructive agent tool calls cheaply.
- Compare a Jev gate with LLM judges.
- Mismatch: tested only on macOS.

## How it works

`tripwire/jev.py` is a stdlib client for `{base}/v1/systemone`; `questions.py` and `policy.py` turn the seven answers into allow/ask/deny under `config.toml`. Integration evidence: [`tripwire/jev.py`](https://github.com/Sraavan/tripwire/blob/c44e68aad345df0a449969070e9200056a3878e6/tripwire/jev.py).

## Get started

Clone, add your key, and register the hook in Claude Code settings as described in the README.

```sh
git clone https://github.com/Sraavan/tripwire.git && cd tripwire
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Sraavan/tripwire/blob/c44e68aad345df0a449969070e9200056a3878e6/README.md](https://github.com/Sraavan/tripwire/blob/c44e68aad345df0a449969070e9200056a3878e6/README.md)

## Limits and data handling

Each tool call's details are sent to TypeSafe before it runs.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit c44e68aad345](https://github.com/Sraavan/tripwire/tree/c44e68aad345df0a449969070e9200056a3878e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
