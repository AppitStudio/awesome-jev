# typesafeai-cli

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python CLI (`typesafe`) for TypeSafe Jev: ask, decide, screen, verify, and related agent-oriented commands over JSON state, using the official TypeSafe SDK.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maddygoround/typesafeai-cli) |
| Maintainer | [maddygoround](https://github.com/maddygoround) / safeaiforeveryone. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **typesafeai-cli 0.3.2** on PyPI; console script `typesafe`. |
| Requirements | Python ≥ 3.10. Live commands need a TypeSafe API key (`typesafe auth` or `TYPESAFE_API_KEY`). Offline unit tests mock the SDK. |
| License | [MIT](https://github.com/maddygoround/typesafeai-cli/blob/ca87ffdebb13415d3d582efea243e77b8ce92387/LICENSE). |

## When to use

Use it when a human or coding agent should invoke Jev from the shell with structured state/questions files, without embedding HTTP clients. Prefer [Advocaat](advocaat.md) or language SDKs when you need an in-process library API instead of a CLI.

## How it works

The [client adapter](https://github.com/maddygoround/typesafeai-cli/blob/ca87ffdebb13415d3d582efea243e77b8ce92387/src/typesafe_cli/client.py) builds `Noul` / `Choice` / `Score` objects for `typesafe_sdk.TypeSafeClient`. Commands under `src/typesafe_cli/commands/` wrap ask/decide/screen/verify and related flows. Bundled skill markdown under `data/` helps agents discover CLI usage. Jev only sees the JSON state you pass.

## Get started

```sh
pip install 'typesafeai-cli==0.3.2'
typesafe --help
# Live: typesafe auth   # then recipe commands from upstream README
```

From the reviewed commit:

```sh
git clone https://github.com/maddygoround/typesafeai-cli.git
cd typesafeai-cli
git checkout ca87ffdebb13415d3d582efea243e77b8ce92387
pip install -e .
pytest -q
```

Live commands are billable. This listing did not call TypeSafe.

## Examples and demos

- [examples/ticket](https://github.com/maddygoround/typesafeai-cli/tree/ca87ffdebb13415d3d582efea243e77b8ce92387/examples/ticket) and [examples/code-change](https://github.com/maddygoround/typesafeai-cli/tree/ca87ffdebb13415d3d582efea243e77b8ce92387/examples/code-change): sample state/questions JSON.
- [tests/](https://github.com/maddygoround/typesafeai-cli/tree/ca87ffdebb13415d3d582efea243e77b8ce92387/tests): offline CLI, client, schema, and recipe coverage.

## Limits and data handling

State and questions go to TypeSafe on live commands. Auth stores credentials per upstream docs—keep them out of shared state files. CLI recipes are conveniences, not validated accuracy benchmarks. Package version and API surface may advance quickly.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ca87ffd](https://github.com/maddygoround/typesafeai-cli/tree/ca87ffdebb13415d3d582efea243e77b8ce92387): **0.3.2**, MIT. AI-assisted source review of client/commands, examples, README, and license. On Python 3.13.5, **`pytest`: 63 passed**. No live TypeSafe calls were performed.

Related: [Advocaat](advocaat.md), [TypeSafe MCP](typesafe-mcp.md).
