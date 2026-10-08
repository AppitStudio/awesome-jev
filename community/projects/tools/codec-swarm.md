# codec-swarm

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local single-user LangGraph orchestrator that takes a Jira ticket to a reviewed local PR with a swarm of Claude Code agents (specifier, architect, coder, reviewer, hardener, QA, judge) in per-repo worktrees; with Jev enabled, every approved Gherkin scenario and every uncovered ticket criterion is scored in the judge step, and risky actions (push, migrations, `terraform apply`) always ask you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/malfarom29/codec-swarm) |
| Maintainer | [malfarom29](https://github.com/malfarom29). Independently curated. |
| Format | Python app (`uv run codec-swarm up`, dashboard on 127.0.0.1:8765) |
| Requirements | Python + uv, Claude Code, git; optional Jira Cloud API token (example tickets otherwise); optional `TYPESAFE_API_KEY` for the Jev judge. |
| License | [MIT](https://github.com/malfarom29/codec-swarm/blob/890bfad09768820a8d46a555fa77f23505ef81f7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run a supervised multi-agent pipeline locally with durable, checkpointed steps.
- Get calibrated per-criterion scores alongside tests and lint before you review a diff.
- Mismatch: single-user local tool; agents never commit or push on their own.

## How it works

The Jev plugin ([`src/codec_swarm/plugins/jev/judge.py`](https://github.com/malfarom29/codec-swarm/blob/890bfad09768820a8d46a555fa77f23505ef81f7/src/codec_swarm/plugins/jev/judge.py), [`gate.py`](https://github.com/malfarom29/codec-swarm/blob/890bfad09768820a8d46a555fa77f23505ef81f7/src/codec_swarm/plugins/jev/gate.py), [`client.py`](https://github.com/malfarom29/codec-swarm/blob/890bfad09768820a8d46a555fa77f23505ef81f7/src/codec_swarm/plugins/jev/client.py)) scores scenarios and criteria into the lane score; every step is event-logged and the graph is checkpointed so restarts resume.

## Get started

Install and start the dashboard (README *Getting started*):

```sh
git clone https://github.com/malfarom29/codec-swarm.git && cd codec-swarm
uv sync
cp .env.example .env   # optional TYPESAFE_API_KEY
uv run codec-swarm up  # http://127.0.0.1:8765
```

Claude Code usage plus Jev scoring calls billed to your keys.

## Examples and demos

- Jev feature spec: [`features/m3_jev.feature`](https://github.com/malfarom29/codec-swarm/blob/890bfad09768820a8d46a555fa77f23505ef81f7/features/m3_jev.feature).

## Limits and data handling

Ticket text, scenarios and diffs go to Anthropic and (if enabled) TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 890bfad09768](https://github.com/malfarom29/codec-swarm/tree/890bfad09768820a8d46a555fa77f23505ef81f7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
