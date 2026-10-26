# jev-use with Cua Driver (bounded browser-action loop where Jev picks the next step)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Public-preview recipe in which Jev chooses the next browser action while Cua Driver observes the page, performs the action and verifies the result; equivalent Python and TypeScript programs run the same bounded loop, prefer fresh DOM and semantic evidence, and keep Jev navigation separate from the calling assistant's answer stage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VenkyKash/jev-use-exp) |
| Maintainer | [VenkyKash](https://github.com/VenkyKash). Independently curated. |
| Format | Python and TypeScript programs |
| Requirements | Python 3.12 with uv, Node.js and npm, and Cua Driver; a TypeSafe API key. |
| License | [AGPL-3.0](https://github.com/VenkyKash/jev-use-exp/blob/6296d2b4b1363885f1a1ef90ad651c66bacf7a9f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`python/jev_adapter.py`](https://github.com/VenkyKash/jev-use-exp/blob/6296d2b4b1363885f1a1ef90ad651c66bacf7a9f/python/jev_adapter.py) at the pinned commit. |

## When to use

- Drive a browser with typed next-action choices instead of free-form agent output.
- Study a bounded computer-use loop with recorded evidence.
- Mismatch: public preview; AGPL-3.0 licensed.

## How it works

`python/jev_adapter.py` turns observed page evidence into a Choice of candidate actions and calls Jev through the official `typesafe_sdk` client; Cua Driver executes and verifies each chosen action. Integration evidence: [`python/jev_adapter.py`](https://github.com/VenkyKash/jev-use-exp/blob/6296d2b4b1363885f1a1ef90ad651c66bacf7a9f/python/jev_adapter.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --frozen --python 3.12
npm ci
export TYPESAFE_API_KEY=...
# see EXPERIMENT.md for evaluation commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/VenkyKash/jev-use-exp#readme](https://github.com/VenkyKash/jev-use-exp#readme)
- Experiment notes: [github.com/VenkyKash/jev-use-exp/blob/main/EXPERIMENT.md](https://github.com/VenkyKash/jev-use-exp/blob/main/EXPERIMENT.md)

## Limits and data handling

Page evidence and candidate actions go to TypeSafe. Cua Driver acts on your browser.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 6296d2b4b136](https://github.com/VenkyKash/jev-use-exp/tree/6296d2b4b1363885f1a1ef90ad651c66bacf7a9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
