# FlightBench (fixed-wing landing simulator and benchmark: can you land a plane better than Jev?)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Landing simulator and benchmark on JSBSim physics with a Three.js view: fly the approach yourself, then compare with Jev, LLMs such as Codex, and classical controllers on the same setup. Jev picks control actions from the flight state each step; recordings and published runs include `jev-1.13.0` and `jev-1.14.0`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlperKartkaya/FlightBench) |
| Maintainer | [AlperKartkaya](https://github.com/AlperKartkaya). Independently curated. |
| Format | Python backend (FastAPI, JSBSim) and TypeScript frontend |
| Requirements | Python with uv, Node.js and a TypeSafe API key for Jev runs. |
| License | [MIT](https://github.com/AlperKartkaya/FlightBench/blob/6039ad3a49ed8abc0876cd46d0002754597f880f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`flightbench/controllers.py`](https://github.com/AlperKartkaya/FlightBench/blob/6039ad3a49ed8abc0876cd46d0002754597f880f/flightbench/controllers.py) at the pinned commit. |

## When to use

- Compare a decision model with LLMs and controllers on a real-time control task.
- Mismatch: a benchmark and game, not flight software.

## How it works

`flightbench/controllers.py` uses `typesafe_sdk` (`TypeSafeClient`, `Choice`) with `jev-1.13.0` by default to choose the next control input from the aircraft state. Integration evidence: [`flightbench/controllers.py`](https://github.com/AlperKartkaya/FlightBench/blob/6039ad3a49ed8abc0876cd46d0002754597f880f/flightbench/controllers.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AlperKartkaya/FlightBench.git && cd FlightBench
./scripts/dev.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Human flight recording: [alperkartkaya.github.io/FlightBench/human-flight/](https://alperkartkaya.github.io/FlightBench/human-flight/)
- README: [github.com/AlperKartkaya/FlightBench#readme](https://github.com/AlperKartkaya/FlightBench#readme)

## Limits and data handling

Flight state goes to TypeSafe during Jev runs.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 6039ad3a49ed](https://github.com/AlperKartkaya/FlightBench/tree/6039ad3a49ed8abc0876cd46d0002754597f880f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
