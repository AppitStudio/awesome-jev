# jeff (Claude Code router)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that uses Jev to route every subtask: model tier, Claude or Codex, which skill, write access, and parallelism, then asks Jev to verify each result and escalates misses.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/jeff) |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | Claude Code plugin (Python, stdlib) |
| Requirements | Claude Code (Codex optional); TypeSafe API key. |
| License | [MIT](https://github.com/saembit/jeff/blob/b588525953e106c25cc2356a0ffa0146fa87101c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jevclient.py`](https://github.com/saembit/jeff/blob/b588525953e106c25cc2356a0ffa0146fa87101c/lib/jevclient.py) at the pinned commit. |

## When to use

- Stop paying frontier prices for renames and lookups.
- Mismatch: routing is heuristic; tune tiers for your work.

## How it works

`lib/jevclient.py` is a stdlib System One client; jev-route asks about all subtasks in one request and jev-verify checks each result. Integration evidence: [`lib/jevclient.py`](https://github.com/saembit/jeff/blob/b588525953e106c25cc2356a0ffa0146fa87101c/lib/jevclient.py).

## Get started

From the upstream README: install the plugin in Claude Code and set your TypeSafe key.

```sh
git clone https://github.com/saembit/jeff
# see README Setup to install the plugin
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README Tiers and Tuning sections

## Limits and data handling

Subtask descriptions and results go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit b588525953e1](https://github.com/saembit/jeff/tree/b588525953e106c25cc2356a0ffa0146fa87101c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
