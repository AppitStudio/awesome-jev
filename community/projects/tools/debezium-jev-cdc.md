# debezium-jev-cdc (semantic decisions on Debezium CDC events with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CDC helper that consumes Debezium change events and asks Jev typed semantic questions about each change (for example whether a row looks like spam or needs human review), with a fixtures mode that needs no API key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/debezium-jev-cdc) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python module/CLI (MIT) |
| Requirements | Python 3, Debezium/Kafka as wired upstream, and `TYPESAFE_API_KEY` unless running with `--fixtures`. |
| License | [MIT](https://github.com/gbesse/debezium-jev-cdc/blob/0c74c0dbafb802d2ace5eaa941366ba1bcec488c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cdc.py`](https://github.com/gbesse/debezium-jev-cdc/blob/0c74c0dbafb802d2ace5eaa941366ba1bcec488c/cdc.py) at the pinned commit. |

## When to use

- Attach semantic gates to CDC streams without a full LLM agent.
- Dry-run with fixtures before spending on live Jev calls.
- Mismatch: you still own the Debezium/Kafka plumbing.

## How it works

`cdc.py` requires `TYPESAFE_API_KEY` without `--fixtures` and posts typed questions about change payloads to TypeSafe. Integration evidence: [`cdc.py`](https://github.com/gbesse/debezium-jev-cdc/blob/0c74c0dbafb802d2ace5eaa941366ba1bcec488c/cdc.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
python cdc.py --help   # see upstream for fixtures vs live modes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/debezium-jev-cdc/blob/0c74c0dbafb802d2ace5eaa941366ba1bcec488c/README.md](https://github.com/gbesse/debezium-jev-cdc/blob/0c74c0dbafb802d2ace5eaa941366ba1bcec488c/README.md)

## Limits and data handling

CDC payloads you forward are sent to TypeSafe on your key. Fixtures mode stays offline.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 0c74c0dbafb8](https://github.com/gbesse/debezium-jev-cdc/tree/0c74c0dbafb802d2ace5eaa941366ba1bcec488c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
