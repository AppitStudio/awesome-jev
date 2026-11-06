# jev-tar (technology-assisted review that ranks documents with Jev and reports elusion statistics)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python TAR toolkit for legal-style review: classify documents against a protocol with TypeSafe Jev, propagate families, resume safely, and emit elusion statistics plus audit artifacts. Offline demos use synthetic fixtures.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-tar) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python 3.11+ CLI/library (MIT) |
| Requirements | Python 3.11+ and `TYPESAFE_API_KEY` for live classify (offline FakeJev demos available). |
| License | [MIT](https://github.com/gbesse/jev-tar/blob/70b51e6a593abc0a14215fac74b7062a44ee0dd6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_tar/client.py`](https://github.com/gbesse/jev-tar/blob/70b51e6a593abc0a14215fac74b7062a44ee0dd6/src/jev_tar/client.py) at the pinned commit. |

## When to use

- Run a protocol-bound document review with audit logs.
- Need elusion intervals even when a sample finds zero misses.
- Mismatch: not legal advice; attorney review still required.

## How it works

`src/jev_tar/client.py` posts classifications to TypeSafe with pinned `jev-1.13.0` and appends audit rows after each document. Integration evidence: [`src/jev_tar/client.py`](https://github.com/gbesse/jev-tar/blob/70b51e6a593abc0a14215fac74b7062a44ee0dd6/src/jev_tar/client.py).

## Get started

Clone and run the offline demo, then set a key for live classify.

```sh
git clone https://github.com/gbesse/jev-tar.git && cd jev-tar
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-dev.txt
python -m examples.offline_demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-tar/blob/70b51e6a593abc0a14215fac74b7062a44ee0dd6/README.md](https://github.com/gbesse/jev-tar/blob/70b51e6a593abc0a14215fac74b7062a44ee0dd6/README.md)

## Limits and data handling

Document text is sent to TypeSafe on your key. Public alpha; matter-specific sampling remains on you.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 70b51e6a593a](https://github.com/gbesse/jev-tar/tree/70b51e6a593abc0a14215fac74b7062a44ee0dd6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
