# mobile-jev × AndroidWorld (Python port of mobile-jev run on the 116-task AndroidWorld benchmark)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Research port of droidrun/mobile-jev to AndroidWorld's action space. Each step turns the accessibility tree into a state and asks Jev, through OpenRouter, which operation to run and which element to target; a small chat model writes typed text and answers. Reported single runs: 37 of 116 tasks (31.9%) with `jev-1.13` and 39 (33.6%) with `jev-1.14`, about $0.25 per full run. Results, steps and run guide included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fclab-skku/jev-using-mobile-androidworld) |
| Maintainer | [fclab-skku](https://github.com/fclab-skku). Independently curated. |
| Format | Python benchmark agent |
| Requirements | Python 3.11+, the Android emulator with an AndroidWorld AVD, android_world at commit 2655e27, and an OpenRouter key (mock providers for dry runs). |
| License | [MIT](https://github.com/fclab-skku/jev-using-mobile-androidworld/blob/14bda537f55fb4165e8e70a136cebb294343e3b3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bench/agents/aw/mobile_jev_port/policy.py`](https://github.com/fclab-skku/jev-using-mobile-androidworld/blob/14bda537f55fb4165e8e70a136cebb294343e3b3/bench/agents/aw/mobile_jev_port/policy.py) at the pinned commit. |

## When to use

- Measure a fast decision model as the action picker of an Android UI agent on a public benchmark.
- Mismatch: single runs per configuration; heavy emulator setup.

## How it works

`policy.py` sends goal, current app, indexed elements and recent actions with an operation question plus one target question per operation, then executes the chosen action on the chosen element. Integration evidence: [`bench/agents/aw/mobile_jev_port/policy.py`](https://github.com/fclab-skku/jev-using-mobile-androidworld/blob/14bda537f55fb4165e8e70a136cebb294343e3b3/bench/agents/aw/mobile_jev_port/policy.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m bench aw-run --agent mobile_jev_aw --provider decision=mock_jev --provider text=mock_text --run-id dry
python -m bench aw-run --agent mobile_jev_aw --tasks ContactsAddContact --run-id try1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/fclab-skku/jev-using-mobile-androidworld/blob/14bda537f55fb4165e8e70a136cebb294343e3b3/docs/RESULTS.md](https://github.com/fclab-skku/jev-using-mobile-androidworld/blob/14bda537f55fb4165e8e70a136cebb294343e3b3/docs/RESULTS.md)

## Limits and data handling

Screen text from the emulator is sent to OpenRouter. Reported numbers are the maintainers' own single runs. Not affiliated with droidrun, Google or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 14bda537f55f](https://github.com/fclab-skku/jev-using-mobile-androidworld/tree/14bda537f55fb4165e8e70a136cebb294343e3b3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
