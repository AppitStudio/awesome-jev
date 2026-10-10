# jevotron

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI for field-level anomaly detection in tabular, structured and text files, SQLite and DuckDB, powered by Jev, that exports a focused review queue of fields worth a second look.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cmungall/jevotron) |
| Maintainer | [cmungall](https://github.com/cmungall). Independently curated. |
| Format | Python CLI (PyPI `jevotron`) |
| Requirements | Python 3.12+; TypeSafe API key for scans (preview needs no key). |
| License | [BSD-3-Clause](https://github.com/cmungall/jevotron/blob/300a67b332dbb6bb6a18fc39532dffcb18fe8055/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Find suspicious fields in a dataset before publishing or ingesting it.
- Mismatch: each scan chunk is a hosted Jev call; accuracy figures come from a small maintainer pilot.

## How it works

Entries are chunked with optional guidance and exemplars, scored by Jev, and cached in SQLite so assessments are reused across file versions. (Summarized from the upstream [README](https://github.com/cmungall/jevotron/blob/300a67b332dbb6bb6a18fc39532dffcb18fe8055/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `uvx jevotron --help`, then `jevotron preview` on a file to see the exact request before scanning.

## Limits and data handling

Scanned field contents are sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 300a67b332db](https://github.com/cmungall/jevotron/tree/300a67b332dbb6bb6a18fc39532dffcb18fe8055). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
