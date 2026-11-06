# openagent-principle (rule-keeping agent that checks principles with Jev-shaped judgments)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent that maintains written principles, collects materials, and checks pass/violation/uncertain with a System One client you point at a Jev-compatible gateway (`JEV_BASE_URL`), with an LLM backend fallback for free-text reasons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YY-Yifei/openagent-principle) |
| Maintainer | [YY-Yifei](https://github.com/YY-Yifei). Independently curated. |
| Format | Python package (MIT) |
| Requirements | Python toolchain, a Jev-compatible gateway URL and key (or LLM backend vars) as documented. |
| License | [MIT](https://github.com/YY-Yifei/openagent-principle/blob/efaf2d06dfee726f14c6a4f7abfbd1b4e3d947ed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/openagent_principle/jev.py`](https://github.com/YY-Yifei/openagent-principle/blob/efaf2d06dfee726f14c6a4f7abfbd1b4e3d947ed/src/openagent_principle/jev.py) at the pinned commit. |

## When to use

- Encode principles as choice questions and check materials against them.
- Keep judgment calibrated while reasons stay optional via LLM.
- Mismatch: you must configure JEV_BASE_URL; no default TypeSafe endpoint is hard-coded.

## How it works

`src/openagent_principle/jev.py` POSTs choice/score questions to `{JEV_BASE_URL}/systemone/v1/systemone` and maps answers back to principle judgments; stdlib HTTP only. Integration evidence: [`src/openagent_principle/jev.py`](https://github.com/YY-Yifei/openagent-principle/blob/efaf2d06dfee726f14c6a4f7abfbd1b4e3d947ed/src/openagent_principle/jev.py).

## Get started

Clone, export JEV_BASE_URL and JEV_API_KEY (or LLM vars), and run the principle-check flow in the README.

```sh
git clone https://github.com/YY-Yifei/openagent-principle.git && cd openagent-principle
export JEV_BASE_URL=https://api.typesafe.ai JEV_API_KEY=...
# follow README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/YY-Yifei/openagent-principle/blob/efaf2d06dfee726f14c6a4f7abfbd1b4e3d947ed/README.md](https://github.com/YY-Yifei/openagent-principle/blob/efaf2d06dfee726f14c6a4f7abfbd1b4e3d947ed/README.md)

## Limits and data handling

Materials under review are sent to your configured gateway. Without JEV_BASE_URL the project falls back to the LLM backend.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit efaf2d06dfee](https://github.com/YY-Yifei/openagent-principle/tree/efaf2d06dfee726f14c6a4f7abfbd1b4e3d947ed). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
