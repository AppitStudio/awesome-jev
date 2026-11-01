# Topic Gate (agent skill that uses Jev to spot topic drift and suggest a session reset)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Skill for Claude Code and Hermes that checks each user message with Jev as same topic, subtopic or new topic; on a clear new topic it writes a handoff note and suggests `/clear` or `/new` so dead context stops costing tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tauseefau/topic-gate) |
| Maintainer | [tauseefau](https://github.com/tauseefau). Independently curated. |
| Format | Agent skill + Python script |
| Requirements | Python; a TypeSafe key. |
| License | [MIT](https://github.com/tauseefau/topic-gate/blob/1e19346f17a8bb47e073e86bb71faf92b3a114eb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/topic_gate.py`](https://github.com/tauseefau/topic-gate/blob/1e19346f17a8bb47e073e86bb71faf92b3a114eb/scripts/topic_gate.py) at the pinned commit. |

## When to use

- Cut context and token costs in long agent sessions that drift.
- Mismatch: only suggests a reset; it does not clear the session itself.

## How it works

`scripts/topic_gate.py check` sends the recent topic summary and new message to TypeSafe Jev (`/v1/systemone`) as a three-way choice and acts only on a clear margin. Integration evidence: [`scripts/topic_gate.py`](https://github.com/tauseefau/topic-gate/blob/1e19346f17a8bb47e073e86bb71faf92b3a114eb/scripts/topic_gate.py).

## Get started

From the upstream README (not run on the review host):

```sh
mkdir -p ~/.hermes/scripts
cp scripts/topic_gate.py ~/.hermes/scripts/
python3 ~/.hermes/scripts/topic_gate.py --check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/tauseefau/topic-gate#readme](https://github.com/tauseefau/topic-gate#readme)

## Limits and data handling

Conversation snippets are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 1e19346f17a8](https://github.com/tauseefau/topic-gate/tree/1e19346f17a8bb47e073e86bb71faf92b3a114eb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
