# a0-plugin-jev-compact (Agent Zero plugin that span-scores context with Jev, tombs stale spans and restores them via MCP)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent Zero plugin that compacting conversation context by scoring spans with Jev (or OpenRouter Decisions / an offline heuristic), keeping high-value spans, tombstoning the rest, and restoring any tombstone verbatim through a bundled MCP server. Off by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/duketopceo/a0-plugin-jev-compact) |
| Maintainer | [duketopceo](https://github.com/duketopceo). Independently curated. |
| Format | Agent Zero Python plugin (MIT; vendors stdlib-only jev-compact) |
| Requirements | Agent Zero ≥0.9 with this repo at `usr/plugins/jev_compact/`; optional `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` for model scoring. |
| License | [MIT](https://github.com/duketopceo/a0-plugin-jev-compact/blob/6d44a7446db6f885691d315c9704b173b4579027/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`helpers/engine/jev_compact/scorer.py`](https://github.com/duketopceo/a0-plugin-jev-compact/blob/6d44a7446db6f885691d315c9704b173b4579027/helpers/engine/jev_compact/scorer.py) at the pinned commit. |

## When to use

- Shrink Agent Zero context without LLM summaries that drop guardrail lines.
- Restore a tombstoned span verbatim when the agent needs it again.
- Mismatch: disabled by default; without a key it uses the offline heuristic scorer.

## How it works

`scorer.py` and the message-loop extension call Jev (or OpenRouter Decisions) to score spans; the MCP server can restore tombstones on demand. Integration evidence: [`helpers/engine/jev_compact/scorer.py`](https://github.com/duketopceo/a0-plugin-jev-compact/blob/6d44a7446db6f885691d315c9704b173b4579027/helpers/engine/jev_compact/scorer.py).

## Get started

From the upstream README (not run on the review host):

```sh
# place repo at <a0>/usr/plugins/jev_compact/ and restart Agent Zero
# set enabled: true in plugin settings; optional TYPESAFE_API_KEY in usr/secrets.env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/duketopceo/a0-plugin-jev-compact/blob/6d44a7446db6f885691d315c9704b173b4579027/README.md](https://github.com/duketopceo/a0-plugin-jev-compact/blob/6d44a7446db6f885691d315c9704b173b4579027/README.md)

## Limits and data handling

Conversation spans scored by Jev leave your machine on your TypeSafe key. Offline mode never calls a provider.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 6d44a7446db6](https://github.com/duketopceo/a0-plugin-jev-compact/tree/6d44a7446db6f885691d315c9704b173b4579027). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
