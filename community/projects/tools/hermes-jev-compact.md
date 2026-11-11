# hermes-jev-compact (Hermes Agent context engine that prunes stale tool calls by Jev score)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Opt-in Hermes Agent context engine that asks Jev, for each stale tool call and result, whether the call and its full output still matter, so compression keeps what the conversation depends on and drops dead weight instead of pruning by age.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TheEpTic/hermes-plugins) |
| Maintainer | [TheEpTic](https://github.com/TheEpTic). Independently curated. |
| Format | Hermes Agent plugin on PyPI (Python, MIT) |
| Requirements | Hermes Agent, `pip install hermes-jev-compact` in the Hermes environment, `context.engine: jev`, and a System One endpoint key (TypeSafe by default). |
| License | [MIT](https://github.com/TheEpTic/hermes-plugins/blob/194fd4b3bd7e477e7979d12ed54e378f98dcf946/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hermes-jev-compact/src/hermes_jev_compact/request.py`](https://github.com/TheEpTic/hermes-plugins/blob/194fd4b3bd7e477e7979d12ed54e378f98dcf946/hermes-jev-compact/src/hermes_jev_compact/request.py) at the pinned commit. |

## When to use

- Keep earlier tool results a long agent session still needs when context is compressed.
- Mismatch: opt-in per profile; the proactive prune path never calls Jev; part of a three-plugin monorepo.

## How it works

`request.py` builds the `/systemone` call against `https://api.typesafe.ai/v1` (default model `jev-latest`) and validates the answers; `engine.py` overrides only the full-compression prune step, and any Jev failure falls back to the built-in deterministic prune. Integration evidence: [`hermes-jev-compact/src/hermes_jev_compact/request.py`](https://github.com/TheEpTic/hermes-plugins/blob/194fd4b3bd7e477e7979d12ed54e378f98dcf946/hermes-jev-compact/src/hermes_jev_compact/request.py).

## Get started

Install into the same Python environment as `hermes`, enable the plugin, set `context.engine: jev`, then `/reset`.

```sh
python -m pip install hermes-jev-compact
hermes plugins enable hermes-jev-compact --no-allow-tool-override
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plugin README: [github.com/TheEpTic/hermes-plugins/blob/194fd4b3bd7e477e7979d12ed54e378f98dcf946/hermes-jev-compact/README.md](https://github.com/TheEpTic/hermes-plugins/blob/194fd4b3bd7e477e7979d12ed54e378f98dcf946/hermes-jev-compact/README.md)

## Limits and data handling

Stale tool calls and results plus the conversation as state go to the configured endpoint during full compression.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 194fd4b3bd7e](https://github.com/TheEpTic/hermes-plugins/tree/194fd4b3bd7e477e7979d12ed54e378f98dcf946). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
