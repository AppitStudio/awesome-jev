# laya-packet-analyser

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Real-time or pcap network security analyser: deterministic packet detectors plus a second opinion from a local Laya (Jev-compatible POST /v1/systemone) server, with a live dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/esterhuizen/laya-packet-analyser) |
| Maintainer | [esterhuizen](https://github.com/esterhuizen). Independently curated. |
| Format | Pure Python stdlib package (`lpa`) + local dashboard. |
| Requirements | Python 3.10+; separate Laya serve process. Windows pktmon for live capture (Admin); Linux file/iface/stdin paths documented. |
| License | [MIT](https://github.com/esterhuizen/laya-packet-analyser/blob/c8ec6d528851a36783e02fe435c12a971a996c33/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Local Laya, not hosted Jev by default. |

## When to use

Use for **laptop traffic triage** where heuristics find alerts and a local decision model classifies conversations.

## How it works

[`lpa/laya.py`](https://github.com/esterhuizen/laya-packet-analyser/blob/c8ec6d528851a36783e02fe435c12a971a996c33/lpa/laya.py) talks to a loopback System One endpoint; detectors decode flows and raise candidates. Dashboard defaults to [http://127.0.0.1:8765/](http://127.0.0.1:8765/).

## Get started

```sh
git clone https://github.com/esterhuizen/laya-packet-analyser.git
cd laya-packet-analyser
git checkout c8ec6d528851a36783e02fe435c12a971a996c33
# start laya-serve separately, then:
# python3 -m lpa analyse path/to/file.pcap
```

## Examples and demos

- `lpa synth demo.pcap` synthetic attacks; `laya-check` latency probe.

## Limits and data handling

Packet/alert context goes to the local Laya server only (unless --laya-url points elsewhere). Not a substitute for signature IDS/IPS. Uses open System One–compatible Laya, not hosted TypeSafe Jev by default.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit c8ec6d5](https://github.com/esterhuizen/laya-packet-analyser/tree/c8ec6d528851a36783e02fe435c12a971a996c33). AI-assisted README and LICENSE inspection of laya client module; install/live paths not executed.
