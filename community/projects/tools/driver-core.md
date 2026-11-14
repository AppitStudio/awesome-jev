# driver-core (drives a local machine as verified extraction → Jev decision → deterministic action, with a hash-chained audit log)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Python driver that watches a machine, cross-checks independent extractions of its state by arithmetic before any decision, asks Jev what should happen next only when the state agreed, and executes from a closed action set with no model in the action tier. Structured sources (CLI, MCP, DOM) are tried before pixels by type, and every step is budgeted and written to a hash-chained audit log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Treystu/driver-core) |
| Maintainer | [Treystu](https://github.com/Treystu). Independently curated. |
| Format | Python package and CLI, stdlib only (no license file; pyproject.toml declares MIT) |
| Requirements | Python 3 and a TypeSafe key; optional vision extraction through the same TypeSafe endpoint. |
| License | No license file (pyproject.toml declares MIT) on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`driver_core/jev_client.py`](https://github.com/Treystu/driver-core/blob/cf3337076b608abdfcf6b726aed7629e1c44eb39/driver_core/jev_client.py) at the pinned commit. |

## When to use

- Automate a repeatable task on your own machine where each action should be auditable and gated on agreed state.
- Mismatch: unattended control of systems you cannot afford to have changed; review the action vocabulary first.

## How it works

`driver_core/jev_client.py` sets `SYSTEM_ONE_URL = https://api.typesafe.ai/v1/systemone`; the vision extractor reuses the same settings, budget, audit log and price list, and its constructor has no way to point at another endpoint. `--dry-run` rehearses a step without side effects and `verify` re-hashes the audit chain. Integration evidence: [`driver_core/jev_client.py`](https://github.com/Treystu/driver-core/blob/cf3337076b608abdfcf6b726aed7629e1c44eb39/driver_core/jev_client.py).

## Get started

Install from the repository (no PyPI package was found on the review date), then check health and rehearse a step.

```sh
pip install git+https://github.com/Treystu/driver-core
driver-core health
driver-core --dry-run step "my-app"
driver-core verify
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Treystu/driver-core/blob/cf3337076b608abdfcf6b726aed7629e1c44eb39/README.md](https://github.com/Treystu/driver-core/blob/cf3337076b608abdfcf6b726aed7629e1c44eb39/README.md)

## Limits and data handling

Extracted machine state goes to TypeSafe on your key; actions such as `write_file` and `delete_file` run locally with backups and refusal rules. The README's `pip install driver-core` does not resolve on PyPI as of 2026-11-14.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit cf3337076b60](https://github.com/Treystu/driver-core/tree/cf3337076b608abdfcf6b726aed7629e1c44eb39). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
