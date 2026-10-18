# hermes-loopguard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin with cheap typed semantic gates (TypeSafe Jev via typesafe-sdk) plus zero-token change gates and computer-use gates to stop automations from burning tokens in loops.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DECRUX9812/hermes-loopguard) |
| Maintainer | [DECRUX9812](https://github.com/DECRUX9812). Independently curated. |
| Format | Python Hermes plugin with TypeSafe backend |
| Requirements | Hermes Agent; Python; typesafe-sdk; TYPESAFE_API_KEY; pinned jev-1.13.0 or jev-1.14.0. |
| License | [MIT](https://github.com/DECRUX9812/hermes-loopguard/blob/ca06198e94304a1dc4fec4acad65817e15d7cb6a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/hermes_loopguard/backends/typesafe.py`](https://github.com/DECRUX9812/hermes-loopguard/blob/ca06198e94304a1dc4fec4acad65817e15d7cb6a/src/hermes_loopguard/backends/typesafe.py) at the pinned commit. |

## When to use

- Stop Hermes loops from re-calling expensive models on unchanged work.
- Want typed Jev semantic gates with pinned model ids (no silent alias drift).
- Mismatch: Hermes-specific plugin; not a general orchestrator.

## How it works

`backends/typesafe.py` imports `typesafe_sdk` and builds Choice/Noul/Score questions for Jev, rejecting aliases like `jev-latest` so behavior cannot drift silently. Integration evidence: [`src/hermes_loopguard/backends/typesafe.py`](https://github.com/DECRUX9812/hermes-loopguard/blob/ca06198e94304a1dc4fec4acad65817e15d7cb6a/src/hermes_loopguard/backends/typesafe.py).

## Get started

Install into Hermes per README, configure the typesafe backend and API key, enable the gates you need.

```sh
git clone https://github.com/DECRUX9812/hermes-loopguard && cd hermes-loopguard
# see README for Hermes plugin install + TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README gate types
- examples/cu_bench interim Jev results

## Limits and data handling

Hermes-oriented. Live Jev calls bill TypeSafe. Bench JSONL is illustrative.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit ca06198e9430](https://github.com/DECRUX9812/hermes-loopguard/tree/ca06198e94304a1dc4fec4acad65817e15d7cb6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
