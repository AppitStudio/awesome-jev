# stuntd

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Jev-compatible proxy that records typed System One decisions and learns to answer them with a small head on a frozen Laya encoder—or serves zero-shot Laya with no provider key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bladedevoff/stuntd) |
| Maintainer | [bladedevoff](https://github.com/bladedevoff). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **stuntd 0.1.0** (PyPI) speaking `POST /v1/systemone` and OpenAI Chat Completions. |
| Requirements | Python **≥ 3.10**. `pip install stuntd` for proxy/serve; `stuntd[train]` pulls Laya for local heads. Optional upstream OpenAI or paid Jev for relay/learn modes. |
| License | [Apache-2.0](https://github.com/bladedevoff/stuntd/blob/f9f1286fe20ee61ba7649107f991a99e840f20ed/LICENSE). Upstream/provider usage billed separately when configured. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. First release / experimental. Source inspected (`stuntd/proxy/jev.py`). Install, training, and live provider runs were **not** executed on the review host. Numbers in upstream README trace to their demos—not re-measured here. |

## When to use

Use it to **point `typesafe-sdk` at a local base URL** with no TypeSafe key, to sit in front of OpenAI/Jev and distill repeated typed decisions, or for a fast local Claude Code PreToolUse gate (`examples/devtools/`). Prefer the paid TypeSafe API directly when you need official Jev calibration without a local model.

## How it works

[`stuntd/proxy/jev.py`](https://github.com/bladedevoff/stuntd/blob/f9f1286fe20ee61ba7649107f991a99e840f20ed/stuntd/proxy/jev.py) implements System One routes: local Laya heads, or proxy modes that relay to a provider and learn from its answers. Uncertain heads hand back to the provider. OpenAI-compatible chat is relayed byte-for-byte when not a typed decision site.

## Get started

```sh
pip install "stuntd[train]"
stuntd config init
stuntd serve
# Point TypeSafeClient(base_url="http://127.0.0.1:8787", api_key="local") at the daemon
```

Pin: [commit f9f1286](https://github.com/bladedevoff/stuntd/tree/f9f1286fe20ee61ba7649107f991a99e840f20ed).

## Examples and demos

- Banking / support / moderation / snake examples under `examples/`.
- Claude Code PreToolUse hook in `examples/devtools/`.

## Limits and data handling

When proxying, request payloads reach the configured upstream. Local mode keeps decisions on-box subject to Laya quality. Distillation quality depends on your traffic; upstream banking77 figures are theirs, not re-run here.

## Review and maintenance

Reviewed on **2026-09-23** at [commit f9f1286](https://github.com/bladedevoff/stuntd/tree/f9f1286fe20ee61ba7649107f991a99e840f20ed) (`stuntd` **0.1.0**, Apache-2.0). AI-assisted review of README, LICENSE, `stuntd/proxy/jev.py`, `pyproject.toml`. No install/live run.

Related: [openjev-sglang](openjev-sglang.md), [SemIf](semif.md), [typesafe-cli](typesafe-cli.md).
