# AgentScope (multi-agent framework with a built-in Jev classifier model)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Popular Apache-2.0 Python framework for building multi-agent applications. Since 2026-09 it ships a classifier interface with `JevClassifierModel`, which turns AgentScope questions into TypeSafe typed questions through the TypeSafe SDK, so agents can hand narrow judgments to Jev instead of a chat model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agentscope-ai/agentscope) |
| Maintainer | [agentscope-ai](https://github.com/agentscope-ai). Independently curated. |
| Format | Python package (`pip install agentscope`) |
| Requirements | Python 3.11+; a TypeSafe key for the Jev classifier. |
| License | [Apache-2.0](https://github.com/agentscope-ai/agentscope/blob/4acacb9ffb8c148a1f1e68263657a978bcb1e5a3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/agentscope/classifier/_jev/_model.py`](https://github.com/agentscope-ai/agentscope/blob/4acacb9ffb8c148a1f1e68263657a978bcb1e5a3/src/agentscope/classifier/_jev/_model.py) at the pinned commit. |

## When to use

- Add calibrated classification steps to an AgentScope multi-agent app.
- Mismatch: the classifier is one optional module of a much larger framework.

## How it works

`src/agentscope/classifier/_jev/_model.py` implements `JevClassifierModel`: it translates AgentScope classifier questions into TypeSafe questions and calls Jev (default `jev-latest`) through the TypeSafe SDK with a `TypeSafeCredential`. The release note is in `docs/NEWS.md`. Integration evidence: [`src/agentscope/classifier/_jev/_model.py`](https://github.com/agentscope-ai/agentscope/blob/4acacb9ffb8c148a1f1e68263657a978bcb1e5a3/src/agentscope/classifier/_jev/_model.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install agentscope
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository: [github.com/agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)
- Release note: [github.com/agentscope-ai/agentscope/blob/main/docs/NEWS.md](https://github.com/agentscope-ai/agentscope/blob/main/docs/NEWS.md)

## Limits and data handling

Classified text is sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 4acacb9ffb8c](https://github.com/agentscope-ai/agentscope/tree/4acacb9ffb8c148a1f1e68263657a978bcb1e5a3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
