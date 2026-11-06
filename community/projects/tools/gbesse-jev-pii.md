# gbesse/jev-pii (column-granularity PII inventory with optional TypeSafe classification)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI that inventories personal data with local checks first and optional semantic classification at column (not row) granularity via TypeSafe. Distinct from the already-listed senthilsweb/jev-pii.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-pii) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python 3.11+ and a TypeSafe key when not using `--local-only`. |
| License | [MIT](https://github.com/gbesse/jev-pii/blob/0106c9b8a16ffa0ec5aa3ae818d7982cde48df78/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_pii/client.py`](https://github.com/gbesse/jev-pii/blob/0106c9b8a16ffa0ec5aa3ae818d7982cde48df78/src/jev_pii/client.py) at the pinned commit. |

## When to use

- Inventory PII columns before a migration or export.
- Prefer local-only mode, then optionally call TypeSafe on samples.
- Mismatch: public alpha; sampled values may leave your host when live.

## How it works

`src/jev_pii/client.py` provides `TypeSafeTransport` and response validation for System One classification after local heuristics. Integration evidence: [`src/jev_pii/client.py`](https://github.com/gbesse/jev-pii/blob/0106c9b8a16ffa0ec5aa3ae818d7982cde48df78/src/jev_pii/client.py).

## Get started

Clone, create a venv, try the offline demo, then review `--dry-run` before any live TypeSafe call.

```sh
git clone https://github.com/gbesse/jev-pii.git && cd jev-pii
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements-dev.txt
python -m examples.offline_demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-pii/blob/0106c9b8a16ffa0ec5aa3ae818d7982cde48df78/README.md](https://github.com/gbesse/jev-pii/blob/0106c9b8a16ffa0ec5aa3ae818d7982cde48df78/README.md)

## Limits and data handling

Sampled real values can be sent to TypeSafe on your key unless `--local-only`. Review dry-run bytes and your processing agreement first.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 0106c9b8a16f](https://github.com/gbesse/jev-pii/tree/0106c9b8a16ffa0ec5aa3ae818d7982cde48df78). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
