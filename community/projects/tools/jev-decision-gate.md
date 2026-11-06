# jev-decision-gate (OpenCode permission gate that uses Jev before irreversible actions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode permission gate (Python CLI + TypeScript plugin) that blocks irreversible tool calls and only interrupts a human when it matters, with TypeSafe Jev behind the decision client.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iDiagoValeta/jev-decision-gate) |
| Maintainer | [iDiagoValeta](https://github.com/iDiagoValeta). Independently curated. |
| Format | Python package + OpenCode plugin (MIT) |
| Requirements | Python 3.10+, Node 20+ for the plugin, OpenCode, and a TypeSafe key. |
| License | [MIT](https://github.com/iDiagoValeta/jev-decision-gate/blob/f2f1f24b23794bae92527d6849a06a75a6d7ebe1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_gate/client.py`](https://github.com/iDiagoValeta/jev-decision-gate/blob/f2f1f24b23794bae92527d6849a06a75a6d7ebe1/src/jev_gate/client.py) at the pinned commit. |

## When to use

- Stop rubber-stamping every OpenCode tool prompt.
- Auto-allow routine work while holding irreversible actions.
- Mismatch: OpenCode-focused; needs a live decision endpoint for the Jev path.

## How it works

`src/jev_gate/client.py` and the plugin call TypeSafe System One for permission decisions; secrets are redacted before logging. Integration evidence: [`src/jev_gate/client.py`](https://github.com/iDiagoValeta/jev-decision-gate/blob/f2f1f24b23794bae92527d6849a06a75a6d7ebe1/src/jev_gate/client.py).

## Get started

Install the Python package and OpenCode plugin per README, set TYPESAFE_API_KEY, and run the doctor/demo flow.

```sh
git clone https://github.com/iDiagoValeta/jev-decision-gate.git && cd jev-decision-gate
export TYPESAFE_API_KEY=...
# follow README plugin + CLI setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/iDiagoValeta/jev-decision-gate/blob/f2f1f24b23794bae92527d6849a06a75a6d7ebe1/README.md](https://github.com/iDiagoValeta/jev-decision-gate/blob/f2f1f24b23794bae92527d6849a06a75a6d7ebe1/README.md)

## Limits and data handling

Tool names, arguments and related context (after redaction) are sent to TypeSafe on your key when the Jev path is enabled.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit f2f1f24b2379](https://github.com/iDiagoValeta/jev-decision-gate/tree/f2f1f24b23794bae92527d6849a06a75a6d7ebe1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
