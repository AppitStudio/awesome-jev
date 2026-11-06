# sounding (analyze one agent session with scout questions plus per-item Jev judgments)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that answers whole-session questions with an inspect_scout-compatible scanner and runs TypeSafe Jev noul judgments on every user message or tool call so you can focus the scanner on high-probability spots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zqverse0/sounding) |
| Maintainer | [zqverse0](https://github.com/zqverse0). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python ≥ 3.11, an OpenAI-compatible key for whole-session questions, and a TypeSafe key for per-item Jev judgments. |
| License | [MIT](https://github.com/zqverse0/sounding/blob/d8540ad5f3886f8fd75236bc0fda638982454ad8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/sounding/jev.py`](https://github.com/zqverse0/sounding/blob/d8540ad5f3886f8fd75236bc0fda638982454ad8/src/sounding/jev.py) at the pinned commit. |

## When to use

- Audit one agent transcript with your own questions.
- Use cheap per-item Jev screens before a slower scout pass.
- Mismatch: needs chat-format session JSON; not a live interceptor.

## How it works

`src/sounding/jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY` (default model `jev-latest`) and returns noul probabilities per user message or tool call. Integration evidence: [`src/sounding/jev.py`](https://github.com/zqverse0/sounding/blob/d8540ad5f3886f8fd75236bc0fda638982454ad8/src/sounding/jev.py).

## Get started

Install with uv from git, export TYPESAFE_API_KEY and an OpenAI-compatible key, then run sounding on a session JSON.

```sh
uv tool install git+https://github.com/zqverse0/sounding
export TYPESAFE_API_KEY=...
# sounding --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zqverse0/sounding/blob/d8540ad5f3886f8fd75236bc0fda638982454ad8/README.md](https://github.com/zqverse0/sounding/blob/d8540ad5f3886f8fd75236bc0fda638982454ad8/README.md)

## Limits and data handling

Per-item snippets of user messages and tool calls are sent to TypeSafe; whole-session text goes to your chat model. Costs are on your keys.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit d8540ad5f388](https://github.com/zqverse0/sounding/tree/d8540ad5f3886f8fd75236bc0fda638982454ad8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
