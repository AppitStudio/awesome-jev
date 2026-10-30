# jev-decision (gated-planner pattern where Jev may only pick one symbolic transition from a frozen whitelist)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill plus a dependency-free Python reference core for putting an LLM or Jev into a closed decision loop without letting it emit numbers, identifiers or verdicts. The planner picks one symbolic transition from a whitelist; deterministic code checks it against the failed gates, applies it to a copy of the state, preflights it and logs accept or reject. A snapshot script freezes the resolved Jev model ID before benchmarks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GanQiao1990/jev-decision) |
| Maintainer | [GanQiao1990](https://github.com/GanQiao1990). Independently curated. |
| Format | Agent skill + Python reference module |
| Requirements | Python 3; the TypeSafe SDK and a TypeSafe key only for the Jev arm (tests run without them). |
| License | [MIT](https://github.com/GanQiao1990/jev-decision/blob/4b0a86db305e543a4c12693fc7509d90a17d54fa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_policy.py`](https://github.com/GanQiao1990/jev-decision/blob/4b0a86db305e543a4c12693fc7509d90a17d54fa/scripts/jev_policy.py) at the pinned commit. |

## When to use

- Let a model suggest the kind of fix in an optimisation or evaluation loop while deterministic code keeps control of every value.
- Mismatch: a pattern and reference core, not a ready product; you supply your own whitelist, apply and preflight functions.

## How it works

`jev_policy.py` sends the failed-gate profile to Jev as a Choice over the whitelisted transitions (with `no_action` allowed) and records service outages as their own status; `freeze_jev_snapshot.py` pins the resolved model before runs. Integration evidence: [`scripts/jev_policy.py`](https://github.com/GanQiao1990/jev-decision/blob/4b0a86db305e543a4c12693fc7509d90a17d54fa/scripts/jev_policy.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pytest tests/ -q
pip install typesafe-sdk
export TYPESAFE_API_KEY=<your-key>
python scripts/freeze_jev_snapshot.py --states examples/states.json --model jev-latest --out jev_snapshot.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example states: [github.com/GanQiao1990/jev-decision/blob/4b0a86db305e543a4c12693fc7509d90a17d54fa/examples/states.json](https://github.com/GanQiao1990/jev-decision/blob/4b0a86db305e543a4c12693fc7509d90a17d54fa/examples/states.json)

## Limits and data handling

The failed-gate profile you pass is sent to TypeSafe on the Jev arm. New repository (first commit 2026-10-30) with no releases. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 4b0a86db305e](https://github.com/GanQiao1990/jev-decision/tree/4b0a86db305e543a4c12693fc7509d90a17d54fa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
