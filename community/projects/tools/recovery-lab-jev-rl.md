# Recovery Lab by Vajraang (incident-recovery RL lab where Jev ranks likely causes from collected logs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local research platform for training a reinforcement-learning controller to investigate and repair a fault-injected service (bad credentials, leaking connections, failed dependencies). Jev, or an offline heuristic, ranks likely causes from the log excerpts the agent chose to collect; the controller picks diagnostics and fixes; independent health probes decide whether recovery lasted. Ships a dashboard and a recorded study of 4,320 paired trajectories comparing checklist, random, repair-first and RL arms with and without the advisor.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Vajraaaang/jev-rl) |
| Maintainer | [Vajraang](https://github.com/Vajraaaang) (Vajraaaang; commits by Vajraang Padisetti). Independently curated. |
| Format | Python package + local web dashboard |
| Requirements | Python 3.10+ with no external dependencies; a TypeSafe API key only for the live advisor. |
| License | [MIT](https://github.com/Vajraaaang/jev-rl/blob/bda65a76c863ad17e940bd4ea4662e34c7ebb7c3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_recovery/jev.py`](https://github.com/Vajraaaang/jev-rl/blob/bda65a76c863ad17e940bd4ea4662e34c7ebb7c3/jev_recovery/jev.py) at the pinned commit. |

## When to use

- Researchers studying how a decision model's diagnosis helps (or does not help) a learned recovery agent.
- Mismatch: production incident response; everything runs against a simulator.

## How it works

`jev_recovery/jev.py` sends the collected log excerpt with three text questions to `https://api.typesafe.ai/v1/systemone`, requires a pinned model version (default `jev-1.13.0`), caches responses and enforces call and cost limits. Jev sees only collected logs and never grades recovery. Integration evidence: [`jev_recovery/jev.py`](https://github.com/Vajraaaang/jev-rl/blob/bda65a76c863ad17e940bd4ea4662e34c7ebb7c3/jev_recovery/jev.py).

## Get started

Run the offline dashboard first; add the live advisor with a key typed at a hidden prompt.

```sh
git clone https://github.com/Vajraaaang/jev-rl && cd jev-rl
python3 -m jev_recovery serve --port 8080
# live Jev advisor:
python3 -m jev_recovery serve --advisor live --prompt-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Measured results: [github.com/Vajraaaang/jev-rl#measured-results](https://github.com/Vajraaaang/jev-rl#measured-results)
- Docs: [github.com/Vajraaaang/jev-rl/tree/master/docs](https://github.com/Vajraaaang/jev-rl/tree/master/docs)

## Limits and data handling

Simulated incidents only; no production shell or arbitrary remediation tool. In live mode, collected log excerpts go to TypeSafe. The README marks it as research status.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit bda65a76c863](https://github.com/Vajraaaang/jev-rl/tree/bda65a76c863ad17e940bd4ea4662e34c7ebb7c3). Inspected the README, LICENSE and `jev_recovery/jev.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
